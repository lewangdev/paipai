#coding=utf8
'''
API docs:
    https://msdn.microsoft.com/en-us/library/aa752084(v=vs.85).aspx#methods
'''

from win32com.client import DispatchEx
import win32gui
import win32con


def open(url):
    ie = DispatchEx('InternetExplorer.Application')
    ie.Visible = 1
    ie.ToolBar = 0
    ie.AddressBar = 0
    ie.MenuBar = 0
    ie.StatusBar = 0
    ie.Resizable = 0
    ie.Width = 860
    ie.Height = 660
    ie.Navigate(url)

    hwnd = ie.HWND
    win32gui.SetForegroundWindow (hwnd)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST,
            0, 0, 860, 660,
            win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE| win32con.SWP_NOOWNERZORDER|win32con.SWP_SHOWWINDOW)

    return ie

if __name__ == '__main__':
    url = 'http://moni.51hupai.com:8081/'
    ie = open(url)
