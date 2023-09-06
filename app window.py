from tkinter import *
import random
from responses import *
    
    

window = Tk()

def fun_one():
    low_str = "qwertyuiopasdfghjklzxcvbnm"
    high_str = "QWERTYUIOPASDFGHJKLZXCVBNM"
    nums = "0123456789"
    all = low_str + high_str + nums
    len_pass = 6
    password = ''.join(random.sample(all,len_pass))
    lbl.config(text=password,anchor="center")



#len_pass = Entry(window)
#len_pass.pack()




lbl = Label(window,bg="grey",fg="white",width=10,font=("arial",20))
lbl.pack()
lbl.place(x=70,y=120)


btn = Button(window, text="Generate", command=fun_one)
btn.place(width=60, height=40, x=125, y=250)


Label(window, text="code by : soran-hes").pack()


window.geometry('300x400')
window.resizable(height=False,width=False)
window.title("Generate Password")
window = mainloop()

#در ادامه میخاهم نرم افزار طول پسوورد یا از کاربر بگیرد و با توجه به ورودی کاربر پسوورد جدید را بسازد...