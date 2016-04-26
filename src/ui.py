# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class EntryPanel
###########################################################################

class EntryPanel ( wx.Panel ):

    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 241,337 ), style = wx.TAB_TRAVERSAL )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

        self.m_button_reg = wx.Button( self, wx.ID_ANY, u"注册投标号(拍牌前必须完成)", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
        sbSizer6.Add( self.m_button_reg, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

        self.m_button_check = wx.Button( self, wx.ID_ANY, u"兼容性检测(拍牌前必须完成)", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
        self.m_button_check.SetMinSize( wx.Size( 200,50 ) )

        sbSizer6.Add( self.m_button_check, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

        self.m_button_test = wx.Button( self, wx.ID_ANY, u"仿真模拟(拍牌前勤加练习)", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
        self.m_button_test.SetMinSize( wx.Size( 200,50 ) )

        sbSizer6.Add( self.m_button_test, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_button_bid = wx.Button( self, wx.ID_ANY, u"正式投标(拍牌当天使用)", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
        sbSizer6.Add( self.m_button_bid, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

        self.m_button_intro = wx.Button( self, wx.ID_ANY, u"软件功能详细介绍", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
        sbSizer6.Add( self.m_button_intro, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


        bSizer3.Add( sbSizer6, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()

    def __del__( self ):
        pass


###########################################################################
## Class StatePanel
###########################################################################

class StatePanel ( wx.Panel ):

    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 311,425 ), style = wx.TAB_TRAVERSAL )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"竞拍状态" ), wx.VERTICAL )

        fgSizer1 = wx.FlexGridSizer( 7, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"本机时间", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        fgSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl_localtime = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl_localtime, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"拍卖系统时间", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        fgSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl_systime = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl_systime, 0, wx.ALL, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"拍卖倒计时", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        fgSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl_resttime = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl_resttime, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"当前可成交价", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        fgSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl_current = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl_current, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"您的出价/当前可成交价差", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        fgSizer1.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl_delta = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl_delta, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"伏击智能提交出价", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        fgSizer1.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl_expected = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl_expected, 0, wx.ALL, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"系统频繁操作检测", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        fgSizer1.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl_freq = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl_freq, 0, wx.ALL, 5 )


        sbSizer4.Add( fgSizer1, 1, wx.EXPAND, 5 )


        bSizer4.Add( sbSizer4, 1, wx.EXPAND|wx.ALL, 5 )

        sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"额度投标网络客户端设置" ), wx.VERTICAL )

        fgSizer12 = wx.FlexGridSizer( 1, 3, 0, 0 )
        fgSizer12.SetFlexibleDirection( wx.BOTH )
        fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText_password = wx.StaticText( self, wx.ID_ANY, u"请输入您的标书密码", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_password.Wrap( -1 )
        fgSizer12.Add( self.m_staticText_password, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, u"12345678", wx.DefaultPosition, wx.Size( 60,-1 ), wx.TE_PASSWORD )
        self.m_textCtrl8.SetMaxLength( 12 )
        fgSizer12.Add( self.m_textCtrl8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_hyperlink1 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"启动投标客户端", u"#", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
        fgSizer12.Add( self.m_hyperlink1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        sbSizer10.Add( fgSizer12, 1, wx.EXPAND, 5 )

        fgSizer14 = wx.FlexGridSizer( 1, 3, 0, 0 )
        fgSizer14.SetFlexibleDirection( wx.BOTH )
        fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"身份证编号", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        fgSizer14.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl_id = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
        self.m_textCtrl_id.SetMaxLength( 32 )
        fgSizer14.Add( self.m_textCtrl_id, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"(可选输入)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        fgSizer14.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        sbSizer10.Add( fgSizer14, 1, wx.EXPAND, 5 )


        bSizer4.Add( sbSizer10, 1, wx.EXPAND|wx.ALL, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()

    def __del__( self ):
        pass


###########################################################################
## Class MainPanel
###########################################################################

class MainPanel ( wx.Panel ):

    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 365,473 ), style = wx.TAB_TRAVERSAL )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"正式竞拍策略(修改立即生效)" ), wx.VERTICAL )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        fgSizer13 = wx.FlexGridSizer( 1, 2, 0, 0 )
        fgSizer13.SetFlexibleDirection( wx.BOTH )
        fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        m_comboBox1Choices = [ u"常规伏击A - 仅需输入验证码按回车", u"常规伏击A - 仅需输入验证码按回车", u"常规伏击C - 仅需输入验证码按回车" ]
        self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,-1 ), m_comboBox1Choices, wx.CB_READONLY )
        self.m_comboBox1.SetSelection( 0 )
        fgSizer13.Add( self.m_comboBox1, 0, wx.ALL, 5 )

        self.m_checkBox4 = wx.CheckBox( self, wx.ID_ANY, u"我的首选", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox4.SetValue(True)
        fgSizer13.Add( self.m_checkBox4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer5.Add( fgSizer13, 1, wx.EXPAND, 5 )

        fgSizer14 = wx.FlexGridSizer( 1, 7, 0, 0 )
        fgSizer14.SetFlexibleDirection( wx.BOTH )
        fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_hyperlink2 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"换一个策略", u"#", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
        fgSizer14.Add( self.m_hyperlink2, 0, wx.ALL, 5 )

        self.m_hyperlink4 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"添加", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
        fgSizer14.Add( self.m_hyperlink4, 0, wx.ALL, 5 )

        self.m_hyperlink5 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"修改", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
        fgSizer14.Add( self.m_hyperlink5, 0, wx.ALL, 5 )

        self.m_hyperlink6 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"删除", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
        fgSizer14.Add( self.m_hyperlink6, 0, wx.ALL, 5 )

        self.m_hyperlink7 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"保存", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
        fgSizer14.Add( self.m_hyperlink7, 0, wx.ALL, 5 )

        self.m_hyperlink8 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"更新", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
        fgSizer14.Add( self.m_hyperlink8, 0, wx.ALL, 5 )

        self.m_hyperlink9 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"操作日志", u"#", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
        fgSizer14.Add( self.m_hyperlink9, 0, wx.ALL, 5 )


        bSizer5.Add( fgSizer14, 1, wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer5.Add( self.m_staticline1, 0, wx.EXPAND|wx.ALL, 5 )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"修改出价时段,拍卖第二次出价策略设定", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        bSizer5.Add( self.m_staticText15, 0, wx.ALL, 5 )

        fgSizer15 = wx.FlexGridSizer( 1, 4, 0, 0 )
        fgSizer15.SetFlexibleDirection( wx.BOTH )
        fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"在拍卖结束前", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        fgSizer15.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl7 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 600, 57 )
        fgSizer15.Add( self.m_spinCtrl7, 0, wx.ALL, 5 )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"秒11:29:03及之后", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        fgSizer15.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_checkBox5 = wx.CheckBox( self, wx.ID_ANY, u"自动出价", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox5.SetValue(True)
        fgSizer15.Add( self.m_checkBox5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer5.Add( fgSizer15, 1, wx.EXPAND, 5 )

        fgSizer16 = wx.FlexGridSizer( 1, 4, 0, 0 )
        fgSizer16.SetFlexibleDirection( wx.BOTH )
        fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_radioBtn6 = wx.RadioButton( self, wx.ID_ANY, u"最低成交价+", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer16.Add( self.m_radioBtn6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl8 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 100 )
        self.m_spinCtrl8.SetMinSize( wx.Size( 60,-1 ) )

        fgSizer16.Add( self.m_spinCtrl8, 0, wx.ALL, 5 )

        self.m_radioBtn5 = wx.RadioButton( self, wx.ID_ANY, u"直接出价", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer16.Add( self.m_radioBtn5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl9 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100000, 100 )
        self.m_spinCtrl9.SetMinSize( wx.Size( 60,-1 ) )

        fgSizer16.Add( self.m_spinCtrl9, 0, wx.ALL, 5 )


        bSizer5.Add( fgSizer16, 1, wx.EXPAND, 5 )

        self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer5.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText151 = wx.StaticText( self, wx.ID_ANY, u"修改出价时段,拍卖第三次出价策略设定", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText151.Wrap( -1 )
        bSizer5.Add( self.m_staticText151, 0, wx.ALL, 5 )

        fgSizer151 = wx.FlexGridSizer( 1, 4, 0, 0 )
        fgSizer151.SetFlexibleDirection( wx.BOTH )
        fgSizer151.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText161 = wx.StaticText( self, wx.ID_ANY, u"第二次出价成功", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText161.Wrap( -1 )
        self.m_staticText161.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

        fgSizer151.Add( self.m_staticText161, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl71 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 600, 0 )
        fgSizer151.Add( self.m_spinCtrl71, 0, wx.ALL, 5 )

        self.m_staticText171 = wx.StaticText( self, wx.ID_ANY, u"秒及之后", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText171.Wrap( -1 )
        fgSizer151.Add( self.m_staticText171, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_checkBox51 = wx.CheckBox( self, wx.ID_ANY, u"自动出价", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox51.SetValue(True)
        fgSizer151.Add( self.m_checkBox51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer5.Add( fgSizer151, 1, wx.EXPAND, 5 )

        fgSizer161 = wx.FlexGridSizer( 1, 4, 0, 0 )
        fgSizer161.SetFlexibleDirection( wx.BOTH )
        fgSizer161.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_radioBtn61 = wx.RadioButton( self, wx.ID_ANY, u"最低成交价+", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer161.Add( self.m_radioBtn61, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl81 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 100 )
        self.m_spinCtrl81.SetMinSize( wx.Size( 60,-1 ) )

        fgSizer161.Add( self.m_spinCtrl81, 0, wx.ALL, 5 )

        self.m_radioBtn51 = wx.RadioButton( self, wx.ID_ANY, u"直接出价", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer161.Add( self.m_radioBtn51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_spinCtrl91 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000000, 10 )
        self.m_spinCtrl91.SetMinSize( wx.Size( 60,-1 ) )

        fgSizer161.Add( self.m_spinCtrl91, 0, wx.ALL, 5 )


        bSizer5.Add( fgSizer161, 1, wx.EXPAND, 5 )

        self.m_staticline111 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer5.Add( self.m_staticline111, 0, wx.EXPAND |wx.ALL, 5 )

        fgSizer23 = wx.FlexGridSizer( 1, 2, 0, 0 )
        fgSizer23.SetFlexibleDirection( wx.BOTH )
        fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_checkBox8 = wx.CheckBox( self, wx.ID_ANY, u"启用编程模式(普通用户请勿使用)", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer23.Add( self.m_checkBox8, 0, wx.ALL, 5 )

        self.m_hyperlink10 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"策略编辑器", u"#", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
        fgSizer23.Add( self.m_hyperlink10, 0, wx.ALL, 5 )


        bSizer5.Add( fgSizer23, 1, wx.EXPAND, 5 )

        self.m_checkBox9 = wx.CheckBox( self, wx.ID_ANY, u"显示策略辅助窗口(该窗口关闭时设置依然生效)", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_checkBox9, 0, wx.ALL, 5 )

        self.m_staticline1111 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer5.Add( self.m_staticline1111, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_checkBox10 = wx.CheckBox( self, wx.ID_ANY, u"进入首次出价阶段自动出价(出价金额为警示价)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox10.SetValue(True)
        bSizer5.Add( self.m_checkBox10, 0, wx.ALL, 5 )

        self.m_checkBox11 = wx.CheckBox( self, wx.ID_ANY, u"将本软件所有窗口置于其它窗口之上(窗口置顶)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox11.SetValue(True)
        bSizer5.Add( self.m_checkBox11, 0, wx.ALL, 5 )


        sbSizer8.Add( bSizer5, 1, wx.EXPAND|wx.ALL, 5 )


        bSizer6.Add( sbSizer8, 1, wx.EXPAND|wx.ALL, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()



    def __del__( self ):
        pass
