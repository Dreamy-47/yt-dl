
import wx
from wx.core import Frame
import wx.xrc
class MyFrame ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition,  size = wx.Size( 700,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )
#Please input correct URL format
#         INPUT URL HERE         
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"         INPUT URL HERE         ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont(wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER, 5)


        format_list = ['mp3','webm', 'mp4']
        self.rb = wx.RadioBox(
                self, wx.ID_ANY, u"format", wx.DefaultPosition, wx.DefaultSize,
                format_list, 3, wx.RA_SPECIFY_COLS | wx.NO_BORDER
                )
        
        bSizer1.Add( self.rb, 0, wx.ALL|wx.ALIGN_CENTER, 5 )


        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,  wx.Size( 500,-1 ), 0 )
        bSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER, 5)

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER, 5 )

        self.Complete_text = wx.StaticText( self, wx.ID_ANY, u"Download complete", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Complete_text.SetFont(wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        bSizer1.Add( self.Complete_text, 0, wx.ALL|wx.ALIGN_CENTER, 5 )
        self.Complete_text.Show(False)
        

        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        self.m_button1.Bind( wx.EVT_BUTTON, self.OnBtnClick )
        

    def __del__( self ):
        pass

    def OnBtnClick( self, event ):
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame(None)
    frm.Show()
    app.MainLoop()