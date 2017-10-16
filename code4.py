import tkinter as tk 

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
		#to make a contanier for your programme 
		container = tk.Frame(self)
		container.pack(side='top',fill="both",expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)
		self.frames={}
		for F in (StartPage,PageOne, PageTow):
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
		label = tk.Label(self,text="START Page",font =Large_Font)
		label.pack(pady=10,padx=10)
		button = tk.Button(self,text="vistit page 1",command=lambda:controller.show_frame(PageOne) ).pack()
		button1 = tk.Button(self,text="vistit page 2",command=lambda:controller.show_frame(PageTow) ).pack()

class PageOne(tk.Frame):
	def __init__ (self,parent,controller):
		tk.Frame.__init__(self,parent)
		label1 = tk.Label(self,text="first Page" ,font=Large_Font).pack(pady=10,padx=10)
		button1 = tk.Button(self,text="pack to start page",command=lambda:controller.show_frame(StartPage) ).pack()
		button1 = tk.Button(self,text="vistit page 2",command=lambda:controller.show_frame(PageTow) ).pack()

class PageTow(tk.Frame):
	def __init__ (self,parent,controller):
		tk.Frame.__init__(self,parent)
		label2 = tk.Label(self,text="Page Tow !!" ,font=Large_Font).pack(pady=10,padx=10)
		button2 = tk.Button(self,text="pack to start page",command=lambda:controller.show_frame(StartPage) ).pack()
		button1 = tk.Button(self,text="vistit page 1",command=lambda:controller.show_frame(PageOne) ).pack()


app = seaoapp()
app.mainloop()
