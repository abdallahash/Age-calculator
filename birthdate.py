from PIL import Image, ImageTk 
from tkinter import ttk 
from tkinter import IntVar 
import datetime 
import tkinter as tk 

#creat a frame 
window = tk.Tk()
#creat frame geometry 
window.geometry("350x350")
#set the title of the frame 
window.title("Age Calculator")

frame = ttk.Frame(window)
frame.grid(column=1,row=5)
frame['borderwidth']= 10
#frame['relief'] = 'groove'
frame['padding'] = 5

#Creating lables 
year_label = tk.Label(text="Year")
year_label.grid(column=0, row=1)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=2)

day_label = tk.Label(text="Day")
day_label.grid(column=0, row=3)

name_label = tk.Label(text="Name")
name_label.grid(column=0, row=4)

age_label = tk.Label(text='Age in ')
age_label.grid(column=0, row=5)

#creating Entry for each label

year_entry = tk.Entry()
year_entry.grid(column=1, row=1)

month_entry = tk.Entry()
month_entry.grid(column=1,row=2)

day_entry = tk.Entry()
day_entry.grid(column=1,row=3)

name_entry = tk.Entry()
name_entry.grid(column=1, row=4)

# This function gets trigert once the CALCULATE button is clicked 
# it handles taking the year,month and day from the entry feilds,
# and use it to creat new object from the person class below. 
def calculate():
    #creating a new object birthday_boy that have a name and a birthdate 
    
    birthday_boy = person(name_entry.get(), datetime.date(int(year_entry.get()),int(month_entry.get()),int(day_entry.get())))

    print(birthday_boy.name)
    print(birthday_boy.age())

    #setting something like a text box to display our answer(age) in it

    text_answer = tk.Text(master=window, height=20, width=30)
    text_answer.grid(column=1, row=7)
    if (var2.get() == 1 and var1.get() == 0):
        text_answer.insert(tk.END,"{} You are {} Years old Congratulations!!!!".format(birthday_boy.name, birthday_boy.age()))
    elif (var1.get() == 1 and var2.get() == 0):
        text_answer.insert(tk.END,"{} You are {} old Congratulations!!!!".format(birthday_boy.name, birthday_boy.age_in_days()))
    else:
        text_answer.insert(tk.END,"Please check ONLY ONE BOX !")

var1 = IntVar()
check_button_1 = ttk.Checkbutton(frame, text="Days", variable=var1)
check_button_1.grid(column=1, row=0)
check_button_1.state(['!alternate'])
print(var1)
var2 = IntVar()
check_button_2 = ttk.Checkbutton(frame, text="Years", variable=var2)
check_button_2.grid(column=2,row=0)
check_button_1.state(['!alternate'])


#Add a button it cannot be added before the calculate fuction or we will get an error. 
calculate_button = tk.Button(window, text="CALCULATE", command=calculate)
calculate_button.grid(column=1,row=6)

class person:
    today = datetime.date.today()
    def __init__(self, name , birthdate):
        self.name= name
        self.birthdate = birthdate 
    
    def age(self):
        #today = datetime.date.today()
        age = self.today.year - self.birthdate.year 
        return age

    def age_in_days(self):
        age_day = self.today - self.birthdate
        return age_day


image = Image.open("/Users/Dell/Downloads/wallhaven-476133.jpg")


image.thumbnail((150, 150), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)




window.mainloop()

