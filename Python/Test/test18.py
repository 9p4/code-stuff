import wx
app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Test18")
frame.Show(True)
app.MainLoop()
app.out("hi")