import wx
import cmd
import subprocess

class GomozConsole(wx.Panel):
    #def __init__(self, panel, *args, **kwds):
    def __init__(self, parent, id, title, prompt):
        wx.Panel.__init__(self, parent=parent)
        self.panel = parent
        if prompt != "" or prompt is not None:
            self.prompt = prompt
        else:
            self.prompt = "user@gomoz:~ "
        self.textctrl = wx.TextCtrl(self.panel, -1, '', style=wx.TE_PROCESS_ENTER|wx.TE_MULTILINE)
        self.default_txt = self.textctrl.GetDefaultStyle()
        self.textctrl.AppendText(self.prompt)
        #self.textctrl.SetForegroundColour('white')
        #self.textctrl.SetBackgroundColour('black')

        self.__set_properties()
        self.__do_layout()
        self.__bind_events()


    def __bind_events(self):
        self.textctrl.Bind(wx.EVT_TEXT_ENTER, self.__enter)


    def __enter(self, e):
        print 'enter'
        self.value = (self.textctrl.GetValue())
        print (self.value)
        self.eval_last_line()
        e.Skip()


    def __set_properties(self):
        self.textctrl.SetFocus()

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.textctrl, 1, wx.EXPAND |wx.ALL, 0)
        self.panel.SetSizer(sizer_1)
        self.Layout()

    def eval_last_line(self):
        nl = self.textctrl.GetNumberOfLines()
        ln = self.textctrl.GetLineText(nl-1)
        ln = ln[len(self.prompt):]
        args = ln.split(" ")
        print ln
        proc = subprocess.Popen(args, stdout=subprocess.PIPE)
        retvalue = proc.communicate()[0]
      
        #c = wx.Colour(239, 177, 177)
        c = wx.Colour(0, 0, 0)
        tc = wx.TextAttr(c)
        self.textctrl.SetDefaultStyle(tc)
        self.textctrl.AppendText('\n')
        self.textctrl.AppendText(retvalue)
        self.textctrl.SetDefaultStyle(self.default_txt)
        self.textctrl.AppendText(self.prompt)
        #self.textctrl.SetInsertionPoint(GetLastPosition() - 1)


 
