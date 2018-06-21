#
#  Adress book
#  
#
#  Created by Tarlan Askaruly.
#  Copyright (c) 2018 Tarlan Askaruly. All rights reserved.
#

def close_win(event):
    root.destroy()

def writing(event):
    if nameent.get() == "" or snameent.get() == "" or addressent.get() == "":
        root3=Tk()
        Presencelab=Label(root3, text='Fill in the fields') 
        Presencelab.grid(row=1, column= 1)
    else :
        file = open('addressbook.txt','r+') 
        file.write('Info about client:'+'\n') 
        file.write('Name:')
        if nameent.get().isdigit() or snameent.get().isdigit() :
            root5=Tk()
            Formatlab=Label(root5, text='Letters only') 
            Formatlab.grid(row=1, column= 1)
        else:
            file.write(nameent.get()+'\n') 
            file.write('Surname:')
            file.write(snameent.get()+'\n')
        file.write('Address:') 
        file.write(addressent.get()+'\n') 
        file.write('Phone Number:')
        if len(phoneent.get()) == 11 and phoneent.get().isdigit():
            file.write(phoneent.get()+'\n')
        else :
            root4=Tk()
            Lengthlab=Label(root4, text='Phone number must contain exactly 11 numbers') 
            Lengthlab.grid(row=1, column= 1)
        file.close()

def search(event):
    def p(SEARCH): 
        for i, line in enumerate(searchlines):
            if searchent.get() in line: 
                for l in searchlines[i:i+5]: 
                    search_r.insert(END, l) 
    root2=Tk() 
    searchlab=Label(root2, text="Search:") 
    searchlab.grid(row=1, column= 1) 
    searchent=Entry(root2, width=10,bd=6) 
    searchent.grid(row=1,column=2) 
    search_r=Text(root2, width=25,bd=6,height=5, wrap="word") 
    search_r.grid(row=2,column=2) 
    s = open("addressbook.txt", "r") 
    searchingbut=Button(root2,text="Search",width=10,bd=6) 
    searchingbut.grid(row=3,column=2) 
    searchingbut.bind("<Button-1>",p) 
    searchlines=s.readlines() 
    s.close()

from tkinter import* 
root=Tk() 
m = Menu(root) 
root.config(menu=m) 
fm = Menu(m) 
m.add_cascade(label="File",menu=fm) 
fm.add_command(label="Exit",command=close_win) 
systemlab=Label(root,text="Address Book").grid(row=0,column=1) 
namelab=Label(root,text="Name").grid(row=1,column=1) 
snamelab=Label(root,text="Surname").grid(row=2,column=1) 
addresslab=Label(root,text="Address").grid(row=3,column=1) 
phonelab=Label(root,text="Phone Number").grid(row=4,column=1) 
nameent=Entry(root,width=10) 
nameent.grid(row=1,column=4) 
snameent=Entry(root,width=10) 
snameent.grid(row=2,column=4) 
addressent=Entry(root,width=10) 
addressent.grid(row=3,column=4) 
phoneent=Entry(root,width=10) 
phoneent.grid(row=4,column=4) 
addbut=Button(root,text="Save") 
exitbut=Button(root,text="Exit") 
searchbut=Button(root,text="Search")
exitbut.grid(row=5,column=2)
searchbut.grid(row=5,column=1)
addbut.grid(row=5,column=0)
searchbut.bind("<Button-1>",search)  
addbut.bind("<Button-1>",writing) 
exitbut.bind("<Button-1>",close_win) 
root.mainloop()
