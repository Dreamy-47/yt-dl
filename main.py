import wx
import wx.xrc
from yt_dlp.utils import url_or_none
import GUI
import yt_dlp
from yt_dlp import YoutubeDL
import youtube_dl
import os
default_music_path = r"C:\Users\Music"

def YT_URL_exactor(video_url):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    return (video_info['id'],video_info['title'],video_info['formats'][::-1])

class GUIFrame(GUI.MyFrame):
    def __init__(self, parent):
        GUI.MyFrame.__init__(self, parent)

    def OnBtnClick(self, event):
        URL = self.m_textCtrl1.GetValue()
        self.Complete_text.Show(False)
        if url_or_none(URL) == None:
            self.m_staticText1.SetLabel('Please input correct URL format')
            self.m_staticText1.SetForegroundColour('Red')
            

        else:
            self.m_staticText1.SetLabel('         INPUT URL HERE         ')
            self.m_staticText1.SetForegroundColour('Black')

            format_index = self.rb.GetSelection()
            
            format_list = ['mp3','webm', 'mp4']
            global default_music_path
            dlg = wx.DirDialog(self, "Choose a directory:",
                            style=wx.DD_DEFAULT_STYLE
                            )
            if dlg.ShowModal() == wx.ID_OK:
                print(dlg.GetPath())
                default_music_path = dlg.GetPath()
            dlg.Destroy()




            id, title,formats = YT_URL_exactor(URL)
            
            filename = f"{title}.{format_list[format_index]}"
            ydl_opts = {}
            if format_index>=1:
                ydl_opts = {
                    'format': f'bv*[ext={format_list[format_index]}]+ba',
                    'outtmpl':os.path.join(default_music_path,filename),
                }
            else:
                ydl_opts = {
                    'format': 'bestaudio',
                    'outtmpl':os.path.join(default_music_path,filename),
                }
            #print(ydl_opts['format'])
            
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([f'{URL}'])
            
            self.Complete_text.Show(True)
            self.Complete_text.SetPosition((225,160))
        #self.m_staticText1.SetLabel(id)
    
if __name__ == '__main__':
    app = wx.App()
    frm = GUIFrame(None)
    frm.Show()
    app.MainLoop()