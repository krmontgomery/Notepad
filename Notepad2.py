import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import * 


class Notepad:
    root = Tk()
    
    #Default Window Width and Height
    theWidth = 500
    theHeight = 500
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT,fill=Y)
    textArea = Text(root, yscrollcommand=scrollbar.set)
    scrollbar.config(command=textArea.yview)
    menuBar = Menu(root)
    fileMenu = Menu(menuBar, tearoff=0)
    editMenu = Menu(menuBar, tearoff=0)
    helpMenu = Menu(menuBar, tearoff=0)
    themeMenu = Menu(menuBar, tearoff=0)

    #Add Scollbar
    # scrollBar = Scrollbar(textArea)
    zfile = None

    def __init__(self, **kwargs):
        # Set Icon
        try:
            self.root.wm_iconbitmap('notepad.ico')
        except:
            pass
        # Set Window size
        try:
            self.theWidth = kwargs['width']
        except KeyError:
            pass
        
        try:
            self.theHeight = kwargs['height']
        except KeyError:
            pass
        
        
        # Set the Window Text 
        self.root.title('Untitled - MyNote')

        # Center the window
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # For left-aligning
        left = (screenWidth / 2 ) - (self.theWidth / 2)

        # For right-aligning 
        top = (screenHeight / 2) - (self.theHeight / 2)

        # Top and Bottom aligning
        self.root.geometry('%dx%d+%d+%d' % (self.theWidth,
                                            self.theHeight,
                                            left, top))
    
        # To Make the textarea auto resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        #Makes text area show for ability to type on
        self.textArea.pack(fill=BOTH, expand=TRUE)
        self.textArea.configure(foreground='#74B9FF', background='#2F363F', font=('Helevitica',12,), insertbackground='White', padx=10)

        #Open a new file
        self.fileMenu.add_command(label="New", command=self.newFile)

        #Open existing file
        self.fileMenu.add_command(label="Open", command=self.openFile)

        #Save a file
        self.fileMenu.add_command(label="Save", command=self.saveFile)

        # To create a line in the dialog
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.exit_application)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        #To give a feature of cut
        self.editMenu.add_command(label="Cut", command=self.cut)

        #To give a copy feature
        self.editMenu.add_command(label='Copy', command=self.copy)

        #To give a paste feature
        self.editMenu.add_command(label="Paste", command=self.paste)

        #To give editing feature
        self.menuBar.add_cascade(label="Edit", menu=self.editMenu)

        #to create a feature of description of the notpad
        self.helpMenu.add_command(label="About MyNote", command=self.showAbout)
        self.menuBar.add_cascade(label="Help", menu=self.helpMenu)

        ################################### Themes #####################################
        self.menuBar.add_cascade(label='Theme', menu=self.themeMenu)
        self.themeMenu.add_command(label='Classic Theme', command=self.classic_theme)
        self.themeMenu.add_command(label="Reverse Original", command=self.reverse_classic)
        self.themeMenu.add_command(label="Original Theme", command=self.regular_theme)
        self.themeMenu.add_command(label="Theme One", command=self.theme_one)
        self.themeMenu.add_command(label="Theme Two", command=self.theme_two)
        self.themeMenu.add_command(label="Theme Three", command=self.theme_three)
        self.themeMenu.add_command(label='Theme Four', command=self.theme_four)
        self.themeMenu.add_command(label='Theme Five', command=self.theme_five)
        ################################### Themes #####################################

        self.editMenu.add_command(label="Word Wrap", command=self.add_wordwrap)

        #This makes menu selection tabs visibile
        self.root.config(menu=self.menuBar)

        # #Makes scroll bar visible
        # self.scrollBar.pack(side=RIGHT,fill=Y)

        # #Scroll bar will adjust automatically according to the content
        # self.scrollBar.config(command=self.textArea.yview,width=14)
        # self.textArea.config(yscrollcommand=self.scrollBar.set)

    def exit_application(self):
        self.root.destroy()

    def showAbout(self):
        showinfo("MyNote", "Kris Montgomery is the BOMB DIGGITY!")

    def openFile(self):
        self.zfile = askopenfilename(defaultextension='.txt',
                                    filetypes=[("All Files", '*.*'),
                                        ('Text Documents', '*.txt')])
        if self.zfile == '':
            self.zfile = None
        else:
            self.root.title(os.path.basename(self.zfile) + ' - Notepad')
            self.textArea.delete(1.0,END)

            nfile = open(self.zfile, 'r')
            self.textArea.insert(1.0,nfile.read())

    def newFile(self):
        self.root.title('Untitled - MyNote')
        self.zfile = None
        self.textArea.delete(1.0,END)

    def saveFile(self):
        if self.zfile == None:
            self.zfile = asksaveasfilename(initialfile="Untitled.txt",
                                           defaultextension=".txt",
                                           filetypes=[("All Files", "*.*"),
                                                      ("Text Documents", "*.txt")])
            showinfo('Save File', '** There is a file with this name already. **')
            if self.zfile == "":
                self.zfile = None
                showinfo('Save File', '** File was not saved. **')
            else:
                # Try to save the file
                nfile = open(self.zfile,"w")
                nfile.write(self.textArea.get(1.0,END))
                nfile.close()
                showinfo('Save File', 'File was saved successfully!')
                #Change the window title
                self.root.title(os.path.basename(self.zfile) + ' - MyNote')
        else:
            nfile = open(self.zfile,"w")
            nfile.write(self.textArea.get(1.0,END))
            nfile.close()
            showinfo('Save File', 'File was saved successfully!')

    def add_wordwrap(self):
        self.textArea.configure(wrap=WORD)
    
    def cut(self):
        self.textArea.event_generate('<<Cut>>')
    
    def copy(self):
        self.textArea.event_generate('<<Copy>>')
    
    def paste(self):
        self.textArea.event_generate('<<Paste>>')
    
    #################################### Theme Functions ###########################################
    def classic_theme(self):
        self.textArea.configure(foreground='black', background='white', font=('Helevitica',12,), insertbackground='Black')

    def reverse_classic(self):
        self.textArea.configure(foreground='White', background="black", font=('Helevitica',12), insertbackground='white')

    def regular_theme(self):
        self.textArea.configure(foreground='#74B9FF', background='#2F363F', font=('Helevitica',12,), insertbackground='White')
    
    def theme_one(self):
        self.textArea.configure(foreground='#1287A5', background='#EAF0F1', font=('Helevitica',12,), insertbackground='#1287A5')
    
    def theme_two(self):
        self.textArea.configure(foreground='#67E6DC', background='#0A3D62', font=('Helevitica',12,), insertbackground='#67E6DC')

    def theme_three(self):
        self.textArea.configure(foreground='#7CEC9F', background='#2C3335', font=('Helevitica',12,), insertbackground='#7CEC9F')
    
    def theme_four(self):
        self.textArea.configure(foreground='#ff9ff3', background='#2c3e50', font=('Helevitica', 12,), insertbackground='White')
    
    def theme_five(self):
        self.textArea.configure(foreground='#192a56', background='#dfe4ea', font=('Helevitica',12), insertbackground='black')
    #################################################################################################
    
    def run(self):
        #Run Application
        self.root.mainloop()


notepad = Notepad(width=600,height=400) 
notepad.run() 