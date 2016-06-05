#coding=utf-8

import ui
import wx
import sys
import os
import time
import logging
import win32gui
import threading

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
        #self.version = '13.35.01'
        self.m_frame = Frame(None, u'投标号:53061106 当前状态', (507,486))
        self.m_panel = ui.PaipaiPanel(self.m_frame)
        self.m_frame.Show()

        # Connect Events

        self.SetTopWindow(self.m_frame)
        return True

    # Virtual event handlers, overide them in your derived class
    def m_hyperlink1OnHyperLink(self, event):
        moniter = Monitor()
        moniter.start()

class Monitor(threading.Thread):
    def __init__(self):
        super(Monitor, self).__init__()
        # create a new thread or process
        # 51hupai.org
        # (left, top), w, h
    def run(self):
        text_pos_info = [
                ((125, 291), 62, 13),
                ((139, 307), 62, 13),
                ((123, 402), 83, 13),
                ((152, 420), 83, 13),
                ((183, 434), 83, 13),
                ]

        controls_pos_info = dict(
                    text_custom_price = (632, 423),
                    btn_set_price = (792, 428)
                )
        ie = open_ie(url="http://moni.51hupai.org")
        time.sleep(5)
        print "%x" % ie.HWND
        hwnd = find_sub_hwnd(ie.hwnd, [("Frame Tab", 0),
            ("TabWindowClass", 0),
            ("Shell DocObject View", 0),
            ("Internet Explorer_Server", 0)])
        #hwnd = find_sub_hwnd(ie.HWND, [("Frame Tab", 0)])
        print "%x" % hwnd

        did = False
        while True:
            img = capture_window(hwnd)
            images = imtool.find_images(img, text_pos_info)
            data = []
            for j in xrange(len(images)):
                data.append(ocr.recog(images[j]))
            (attcount, limit, bidtime, price, pricetime) = tuple(data)
            logging.info(','.join(data))
            if bidtime == '11:29:59':
                break

            if int(bidtime.split(':')[2]) > 7 and not did:
                did = True
                # set mouse pos
                x, y = controls_pos_info['text_custom_price']
                print x, y
                mouse_click(hwnd, x, y)
                key_input(hwnd, "%s" % (int(price) + 700))
                time.sleep(0.1)

                # 点击出价
                x, y = controls_pos_info['btn_set_price']
                print x, y
                mouse_click(hwnd, x, y)

def main():
    app = App()
    app.MainLoop()

if __name__ == '__main__':
    main()
