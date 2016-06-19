#coding=utf-8

import wx
import sys
import os
import time
from datetime import datetime
import logging
import win32gui
import threading

from gui import ui
from utils import imtool
from utils import ocr

from utils.win.capture import capture_inactive_window as capture_window
from utils.win.browser import open_ie
from utils.win.window import find_sub_hwnd
from utils.win.event import key_input, mouse_click

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Frame(wx.Frame):
    def __init__(self, parent, title, size):
        wx.Frame.__init__(self, parent, title=title, size=size,
                style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        ico = wx.Icon(resource_path('resources/paipai.ico'), wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

class App(wx.App):
    def OnInit(self):
        self.version = '13.35.01'
        self.name = u'拍牌小助手 - %s' % self.version
        self.m_frame = Frame(None, self.name, (511, 506))
        self.m_panel = ui.PaipaiPanel(self.m_frame)
        self.m_frame.Show()

        # Connect Events
        self.m_panel.m_button_start.Bind(wx.EVT_BUTTON, self.m_OnStart)

        self.SetTopWindow(self.m_frame)
        return True

    # Virtual event handlers, overide them in your derived class
    def m_OnStart(self, event):
        #ie = open_ie(url="http://moni.51hupai.org")
        ie = open_ie(url="https://paimai2.alltobid.com/bid/2016061801/bid.htm")
        time.sleep(5)
        print "%x" % ie.HWND
        hwnd = find_sub_hwnd(ie.HWND, [("Frame Tab", 0),
            ("TabWindowClass", 0),
            ("Shell DocObject View", 0),
            ("Internet Explorer_Server", 0)])
        moniter = Monitor(hwnd, self.m_panel)
        moniter.start()

class Monitor(threading.Thread):
    def __init__(self, hwnd, panel):
        super(Monitor, self).__init__()
        self.hwnd = hwnd
        self.panel = panel

    def run(self):
        enter_key_down = True
        text_pos_info = [
                ((125, 291), 62, 13),
                ((139, 307), 62, 13),
                ((123, 402), 83, 13),
                ((152, 420), 83, 13),
                ((182, 434), 84, 13),
                ]
        pincode_pos_info = dict(
                login = ((747, 386), 120, 30), # Todo 登录验证码
                first = ((747, 386), 120, 30), # Todo 首轮警示价验证码
                edit = ((747, 386), 120, 54) # 修改出价阶段
                )

        controls_pos_info = dict(
                    text_custom_price = (734, 427),
                    btn_set_price = (792, 428),
                    text_pincode = (605, 396),
                    btn_submit = (520, 505)
                )

        did = False
        price_expected = None
        while True:
            try:
                img = capture_window(self.hwnd)
                images = imtool.find_images(img, text_pos_info)
                data = []
                for j in xrange(len(images)):
                    data.append(ocr.recog(images[j]))
                (attcount, limit, remotetime, price, newpricetime) = tuple(data)

                self.panel.m_text_localtime.SetValue(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                self.panel.m_text_remotetime.SetValue('%s %s' % (datetime.now().strftime('%Y-%m-%d'), remotetime))
                self.panel.m_textl_newprice.SetValue('%s/%s' % (price, newpricetime))

                logging.info(','.join(data))
                if remotetime == '11:30:00':
                    break

                if int(remotetime.split(':')[2]) >= 45:
                    self.panel.m_text_stat.SetValue(u'等待输入验证码')
                    did = True
                    # set mouse pos
                    x, y = controls_pos_info['text_custom_price']
                    print x, y
                    mouse_click(self.hwnd, x, y)
                    price_expected = int(price) + 800
                    key_input(self.hwnd, "%s" % price_expected)
                    time.sleep(0.1)

                    # 点击出价
                    x, y = controls_pos_info['btn_set_price']
                    print x, y
                    mouse_click(self.hwnd, x, y)
                    time.sleep(0.5)

                    # 光标放到校验码上面
                    x, y = controls_pos_info['text_pincode']
                    mouse_click(self.hwnd, x, y)

                if did and enter_key_down and price_expected is not None:
                    if price_expected - int(price) <= 300:
                        # 提交出价
                        x, y = controls_pos_info['btn_submit']
                        mouse_click(self.hwnd, x, y)
            except:
                pass

def main():
    app = App()
    app.MainLoop()

if __name__ == '__main__':
    logging.basicConfig(
            filename='paipai.log',
            format='%(asctime)s %(levelname)s %(message)s',
            level=logging.DEBUG)
    main()
