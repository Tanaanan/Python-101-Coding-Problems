import tkinter as tk #Tkinter library สร้าง GUI (Desktop App)

def show_output():
    number = int(number_input.get()) # .get() ดึงข้อความเข้าไปให้ใช้งานได้

    if number == 0:
        output_label.configure(text="bruh 0 x anything == 0") #configure() = เปลี่ยนparameter
        return # return เดี่ยวๆ == สิ้นสุการทำง่นของ function

    output = ""
    for i in range (1,13):
        output += str(number) + " x " + str(i)
        output += ' = ' + str(number * i) +'\n' # \n == เว้นบรรทัด

    output_label.configure(text=output)

window = tk.Tk() #create window
window.title('JustPython') #name display on app
window.minsize(width=400,height=400) # size ที่เล็กที่สุดได้เท่าไหร่ width กว้าง height สูง

title_label = tk.Label(master=window, text="สูตรคูณแม่") # add UI
title_label.pack(pady=20) # เพิ่มขนาด padx = แนวนอน pady == แนวตั้ง

number_input = tk.Entry(master=window, width=15) #ใส่กรอบ
number_input.pack() # display

go_button = tk.Button(master=window, text="ได้แก่", command = show_output,
                      width=15, height=2
                      ) # create button
go_button.pack()

output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop() # start application