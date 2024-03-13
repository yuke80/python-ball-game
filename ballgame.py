import tkinter as tk
#import pygame
 
WINDOWWIDTH = 420
WINDOWHEIGHT = 400
 
class BallGame(tk.Frame):
    def __init__(self, master=None, size=(940,800)): #default value is kind of no matter, just a position, change it when you create the instance.
        super().__init__(master, width=size[0], height=size[1])
        self.pack()
        self.create_widgets(size)
 
    def create_widgets(self, size): #this is method. not instance. self is orientation data to the instance that will be created after.
        self.pos = 0
        self.w = size[0]
        self.h = size[1]
        # Barの大きさと位置
        self.bar_height = 20
        self.bar_width = 60
        self.bar_upper_pos = self.h - 80
        self.bar_bottom_pos = self.h - 60
        # キャンバスの生成と配置
        self.canvas  = tk.Canvas(self, width = self.w, height = self.h, bg="#fff")
        self.canvas.place(x=0, y=0)
        # バーを左右に動かすスケールの生成と配置
        self.scale_pos = tk.IntVar()    # Add 2020-08-24
        self.s1 = tk.Scale(self, label = '', orient = 'h',
            from_=0, to = self.w - self.bar_width,
            command = self.change_pos,
            showvalue = 0,
            length = self.w,
            variable = self.scale_pos)      # Add 2020-08-24 
        self.s1.place(x=0, y=self.h - 20)
        print("self.w - self.bar_width",self.w - self.bar_width)
 
        # 変数スコアの定義と初期化
        self.score = 100
        # ボールのプロパティ定義
        self.x = 30
        self.y = 10
        self.vx = 14
        self.vy = 10
 
        self.dia = 20
 
        # タイマースタート
        self.onTimer()
 
    def change_pos(self, pos):
        #print(pos)
        self.pos = int(pos)
 
    def onTimer(self):
        # Clear Canvas
        self.canvas.delete('all')
        h = self.h
        w = self.w
 
        # スコアを表示
        self.canvas.create_text(w/2, h/2, text=str(self.score),
                              font=('FixedSys',48),fill='gray')
 
 
        # Update Circle Pos
        self.x += self.vx
        self.y += self.vy
#        print("self.x: ", self.x, "self.y:",self.y)
 
        if self.x > w or self.x < 0:
            self.vx = - self.vx
            self.x = 0 if self.x < 0 else w
        if self.y > h or self.y < 0:
            self.vy = - self.vy
            # score count down 下の壁に当たるとself.vyは(-)になる
            if self.vy < 0:
                self.score -= 1
 
        #ボールがバーに当たったかの判定
        x = self.x
        if self.y==self.bar_upper_pos and (self.pos <= x <= self.pos + self.bar_width) and self.vy > 0:
            #print("True x-y: ",self.x, self.y)
            self.vy = -self.vy
            # score count up
            self.score += 1
        else:
            pass
            #print("False x-y: ",self.x, self.y)            
 
        # Draw Circle on Canvas
        self.canvas.create_oval(self.x - self.dia/2, self.y - self.dia/2,
                                self.x + self.dia/2, self.y + self.dia/2,
                                fill="red")
        # Draw Bar on Canvas
        #self.canvas.create_rectangle(self.pos, h - 80, self.pos+60, h - 60, fill = 'blue')
        self.canvas.create_rectangle(self.pos, self.bar_upper_pos, self.pos + self.bar_width, self.bar_bottom_pos, fill = 'blue')
        #print("pos: ",self.pos)
        self.after(100, self.onTimer)
 
if __name__=="__main__":
    root=tk.Tk()
    root.title("Tkinter Game")
    app = BallGame(master=root, size=(WINDOWWIDTH,WINDOWHEIGHT)) #can change default size value when create the instance of ballgame which is a sub class of tk.Frame.
    app.mainloop()
