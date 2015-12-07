#coding=utf8
import keyboard_mouse as kbm

def test1():
    kbm.mouse_click(800,200)
    print kbm.get_mouse_point()
    kbm.mouse_move(1024,470)
    print kbm.get_mouse_point()
    kbm.mouse_dblclick(400,600)
    print kbm.get_mouse_point()
    kbm.mouse_click(1000,440)
    print kbm.get_mouse_point()
    str = 'hello'
    kbm.key_input(str)
    print kbm.get_mouse_point()

if __name__ == "__main__":
    test1()
