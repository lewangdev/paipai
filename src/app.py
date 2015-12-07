#coding=utf-8

from gui import main_panel as mp
import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(428,448), style= wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        main_panel = mp.MainPanel(self)
        self.Show(True)

app = wx.App(False)
main_frame = MainFrame(None, u"拍牌设置")
app.MainLoop()
