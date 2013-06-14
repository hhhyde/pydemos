'''
Created on 2013-2-27

@author: k0000010359
'''

import wx

class Frame(wx.Frame): #3
    def __init__(self, parent = None, id =-1, pos = wx.DefaultPosition, title = 'Hello, wxPython!'):
#        temp=image.ConvertToBitmap()
#        size=temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos)
#        self.bmp=wx.StaticBitmap(parent = self, bitmap = temp)

class App(wx.App):
    def OnInit(self):
#        image=wx.Image('D:/123.jpg', wx.BITMAP_TYPE_JPEG)
#        but=wx.Button()
#        self.frame=Frame(but)
        self.frame.Show()
        return True

def main(): #7
    app=App()
    app.MainLoop()

if __name__=='__main__':
    main()
#    app=wx.PySimpleApp()
#    frame=Frame(None)
#    frame.Show()
#    app.MainLoop()
