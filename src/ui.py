# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import wxx

###########################################################################
## Class PaipaiPanel
###########################################################################

class PaipaiPanel ( wx.Panel ):

	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 507,486 ), style = wx.TAB_TRAVERSAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 1, 2, 10, 10 )

		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"拍牌策略" ), wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox_second = wx.CheckBox( self, wx.ID_ANY, u"第二轮出价策略", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_second.SetValue(True)
		bSizer5.Add( self.m_checkBox_second, 0, wx.ALL, 5 )

		fgSizer15 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"出价于拍卖结束倒数第", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer15.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spin_second_countdown = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 600, 57 )
		fgSizer15.Add( self.m_spin_second_countdown, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"秒", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer15.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( fgSizer15, 1, wx.EXPAND, 5 )

		fgSizer16 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText351 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText351.Wrap( -1 )
		fgSizer16.Add( self.m_staticText351, 0, wx.ALL, 5 )

		self.m_radio_second_low = wx.RadioButton( self, wx.ID_ANY, u"最低成交价+", wx.Point( -1,-1 ), wx.DefaultSize, wx.RB_GROUP )
		self.m_radio_second_low.SetValue( True )
		fgSizer16.Add( self.m_radio_second_low, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spin_second_low = wxx.StepSpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 100 )
		self.m_spin_second_low.SetMinSize( wx.Size( 65,-1 ) )

		fgSizer16.Add( self.m_spin_second_low, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		fgSizer16.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.m_radio_second_direct = wx.RadioButton( self, wx.ID_ANY, u"直接出价", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.m_radio_second_direct, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_spin_second_direct = wxx.StepSpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 200000, 85000 )
		self.m_spin_second_direct.SetMinSize( wx.Size( 65,-1 ) )

		fgSizer16.Add( self.m_spin_second_direct, 0, wx.ALL, 5 )


		bSizer5.Add( fgSizer16, 1, wx.ALIGN_CENTER|wx.ALIGN_RIGHT|wx.EXPAND, 5 )

		self.m_staticline1111 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline1111, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_checkBox_third = wx.CheckBox( self, wx.ID_ANY, u"第三轮出价策略", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_third.SetValue(True)
		bSizer5.Add( self.m_checkBox_third, 0, wx.ALL, 5 )

		fgSizer151 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer151.SetFlexibleDirection( wx.BOTH )
		fgSizer151.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText161 = wx.StaticText( self, wx.ID_ANY, u"出价于拍卖结束倒数第", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		fgSizer151.Add( self.m_staticText161, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spin_third_countdown = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 600, 57 )
		fgSizer151.Add( self.m_spin_third_countdown, 0, wx.ALL, 5 )

		self.m_staticText171 = wx.StaticText( self, wx.ID_ANY, u"秒", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )
		fgSizer151.Add( self.m_staticText171, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( fgSizer151, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALIGN_RIGHT|wx.ALIGN_TOP|wx.EXPAND|wx.RIGHT, 5 )

		fgSizer161 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer161.SetFlexibleDirection( wx.BOTH )
		fgSizer161.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3511 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3511.Wrap( -1 )
		fgSizer161.Add( self.m_staticText3511, 0, wx.ALL, 5 )

		self.m_radio_third_low = wx.RadioButton( self, wx.ID_ANY, u"最低成交价+", wx.Point( -1,-1 ), wx.DefaultSize, wx.RB_GROUP )
		self.m_radio_third_low.SetValue( True )
		fgSizer161.Add( self.m_radio_third_low, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spin_third_low = wxx.StepSpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 100 )
		self.m_spin_third_low.SetMinSize( wx.Size( 65,-1 ) )

		fgSizer161.Add( self.m_spin_third_low, 0, wx.ALL, 5 )

		self.m_staticText352 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText352.Wrap( -1 )
		fgSizer161.Add( self.m_staticText352, 0, wx.ALL, 5 )

		self.m_radio_third_direct = wx.RadioButton( self, wx.ID_ANY, u"直接出价", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer161.Add( self.m_radio_third_direct, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_spin_third_direct = wxx.StepSpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100000, 70000 )
		self.m_spin_third_direct.SetMinSize( wx.Size( 65,-1 ) )

		fgSizer161.Add( self.m_spin_third_direct, 0, wx.ALL, 5 )


		bSizer5.Add( fgSizer161, 1, wx.EXPAND, 5 )

		self.m_staticline11111 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline11111, 0, wx.EXPAND |wx.ALL, 5 )

		fgSizer152 = wx.FlexGridSizer( 3, 3, 0, 0 )
		fgSizer152.SetFlexibleDirection( wx.BOTH )
		fgSizer152.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox_option_one = wx.CheckBox( self, wx.ID_ANY, u"在拍卖结束倒数第", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_option_one.SetValue(True)
		fgSizer152.Add( self.m_checkBox_option_one, 0, wx.ALIGN_CENTER, 5 )

		self.m_spin_option_one_countdown = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 600, 7 )
		fgSizer152.Add( self.m_spin_option_one_countdown, 0, 0, 5 )

		self.m_staticText172 = wx.StaticText( self, wx.ID_ANY, u"秒", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText172.Wrap( -1 )
		fgSizer152.Add( self.m_staticText172, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText17211 = wx.StaticText( self, wx.ID_ANY, u"   ≤最低成交价", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17211.Wrap( -1 )
		fgSizer152.Add( self.m_staticText17211, 0, wx.ALL, 5 )

		self.m_spin_option_one_pricedelta = wxx.StepSpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 1000, 400 )
		fgSizer152.Add( self.m_spin_option_one_pricedelta, 0, 0, 5 )

		self.m_staticText172111 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText172111.Wrap( -1 )
		fgSizer152.Add( self.m_staticText172111, 0, wx.ALL, 5 )

		self.m_staticText172112 = wx.StaticText( self, wx.ID_ANY, u"   提前\n   强制提交出价", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText172112.Wrap( -1 )
		fgSizer152.Add( self.m_staticText172112, 0, wx.ALL, 5 )

		self.m_spin_option_one_premillis = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 1000, 500 )
		fgSizer152.Add( self.m_spin_option_one_premillis, 0, 0, 5 )

		self.m_staticText1721 = wx.StaticText( self, wx.ID_ANY, u"毫秒", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1721.Wrap( -1 )
		fgSizer152.Add( self.m_staticText1721, 0, wx.ALL, 5 )


		bSizer5.Add( fgSizer152, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

		fgSizer1521 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1521.SetFlexibleDirection( wx.BOTH )
		fgSizer1521.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_checkBox_option_two = wx.CheckBox( self, wx.ID_ANY, u"在拍卖结束倒数第", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_option_two.SetValue(True)
		fgSizer1521.Add( self.m_checkBox_option_two, 0, wx.ALIGN_CENTER, 5 )

		self.m_spin_option_two_countdown = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 600, 4 )
		fgSizer1521.Add( self.m_spin_option_two_countdown, 0, 0, 5 )

		self.m_staticText1722 = wx.StaticText( self, wx.ID_ANY, u"秒", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1722.Wrap( -1 )
		fgSizer1521.Add( self.m_staticText1722, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText172113 = wx.StaticText( self, wx.ID_ANY, u"   强制提交出价", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText172113.Wrap( -1 )
		fgSizer1521.Add( self.m_staticText172113, 0, wx.ALL, 5 )


		bSizer5.Add( fgSizer1521, 1, wx.EXPAND, 5 )


		sbSizer8.Add( bSizer5, 1, wx.EXPAND|wx.ALL, 5 )


		gSizer1.Add( sbSizer8, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		sbSizer81 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"拍牌状态" ), wx.VERTICAL )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 5, 2, 10, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"本地时间", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_text_localtime = wx.TextCtrl( self, wx.ID_ANY, u"0000-00-00 00:00:00", wx.DefaultPosition, wx.Size( 165,-1 ), wx.TE_READONLY )
		self.m_text_localtime.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_text_localtime.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_text_localtime.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		fgSizer1.Add( self.m_text_localtime, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"国拍时间", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_text_remotetime = wx.TextCtrl( self, wx.ID_ANY, u"0000-00-00 00:00:00", wx.DefaultPosition, wx.Size( 165,-1 ), wx.TE_READONLY )
		self.m_text_remotetime.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_text_remotetime.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_text_remotetime.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		fgSizer1.Add( self.m_text_remotetime, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"倒计时", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_text_countdown = wx.TextCtrl( self, wx.ID_ANY, u"00:00:00.000", wx.DefaultPosition, wx.Size( 165,-1 ), wx.TE_READONLY )
		self.m_text_countdown.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_text_countdown.SetForegroundColour( wx.Colour( 255, 193, 193 ) )
		self.m_text_countdown.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		fgSizer1.Add( self.m_text_countdown, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"新成交价", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textl_newprice = wx.TextCtrl( self, wx.ID_ANY, u"00000/00:00:00", wx.DefaultPosition, wx.Size( 165,-1 ), wx.TE_READONLY )
		self.m_textl_newprice.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_textl_newprice.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_textl_newprice.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		fgSizer1.Add( self.m_textl_newprice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"状态", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		fgSizer1.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.m_text_stat = wx.TextCtrl( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 165,100 ), wx.TE_MULTILINE|wx.TE_NOHIDESEL|wx.TE_NO_VSCROLL|wx.TE_READONLY )
		self.m_text_stat.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.m_text_stat.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_text_stat.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		fgSizer1.Add( self.m_text_stat, 0, wx.ALL, 5 )


		bSizer51.Add( fgSizer1, 1, 0, 5 )


		sbSizer81.Add( bSizer51, 1, wx.EXPAND|wx.ALL, 5 )


		bSizer9.Add( sbSizer81, 1, wx.EXPAND, 5 )

		bSizer511 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText162 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText162.Wrap( -1 )
		bSizer511.Add( self.m_staticText162, 0, wx.ALL, 5 )


		bSizer9.Add( bSizer511, 1, 0, 5 )

		bSizer5111 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_start = wx.Button( self, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.Size( 240,50 ), 0 )
		self.m_button_start.SetFont( wx.Font( 20, 70, 90, 90, False, "宋体" ) )

		bSizer5111.Add( self.m_button_start, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox_first = wx.CheckBox( self, wx.ID_ANY, u"首轮自动出价", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_first.SetValue(True)
		bSizer5111.Add( self.m_checkBox_first, 0, wx.ALL, 5 )

		self.m_checkBox_simulation = wx.CheckBox( self, wx.ID_ANY, u"模拟拍牌", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5111.Add( self.m_checkBox_simulation, 0, wx.ALL, 5 )


		bSizer9.Add( bSizer5111, 1, wx.ALIGN_CENTER, 5 )


		gSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )


		bSizer6.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

	def __del__( self ):
		pass


