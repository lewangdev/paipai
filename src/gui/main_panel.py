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
## Class MainPanel
###########################################################################

class MainPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 448,428 ), style = wx.TAB_TRAVERSAL )
		
		gbSizer1 = wx.GridBagSizer( 0, 5 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"竞拍策略" ), wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 3, 1, 5, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"首次出价时段，第一次出价" ), wx.VERTICAL )
		
		self.m_auction1_CheckBox = wx.CheckBox( self, wx.ID_ANY, u"启用(自动出价金额为警示价)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_auction1_CheckBox.SetValue(True) 
		sbSizer6.Add( self.m_auction1_CheckBox, 0, wx.ALL, 5 )
		
		
		fgSizer4.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"修改出价时段，第二次出价" ), wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auction2_checkBox = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_auction2_checkBox.SetValue(True) 
		bSizer3.Add( self.m_auction2_checkBox, 0, wx.ALL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer5 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"在拍牌结束倒数第", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_second2_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 120, 15 )
		fgSizer5.Add( self.m_second2_spinCtrl, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"秒", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer5.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		fgSizer6 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, u"当前可成交价加", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn2.SetValue( True ) 
		fgSizer6.Add( self.m_radioBtn2, 0, wx.ALL, 5 )
		
		self.m_delta2_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 9900, 700 )
		fgSizer6.Add( self.m_delta2_spinCtrl, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		fgSizer8 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_radioBtn1 = wx.RadioButton( self, wx.ID_ANY, u"直接出价", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_radioBtn1, 0, wx.ALL, 5 )
		
		self.m_direct2_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 120000, 85000 )
		fgSizer8.Add( self.m_direct2_spinCtrl, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		sbSizer7.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		fgSizer4.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"修改出价时段，第三次出价" ), wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auction3_checkBox = wx.CheckBox( self, wx.ID_ANY, u"启用", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_auction3_checkBox.SetValue(True) 
		bSizer4.Add( self.m_auction3_checkBox, 0, wx.ALL, 5 )
		
		fgSizer31 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer31.SetFlexibleDirection( wx.BOTH )
		fgSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer51 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer51.SetFlexibleDirection( wx.BOTH )
		fgSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"在第二次出价成功后", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		fgSizer51.Add( self.m_staticText61, 0, wx.ALL, 5 )
		
		self.m_second3_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 120, 0 )
		fgSizer51.Add( self.m_second3_spinCtrl, 0, wx.ALL, 5 )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"秒", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		fgSizer51.Add( self.m_staticText71, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( fgSizer51, 1, wx.EXPAND, 5 )
		
		fgSizer61 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer61.SetFlexibleDirection( wx.BOTH )
		fgSizer61.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_radioBtn21 = wx.RadioButton( self, wx.ID_ANY, u"第二次出价加", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn21.SetValue( True ) 
		fgSizer61.Add( self.m_radioBtn21, 0, wx.ALL, 5 )
		
		self.m_delta3_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 9900, 700 )
		fgSizer61.Add( self.m_delta3_spinCtrl, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( fgSizer61, 1, wx.EXPAND, 5 )
		
		fgSizer81 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer81.SetFlexibleDirection( wx.BOTH )
		fgSizer81.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_radioBtn11 = wx.RadioButton( self, wx.ID_ANY, u"直接出价", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer81.Add( self.m_radioBtn11, 0, wx.ALL, 5 )
		
		self.m_direct3_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 120000, 85000 )
		fgSizer81.Add( self.m_direct3_spinCtrl, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( fgSizer81, 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( fgSizer31, 1, wx.EXPAND, 5 )
		
		
		sbSizer10.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		fgSizer4.Add( sbSizer10, 1, wx.EXPAND, 5 )
		
		
		sbSizer2.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		gbSizer1.Add( sbSizer2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"竞拍状态" ), wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 4, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"本机时间", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_localtime_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer1.Add( self.m_localtime_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"拍卖系统时间", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_systemtime_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer1.Add( self.m_systemtime_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"拍卖倒计时", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_resttime_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer1.Add( self.m_resttime_textCtrl, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"当前可成交价", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_current_price_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer1.Add( self.m_current_price_textCtrl, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		gbSizer1.Add( sbSizer4, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		self.SetSizer( gbSizer1 )
		self.Layout()
	
	def __del__( self ):
		pass
	

