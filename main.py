from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=600, height=600)
window.config(padx=20,pady=20)

def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both weight and hight!")
    else:
        try:
            bmi = int(weight) / (int(height)/ 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number")

#ui
weight_input_label = Label(text="Enter Your Weight(kg)")
weight_input_label.config(padx=10, pady=10)
weight_input_label.pack()

weight_input = Entry(width = 10)
weight_input.pack()

height_input_label = Label(text="Enter Your Height (cm)")
height_input_label.pack()

height_input = Entry(width = 10)
height_input.pack()

calculate_button = Button(text="Calculate", command=calculate_bmi)
calculate_button.config(padx=10,pady=10)
calculate_button.pack()

result_label = Label()
result_label.pack()

def write_result(bmi):
    result_string = f"Your BMI is: {bmi}. You are "
    if bmi <= 16:
        result_string += "Severely Thin!"
    elif bmi > 16 and bmi <=17:
        result_string += "Moderately Thin!"
    elif bmi > 17 and bmi <= 18.5:
        result_string +="Mild Thin!"
    elif bmi > 18.5 and bmi <= 25:
        result_string +="Normal!"
    elif bmi > 25 and bmi <= 30:
        result_string +="Overweight!"
    elif bmi > 30 and bmi <= 35:
        result_string +="Obese Class 1!"
    elif bmi > 35 and bmi <= 40:
        result_string +="Obese Class 2!"
    else:
        result_string += "Obese Class 3!"
    return result_string

window.mainloop()