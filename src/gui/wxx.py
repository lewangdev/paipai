#coding=utf8

# extend of wx
import wx

class StepSpinCtrl(wx.SpinCtrl):
    def __init__(self, *args, **kwargs):
        wx.SpinCtrl.__init__(self, *args, **kwargs)
        self.step = kwargs.get('step', 99)
        self.last_value = 0
        self.Bind(wx.EVT_SPINCTRL, self.OnSpin)

    def OnSpin(self, event):
        delta = self.GetValue() - self.last_value
        if delta == 0:
            return
        elif delta > 0:
            self.last_value = self.GetValue() + self.step
        else:
            self.last_value = self.GetValue() - self.step
        self.SetValue(self.last_value)
