from tkinter import *
from difflib import SequenceMatcher

def check():
    text_1 = file_1.get()
    text_2 = file_2.get()
    
    with open(text_1) as file1,open(text_2) as file2:
        file1_data = file1.read()
        file2_data = file2.read()
        data = SequenceMatcher(None , file1_data,file2_data).ratio()*100
        file_3_label.config(text=data)
    
root = Tk()

root.geometry("600x400")

root.configure(bg='#3AB3E0')

file_1_label = Label(root,text="Enter File-1 Path",font=14,bg='#3AB3E0',fg='white')
file_1_label.place(relx = 0.2, rely = 0.3,anchor='center')

file_1 = Entry(root,font=20)
file_1.place(relx = 0.6, rely = 0.3,anchor='center')


file_2_label = Label(root,text="Enter File-2 Path",font=14,bg='#3AB3E0',fg='white')
file_2_label.place(relx = 0.2, rely = 0.5,anchor='center')

file_2 = Entry(root,font=20)
file_2.place(relx = 0.6, rely = 0.5,anchor='center')

btn = Button(root,text="Answer",padx=5,pady=5,font=16,bd=1,bg='#120E67',fg='white',command=check)
btn.place(relx=0.5,rely=0.8,anchor='center')

file_3_label = Label(root,text="",font=14,bg='#3AB3E0',fg='white')
file_3_label.place(relx = 0.5, rely = 0.95,anchor='center')

root.mainloop()