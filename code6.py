import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk 
from tkinter import ttk
from PIL import ImageTk
Large_Font = ("Verdana",12)
class seaoapp(tk.Tk):
	#this will alwase run when you start your class 
	#like when you start computer there are programmes shoud be run
	# args any number of variable to the functions 
	#kwargs to pass adictionary thro the function
	def __init__ (self,*args,**kwargs):
		''' this is a basic programme to have multi screen on tkinter '''
		# to initilaize tk 
		tk.Tk.__init__(self,*args,**kwargs)
		#to add icon to our broject
		ic = '~/Destop/sendxtk/4.ico'
		#tk.Tk.iconbitmap(self,default='4.ico')
		tk.Tk.wm_title(self,"sea of BTC client")
		#to make a contanier for your programme 
		container = tk.Frame(self)
		container.pack(side='top',fill="both",expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)
		self.frames={}
		for F in (StartPage,PageOne, PageTow ,PageThree):
			frame = F(container,self)
			self.frames[F] = frame
			#we will use grid
			#sticky = north south est west to stritch every thing to the size of the window

			frame.grid(row=0,column=0,sticky="nsew")		




		self.show_frame(StartPage)
	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		self.image1 = tk.PhotoImage(file="1.png")
		label = ttk.Label(self,text="START Page",image=self.image1,compound="right",font =Large_Font)
		label.pack(pady=10,padx=10)
		self.image = tk.PhotoImage(file="4.png")

		button = ttk.Button(self,text="vistit page 1",image=self.image,compound="left",command=lambda:controller.show_frame(PageOne) )
		#button.image=image
		

		button.pack()
		
		button1 = ttk.Button(self,text="vistit page 2",image=self.image,compound="left",command=lambda:controller.show_frame(PageTow) ).pack()
		button1 = ttk.Button(self,text="Grap page",image=self.image,compound="left",command=lambda:controller.show_frame(PageThree) ).pack()
class PageOne(tk.Frame):
	def __init__ (self,parent,controller):
		tk.Frame.__init__(self,parent)
		self.image = tk.PhotoImage(file="4.png")
		self.image1 = tk.PhotoImage(file="1.png")
		label1 = ttk.Label(self,text="first Page" ,image=self.image1,compound="right",font=Large_Font).pack(pady=10,padx=10)
		button1 = ttk.Button(self,text="pack to start page",image=self.image,compound="left",command=lambda:controller.show_frame(StartPage) ).pack()
		button1 = ttk.Button(self,text="vistit page 2",image=self.image,compound="left",command=lambda:controller.show_frame(PageTow) ).pack()

class PageTow(tk.Frame):
	def __init__ (self,parent,controller):
		tk.Frame.__init__(self,parent)
		self.image = tk.PhotoImage(file="4.png")
		self.image1 = tk.PhotoImage(file="1.png")
		label2 = ttk.Label(self,text="Page Tow !!" ,image=self.image1,compound="right",font=Large_Font).pack(pady=10,padx=10)
		button2 = ttk.Button(self,text="pack to start page",image=self.image,compound="left",command=lambda:controller.show_frame(StartPage) ).pack()
		button1 = ttk.Button(self,text="vistit page 1",image=self.image,compound="left",command=lambda:controller.show_frame(PageOne) ).pack()
class PageThree(tk.Frame):
	def __init__ (self,parent,controller):
		tk.Frame.__init__(self,parent)
		self.image = tk.PhotoImage(file="4.png")
		self.image1 = tk.PhotoImage(file="1.png")
		label2 = ttk.Label(self,text="Graph Page  !!" ,image=self.image1,compound="right",font=Large_Font).pack(pady=10,padx=10)
		button2 = ttk.Button(self,text="pack to start page",image=self.image,compound="left",command=lambda:controller.show_frame(StartPage) ).pack()
		f = Figure(figsize=(5,5),dpi=100)
		a = f.add_subplot(111)
		a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
		canvas = FigureCanvasTkAgg(f,self)
		#canvas.show()
		#canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)
		#add navigator bar
		toolbar = NavigationToolbar2TkAgg(canvas,self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)	
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)	






























app = seaoapp()
app.mainloop()
