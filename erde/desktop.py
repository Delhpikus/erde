#import modulů, které jsou nutné pro fungování
from tkinter import *
from time import strftime
from datetime import *
import os

#vytvoření funkce init pro tkinter 
class Main:
	def __init__ (self,root):
		self.root = root
		self.root.title("Desktop")
		self.root.geometry("300x300")
  
#tkinter konfigurace
if __name__ == '__main__':
	root = Tk()
	root.attributes('-fullscreen', True)
	root.columnconfigure(0, weight=1)
	root.rowconfigure(0, weight=1)
	container = Frame(root)
	container.grid(row=0, column=0)
 
#import obrázků pro ikony aplikací
	icon_exit = PhotoImage(file = r"/opt/erde/img/exit.png")
	icon_off = PhotoImage(file = r"/opt/erde/img/power.png")
	icon1 = PhotoImage(file = r"/opt/erde/img/browser.png")
	icon2 = PhotoImage(file = r"/opt/erde/img/image.png")
	icon3 = PhotoImage(file = r"/opt/erde/img/calendar.png")
	icon4 = PhotoImage(file = r"/opt/erde/img/calculator.png")
	icon5 = PhotoImage(file = r"/opt/erde/img/store.png")
	icon6 = PhotoImage(file = r"/opt/erde/img/folder.png")
	icon7 = PhotoImage(file = r"/opt/erde/img/text_editor.png")
	icon8 = PhotoImage(file = r"/opt/erde/img/email.png")
	icon9 = PhotoImage(file = r"/opt/erde/img/docs.png")
	icon10 = PhotoImage(file = r"/opt/erde/img/settings.png")
	
	
#vytvoření tlačítek pro spoučtění aplikací	
	button1 = Button(container, width = 120, height = 120, borderwidth = 0, image = icon1, command = lambda: os.system("firefox")).grid(column = 0, row = 1, padx = 30)
	label = Label(container, text = 'Internet', font =('Roboto', 15, 'bold')).grid(column = 0, row = 2)
	
#aplikace se spouští pomocí funkce, která využívá modul os a jeho funkci system pro zapsání jména aplikace do terminálu, čímž se apliakce spustí
	button2 = Button(container, width = 120, height = 120, borderwidth = 0, image = icon2, command = lambda: os.system("eog")).grid(column = 1, row = 1, padx = 30)
	label = Label(container, text = 'Galerie', font =('Roboto', 15, 'bold')).grid(column = 1, row = 2, padx = 20)
	
	button3 = Button(container, width = 120, height = 120, borderwidth = 0, image = icon3, command = lambda: os.system("gnome-calendar")).grid(column = 2, row = 1, padx = 30)
	label = Label(container, text = 'Kalendář', font =('Roboto', 15, 'bold')).grid(column = 2, row = 2)
	
	button4 = Button(container, width = 120, height = 120, borderwidth = 0, image = icon4, command = lambda: os.system("gnome-calculator")).grid(column = 3, row = 1, padx = 30)
	label = Label(container, text = 'Kalkulačka', font =('Roboto', 15, 'bold')).grid(column = 3, row = 2)
	
	button5 = Button(container, width = 120, height = 120, borderwidth = 0, image = icon5, command = lambda: os.system("gnome-software")).grid(column = 4, row = 1, padx = 30)
	label = Label(container, text = 'Obchod', font =('Roboto', 15, 'bold')).grid(column = 4, row = 2)
	
	button6 = Button(container, width = 120, height = 120, borderwidth = 0, image = icon6, command = lambda: os.system("nautilus")).grid(column = 0, row = 3, padx = 30)
	label = Label(container, text = 'Soubory', font =('Roboto', 15, 'bold')).grid(column = 0, row = 4)
	
	button7 = Button(container, width = 120, height = 120, borderwidth = 0, image = icon7, command = lambda: os.system("gedit")).grid(column = 1, row = 3, padx = 30)
	label = Label(container, text = 'Textový editor', font =('Roboto', 15, 'bold')).grid(column = 1, row = 4)
	
	button8 = Button(container, width = 120, height = 120, borderwidth = 0, image = icon8, command = lambda: os.system("thunderbird")).grid(column = 2, row = 3, padx = 30)
	label = Label(container, text = 'E-mail', font =('Roboto', 15, 'bold')).grid(column = 2, row = 4)
	
	button9 = Button(container, width = 120, height = 120, borderwidth = 0, image = icon9, command = lambda: os.system("evince")).grid(column = 3, row = 3, padx = 30)
	label = Label(container, text = 'Dokumenty', font =('Roboto', 15, 'bold')).grid(column = 3, row = 4)
	
	button10 = Button(container, width = 120, height = 120, borderwidth = 0, image = icon10, command = lambda: os.system("gnome-control-center")).grid(column = 4, row = 3, padx = 30)
	label = Label(container, text = 'Nastavení', font =('Roboto', 15, 'bold')).grid(column = 4, row = 4)

#tlačítko pro vypnutí počítače
	off_button = Button(root, width = 120, height = 120, borderwidth = 0, image = icon_off, command = lambda: os.system("poweroff"))
	off_button.place(relx = 0.90, rely = 0)

#tlačítko pro ukončení skriptu
	exit_button = Button(root, width = 120, height = 120, borderwidth = 0, image = icon_exit, command = lambda: exit())
	exit_button.place(relx = 0.90, rely = 0.85)

#vytvoření popisu pro funkční hodiny
	clock_label = Label(root, fg="black", font = ("Roboto", 25, 'bold'), relief='flat')
	clock_label.place(relx = 0.02, rely = 0.03)
	
	date_label = Label(root, fg="black", font = ("Roboto", 25, 'bold'), relief='flat')
	date_label.place(relx = 0.41, rely = 0.03)

#funkce, která zobrazuje aktuální čas ze systému a aktualizuje se každou vteřinu
	def update_label():
		current_time = strftime('%-H: %M: %S')
		current_date = datetime.now().strftime('%-d. %B')
		
#přepsání anglického názvu měsíce do češtiny
		if "January" in current_date:
			current_date = current_date.replace("January", "Ledna")
		elif "February" in current_date:
			current_date = current_date.replace("February", "Února")
		elif "March" in current_date:
			current_date = current_date.replace("March", "Března")
		elif "April" in current_date:
			current_date = current_date.replace("April", "Dubna")
		elif "May" in current_date:
			current_date = current_date.replace("May", "Května")
		elif "June" in current_date:
			current_date = current_date.replace("June", "Června")
		elif "July" in current_date:
			current_date = current_date.replace("July", "Července")
		elif "August" in current_date:
			current_date = current_date.replace("August", "Srpna")
		elif "September" in current_date:
			current_date = current_date.replace("September", "Září")
		elif "October" in current_date:
			current_date = current_date.replace("October", "Října")
		elif "November" in current_date:
			current_date = current_date.replace("November", "Listopadu")
		elif "December" in current_date:
			current_date = current_date.replace("December", "Prosince")
			
#funkce volá sama sebe po jedné vteřině	
		clock_label.configure(text = current_time)
		clock_label.after(80, update_label)
		date_label.configure(text = current_date)

#skript se spustí
	update_label()
	obj = Main(root)
	root.mainloop()
