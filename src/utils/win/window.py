#coding=utf8
"""
查找窗口句柄.

一个进程窗口由多个窗口组成，需要查找到最直接的那个窗口
"""
import win32gui

def find_sub_hwnd_in_index(hwnd, win_class, index=0):
    """
    已知子窗口的窗体类名
    寻找第index号个同类型的兄弟窗口
    """
    assert type(index) == int and index >= 0
    sub_hwnd= win32gui.FindWindowEx(hwnd, 0, win_class, None)
    while index > 0:
        sub_hwnd = win32gui.FindWindowEx(hwnd, handle, win_class, None)
        index -= 1
    return sub_hwnd


def find_sub_hwnd(hwnd, win_classes):
    """
    递归寻找子窗口的句柄

    hwnd是祖父窗口的句柄
    win_classes是各个子窗口的class列表，父辈的list-index小于子辈
    """
    assert type(win_classes) == list
    if len(win_classes) == 1:
        return find_sub_hwnd_in_index(hwnd,
                win_classes[0][0],
                win_classes[0][1])
    else:
        hwnd = find_sub_hwnd_in_index(hwnd,
                win_classes[0][0],
                win_classes[0][1])
        return find_sub_hwnd(hwnd, win_classes[1:])


if __name__ == '__main__':
    ie_hwnd = 0x000a041c
    hwnd = find_sub_hwnd(ie_hwnd, [("Frame Tab", 0),
        ("TabWindowClass", 0),
        ("Shell DocObject View", 0),
        ("Internet Explorer_Server", 0)])
    print "%x" % (hwnd)
