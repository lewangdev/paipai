#coding=utf8
'''
API docs:
    https://msdn.microsoft.com/en-us/library/aa752084(v=vs.85).aspx#methods
'''

from win32com.client import DispatchEx


def open(url):
    ie = DispatchEx('InternetExplorer.Application')
    ie.Visible = 1
    ie.ToolBar = 0
    ie.AddressBar = 0
    ie.MenuBar = 0
    ie.StatusBar = 0
    ie.Resizable = 0
    ie.Width = 800
    ie.Height = 600
    ie.Navigate(url)
    return ie

if __name__ == '__main__':
    url = 'http://moni.51hupai.com:8081/'
    ie = open(url)
