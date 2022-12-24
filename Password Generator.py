import random as r

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

for i in range(4):
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

input()


