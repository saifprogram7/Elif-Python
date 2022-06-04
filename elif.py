#Using ELIF Statement
leveloneaccess = True
leveltwoaccess = True
levelthreeaccess = False
if leveloneaccess == True:
    print("Access Granted")
elif leveltwoaccess == True:
    print("Access Granted")
elif levelthreeaccess == True:
    print("Access Granted")
else:
    print("Access Denied")
#Simplify ELIF Statement
oneaccess = False
twoaccess = True
threeaccess = True
if oneaccess == True and twoaccess == True:
    print("Access Granted")
elif twoaccess == True and threeaccess == False:
    print("Access Granted")
else:
    print("Access Denied")