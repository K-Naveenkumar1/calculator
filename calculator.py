from tkinter import *
class calculator:
    def __init__(self,master):
        master.title("calcuator")
        master.geometry("357x420+0+0")
        master.config(bg='grey')
        master.resizable(False,False)

        self.equation=StringVar()
        self.Entry_value=''
        Entry(width=17,bg='#ccd',font=('arial bold',28),textvariable=self.equation).place(x=0,y=0)

        Button(width=11,height=4,text='(',relief='raised',bg='white',command=lambda:self.show('(')).place(x=0 ,y=50)
        Button(width=11,height=4,text=')',relief='raised',bg='white',command=lambda:self.show(')')).place(x=90 ,y=50 )
        Button(width=11,height=4,text='%',relief='raised',bg='white',command=lambda:self.show('%')).place(x=180 ,y=50 )
        Button(width=11,height=4,text='1',relief='raised',bg='white',command=lambda:self.show(1)).place(x=0 ,y=125 )
        Button(width=11,height=4,text='2',relief='raised',bg='white',command=lambda:self.show(2)).place(x=90 ,y=125 )
        Button(width=11,height=4,text='3',relief='raised',bg='white',command=lambda:self.show(3)).place(x=180 ,y=125 )
        Button(width=11,height=4,text='4',relief='raised',bg='white',command=lambda:self.show(4)).place(x=0 ,y=200 )
        Button(width=11,height=4,text='5',relief='raised',bg='white',command=lambda:self.show(5)).place(x=90 ,y=200 )
        Button(width=11,height=4,text='6',relief='raised',bg='white',command=lambda:self.show(6)).place(x= 180,y=200 )
        Button(width=11,height=4,text='7',relief='raised',bg='white',command=lambda:self.show(7)).place(x=0 ,y=275 )
        Button(width=11,height=4,text='8',relief='raised',bg='white',command=lambda:self.show(8)).place(x=180 ,y=275 )
        Button(width=11,height=4,text='9',relief='raised',bg='white',command=lambda:self.show(9)).place(x=90 ,y=275 )
        Button(width=11,height=4,text='0',relief='raised',bg='white',command=lambda:self.show(0)).place(x=90 ,y=350 )
        Button(width=11,height=4,text='.',relief='raised',bg='white',command=lambda:self.show('.')).place(x=180 ,y= 350)
        Button(width=11,height=4,text='+',relief='raised',bg='white',command=lambda:self.show('+')).place(x=270 ,y=275 )
        Button(width=11,height=4,text='-',relief='raised',bg='white',command=lambda:self.show('-')).place(x=270 ,y=200 )
        Button(width=11,height=4,text='/',relief='raised',bg='white',command=lambda:self.show('/')).place(x= 270,y=50 )
        Button(width=11,height=4,text='*',relief='raised',bg='white',command=lambda:self.show('*')).place(x=270 ,y=125 )
        Button(width=11,height=4,text='=',relief='raised',bg='light blue',command=self.solve).place(x=270 ,y=350 )
        Button(width=11,height=4,text='c',relief='raised',command=self.clear).place(x=0 ,y=350 )
    def show(self,value):
        self.Entry_value+=str(value)
        self.equation.set(self.Entry_value)  
    def clear (self):
        self.Entry_value=''
        self.equation.set(self.Entry_value)
    def solve(self):
        result=eval(self.Entry_value)
        self.equation.set(result)


root=Tk()
calculator=calculator(root)
root.mainloop()