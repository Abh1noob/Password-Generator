import random as r
import xlsxwriter as x
import pyperclip

workbook = x.Workbook(r'C:\Users\Admin\Desktop\userpass.xlsx')
worksheet = workbook.add_worksheet()

length = int(input("Enter Length of Password: "))
username = input("Enter Username: ")

sml = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cap = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
num = ["1","2","3","4","5","6","7","8","9","0"]
spl = ["@","#","%","&","*","(",")","!",".","/"]

choic = ["sml","cap","num","spl"]
pwd = []
fpwd = ""

pwd.append(r.choice(sml))
pwd.append(r.choice(cap))
pwd.append(r.choice(num))
pwd.append(r.choice(spl))

if length<4:
    print("Minimum Length is 4")
else:
    for i in range(length-4):
        a = r.choice(choic)

        if a == 'sml':
            pwd.append(r.choice(sml))

        if a == 'cap':
            pwd.append(r.choice(cap))

        if a == 'num':
            pwd.append(r.choice(num))

        if a == 'spl':
            pwd.append(r.choice(spl))

    r.shuffle(pwd)

    for i in pwd:
        fpwd+=i

print(fpwd)

pyperclip.copy(fpwd)

worksheet.write(0,0,'Username')
worksheet.write(0,1,'Password')

worksheet.write(1,0,username)
worksheet.write(1,1,fpwd)

workbook.close()

input()


