import cv2
import pytesseract as pt
import numpy as np
from tkinter import *

pt.pytesseract.tesseract_cmd = r'E:\Tesseract-OCR\tesseract.exe'

img = cv2.imread('bsx_oto.png')

'''LAY MA MAU
opencv chỉ chấp nhận RGB trong BGR
'''
''''
'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
'''

'''XU LY ANH'''

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] #tach nen
binary = cv2.medianBlur(binary,5)

kernel1 = np.ones((5,5),np.uint8)
binary = cv2.dilate(binary, kernel1, iterations = 2)

kernel2 = np.ones((5,5),np.uint8)
binary = cv2.erode(binary, kernel2, iterations = 2)

kernel3 = np.ones((5,5),np.uint8)
binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel3)

binary = cv2.bilateralFilter(binary, 11, 17, 17)  # Blur to reduce noise



text = pt.image_to_string(binary, lang='eng', config ='-l eng --psm 6 --oem 3')

# print('text',text)

cv2.imshow('First', img)
cv2.imshow('Result', binary)
# cv2.waitKey(0) #dung tat anh de hien thị thoi gian dai

top = Tk()
top.geometry("400x120")
top.title("Bien So Xe")
top.config(bg='lightblue')

dict1 = {
    11: 'Cao Bang', 12: 'Lang Son', 14: 'Quang Ninh', 15: 'Hai Phong', 16: 'Hai Phong', 17: 'Thai Binh', 18: 'Nam Dinh', 19: 'Phu Tho', 20: 'Thai Nguyen',
    21: 'Yen Bai', 22: 'Tuyen Quang', 23: 'Ha Giang', 24: 'Lao Cai', 25: 'Lai Chau', 26: 'Son La', 27: 'Dien Bien', 28: 'Hoa Binh', 29: 'Ha Noi', 30: 'Ha Noi',
    31: 'Ha Noi', 32: 'Ha Noi', 33: 'Ha Tay', 34: 'Hai Duong', 35: 'Ninh Binh', 36: 'Thanh Hoa', 37: 'Nghe An', 38: 'Ha Tinh',
    43: 'Da Nang', 47: 'Da Nang', 48: 'Dak Nong', 49: 'Lam Dong', 50: 'Tp.HCM',
    51: 'Tp.HCM',52: 'Tp.HCM',53: 'Tp.HCM',54: 'Tp.HCM',55: 'Tp.HCM',56: 'Tp.HCM',57: 'Tp.HCM',58: 'Tp.HCM',59: 'Tp.HCM', 60: 'Dong nai',
    61: 'Binh Duong', 62: 'Long An', 63: 'Tien Giang', 64: 'Vinh Long', 65: 'Can Tho', 66: 'Dong Thap', 67: 'An Giang', 68: 'Kien Giang', 69: 'Ca Mau', 70: 'Tay Ninh',
    71: 'Ben Tre', 72: 'Ba Ria Vung Tau', 73: 'Quang Binh', 74: 'Quang Tri', 75: 'Hue', 76: 'Quang Ngai', 77: 'Binh Dinh', 78: 'Phu Yen', 79: 'Khanh Hoa',
    81: 'Gia Lai', 82: 'Kon Tum', 83: 'Soc Trang', 84: 'Tra Vinh', 85: 'Ninh Thuan', 86: 'Binh Thuan', 88: 'Vinh Phuc', 89: 'Hung Yen', 90: 'Ha Nam',
    92: 'Quang Nam', 93: 'Binh Phuoc', 94: 'Bac Lieu', 95: 'Hau Giang', 97: 'Bac Kan', 98: 'Bac Giang', 99: 'Bac Ninh'
}

def check():
    id = text[1].isnumeric()
    if id == True:
        a = int(text[0:2])
    else:
        a = int(text[0:1])
    return dict1[a]

Label(text='BIEN SO XE', font = '20', bg='lightblue', fg = 'black').place(x=10, y=15)
Label(text=text, font = '30', bg='lightblue', fg = 'black').place(x=25, y=50)

Label(text='TINH THANH', font = '20', bg='lightblue', fg = 'black').place(x=260, y=15)
Label(text=check(), font = '30', bg='lightblue', fg = 'black').place(x=275, y=50)

top.mainloop()
