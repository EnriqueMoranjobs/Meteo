
import tkinter as tk

LARGE_FONT = ("Verdana",12)

class SeaofBTCapp(tk.Tk):
    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self,*args, **kwargs)
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        #diccionario vacio
        self.frames={}

        for F in(StartPage,PageOne):
            frame= F(container,self)
            self.frames[F]= frame
            frame.grid(row=0, column=0, sticky = "nsew")

   
       
        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text ="Start page", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        button = tk.Button(self,text="PAGINA1",command=lambda: controller.show_frame(PageOne))
        button.pack()

class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text ="page oneeee", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self,text="Back to home",
        command= lambda:controller.show_frame(StartPage))
        button1.pack()

app=SeaofBTCapp()
app.mainloop()

    
    


