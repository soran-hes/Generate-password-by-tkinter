import random
from tkinter import *

def fun_one():
    low_str = "qwertyuiopasdfghjklzxcvbnm"
    high_str = "QWERTYUIOPASDFGHJKLZXCVBNM"
    nums = "0123456789"
    all = low_str + high_str + nums
    len_pass = 6
    password = ''.join(random.sample(all,len_pass))
    print(password)
    
    
