from tkinter import *
from tkinter import ttk
from tkinter import messagebox


#list for dropdown of type
type_list = ['LH','LA','TR','CA','Mess','Shop','Moot Court','Wellness Center','IT Department','Boys Washroom','Girls Washroom','Admin Desk']

#function to change input to meaningful string that this program can use
def filename(block,type,roomno):
    type_list1 = ['LH','LA','TR','CA']  
    type_code_list = ['LH','LA','TR','CA']
    if type in type_list1:
        index = type_list1.index(type)
        filep = block + str(type_code_list[index]) + roomno
    else:
        filep=type
    return filep


#room names for blockB for error coding and path decision
rooms=['Mess','Shop','Wellness Center','IT Derpartment','Boys Washroom','Girls Washroom','Admin Desk','Moot Court','BLA101','BLA102','BLA103','BLA104','BLA105','BLA106A','BLA106B','BLA106C','BLA106D','BLA108A','BLA108B','BLA108C','BLA107','BLA109','BLA110','BLA206','BLA205','BLA204','BLA203','BLA202A','BLA202B','BCA220','BCA219','BLA201','BTR218','BLA217','BLA215','BLA214','BLA213','BLA212','BLA211A','BLA211B','BLA210','BLA209','BLA208','BLA207','BTR222','BTR221','BLA216','BTR223','BLA308','BCA312','BCA311','BLA306A','BLA306B','BCA310','BCA309','BLA304','BTR308','BTR307','BLA303','BCA306','BCA305','BLA302A','BLA302B','BCA304','BCA303','BLA301','BTR302','BTR301','BLA307','BLA305']
patha = ['BLA308','BCA312','BCA311','BLA306A','BLA306B','BCA310','BCA309','BLA304','BTR308','BTR301','Boys Washroom','BTR302','BTR307']
pathb = ['BLA307','BLA303','BCA306','BCA305','BLA302A','BLA302B','BCA304','BCA303','BLA301','BLA305','Girls Washroom']
patha2 = ['BLA206','BLA205','BLA204','BLA203','BLA202A','BLA202B','BCA220','BCA219','BLA201','BTR218','Boys Washroom','Girls Washroom','BTR223']
pathb2 = ['BLA217','BLA215','BLA214','BLA213','BLA212','BLA211A','BLA211B','BLA210','BLA209','BLA208','BLA207','BTR222','BLA216']

#path for checking routes for stairs
Path0='P'
Path1='A'
Path2='B'


#function for getting inputs (main GUI interface)
def DISPLAY():
    global entry1
    global entry2
    #get for getting input from main interface
    block = click.get()
    type = click1.get()
    roomno = entry2.get()
    filep1= filename(block,type,roomno) 
    if filep1 not in rooms:
        messagebox.showerror('Room not found', 'Please enter the appropriate details')
    else:
        window.destroy()
        gfloor=['Mess','Shop','Moot Court','Wellness Center','IT Department','Admin Desk']
        if type in gfloor:
            floor=0
        else:
            floor=int(roomno[0])

        #functions for changing paths
        def QMaker():
            win.destroy()
            global Path0
            Path0='Q'
        def LiftMaker():
            win.destroy()
            global Path0
            Path0='Lift'      
        
        
        if filep1 in patha:
            Path1 = 'B'
            Path2 = 'A'
        elif filep1 in pathb:
            Path1 = 'A'
            Path2 = 'B'

        elif filep1 in patha2:
            Path1 = 'A'
        elif filep1 in pathb2:
            Path1 = 'B'

    #Floor 0------------------------------Floor 0------------------------------------------------Floor 0---------------------------------------------------Floor 0--------------------------------------------------Floor 0# 


        #part for ground floor
        if floor==0:   
            win = Tk()
            win.geometry("2560x1440")
            win.configure(bg = "#000000")
            canvas = Canvas(
                win,
                bg = "#000000",
                height = 1440,
                width = 2560,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
            canvas.place(x = 0, y = 0)

            lol_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\Floor\Floor 0\{}.png".format(filep1))
            Trial = canvas.create_image(
            1280.0, 690.0,
            image=lol_img)
            win.mainloop()

    #FLOOR 1----------------------------------------------FLOOR 1------------------------------------------------FLOOR 1------------------------------------------FLOOR 1----------------------------------------FLOOR 1# 

        #part for first floor
        elif floor==1:
            win = Tk()
            win.geometry("2560x1440")
            win.configure(bg = "#000000")
            canvas = Canvas(
                win,
                bg = "#000000",
                height = 1440,
                width = 2560,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
            canvas.place(x = 0, y = 0)

            lol_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\Floor\Defaults\choice.png")
            Trial = canvas.create_image(
            1280.0, 690.0,
                image=lol_img)

            #code for stair choice buttons
            P_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\Buttons\StairsP.png")
            StairP = Button(
                image = P_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = win.destroy,
                relief = "flat")

            StairP.place(x = 1694, y = 1222)

            
            #code for stair choice buttons
            li_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\Buttons\LIFT BUTTON.png")
            lift = Button(
                win,
                image = li_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = LiftMaker,
                relief = "flat")

            lift.place(x = 1164, y = 1222)

            #code for stair choice buttons
            Q_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\Buttons\StairQ.png")
            StairQ = Button(
                win,
                image = Q_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = QMaker,
                relief = "flat")

            StairQ.place(x = 634, y = 1222)

            win.mainloop()
            #mainloop end for tkinter window
            

            #checking for choice for stair or lift and codes for same
            if Path0=='Lift':
                win = Tk()
                win.geometry("2560x1440")
                win.configure(bg = "#000000")
                canvas = Canvas(
                    win,
                    bg = "#000000",
                    height = 1440,
                    width = 2560,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
                canvas.place(x = 0, y = 0)

                lol_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\Floor\Floor 1\from lift\{}.png".format(filep1))
                Trial = canvas.create_image(
                1280.0, 690.0,
                    image=lol_img)
                win.mainloop()
            else:
                win = Tk()
                win.geometry("2560x1440")
                win.configure(bg = "#000000")
                canvas = Canvas(
                    win,
                    bg = "#000000",
                    height = 1440,
                    width = 2560,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
                canvas.place(x = 0, y = 0)

                lol_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\Floor\Floor 1\from stairs\Stair {}\{}.png".format(Path0,filep1))
                Trial = canvas.create_image(
                1280.0, 690.0,
                    image=lol_img)
                win.mainloop()


    #FLOOR 2-----------------------------------------------------------------FLOOR 2--------------------------------------------------------------FLOOR 2----------------------------------------------FLOOR 2#   

        #code for second floor
        elif floor==2:
            win = Tk()
            win.geometry("2560x1440")
            win.configure(bg = "#000000")
            canvas = Canvas(
                win,
                bg = "#000000",
                height = 1440,
                width = 2560,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
            canvas.place(x = 0, y = 0)

            lol_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\Floor\Defaults\choice.png")
            Trial = canvas.create_image(
            1280.0, 690.0,
                image=lol_img)


            P_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\Buttons\StairsP.png")
            StairP = Button(
                image = P_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = win.destroy,
                relief = "flat")

            StairP.place(x = 1694, y = 1222)


            li_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\Buttons\LIFT BUTTON.png")
            lift = Button(
                win,
                image = li_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = LiftMaker,
                relief = "flat")

            lift.place(x = 1164, y = 1222)

            Q_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\Buttons\StairQ.png")
            StairQ = Button(
                win,
                image = Q_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = QMaker,
                relief = "flat")

            StairQ.place(x = 634, y = 1222)

            win.mainloop()
            
            if Path0=='Lift':
                win = Tk()
                win.geometry("2560x1440")
                win.configure(bg = "#000000")
                canvas = Canvas(
                    win,
                    bg = "#000000",
                    height = 1440,
                    width = 2560,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
                canvas.place(x = 0, y = 0)

                lol_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\Floor\Floor {}\from lift\{}.png".format(floor,filep1))
                Trial = canvas.create_image(
                1280.0, 690.0,
                    image=lol_img)
                win.mainloop() 
            else:
                win = Tk()
                win.geometry("2560x1440")
                win.configure(bg = "#000000")
                canvas = Canvas(
                    win,
                    bg = "#000000",
                    height = 1440,
                    width = 2560,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
                canvas.place(x = 0, y = 0)
                lol_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\Floor\Defaults\STAIR{} TO STAIR{}.png".format(Path0,Path1))
                Trial = canvas.create_image(
                1280.0, 690.0,
                    image=lol_img)

                #code for button to next floor
                Next_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\Buttons\NextFloor.png")
                Next = Button(
                    image = Next_img,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = win.destroy,
                    relief = "flat")

                Next.place(x = 1164, y = 1222)
                win.mainloop()
                
                win = Tk()
                win.geometry("2560x1440")
                win.configure(bg = "#000000")
                canvas = Canvas(
                    win,
                    bg = "#000000",
                    height = 1440,
                    width = 2560,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
                canvas.place(x = 0, y = 0)

                lol_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\Floor\Floor {}\from stairs\{}.png".format(floor,filep1))
                Trial = canvas.create_image(
                1280.0, 690.0,
                    image=lol_img)
                win.mainloop()


    #FLOOR 3---------------------------------FLOOR 3--------------------------------------------FLOOR 3---------------------------------------------------FLOOR 3-------------------------------------FLOOR 3#

        #code for third floor
        

        elif floor==3:
            win = Tk()
            win.geometry("2560x1440")
            win.configure(bg = "#000000")
            canvas = Canvas(
                win,
                bg = "#000000",
                height = 1440,
                width = 2560,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
            canvas.place(x = 0, y = 0)

            lol_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\Floor\Defaults\choice.png")
            Trial = canvas.create_image(
            1280.0, 690.0,
                image=lol_img)


            P_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\Buttons\StairsP.png")
            StairP = Button(
                image = P_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = win.destroy,
                relief = "flat")

            StairP.place(x = 1694, y = 1222)


            li_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\Buttons\LIFT BUTTON.png")
            lift = Button(
                win,
                image = li_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = LiftMaker,
                relief = "flat")

            lift.place(x = 1164, y = 1222)

            Q_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\Buttons\StairQ.png")
            StairQ = Button(
                win,
                image = Q_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = QMaker,
                relief = "flat")

            StairQ.place(x = 634, y = 1222)

            win.mainloop()
            

            #code again fro paths
            if Path0=='Lift':
                win = Tk()
                win.geometry("2560x1440")
                win.configure(bg = "#000000")
                canvas = Canvas(
                    win,
                    bg = "#000000",
                    height = 1440,
                    width = 2560,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
                canvas.place(x = 0, y = 0)

                lol_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\Floor\Floor {}\from lift\{}.png".format(floor,filep1))
                Trial = canvas.create_image(
                1280.0, 690.0,
                    image=lol_img)
                win.mainloop() 
            else:
                win = Tk()
                win.geometry("2560x1440")
                win.configure(bg = "#000000")
                canvas = Canvas(
                    win,
                    bg = "#000000",
                    height = 1440,
                    width = 2560,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
                canvas.place(x = 0, y = 0)
                lol_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\Floor\Defaults\STAIR{} TO STAIR{}.png".format(Path0,Path1))######
                Trial = canvas.create_image(
                1280.0, 690.0,
                    image=lol_img)
                Next_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\Buttons\NextFloor.png")
                Next = Button(
                    image = Next_img,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = win.destroy,
                    relief = "flat")

                #code for button to next floor
                Next.place(x = 1164, y = 1222)
                win.mainloop()

                win = Tk()
                win.geometry("2560x1440")
                win.configure(bg = "#000000")
                canvas = Canvas(
                    win,
                    bg = "#000000",
                    height = 1440,
                    width = 2560,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
                canvas.place(x = 0, y = 0)
                lol_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\Floor\Defaults\STAIR{} TO STAIR{}.png".format(Path1,Path2))######
                Trial = canvas.create_image(
                1280.0, 690.0,
                    image=lol_img)



                Next_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\Buttons\NextFloor.png")
                Next = Button(
                    image = Next_img,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = win.destroy,
                    relief = "flat")

                Next.place(x = 1164, y = 1222)
                win.mainloop()
                
                win = Tk()
                win.geometry("2560x1440")
                win.configure(bg = "#000000")
                canvas = Canvas(
                    win,
                    bg = "#000000",
                    height = 1440,
                    width = 2560,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
                canvas.place(x = 0, y = 0)

                lol_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\Floor\Floor {}\from stairs\{}.png".format(floor,filep1))
                Trial = canvas.create_image(
                1280.0, 690.0,
                    image=lol_img)
                win.mainloop()


#MAIN------------------------MAIN------------------------MAIN-----------------------------------MAIN-------------------------------MAIN----------------------------MAIN#
        

window = Tk()

window.geometry("1000x600")
window.configure(bg = "#000000")
canvas = Canvas(
    window,
    bg = "#000000",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\T1\Design\background.png")
background = canvas.create_image(
    370.0, 268.0,
    image=background_img)

entry0_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\T1\Design\img_textBox0.png")
entry0_bg = canvas.create_image(
    497.0, 209.0,
    image = entry0_img)




entry1_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\T1\Design\img_textBox2.png")
entry1_bg = canvas.create_image(
    497.0, 314.0,
    image = entry1_img)

click1=StringVar()
click1.set('Select the type of room')
entry1=OptionMenu(window,click1,*type_list)
entry1.configure(direction='right',background="#0f0e0e",fg = '#ffffff',highlightbackground='#0f0e0e',borderwidth=0,justify='left')
entry1['menu'].configure(background="#0f0e0e",fg = '#ffffff',borderwidth=0)
entry1.pack()
entry1.place(
    x = 314.0, y = 296,
    width = 366.0,
    height = 36)

entry2_img = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\T1\Design\img_textBox1.png")
entry2_bg = canvas.create_image(
    500.0, 422.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#0f0e0e",
    fg = '#FFFFFF',
    highlightthickness = 0,
    insertbackground= 'white')
    
entry2.place(
    x = 314.0, y = 404,
    width = 366.0,
    height = 36)

img0 = PhotoImage(file = r"C:\Users\sdzyr\Desktop\University\Programms\UI test\T1\Design\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = DISPLAY,
    relief = "raised")

b0.place(
    x = 419, y = 497,
    width = 147,
    height = 36)

options = ['B']
click = StringVar()
click.set('Select Block')

drop= OptionMenu(window , click , *options)
drop.configure(direction='right',background="#0f0e0e",fg = '#ffffff',highlightbackground='#0f0e0e',borderwidth=0,justify='left')
drop['menu'].configure(background="#0f0e0e",fg = '#ffffff',borderwidth=0)
drop.pack()
drop.place(
    x = 314.0, y = 187,
    width = 366.0,
    height = 36)

window.resizable(False, False)
window.mainloop()
