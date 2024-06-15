from tkinter import *
import tkinter.font
from PIL import Image, ImageTk

class Weather_widget2:
    def __init__(self) -> None:
        self.main_window = Tk()          
        self.main_window.geometry('300x500+0+0')
        self.main_window.title('WeatherMan')
        self.main_window.resizable(False,False)

        self.icon = ImageTk.PhotoImage(file = "./skkk.jpeg")
        self.data_font = tkinter.font.Font(size="10")
        self.current_font = tkinter.font.Font(size="13")


        self.d_l = Label(self.main_window,text='2023/8/19 // 동탄1동',font=self.data_font)
        self.frame1 = Frame(self.main_window,relief='solid',borderwidth=1)
        self.icon_label = Label(self.frame1,image=self.icon,width=140,height=120)
        self.temp = Label(self.frame1,text='25℃',width=12,font=self.current_font,bg='white')
        self.humidity = Label(self.frame1,text='70%',width=12,font=self.current_font,bg='white')
        self.wind = Label(self.frame1,text='남동풍 // 3m/s',width=12,font=self.current_font,bg='white')
        self.frame2 = Frame(self.main_window,relief='solid',borderwidth=1)
        self.frame2_1 = Frame(self.frame2,relief='solid',borderwidth=2)
        self.frame2_2 = Frame(self.frame2,relief='solid',borderwidth=2)
        self.frame2_3 = Frame(self.frame2,relief='solid',borderwidth=2)

        self.frame2_1_1 = Frame(self.frame2_1,relief='solid',borderwidth=1)
        self.frame2_1_1_icon = Label(self.frame2_1_1,image=self.icon,width=50,height=80)
        self.frame2_1_1_t = Label(self.frame2_1_1,text='30℃')

        self.frame2_1_2 = Frame(self.frame2_1,relief='solid',borderwidth=1)
        self.frame2_1_2_icon = Label(self.frame2_1_2,image=self.icon,width=50,height=80)
        self.frame2_1_2_t = Label(self.frame2_1_2,text='30℃')

        self.frame2_2_1 = Frame(self.frame2_2,relief='solid',borderwidth=1)
        self.frame2_2_1_icon = Label(self.frame2_2_1,image=self.icon,width=50,height=80)
        self.frame2_2_1_t = Label(self.frame2_2_1,text='30℃')

        self.frame2_2_2 = Frame(self.frame2_2,relief='solid',borderwidth=1)
        self.frame2_2_2_icon = Label(self.frame2_2_2,image=self.icon,width=50,height=80)
        self.frame2_2_2_t = Label(self.frame2_2_2,text='30℃')

        self.frame2_3_1 = Frame(self.frame2_3,relief='solid',borderwidth=1)
        self.frame2_3_1_icon = Label(self.frame2_3_1,image=self.icon,width=50,height=80)
        self.frame2_3_1_t = Label(self.frame2_3_1,text='30℃')

        self.frame2_3_2 = Frame(self.frame2_3,relief='solid',borderwidth=1)
        self.frame2_3_2_icon = Label(self.frame2_3_2,image=self.icon,width=50,height=80)
        self.frame2_3_2_t = Label(self.frame2_3_2,text='30℃')


        self.d_l.pack()
        self.frame1.pack()
        self.icon_label.grid(row=0,column=0,rowspan=3)
        self.temp.grid(row=0,column=1)
        self.humidity.grid(row=1,column=1)
        self.wind.grid(row=2,column=1)

        self.frame2.pack()

        self.frame2_1.grid(row=0,column=0)

        self.frame2_1_1.grid(row=0,column=0)
        self.frame2_1_1_icon.grid(row=0,column=0)
        self.frame2_1_1_t.grid(row=1,column=0)

        self.frame2_1_2.grid(row=0,column=1)
        self.frame2_1_2_icon.grid(row=0,column=0)
        self.frame2_1_2_t.grid(row=1,column=0)

        self.frame2_2.grid(row=0,column=1)

        self.frame2_2_1.grid(row=0,column=0)
        self.frame2_2_1_icon.grid(row=0,column=0)
        self.frame2_2_1_t.grid(row=1,column=0)

        self.frame2_2_2.grid(row=0,column=1)
        self.frame2_2_2_icon.grid(row=0,column=0)
        self.frame2_2_2_t.grid(row=1,column=0)

        self.frame2_3.grid(row=0,column=2)

        self.frame2_3_1.grid(row=0,column=0)
        self.frame2_3_1_icon.grid(row=0,column=0)
        self.frame2_3_1_t.grid(row=1,column=0)
        
        self.frame2_3_2.grid(row=0,column=1)
        self.frame2_3_2_icon.grid(row=0,column=0)
        self.frame2_3_2_t.grid(row=1,column=0)


        self.main_window.mainloop()

a = Weather_widget2()
