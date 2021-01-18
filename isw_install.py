#! /usr/bin/python3

from tkinter import *
from tkinter import messagebox
import git
import getpass
import os

username = getpass.getuser()
path_check = "/home/" + username + "/isw"
check = os.path.exists(path_check)
path = "/home/" + username

window = Tk()
window.title('ISW-GUI')

lable1 = Label(window, text = "ISW is opposite of MSI", fg = 'red', font=("Helvetica", 20))
lable1.grid(row = 1, column = 0)
lable2 = Label(window, text = "please enter your laptop model.\nFor model details visit :-> https://github.com/YoyPa/isw", fg = 'black', font=("Helvetica", 16))
lable2.grid(row = 2, column = 0)

laptop_model = Entry(window, font=("Helvetica", 20))
laptop_model.grid(row = 3, column = 0)

def install():
    if check == False:
        git.Git(path).clone("https://github.com/YoyPa/isw")
        messagebox.showinfo('ISW-GUI', 'ISW folder is copied to HOME folder from GIT page!\nSystem will reboot now and then set your laptop model fan speed curve!')
    if check == True:
        messagebox.showinfo('ISW-GUI', 'ISW folder already exist!')
    os.system("gnome-terminal -e 'bash -c \"sudo apt install nautilus-admin && sudo isw -r && install -Dm 644 etc/isw.conf \"${pkgdir}/etc/isw.conf\" && install -Dm 644 etc/modprobe.d/isw-ec_sys.conf \"${pkgdir}/etc/modprobe.d/isw-ec_sys.conf\" && install -Dm 644 etc/modules-load.d/isw-ec_sys.conf \"${pkgdir}/etc/modules-load.d/isw-ec_sys.conf\" && install -Dm 644 usr/lib/systemd/system/isw@.service \"${pkgdir}/usr/lib/systemd/system/isw@.service\" && install -Dm 755 isw \"${pkgdir}/usr/bin/isw\"; exec bash\"'")
    os.system("gnome-terminal -x reboot")
    return

def monitor():
    laptop = laptop_model.get()
    messagebox.showinfo('Message', 'You clicked the monitor button!')
    command = "gnome-terminal -x sudo isw -w " + laptop
    os.system(command)
    os.system("gnome-terminal -x sudo isw -r")
    return

def startup():
    laptop = laptop_model.get()
    command = "gnome-terminal -x systemctl enable isw@" + laptop + ".service"
    messagebox.showinfo('Message', 'You clicked the startup button!')
    os.system(command)
    return

def uninstall():
    messagebox.showinfo('Message', 'You clicked the uninstall ISW button!')
    os.system("gnome-terminal -e 'bash -c \"sudo rm /etc/isw.conf /etc/modprobe.d/isw-ec_sys.conf /etc/modules-load.d/isw-ec_sys.conf /usr/lib/systemd/system/isw@.service /usr/bin/isw; exec bash\"'")
    messagebox.showinfo('ISW-GUI', 'ISW is installed.\nSystem will reboot now and then set your laptop model fan speed curve!')
    os.system("gnome-terminal -x reboot")
    return

button1 = Button(window, text = "Install ISW", width = 20, fg = 'blue', command = install)
button1.grid(row = 4, column = 0)
button3 = Button(window, text = "Monitor Temperature", width = 20, fg = 'green', command = monitor)
button3.grid(row = 5, column = 0)
button4 = Button(window, text = "Run at Startup", width = 20, fg = 'yellow', command = startup)
button4.grid(row = 6, column = 0)
button5 = Button(window, text = "Uninstall ISW", width = 20, fg = 'red', command = uninstall)
button5.grid(row = 7, column = 0)

window.mainloop()
