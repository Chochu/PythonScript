from tkinter import *

#Author: Jun Zhang

def main():
    root = Tk()

    root.title("CSS Extra Style Remover")
    root.geometry("500x120")
    
    app = Frame(root)
    app.grid()

    #Create label for "file to clean" --------------------------------------------
    FClabel = Label(app, text = "File to Clean: ")
    FClabel.grid(row = 0, column = 0)

    path1 = Label(app)
    path1.grid(row = 0, column = 1)

    button1 = Button(app, text = "File path", command = lambda: buttonclick(path1))
    button1.grid(row = 1, column = 0)

    #Create label for "file to compare" -------------------------------------------
    Flabel = Label(app, text = "File to Compare: ")
    Flabel.grid(row = 2, column = 0)

    path2 = Label(app)
    path2.grid(row = 2, column = 1)

    button2 = Button(app, text = "File path", command = lambda: buttonclick(path2))
    button2.grid(row = 3, column = 0)

    #Button to start comparing -----------------------------------------------------
    button2 = Button(app, text = "Remove Extra Style ", command = lambda: removeStyle(path1["text"],path2["text"]))
    button2.grid(row = 5, column = 0)

def removeStyle(FiletoClean, FiletoCompare):
    print(FiletoClean)
    print(FiletoCompare)

    with open(FiletoClean) as f:
        F2CText = f.read()
    with open(FiletoCompare) as f:
        F2ComText = f.read()

    print(F2ComText)
    print(F2CText)

    
    

    #Set the file location----------------------------------------------------------
def buttonclick(label): 
    filename1 = filedialog.askopenfilename(filetypes = (("CSS Files", "*.css"),), title = "Choose a file")
    label["text"]= filename1
    
if __name__ == "__main__":
    main()



