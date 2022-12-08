import tkinter as tk
import math
from turtle import back

window = tk.Tk()
window.title('BMI App')
window.geometry('800x600')
window.configure(background='white')

def calcuate_bmi_number():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi_value = round(weight / math.pow(height, 2), 2)
    result = 'BMI: {} {}'.format(bmi_value, get_bmi_status_description(bmi_value))
    result_label.configure(text=result)
    
def get_bmi_status_description(bmi_value):
    if bmi_value <18.5:
        return 'Eat more'
    elif bmi_value >= 18.5 and bmi_value < 24:
        return 'Nice'
    elif bmi_value >= 24:
        return 'Fat'

header_label = tk.Label(window, text='BMI counter')
header_label.pack()

height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP)
height_label = tk.Label(height_frame, text='Height(m)')
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(height_frame)
height_entry.pack(side=tk.LEFT)

weight_frame = tk.Frame(window)
weight_frame.pack(side=tk.TOP)
weight_label = tk.Label(weight_frame, text='Weight(kg')
weight_label.pack(side=tk.LEFT)
weight_entry = tk.Entry(weight_frame)
weight_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

calcuate_btn = tk.Button(window, text='Calcuate', command=calcuate_bmi_number)
calcuate_btn.pack()
window.mainloop()
