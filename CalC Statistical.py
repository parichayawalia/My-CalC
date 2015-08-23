# My CalC
from tkinter import *
from statistics import *
import math
import fractions
import numpy as np

ee, ten=math.e, 10



root = Tk()
calc = Frame(root)
calc.grid()



root.title("Calculator")
text_box = Entry(calc, justify=RIGHT)
text_box.grid(row = 0, column = 0, columnspan = 3, pady = 5)
text_box.insert(0, "0")


# Main class
class Calc():
    def __init__(self):
        self.total = 0
        self.begin= False
        self.lst=[]
        self.whole_str='\0'    #if whole data with commas is on screen Already
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False
        self.t,self.num2=0.0, 0.0
        self.data=0.0
        self.display("Comma Seperated Data")
    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num:        #for another no
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2   #string concatenation of nos
        self.display(self.current)
        print("current " +str(self.current))

    def end(self):
        self.whole_str=self.current
        self.lst=self.whole_str.split(",")
        print(self.lst)
        ##Conversion to float values  **
        for j in range(len(self.lst)):
            self.lst[j]=float(self.lst[j])
        self.total=self.lst[len(self.lst)-1]            #Last element=Total current ele for other Arith op
        print("taken "+str(self.total))
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
    def add(self): ###
        print("self totl" + str(self.total))
        self.current = float(self.current)   #prev val stored  
        self.total =float(self.total)+float(self.current)
        self.display(self.total)
    def do_sum(self):       #do all the calculations HERE
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op=="comma":
            self.string=","
            
            self.display(str(self.total)+",")
        if self.op=="beg":
             beg()

        if self.op=="end":
            print("total "+self.total)
             
            print(self.lst)
        
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
                 
        
        self.new_num = True
        self.op_pending = False      #operation done
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
        #self.display("PRESS Begin")
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0.0
        self.display(self.total)

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)
    def new(self):
        print("hi")

        
        ########        STATISTICAL FUNCTIONS
    def mean(self):
        self.data= self.total= np.mean(self.lst)
        self.display(self.total)
    def mode(self):
        counts = np.bincount(self.lst)
        self.total= np.argmax(counts)
         
        self.display(self.total)
    def median(self):
        self.total=np.median(self.lst)
        self.display(self.total)
    def am(self):
        self.mean()
    def gm(self):
        l=len(self.lst)
        ans=1
        for j in range (len(self.lst)):
            ans=float(ans)*float(self.lst[j])
        ans=ans**(1.0/int(l))
        self.total=ans
        self.display(self.total)
    def hm(self):
        ans, l=0.0, len(self.lst)
        
        for j in range(len(self.lst)):
            ans+=float (1.0/self.lst[j])
        ans=float(l*float(1.0/ans))         #By Definition, HM
        self.total=ans
        self.display(self.total)
    def var(self):
        ans=float(np.std(self.lst))
        ans=ans*ans
        self.total=ans
        self.display(self.total)
    def std(self):
        ans=float(np.std(self.lst))
        self.total=ans
        self.display(self.total)
    def coeff(self):
        a1, a2=np.std(self.lst), np.mean(self.lst)
        ans=float(a1/a2)
        self.total=ans
        self.display(self.total)
    def ncr(self):
        if len(self.lst)>2:
            self.display("Invalid Syntax")
        else:
            
            n,r=float(self.lst[0]), float(self.lst[1])
            ans=fac(n)/(fac(r)*fac(n-r))
            self.total=ans
            self.display(self.total)
    def npr(self):
        if len(self.lst)>2:
            self.display("Invalid Syntax")
        else:
            n,r=float(self.lst[0]), float(self.lst[1])
            ans=fac(n)/fac(n-r)
            self.total=ans
            self.display(self.total)
    
        
###################NOTE : ADD PREV CALCULATOR FEATURES HERE TOO.        
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
def beg():
    self.cancel()


    


sum1 = Calc()

# make the buttons
numbers = "789456123"
number2=","
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
add["command"] = lambda: sum1.add()
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
 

bttn.append(Button(calc, text = ','))                   ##COMMAS DISPLAY
bttn[i].grid(row = 0, column = 3, pady = 5)
bttn[i]["command"] = lambda x = number2: sum1.num_press(x)

 
end = Button(calc, text ="SUBMIT_DATA")
end["command"] = lambda: sum1.end()
end.grid(row = 0, column = 4, pady = 5)


x2 = Button(calc, text = "x^2")
x2["command"] = lambda: sum1.operation("x2")
x2.grid(row = 1, column = 7, pady = 5)

x3 = Button(calc, text = "x^3")
x3["command"] = lambda: sum1.operation("x3")
x3.grid(row = 1, column = 8, pady = 5)

xy = Button(calc, text = "x^y")
xy["command"] = lambda: sum1.operation("xy")
xy.grid(row = 1, column = 9, pady = 5)

ex = Button(calc, text = "e^x")
ex["command"] = lambda: sum1.operation("ex")
ex.grid(row = 1, column = 10, pady = 5)
 
fracx = Button(calc, text = "1/x")
fracx["command"] = lambda: sum1.operation("fracx")
fracx.grid(row = 2, column = 7, pady = 5)

sqrtx = Button(calc, text = "x^1/2")
sqrtx["command"] =  lambda: sum1.operation("sqrtx")
sqrtx.grid(row = 2, column = 8, pady = 5)

crtx = Button(calc, text = "x^1/3")
crtx["command"] =lambda: sum1.operation("crtx")
crtx.grid(row = 2, column = 9, pady = 5)

pwrx = Button(calc, text = "x^1/y")
pwrx["command"] =lambda: sum1.operation("pwrx")
pwrx.grid(row = 2, column = 10, pady = 5)

logten = Button(calc, text = "log10")
logten["command"] = lambda: sum1.operation("logten")
logten.grid(row = 2, column = 7, pady = 5)

facx = Button(calc, text = "x!")
facx["command"] =  lambda: sum1.operation("fac")
facx.grid(row = 3, column = 8, pady = 5)

sinx = Button(calc, text = "sinx")
sinx["command"] = lambda: sum1.operation("sinx")
sinx.grid(row = 3, column = 7, pady = 5)
cosx = Button(calc, text = "cosx")
cosx["command"] =lambda: sum1.operation("cosx")
cosx.grid(row = 3, column = 8, pady = 5)
tanx = Button(calc, text = "tanx")
tanx["command"] =    lambda: sum1.operation("tanx")
tanx.grid(row = 3, column = 9, pady = 5)
e = Button(calc, text = "e")
e["command"] = lambda: sum1.operation("e") 
e.grid(row = 3, column = 10, pady = 5)

mean = Button(calc, text = "Mean()")
mean["command"] = lambda: sum1.mean()
mean.grid(row = 1, column = 4, pady = 5)

mode = Button(calc, text = "Mode()")
mode["command"] = lambda: sum1.mode()
mode.grid(row = 1, column = 5, pady = 5)

median = Button(calc, text = "Median()")
median["command"] = lambda: sum1.median()
median.grid(row = 1, column = 6, pady = 5)
 
 

am = Button(calc, text = "A.M.")
am["command"] =  lambda: sum1.am()
am.grid(row = 2, column = 4, pady = 5)

gm = Button(calc, text = "G.M.")
gm["command"] =lambda: sum1.gm()
gm.grid(row = 2, column = 5, pady = 5)

hm = Button(calc, text = "H.M.")
hm["command"] =lambda: sum1.hm()
hm.grid(row = 2, column = 6, pady = 5)

var = Button(calc, text = "Var(x)")
var["command"] =  lambda: sum1.var()
var.grid(row = 3, column = 4, pady = 5)

std = Button(calc, text = "StdD(x)")
std["command"] =lambda: sum1.std()
std.grid(row = 3, column = 5, pady = 5)

coeff = Button(calc, text = "CoeffVar(x)")
coeff["command"] =lambda: sum1.coeff()
coeff.grid(row = 3, column = 6, pady = 5)

ncr = Button(calc, text = "nCr")
ncr["command"] =  lambda: sum1.ncr()
ncr.grid(row = 4, column = 4, pady = 5)

npr = Button(calc, text = "nPr")
npr["command"] =lambda: sum1.npr()
npr.grid(row = 4, column = 5, pady = 5)

#coeff = Button(calc, text = "CoeffVar(x)")
#coeff["command"] =lambda: sum1.coeff()
#coeff.grid(row = 4, column = 6, pady = 5)

equals = Button(calc, text = "=")
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 11, pady = 5)

root.mainloop()
