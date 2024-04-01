


def BMI_Calculator(Weight, Height):
    weight=float(Weight)
    height=float(Height)
    BMI = round(weight/(height*height), 2)
    return BMI


def WHR_Calculator(Waist, Hip):
    waist=float(Waist)
    hip=float(Hip)
    WHR = round(waist/hip, 2)
    return WHR


def WHtR_Calculator(Waist, Height):
    waist=float(Waist)
    height=float(Height)
    WHtR = round((waist/height)/100, 2)
    return WHtR