from tkinter import *
from PIL import ImageTk, Image

class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        #self.window.state("zoomed")
        #self.window.resizable(0,0)

        # background image
        self.bgFrame = Image.open('images/bg.png')
        bgPhoto = ImageTk.PhotoImage(self.bgFrame)
        self.bgPanel = Label(self.window, image=bgPhoto)
        self.bgPanel.image = bgPhoto
        self.bgPanel.pack(fill="both", expand='yes')

        # icon image
        self.icon = PhotoImage(file="images/icon.png")
        window.iconphoto(True, self.icon)

        # login frame
        self.loginFrame = Frame(self.window, bg="#040405", width="950", height="600")
        self.loginFrame.place(relx=0.5, rely=0.5, anchor= CENTER)

        self.txt= "COIN MANAGER"
        self.heading = Label(self.loginFrame, text=self.txt, font=("arial",30,"bold"), bg="black", fg="white")
        self.heading.place(x=30, y=80, width=500, height=30)


def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()



if __name__ == "__main__":
    page()