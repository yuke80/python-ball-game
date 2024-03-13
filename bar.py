# -*- coding: utf-8 -*-
import tkinter as tk
 
WINDOWWIDTH = 400
WINDOWHEIHGT = 420
 
class Bar(tk.Frame): 
    def __init__(self,  master=None, size=(WINDOWWIDTH, WINDOWHEIHGT)):
        super().__init__(master, width=size[0], height=size[1])
        self.pack()
        self.create_widgets(size)
    
    def create_widgets(self, size):
        self.pos = 0
        self.w = size[0]
        self.h = size[1]                
        # キャンバスの生成と配置
        self.canvas  = tk.Canvas(self, width = self.w, height = self.h, bg="#fff")
        self.canvas.place(x=0, y=0)
        # バーを左右に動かすスケールの生成と配置
        self.s1 = tk.Scale(self, label = '', orient = 'h',
            from_=0, to = self.w-60, 
            command = self.change_pos,
            showvalue = 0,
            length = self.w)
        self.s1.place(x=0, y=self.h, anchor=tk.SW);       
 
        self.onTimer()
 
    def change_pos(self, pos):
#        print(pos)
        self.pos = int(pos)
    
    def onTimer(self):
        # Clear Canvas
        self.canvas.delete('all')
        h = self.h
        #w = self.w
        # Scaleの位置にBarを描画
        self.canvas.create_rectangle(self.pos, h - 80, self.pos+60, h - 60, fill = 'blue')
 
        self.after(20, self.onTimer)
 
 
if __name__=="__main__":
    root=tk.Tk()
    root.title("Tkinter Game")
    app = Bar(master=root)
    app.mainloop()