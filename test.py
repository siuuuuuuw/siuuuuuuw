from tkinter import*
def click ():
    print('dd')
screen = Tk()
screen.title('test')
screen.geometry('400x400+100+100')
button = Button(screen,height=2,width=18,text='button',command=click)
button.place(x=100,y=100)
screen.mainloop()