from tkinter import *

root = Tk()
root.title("VSB Calc v2")
root.iconbitmap("vsb_calc/icon.ico")
root.geometry("1200x600")
root.config(bg = "black")

class MainWindow:

    def __init__(self, main):

        frame = Frame(main, background = "grey", width = 245, height = 890, borderwidth = 5, relief = RAISED)
        frame.pack(side = LEFT, fill = BOTH)
        heading = Label(frame, text = "Hello in VSB Calc! Just follow the instructions below in order.", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
        heading.pack(anchor = W)
        line0 = Label(frame, text = " ", bg = "grey", padx = 5, pady = 5) 
        line0.pack(anchor = W)   

        line1 = Label(frame, text = "1. Enter your budget:", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
        line1.pack(anchor = W)
        self.button1 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick1, font = ('Courier New', 8))
        self.button1.pack(anchor = W, padx = 3)
        self.inputField1 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
        self.inputField1.pack(anchor = W,)
        
        line2 = Label(frame, text = "2. Enter a planned profit from a one customer: (In PLN.)", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
        line2.pack(anchor = W)
        self.button2 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick2, font = ('Courier New', 8))
        self.button2.pack(anchor = W, padx = 3)
        self.inputField2 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
        self.inputField2.pack(anchor = W,)
        
        line3 = Label(frame, text = "3. Enter a planned number of a customers:", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
        line3.pack(anchor = W)
        self.button3 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick3, font = ('Courier New', 8))
        self.button3.pack(anchor = W, padx = 3)
        self.inputField3 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
        self.inputField3.pack(anchor = W,)

        line4 = Label(frame, text = "4. Enter a fixed costs:", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
        line4.pack(anchor = W)
        self.button4 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick4, font = ('Courier New', 8))
        self.button4.pack(anchor = W, padx = 3)
        self.inputField4 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
        self.inputField4.pack(anchor = W,)

        line5 = Label(frame, text = "5. Add and enter one of a variable costs: (You can add several.)", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
        line5.pack(anchor = W)
        self.button5 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick5, font = ('Courier New', 8))
        self.button5.pack(anchor = W, padx = 3)
        self.inputField5 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
        self.inputField5.pack(anchor = W,)

        line6 = Label(frame, text = "6. Generate a summary.", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
        line6.pack(anchor = W)
        self.button6 = Button(frame, width = 63, text = "Click here to generate!", bg = "dark grey", command = self.bclick6, font = ('Courier New', 8))
        self.button6.pack(anchor = W, padx = 3)

        line7 = Label(frame, text = "7. Clear and start from the beginning.", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
        line7.pack(anchor = W)
        self.button7 = Button(frame, width = 63, text = "Click here to clear!", bg = "dark grey", command = self.bclick7, font = ('Courier New', 8))
        self.button7.pack(anchor = W, padx = 3)        

    def bclick1(self):
        self.budget = int(self.inputField1.get())
        label1 = Label(root, fg = "white", bg = "black", text = "Budget added.", font = ('Courier New', 8))
        label1.pack(anchor = W)
        self.inputField1.delete(0, END) 

    def bclick2(self):
        self.profit = int(self.inputField2.get())
        label2 = Label(root, fg = "white", bg = "black", text = "Profit added.", font = ('Courier New', 8))
        label2.pack(anchor = W)
        self.inputField2.delete(0, END)

    def bclick3(self):
        self.customers = int(self.inputField3.get())
        label3 = Label(root, fg = "white", bg = "black", text = "Customers added.", font = ('Courier New', 8))
        label3.pack(anchor = W)
        self.inputField3.delete(0, END)

    def bclick4(self):
        self.fixedCosts = int(self.inputField4.get())
        label4 = Label(root, fg = "white", bg = "black", text = "Fixed costs added.", font = ('Courier New', 8))
        label4.pack(anchor = W)
        self.inputField4.delete(0, END)

    def bclick5(self):
        self.variableCosts = int(self.inputField5.get())
        self.variableCostsList.append(self.variableCosts)
        label5 = Label(root, fg = "white", bg = "black", text = "Variable cost added.", font = ('Courier New', 8))
        label5.pack(anchor = W)
        self.inputField5.delete(0, END)

    def bclick6(self):
        label6 = Label(root, fg = "white", bg = "black", text = "*********************", font = ('Courier New', 8))
        label6.pack(anchor = W)
        self.allVariableCosts = sum(self.variableCostsList)
        self.costs = self.fixedCosts + self.allVariableCosts
        label6 = Label(root, fg = "white", bg = "black", text = "All costs are " + str(self.costs) + " PLN.", font = ('Courier New', 8))
        label6.pack(anchor = W)
        self.profFromCust = self.costs / self.customers + self.profit
        label6 = Label(root, fg = "white", bg = "black", text = "Ticket price for a one customer at profit " + str(self.profit) + " PLN is " + str(self.profFromCust) + " PLN.", font = ('Courier New', 8))
        label6.pack(anchor = W)
        self.budgetAfter = (self.budget - self.costs) + (self.customers * self.profFromCust)
        label6 = Label(root, fg = "white", bg = "black", text = "The budget after this event will be " + str(self.budgetAfter) + " PLN.", font = ('Courier New', 8))
        label6.pack(anchor = W)
        if (self.costs > self.budget):
            label6 = Label(root, fg = "white", bg = "black", text = "Not enough funds!", font = ('Courier New', 8))
            label6.pack(anchor = W)
        elif (self.costs < self.budget):
            label6 = Label(root, fg = "white", bg = "black", text = "Enough funds!", font = ('Courier New', 8))
            label6.pack(anchor = W)
#Restart 1:
    def bclick7(self):
        root = Tk()
        root.title("VSB Calc v2")
        root.iconbitmap("vsb_calc/icon.ico")
        root.geometry("1200x600")
        root.config(bg = "black")

        class MainWindow:

            def __init__(self, main):

                frame = Frame(main, background = "grey", width = 245, height = 890, borderwidth = 5, relief = RAISED)
                frame.pack(side = LEFT, fill = BOTH)
                heading = Label(frame, text = "Hello in VSB Calc! Just follow the instructions below in order.", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                heading.pack(anchor = W)
                line0 = Label(frame, text = " ", bg = "grey", padx = 5, pady = 5) 
                line0.pack(anchor = W)   

                line1 = Label(frame, text = "1. Enter your budget:", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                line1.pack(anchor = W)
                self.button1 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick1, font = ('Courier New', 8))
                self.button1.pack(anchor = W, padx = 3)
                self.inputField1 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
                self.inputField1.pack(anchor = W,)
                
                line2 = Label(frame, text = "2. Enter a planned profit from a one customer: (In PLN.)", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                line2.pack(anchor = W)
                self.button2 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick2, font = ('Courier New', 8))
                self.button2.pack(anchor = W, padx = 3)
                self.inputField2 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
                self.inputField2.pack(anchor = W,)
                
                line3 = Label(frame, text = "3. Enter a planned number of a customers:", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                line3.pack(anchor = W)
                self.button3 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick3, font = ('Courier New', 8))
                self.button3.pack(anchor = W, padx = 3)
                self.inputField3 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
                self.inputField3.pack(anchor = W,)

                line4 = Label(frame, text = "4. Enter a fixed costs:", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                line4.pack(anchor = W)
                self.button4 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick4, font = ('Courier New', 8))
                self.button4.pack(anchor = W, padx = 3)
                self.inputField4 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
                self.inputField4.pack(anchor = W,)

                line5 = Label(frame, text = "5. Add and enter one of a variable costs: (You can add several.)", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                line5.pack(anchor = W)
                self.button5 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick5, font = ('Courier New', 8))
                self.button5.pack(anchor = W, padx = 3)
                self.inputField5 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
                self.inputField5.pack(anchor = W,)

                line6 = Label(frame, text = "6. Generate a summary.", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                line6.pack(anchor = W)
                self.button6 = Button(frame, width = 63, text = "Click here to generate!", bg = "dark grey", command = self.bclick6, font = ('Courier New', 8))
                self.button6.pack(anchor = W, padx = 3)

                line7 = Label(frame, text = "7. Clear and start from the beginning.", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                line7.pack(anchor = W)
                self.button7 = Button(frame, width = 63, text = "Click here to clear!", bg = "dark grey", command = self.bclick7, font = ('Courier New', 8))
                self.button7.pack(anchor = W, padx = 3)        

            def bclick1(self):
                self.budget = int(self.inputField1.get())
                label1 = Label(root, fg = "white", bg = "black", text = "Budget added.", font = ('Courier New', 8))
                label1.pack(anchor = W)
                self.inputField1.delete(0, END) 

            def bclick2(self):
                self.profit = int(self.inputField2.get())
                label2 = Label(root, fg = "white", bg = "black", text = "Profit added.", font = ('Courier New', 8))
                label2.pack(anchor = W)
                self.inputField2.delete(0, END)

            def bclick3(self):
                self.customers = int(self.inputField3.get())
                label3 = Label(root, fg = "white", bg = "black", text = "Customers added.", font = ('Courier New', 8))
                label3.pack(anchor = W)
                self.inputField3.delete(0, END)

            def bclick4(self):
                self.fixedCosts = int(self.inputField4.get())
                label4 = Label(root, fg = "white", bg = "black", text = "Fixed costs added.", font = ('Courier New', 8))
                label4.pack(anchor = W)
                self.inputField4.delete(0, END)

            def bclick5(self):
                self.variableCosts = int(self.inputField5.get())
                self.variableCostsList.append(self.variableCosts)
                label5 = Label(root, fg = "white", bg = "black", text = "Variable cost added.", font = ('Courier New', 8))
                label5.pack(anchor = W)
                self.inputField5.delete(0, END)

            def bclick6(self):
                label6 = Label(root, fg = "white", bg = "black", text = "*********************", font = ('Courier New', 8))
                label6.pack(anchor = W)
                self.allVariableCosts = sum(self.variableCostsList)
                self.costs = self.fixedCosts + self.allVariableCosts
                label6 = Label(root, fg = "white", bg = "black", text = "All costs are " + str(self.costs) + " PLN.", font = ('Courier New', 8))
                label6.pack(anchor = W)
                self.profFromCust = self.costs / self.customers + self.profit
                label6 = Label(root, fg = "white", bg = "black", text = "Ticket price for a one customer at profit " + str(self.profit) + " PLN is " + str(self.profFromCust) + " PLN.", font = ('Courier New', 8))
                label6.pack(anchor = W)
                self.budgetAfter = (self.budget - self.costs) + (self.customers * self.profFromCust)
                label6 = Label(root, fg = "white", bg = "black", text = "The budget after this event will be " + str(self.budgetAfter) + " PLN.", font = ('Courier New', 8))
                label6.pack(anchor = W)
                if (self.costs > self.budget):
                    label6 = Label(root, fg = "white", bg = "black", text = "Not enough funds!", font = ('Courier New', 8))
                    label6.pack(anchor = W)
                elif (self.costs < self.budget):
                    label6 = Label(root, fg = "white", bg = "black", text = "Enough funds!", font = ('Courier New', 8))
                    label6.pack(anchor = W)
#Restart 2:
            def bclick7(self):
                root = Tk()
                root.title("VSB Calc v2")
                root.iconbitmap("vsb_calc/icon.ico")
                root.geometry("1200x600")
                root.config(bg = "black")

                class MainWindow:

                    def __init__(self, main):

                        frame = Frame(main, background = "grey", width = 245, height = 890, borderwidth = 5, relief = RAISED)
                        frame.pack(side = LEFT, fill = BOTH)
                        heading = Label(frame, text = "Hello in VSB Calc! Just follow the instructions below in order.", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                        heading.pack(anchor = W)
                        line0 = Label(frame, text = " ", bg = "grey", padx = 5, pady = 5) 
                        line0.pack(anchor = W)   

                        line1 = Label(frame, text = "1. Enter your budget:", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                        line1.pack(anchor = W)
                        self.button1 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick1, font = ('Courier New', 8))
                        self.button1.pack(anchor = W, padx = 3)
                        self.inputField1 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
                        self.inputField1.pack(anchor = W,)
                        
                        line2 = Label(frame, text = "2. Enter a planned profit from a one customer: (In PLN.)", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                        line2.pack(anchor = W)
                        self.button2 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick2, font = ('Courier New', 8))
                        self.button2.pack(anchor = W, padx = 3)
                        self.inputField2 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
                        self.inputField2.pack(anchor = W,)
                        
                        line3 = Label(frame, text = "3. Enter a planned number of a customers:", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                        line3.pack(anchor = W)
                        self.button3 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick3, font = ('Courier New', 8))
                        self.button3.pack(anchor = W, padx = 3)
                        self.inputField3 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
                        self.inputField3.pack(anchor = W,)

                        line4 = Label(frame, text = "4. Enter a fixed costs:", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                        line4.pack(anchor = W)
                        self.button4 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick4, font = ('Courier New', 8))
                        self.button4.pack(anchor = W, padx = 3)
                        self.inputField4 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
                        self.inputField4.pack(anchor = W,)

                        line5 = Label(frame, text = "5. Add and enter one of a variable costs: (You can add several.)", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                        line5.pack(anchor = W)
                        self.button5 = Button(frame, width = 63, text = "Click to add!", bg = "dark grey", command = self.bclick5, font = ('Courier New', 8))
                        self.button5.pack(anchor = W, padx = 3)
                        self.inputField5 = Entry(frame, width = 63, fg = "black", bg = "antiquewhite3", borderwidth = 5, font = ('Courier New', 8))
                        self.inputField5.pack(anchor = W,)

                        line6 = Label(frame, text = "6. Generate a summary.", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                        line6.pack(anchor = W)
                        self.button6 = Button(frame, width = 63, text = "Click here to generate!", bg = "dark grey", command = self.bclick6, font = ('Courier New', 8))
                        self.button6.pack(anchor = W, padx = 3)

                        line7 = Label(frame, text = "7. Clear and start from the beginning.", bg = "grey", padx = 5, pady = 5, font = ('Courier New', 8)) 
                        line7.pack(anchor = W)
                        self.button7 = Button(frame, width = 63, text = "Click here to clear!", bg = "dark grey", command = self.bclick7, font = ('Courier New', 8))
                        self.button7.pack(anchor = W, padx = 3)        

                    def bclick1(self):
                        self.budget = int(self.inputField1.get())
                        label1 = Label(root, fg = "white", bg = "black", text = "Budget added.", font = ('Courier New', 8))
                        label1.pack(anchor = W)
                        self.inputField1.delete(0, END) 

                    def bclick2(self):
                        self.profit = int(self.inputField2.get())
                        label2 = Label(root, fg = "white", bg = "black", text = "Profit added.", font = ('Courier New', 8))
                        label2.pack(anchor = W)
                        self.inputField2.delete(0, END)

                    def bclick3(self):
                        self.customers = int(self.inputField3.get())
                        label3 = Label(root, fg = "white", bg = "black", text = "Customers added.", font = ('Courier New', 8))
                        label3.pack(anchor = W)
                        self.inputField3.delete(0, END)

                    def bclick4(self):
                        self.fixedCosts = int(self.inputField4.get())
                        label4 = Label(root, fg = "white", bg = "black", text = "Fixed costs added.", font = ('Courier New', 8))
                        label4.pack(anchor = W)
                        self.inputField4.delete(0, END)

                    def bclick5(self):
                        self.variableCosts = int(self.inputField5.get())
                        self.variableCostsList.append(self.variableCosts)
                        label5 = Label(root, fg = "white", bg = "black", text = "Variable cost added.", font = ('Courier New', 8))
                        label5.pack(anchor = W)
                        self.inputField5.delete(0, END)

                    def bclick6(self):
                        label6 = Label(root, fg = "white", bg = "black", text = "*********************", font = ('Courier New', 8))
                        label6.pack(anchor = W)
                        self.allVariableCosts = sum(self.variableCostsList)
                        self.costs = self.fixedCosts + self.allVariableCosts
                        label6 = Label(root, fg = "white", bg = "black", text = "All costs are " + str(self.costs) + " PLN.", font = ('Courier New', 8))
                        label6.pack(anchor = W)
                        self.profFromCust = self.costs / self.customers + self.profit
                        label6 = Label(root, fg = "white", bg = "black", text = "Ticket price for a one customer at profit " + str(self.profit) + " PLN is " + str(self.profFromCust) + " PLN.", font = ('Courier New', 8))
                        label6.pack(anchor = W)
                        self.budgetAfter = (self.budget - self.costs) + (self.customers * self.profFromCust)
                        label6 = Label(root, fg = "white", bg = "black", text = "The budget after this event will be " + str(self.budgetAfter) + " PLN.", font = ('Courier New', 8))
                        label6.pack(anchor = W)
                        if (self.costs > self.budget):
                            label6 = Label(root, fg = "white", bg = "black", text = "Not enough funds!", font = ('Courier New', 8))
                            label6.pack(anchor = W)
                        elif (self.costs < self.budget):
                            label6 = Label(root, fg = "white", bg = "black", text = "Enough funds!", font = ('Courier New', 8))
                            label6.pack(anchor = W)

                    def bclick7(self):
                        pass
                        
                    budget = int() 
                    profit = int() 
                    customers = int() 
                    fixedCosts = int() 
                    variableCosts = int() 
                    variableCostsList = []
                
                run = MainWindow(root)

                root.mainloop()
                pass
                
            budget = int() 
            profit = int() 
            customers = int() 
            fixedCosts = int() 
            variableCosts = int() 
            variableCostsList = []
        
        run = MainWindow(root)

        root.mainloop()
        pass
#Main root values:        
    budget = int() 
    profit = int() 
    customers = int() 
    fixedCosts = int() 
    variableCosts = int() 
    variableCostsList = []
 
run = MainWindow(root)

root.mainloop()
