#coding=utf-8

from gui import main_panel
import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(428,448), style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        self.m_main_panel = main_panel.MainPanel(self)
        self.Show(True)

class App(wx.App):
    def OnInit(self):
        self.m_main_frame = MainFrame(None, u'测试')
        self.SetTopWindow(self.m_main_frame)
        self.m_main_frame.Show()
        return True

def main():
    app = App()
    app.MainLoop()

if __name__ == '__main__':
    main()
