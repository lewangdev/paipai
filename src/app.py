#coding=utf-8

import ui
import wx

class EntryFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(241,357), style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        self.m_entry_panel = ui.EntryPanel(self)
        ico = wx.Icon('paipai.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        self.Show(True)

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(365,460), style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        self.m_main_panel = ui.MainPanel(self)
        ico = wx.Icon('paipai.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        self.Show(True)

class StateFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(311,425), style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        self.m_State_panel = ui.StatePanel(self)
        ico = wx.Icon('paipai.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)
        self.Show(True)

class App(wx.App):
    def OnInit(self):
        self.version = '13.35.01'
        self.m_entry_frame = EntryFrame(None, self.version)
        self.m_main_frame = MainFrame(None, self.version)
        self.m_state_frame = StateFrame(None, u'投标号:53061106 当前状态')
        self.SetTopWindow(self.m_entry_frame)
        self.m_entry_frame.Show()
        self.m_main_frame.Show()
        self.m_state_frame.Show()
        return True

def main():
    app = App()
    app.MainLoop()

if __name__ == '__main__':
    main()
