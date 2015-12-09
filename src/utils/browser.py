#coding=utf8
"""浏览器控制

通过windows com 组建启动 IE 浏览器并打开到指定页面。
参考文档：
    https://msdn.microsoft.com/en-us/library/aa752084(v=vs.85).aspx#methods
"""

from win32com.client import DispatchEx
import win32gui
import win32con

def open_ie(url, size=(860, 660)):
    """打开IE浏览器"""
    width, height = size

    ie = DispatchEx('InternetExplorer.Application')

    # 设置窗口style
    ie.Visible = 1
    ie.ToolBar = 0
    ie.AddressBar = 0
    ie.MenuBar = 0
    ie.StatusBar = 0
    ie.Resizable = 0
    ie.Width = width
    ie.Height = height

    # 设置打开的 URL
    ie.Navigate(url)

    win32gui.SetForegroundWindow(ie.HWND)
    win32gui.SetWindowPos(ie.HWND, win32con.HWND_TOPMOST,
            0, 0, width, height,
            win32con.SWP_NOACTIVATE |
            win32con.SWP_NOOWNERZORDER |
            win32con.SWP_SHOWWINDOW)

    return ie

if __name__ == '__main__':
    url = 'http://moni.51hupai.com:8081/'
    ie = open_ie(url)
