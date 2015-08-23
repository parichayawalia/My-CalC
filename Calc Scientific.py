# My CalC
from tkinter import *
from statistics import *
import math
import fractions

ee, ten=math.e, 10


# Main class
class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.error=False
        self.op = ""
        self.eq = False
        self.t,self.num2=0.0, 0.0

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2   #string concatenation of nos
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):       #do all the calculations HERE
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op=="x2":
            self.total*=self.total
        if self.op=="x3":
            self.total*=self.total*self.total
        if self.op=="xy":
            self.total=xxyy(self.total,self.current)
        if self.op=="ex":
            self.total= ee**self.total             #using same exponential function
        if self.op=="tenx":
           self.total=xxyy(ten, self.total)
        if self.op=="fracx":
           self.t= float (1.0/self.total)
           self.total=self.t
        
        if self.op=="sqrtx":
            print("qrt")
           # self.num2=Fraction('1/2')
            #self.total=Fraction(self.total)
            self.total=self.total**(1.0/2)          #imp to write this way, else error/ wrong o/p
        if self.op=="crtx":
            self.total=self.total**(1.0/3)
        if self.op=="pwrx":
            self.total=self.total**(1.0/int(self.current))
        if self.op=="logten":
            self.total=float(math.log(self.total)/math.log(10))         #to make it to the base10
        if self.op=="fac":
            self.total= fac(self.total)
        
        if self.op=="sinx":
            self.total= float(math.sin((math.pi*self.current)/180))
        if self.op=="cosx":
            self.total= float(math.sin((math.pi*self.current)/180))
        if self.op=="tanx":
            self.total= float(math.sin((math.pi*self.current)/180))

        #INVERSE TRIG:    
        if self.op=="sini":
           
            if self.current>1 or self.current<1:
                self.error=True
            else:
                self.total= math.asin(self.current)  #radian
                self.total=(self.total*180)/math.pi
        if self.op=="cosi":
            if self.current>1 or self.current<1:
                self.error=True
            else:
                self.total= math.acos(self.current)  #radian
                self.total=(self.total*180)/math.pi
        if self.op=="tani":
            self.total=math.atan(self.current)  #radian
            self.total=(self.total*180)/math.pi
        
       #HYPERBOLIC TRIG:
        if self.op=="sinh":
           
            if self.current>1 or self.current<1:
                self.error=True
            else:
                self.total= float(math.sinh((math.pi*self.current)/180))
                 
        if self.op=="cosh":
            if self.current>1 or self.current<1:
                self.error=True
            else:
                 
                self.total=float(math.cosh((math.pi*self.current)/180))
        if self.op=="tanh":
            self.total=float(math.tanh((math.pi*self.current)/180))
             
        
        self.new_num = True
        self.op_pending = False      #operation done
        if self.error==True:
            self.display("Error!")
        else:
            
            self.display(self.total)

    def operation(self, op): 
        self.current = float(self.current)   #prev val stored   
        if self.op_pending:
            self.do_sum()           #Call the Func where operations actually take place 
        elif not self.eq:
            self.total = self.current        
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)
    def new(self):
        print("hi")

    
def xxyy( a, b):
        if b==0:
            return 1
        if b==1:
            return a
        else:
            return a* xxyy(int(a),int(b-1))
def fac (x):
    if x==1:
        return 1;
    return x*fac(x-1)


sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Calculator")
text_box = Entry(calc, justify=RIGHT)
text_box.grid(row = 0, column = 0, columnspan = 3, pady = 5)
text_box.insert(0, "0")

# make the buttons
numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(calc, text = numbers[i]))
        bttn[i].grid(row = j, column = k, pady = 5)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

bttn_0 = Button(calc, text = "0")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 1, pady = 5)

bttn_div = Button(calc, text = chr(247))
bttn_div["command"] = lambda: sum1.operation("divide")
bttn_div.grid(row = 1, column = 3, pady = 5)

bttn_mult = Button(calc, text = "x")
bttn_mult["command"] = lambda: sum1.operation("times")
bttn_mult.grid(row = 2, column = 3, pady = 5)

minus = Button(calc, text = "-")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3, pady = 5)

point = Button(calc, text = ".")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 0, pady = 5)

add = Button(calc, text = "+")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3, pady = 5)

neg= Button(calc, text = "+/-")
neg["command"] = sum1.sign
neg.grid(row = 5, column = 0, pady = 5)

clear = Button(calc, text = "C")
clear["command"] = sum1.cancel
clear.grid(row = 5, column = 1, pady = 5)

all_clear = Button(calc, text = "AC")
all_clear["command"] = sum1.all_cancel
all_clear.grid(row = 5, column = 2, pady = 5)

equals = Button(calc, text = "=")
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 3, pady = 5)

x2 = Button(calc, text = "x^2")
x2["command"] = lambda: sum1.operation("x2")
x2.grid(row = 1, column = 4, pady = 5)

x3 = Button(calc, text = "x^3")
x3["command"] = lambda: sum1.operation("x3")
x3.grid(row = 1, column = 5, pady = 5)

xy = Button(calc, text = "x^y")
xy["command"] = lambda: sum1.operation("xy")
xy.grid(row = 1, column = 6, pady = 5)

ex = Button(calc, text = "e^x")
ex["command"] = lambda: sum1.operation("ex")
ex.grid(row = 1, column = 7, pady = 5)

tenx = Button(calc, text = "10^x")
tenx["command"] = lambda: sum1.operation("tenx")
tenx.grid(row = 1, column = 8, pady = 5)

fracx = Button(calc, text = "1/x")
fracx["command"] = lambda: sum1.operation("fracx")
fracx.grid(row = 2, column = 4, pady = 5)

sqrtx = Button(calc, text = "x^1/2")
sqrtx["command"] =  lambda: sum1.operation("sqrtx")
sqrtx.grid(row = 2, column = 5, pady = 5)

crtx = Button(calc, text = "x^1/3")
crtx["command"] =lambda: sum1.operation("crtx")
crtx.grid(row = 2, column = 6, pady = 5)

pwrx = Button(calc, text = "x^1/y")
pwrx["command"] =lambda: sum1.operation("pwrx")
pwrx.grid(row = 2, column = 7, pady = 5)

logten = Button(calc, text = "log10")
logten["command"] = lambda: sum1.operation("logten")
logten.grid(row = 2, column = 8, pady = 5)

facx = Button(calc, text = "x!")
facx["command"] =  lambda: sum1.operation("fac")
facx.grid(row = 3, column = 4, pady = 5)

sinx = Button(calc, text = "sinx")
sinx["command"] = lambda: sum1.operation("sinx")
sinx.grid(row = 3, column = 5, pady = 5)
cosx = Button(calc, text = "cosx")
cosx["command"] =lambda: sum1.operation("cosx")
cosx.grid(row = 3, column = 6, pady = 5)
tanx = Button(calc, text = "tanx")
tanx["command"] =    lambda: sum1.operation("tanx")
tanx.grid(row = 3, column = 7, pady = 5)
#inverse Trig Functions
sini = Button(calc, text = "Inv(sinx)")
sini["command"] = lambda: sum1.operation("sini")
sini.grid(row = 4, column = 5, pady = 5)
cosi = Button(calc, text = "Inv(cosx)")
cosi["command"] =lambda: sum1.operation("cosi")
cosi.grid(row = 4, column = 6, pady = 5)
tani = Button(calc, text = "Inv(tanx)")
tani["command"] =    lambda: sum1.operation("tani")
tani.grid(row = 4, column = 7, pady = 5)
e = Button(calc, text = "e")
e["command"] = lambda: sum1.operation("e") 
e.grid(row = 3, column = 8, pady = 5)
#Hyperbolic Trig Functions
sinh = Button(calc, text = "sinh(x)")
sinh["command"] = lambda: sum1.operation("sinh")
sinh.grid(row = 5, column = 5, pady = 5)
cosh = Button(calc, text = "cosh(x)")
cosh["command"] =lambda: sum1.operation("cosh")
cosh.grid(row = 5, column = 6, pady = 5)
tanh = Button(calc, text = "tanh(x)")
tanh["command"] =    lambda: sum1.operation("tanh")
tanh.grid(row = 5, column = 7, pady = 5)



root.mainloop()
