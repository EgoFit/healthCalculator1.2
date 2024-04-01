import customtkinter
import CalculatorMadules




window = customtkinter.CTk()
window.title("BMI Calculator 1.2")
window.geometry("600x450+700+200")
window.minsize(600,450)
window.maxsize(600,450)
window.grid_columnconfigure(0, weight=1)
window._set_appearance_mode("dark")



# ------------------- functions ---------------------


def calculate():
    
    cal = CalculatorMadules.BMI_Calculator(entry1.get(), entry2.get())
    cal2 = CalculatorMadules.WHR_Calculator(waistentery.get(), hipentery.get())
    cal3 = CalculatorMadules.WHtR_Calculator(waistentery.get(), entry2.get())
        
   
    # ---------variables of enteries----------

    choose = gendercombo.get()
 
    
    # -------- loops and if --------------------
    
    
    
    
    if cal < 18.5:
        LabelPrint1.configure(text=f"your BMI is {cal} and you are under weight", text_color="yellow")
    elif cal > 25:
        LabelPrint1.configure(text=f"your BMI is {cal} and you are over weight", text_color="red")
    elif cal >= 18.5 or cal <= 25:
        LabelPrint1.configure(text=f"your BMI is {cal} and you are in normal weight", text_color="green")
    else:
         LabelPrint2.configure(text="you don't Enter right Number")  
         
          
    if choose == "man":
        if cal2 < 0.90:
            LabelPrint2.configure(text=f"your WHR is {cal2} and you normal weight", text_color="green")
        elif cal2 == 0.90 or cal2 <= 0.99:
            LabelPrint2.configure(text=f"your WHR is {cal2} and you are over weight", text_color="yellow")
        elif cal2 > 0.99:
            LabelPrint2.configure(text=f"your WHR is {cal2} and you are obese", text_color="red")
        else:
            LabelPrint2.configure(text="you don't Enter right Number")    
    elif choose =="woman":
        if cal2 < 0.80:
            LabelPrint2.configure(text=f"your WHR is {cal2} and you have normal weight", text_color="green")
        elif cal2 == 0.80 or cal2 <= 0.85:
            LabelPrint2.configure(text=f"your WHR is {cal2} and you are over weight", text_color="yellow")
        elif cal2 > 0.85:
            LabelPrint2.configure(text=f"your WHR is {cal2} and you are obese", text_color="red")
        else:
            LabelPrint2.configure(text="you don't Enter right Number")
            
            
            
    if choose == "man":      
        if cal3 <= 0.46:
            LabelPrint3.configure(text=f"your WHtR is {cal3} and Take Care, you might be underweight.", text_color="brwon")
        elif cal3 >0.46 and cal3 <= 0.58:
            LabelPrint3.configure(text=f"your WHtR is {cal3} and your weight is Normal.", text_color="green")
        elif cal3 > 0.58:
            LabelPrint3.configure(text=f"your WHtR is {cal3} and you are in a risky zone.", text_color="red")
        else:
            LabelPrint3.configure(text="you don't Enter right Number")
    elif choose == "woman":
        if cal3 <= 0.46:
            LabelPrint3.configure(text=f"your WHtR is {cal3} and Take Care, you might be underweight.", text_color="brwon")
        elif cal3 >0.46 and cal3 <= 0.54:
            LabelPrint3.configure(text=f"your WHtR is {cal3} and your weight is Normal.", text_color="green")
        elif cal3 > 0.54:
            LabelPrint3.configure(text=f"your WHtR is {cal3} and you are in a risky zone.", text_color="red")
        else:
            LabelPrint3.configure(text="you don't Enter right Number")
        
    
    
    
    
# -------------------------- labels -----------------------

label = customtkinter.CTkLabel(window,text="BMI Calculator 1.2",fg_color="transparent")
label.cget("font").configure(size=25)
label.grid(row=0, column=1, padx=20, pady=20)

# ---------------------- labels of Enteries ---------------
label2 = customtkinter.CTkLabel(window,text="Enter your weight (Kg)", fg_color="transparent")
label2.cget("font").configure(size=10)
label2.grid(row=1, column=0)


label3 = customtkinter.CTkLabel(window,text="Enter your height (M)", fg_color="transparent")
label3.cget("font").configure(size=10)
label3.grid(row=3, column=0)


gender = customtkinter.CTkLabel(window,text="Choice your Gender", fg_color="transparent")
gender.cget("font").configure(size=10)
gender.grid(row=2, column=1)


Waistlabel = customtkinter.CTkLabel(window,text="Enter your waist (cm)", fg_color="transparent")
Waistlabel.cget("font").configure(size=10)
Waistlabel.grid(row=1, column=2)

hiplabel = customtkinter.CTkLabel(window,text="Enter your hip (cm)", fg_color="transparent")
hiplabel.cget("font").configure(size=10)
hiplabel.grid(row=3, column=2)


# ------------------- labelprint of Print Analsis -------------
LabelPrint1 = customtkinter.CTkLabel(window,
                        text="please Enter your Numeric Number  in above",
                        fg_color="transparent",
                        )
LabelPrint1.cget("font").configure(size=16)
LabelPrint1.grid(row=6, column=0, pady=5, columnspan=3)


LabelPrint2 = customtkinter.CTkLabel(window,
                        text="",
                        fg_color="transparent",
                        )
LabelPrint2.cget("font").configure(size=16)
LabelPrint2.grid(row=7, column=0, pady=5, columnspan=3)

LabelPrint3 = customtkinter.CTkLabel(window,
                        text="",
                        fg_color="transparent",
                        )
LabelPrint3.cget("font").configure(size=16)
LabelPrint3.grid(row=8, column=0, pady=5, columnspan=3)



# -------------------- Bombo boxes -----------------------
gender = ["man", "woman"]
gendercombo = customtkinter.CTkComboBox(window, values=gender)
gendercombo.grid(row=3, column=1, padx=20, pady=5)



# --------------------- Enteries ---------------------------

entry1 = customtkinter.CTkEntry(window, placeholder_text="70")
entry1.grid(row=2, column=0, padx=20, pady=5)

entry2 = customtkinter.CTkEntry(window, placeholder_text="1.85")
entry2.grid(row=4, column=0, padx=20, pady=5)

waistentery = customtkinter.CTkEntry(window, placeholder_text="89")
waistentery.grid(row=2, column=2, padx=20, pady=5)

hipentery = customtkinter.CTkEntry(window, placeholder_text="100")
hipentery.grid(row=4, column=2, padx=20, pady=5)


# ------------------ Buttons ---------------------------------
button = customtkinter.CTkButton(window,
                                 text="Calcualation",
                                 command=calculate
                                 )
button.grid(row=5, column=1, padx=20, pady=20)




window.mainloop()