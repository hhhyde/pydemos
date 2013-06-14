'''
Created on 2013-2-27

@author: k0000010359
'''
import wx

class InsertFrame(wx.Frame):
    def cmooo(self, a):
        return a

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame with button', size = (300, 100))
        panel=wx.Panel(self)
        btn=wx.Button(panel, label = 'Close', pos = (125, 10), size = (50, 50))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, btn)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self, event):
        print self.cmooo(123)
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()

if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=InsertFrame(parent = None, id = 0)
    frame.Show()
    app.MainLoop()
