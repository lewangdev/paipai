#coding=utf-8

import ui
import wx
import sys
import os

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
        self.m_entry_frame = Frame(None, self.version, (241,357))
        self.m_entry_panel = ui.EntryPanel(self.m_entry_frame)
        self.m_entry_frame.Show()

        self.m_main_frame = Frame(None, self.version, (365,493))
        self.m_main_panel = ui.MainPanel(self.m_main_frame)
        self.m_main_frame.Hide()

        self.m_state_frame = Frame(None, u'投标号:53061106 当前状态', (311,425))
        self.m_state_panel = ui.StatePanel(self.m_state_frame)
        self.m_state_frame.Hide()

        self.SetTopWindow(self.m_entry_frame)
        return True

def main():
    app = App()
    app.MainLoop()

if __name__ == '__main__':
    main()
