#coding=utf8

import pythoncom
import pyHook
import capture

def onMouseEvent(event):
	# 监听鼠标事件
	#print "MessageName:", event.MessageName
	#print "Message:", event.Message
	#print "Time:", event.Time
	#print "Window:", event.Window
	#print "WindowName:", event.WindowName
	#print "Position:", event.Position
	#print "Wheel:", event.Wheel
	#print "Injected:", event.Injected
	#print "---"
    rect = capture.get_window_rect(event.Window)
    x, y = event.Position
    print x - rect.left, y - rect.top
    return True

def onKeyboardEvent(event):
	# 监听键盘事件
	print "MessageName:", event.MessageName
	print "Message:", event.Message
	print "Time:", event.Time
	print "Window:", event.Window
	print "WindowName:", event.WindowName
	print "Ascii:", event.Ascii, chr(event.Ascii)
	print "Key:", event.Key
	print "KeyID:", event.KeyID
	print "ScanCode:", event.ScanCode
	print "Extended:", event.Extended
	print "Injected:", event.Injected
	print "Alt", event.Alt
	print "Transition", event.Transition
	print "---"

	return True

def main():
	hm = pyHook.HookManager()

	hm.KeyDown = onKeyboardEvent
	hm.HookKeyboard()

	hm.MouseLeftUp = onMouseEvent
	hm.HookMouse()

	pythoncom.PumpMessages()

if __name__ == "__main__":
	main()
