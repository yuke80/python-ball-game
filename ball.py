
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
 
WINDOWWIDTH = 400
WINDOWHEIHGT = 420
 
class Ball(tk.Frame): 
    def __init__(self,  master=None, size=(WINDOWWIDTH, WINDOWHEIHGT)):#master引数は必須であり、配置される親フレームを表す。=Noneの設定は親クラスのコンストラクタ引数との衝突解決するため。
        super().__init__(master, width=size[0], height=size[1])
        self.pack()
        self.create_widgets(size)
        
    def create_widgets(self, size): #size is waiting to use as a argument.
        self.w = size[0]
        self.h = size[1]
        # キャンバスの生成と配置
        self.canvas  = tk.Canvas(self, width = self.w, height = self.h, bg="#fff")
        self.canvas.place(x=0, y=0, anchor=tk.NW)
 
        # ボールのプロパティ定義
        self.x = 300 #初期位置
        self.y = 10
        self.vx = 7 #移動方向
        self.vy = 3
        
        self.dia = 20 #直径
        
        # タイマースタート
        self.onTimer()
 
    #timer event
    def onTimer(self):
        # Clear Canvas
        self.canvas.delete('all')
        h = self.h #same instance can access data in others method.
        w = self.w
 
        # Update Circle Pos
        self.x += self.vx
        self.y += self.vy
        
        if self.x > w or self.x < 0: #左右壁判断
            self.vx = - self.vx
        if self.y > h or self.y < 0: #上下壁判断
            self.vy = - self.vy
    
        # Draw Circle on Canvas with coordinates x1,y1,x2,y2
        self.canvas.create_oval(self.x - self.dia/2, self.y - self.dia/2,
                                self.x + self.dia/2, self.y + self.dia/2,
                                fill="red")
 
        self.after(500, self.onTimer) #call onTimer every 20 millisecond(timer event)

 
if __name__=="__main__":
    root=tk.Tk()
    root.title("Tkinter Game")
    app = Ball(master=root)
    app.mainloop()
