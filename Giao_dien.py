from tkinter import *
import Thuat_toan
from PIL import ImageTk, Image
import time


class Board(Frame):
    tile_size = 60

    def __init__(self, parent, n, startX, startY):
        self.parent = parent
        self.n = n
        self.color1 = 'brown'
        self.color2 = 'white'
        self.tour, self.path = Thuat_toan.KnightsTour(n).solve(startX, startY)

        canvas_width = n*self.tile_size
        canvas_height = n*self.tile_size
        Frame.__init__(self,parent)
        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        color = self.color2
        for row in range(self.n):
            if self.n % 2 == 0:
                color = self.color1 if color == self.color2 else self.color2
            for col in range(self.n):
                x1 = (col * self.tile_size)
                y1 = (row * self.tile_size)
                x2 = x1 + self.tile_size
                y2 = y1 + self.tile_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black",fill=color,tags="square")
                color = self.color1 if color == self.color2 else self.color2
                self.canvas.create_text(col * self.tile_size + self.tile_size / 2, row * self.tile_size + self.tile_size / 2,
                                        text=str(self.tour[row][col]), fill='black')



        image = Image.open("try3.png")
        image = image.resize((int(self.tile_size / 3), int(self.tile_size / 2)), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(image, master=self.parent)
        self.moveI = self.canvas.create_image(startY*self.tile_size + self.tile_size / 2, startX*self.tile_size + self.tile_size / 2, image =self.image)

    def move(self,stepSize = 10):
        while len(self.path) != 0:
            coord = self.path.pop()
            xc = coord[1] * self.tile_size + self.tile_size / 2
            yc = coord[0] * self.tile_size + self.tile_size / 2

            picX = self.canvas.coords(self.moveI)[0]
            picY = self.canvas.coords(self.moveI)[1]
            oldPicX = picX
            oldPicY = picY
            while xc != picX or yc != picY:
                if picX > xc:
                    self.canvas.move(self.moveI, -stepSize, 0)
                    # self.canvas.update()
                elif picX < xc:
                    self.canvas.move(self.moveI, stepSize, 0)
                    # self.canvas.update()

                elif picY> yc:
                    self.canvas.move(self.moveI, 0, -stepSize)
                    # self.canvas.update()

                elif picY < yc:
                    self.canvas.move(self.moveI, 0, stepSize)
                    # self.canvas.update()

                picX = self.canvas.coords(self.moveI)[0]
                picY = self.canvas.coords(self.moveI)[1]

                time.sleep(.005)
            self.canvas.create_line(oldPicX, oldPicY, picX, picY, fill='black', width=3)
            self.canvas.update()
            time.sleep(1)


if __name__ == '__main__':
    root = Tk()
    board = Board(root,8,1,3)
    board.pack(side="top", fill="both", expand="true", padx=0, pady=0)
    root.after(50,board.move)
    root.mainloop()