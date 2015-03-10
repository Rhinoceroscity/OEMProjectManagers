'''
Created on Jan 28, 2015

@author: cgi-28
'''
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os, shutil, project
from subprocess import call

class Car(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.index = 0
        self.name = tk.StringVar()
        self.observer=None
        #Car Label
        tk.Label(self, text = "Car Name: ").pack(side=tk.LEFT, fill=tk.X, expand = 1)
        #Entry Widget
        self.name_entry = tk.Entry(self, textvariable = self.name)
        self.name_entry.pack(side=tk.LEFT, fill=tk.X, expand = 1)
        #Remove Button
        self.icon = tk.PhotoImage(file = "exit_icon.pbm")
        self.remove_button = tk.Button(self, width = 20, height = 20,  image=self.icon,command = lambda: self.remove())
        self.remove_button.pack(side=tk.LEFT, fill=tk.X)
    
    def setName(self, name):
        self.name.set(name)
    
    def setIndex(self, index):
        self.index = index
        print("Set index: %s"%(self.index))
    
    def removeTrace(self):
        if self.observer!=None:
            self.name.trace_vdelete("w", self.observer)
            
    def remove(self):
        #Destroy the frame
        self.removeTrace()
        self.destroy()

class OEMProjectSetup():
    def __init__(self):
        self.initVars()
        self.initImages()
        self.initGUI()
    
    def initVars(self):
        self.project = project.Project()
        #Set the root variable
        self.root = tk.Tk()        
        #TKinter variables
        
        self.projectName = tk.StringVar()
        
        def projectNameTrace(x, y, z):
            self.project.projectName = self.projectName.get()
        
        self.projectName.trace("w", projectNameTrace)
        self.project_directories = (("/Volumes/bto-secure/","BTO Secure"),("/Volumes/Creative/Client_Projects/","Client Projects"))
        self.selected_directory = tk.StringVar()
        self.selected_directory.set(self.project_directories[0][1])
        
    def initImages(self):
        #Create a dictionary of image names
        self.images = {"FolderImage":tk.PhotoImage(file = "folder.pbm"),
                       "FolderImageSmall":tk.PhotoImage(file = "folder_small.pbm"),
                       "ArrowRight":tk.PhotoImage(file = "arrow_right.pbm"),
                       "ArrowLeft":tk.PhotoImage(file = "arrow_left.pbm"),
                       "ExitIcon":tk.PhotoImage(file = "exit_icon.pbm"),
                       "AddIcon":tk.PhotoImage(file = "add_icon.pbm"),
                       "PageIcon":tk.PhotoImage(file = "page_icon.pbm"),
                       "FloppyDisk":tk.PhotoImage(file = "floppy_disc.pbm")}
    
    def loadProject(self):
        if not self.project.projectCreated() or messagebox.askokcancel("Project already created.", "Are you sure you want to open a new project?")==True:
            directory = filedialog.askdirectory()
            if directory!=None and directory!="":
                self.project = project.Project()
                if self.project.loadProject(directory)==True:
                    #Backtrack the project name
                    self.projectName.set(self.project.projectName)
                    #Refresh the UI for the cars
                    self.refreshUI()
                else:
                    messagebox.showerror("Invalid Project", "This folder is not a project folder.  Please select the core folder of a project.")
                    self.project=None
    
    def createProject(self):
        if self.project.projectCreated()==False or messagebox.askokcancel("Project already created.", "This project has already been created.  Would you like to update it?")==True:
            if self.projectName.get()!="":
                if len(self.getAllCarNames())>0 or all((len(self.getAllCarNames())==0, messagebox.askyesno("No car models", "This project has no car models entered.  Create the project anyways?")==True)):
                    if not "" in self.getAllCarNames():
                        if not len(set(self.getAllCarNames()))<len(self.getAllCarNames()):
                            for i in self.project_directories:
                                if i[1]==self.selected_directory.get():
                                    directory = i[0]
                                    break
                            
                            if os.path.isdir(directory):
                                #Tell the project folder to initialize everything
                                self.project.initFolderStructure(directory, True)
                                self.project.generateAllDataFolders()
                                self.project.generateAllRetouchingFolders()
                                self.project.saveProject()
                                call(["open", "-R", self.project.coreFolder])
                                #cars = self.getAllCarNames()
    
                                #if len(cars)>0:
                                #    for car in cars:
                                #        self.project.generateDataFolder(car.replace(" ","_"))
                                #        self.project.generateRetouchingFolder(car.replace(" ","_"))
                                
                                #Set the project's cars to the cars that are entered.
                                #self.project.cars = cars
                                #self.project.saveProjectData()
                                #call(["open", "-R", self.project.coreFolder])
                            else:
                                messagebox.showerror("Directory not found", "%s could not be found, make sure your drives are properly mounted."%(directory))
                        else:
                            messagebox.showerror("Duplicated Car Names","A car name is used more than once, please make sure the cars all have unique names.")
                    else:
                        messagebox.showerror("Invalid car name", "One of the cars does not have a name entered, please make sure all cars have valid names.")
            else:
                messagebox.showerror("No Project Name", "Please enter a project name.")
    
    def updateProject(self):
        pass
    
    def refreshUI(self):
        #widgets = self.carModelsFrame.winfo_children()
        #project_cars = self.project.Cars
        #If theres no cars (new project, or project has been reset), just do a hardcoded delete of all cars
        if len(self.project.Cars)==0:
            if len(self.carModelsFrame.winfo_children())>0:
                [x.destroy() for x in self.carModelsFrame.winfo_children()]
        else:
            #If theres fewer widgets than cars, add  more car widgets
            if len(self.carModelsFrame.winfo_children())<len(self.project.Cars):
                for x in range(len(self.project.Cars)-len(self.carModelsFrame.winfo_children())):
                    Car(self.carModelsFrame).pack(side=tk.TOP, fill=tk.X, expand = 1)
            #If theres more widgets than cars, trim down the list of cars
            if len(self.carModelsFrame.winfo_children())>len(self.project.Cars):
                for x in range(len(self.carModelsFrame.winfo_children())-len(self.project.Cars)):
                    self.carModelsFrame.winfo_children()[x].remove()
            
            #Once we have the appropriate amount of widgets, if we have more than one car, grab the names from the list of cars and reassign the names and indexes to the widgets
            if len(self.project.Cars)>0:
                for index, widget in enumerate(self.carModelsFrame.winfo_children()):
                    widget.removeTrace()
                    
                    def assignWidgetName(index = index):
                        widget.name.set(self.project.Cars[index].name)
                    
                    assignWidgetName()
                    #Update the name and index of the car widget to link to the appropriate location                 
                    def traceCommand(x, y, z, index=index, widget=widget):
                        self.setProjectCarName(index, widget.name.get())
                        #print(widget.index)
                        print("%s %s %s %s"%(x, y, z, index))
                    
                    def removeCommand(index = index):
                        self.removeProjectCar(index)
                    
                    #Rebind the car widget commands to link to the appropriate indexes and such
                    widget.observer = widget.name.trace("w", traceCommand)
                    widget.remove_button.config(command = removeCommand)
    
    def setProjectCarName(self, index, name):
        print(name)
        self.project.setCarName(index, name)
    
    def removeProjectCar(self, index):
        self.project.removeCar(index)
        for x in self.project.Cars:
            print(x.name)
        self.refreshUI()
    
    def addCar(self):
        self.project.addCar("New Car Trim")
        for x in self.project.Cars:
            print(x.name)
        self.refreshUI()
        #Car(self.carModelsFrame).pack(side=tk.TOP, fill=tk.X, expand = 1)
        
    def getAllCarNames(self):
        #return [x.car_name.get() for x in self.carModelsFrame.winfo_children()]
        return [car.name for car in self.project.Cars]
    
    def newProject(self):
        if messagebox.askokcancel("New Project", "Would you like to create a new project?")==True:
            self.project.resetProject()
            self.projectName.set("")
            self.refreshUI()

    def initGUI(self):
        self.root.title("OEM Project Creator")

        #Main frame to pack subframes for different things in
        mainFrame = tk.Frame(self.root, padx = 4, pady = 4)
        mainFrame.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
        
        toolbarFrame = tk.Frame(mainFrame, padx = 4, pady = 4)
        toolbarFrame.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
        
        #Menu
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Quit", command=lambda: self.root.destroy())
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu = menubar)

        #New and Load buttons
        tk.Button(toolbarFrame, image = self.images["PageIcon"], relief = tk.SUNKEN, command = lambda: self.newProject(), width = 20, height = 20).pack(side = tk.LEFT)
        tk.Button(toolbarFrame, image = self.images["FolderImageSmall"], relief = tk.SUNKEN, command = lambda: self.loadProject(), width = 20, height = 20).pack(side = tk.LEFT)
        tk.Button(toolbarFrame, image = self.images["FloppyDisk"], relief = tk.SUNKEN, command = lambda: self.createProject(), width = 20, height = 20).pack(side = tk.LEFT)

        #The main frame for all the settings
        settingsFrame = tk.LabelFrame(mainFrame, text = "Settings", padx = 4, pady = 4)
        settingsFrame.pack(side = tk.TOP, fill=tk.BOTH, expand = 1)
        
        #Project name
        tk.Label(settingsFrame, text = "Project Name: ").grid(          row=0, column=0, sticky = "W")
        tk.Entry(settingsFrame, textvariable = self.projectName).grid(  row=0, column=1, columnspan=2, sticky = "E W" )
        
        #Project directory setting
        tk.Label(settingsFrame, text = "Create Project In: ").grid(row=1, column=0, sticky = "W")
        tk.OptionMenu(settingsFrame, self.selected_directory, self.project_directories[0][1], self.project_directories[1][1]).grid(row=1, column = 1, columnspan=2, sticky = "E W")
        
        #The interior car models frame for all the individual car models
        carsFrame = tk.LabelFrame(settingsFrame,text = "Car Trims", padx=4, pady=4)
        carsFrame.grid(row=2, column=0, columnspan=2, rowspan = 2, sticky = "N E W S")
        #carsFrame.grid_propagate(0)
        
        canvas = tk.Canvas(carsFrame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
        self.carModelsFrame = tk.Frame(canvas)
        self.carModelsFrame.pack(side=tk.TOP, fill=tk.BOTH, expand = 1)
        
        s = tk.Scrollbar(carsFrame, orient=tk.VERTICAL, command = canvas.yview)
        s.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=s.set)
        canvas.create_window((0,0), window=self.carModelsFrame, anchor='nw')
        self.carModelsFrame.bind("<Configure>",lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        
        #The add car model button
        tk.Button(settingsFrame, image = self.images["AddIcon"], width = 20, height = 20, command = lambda: self.addCar()).grid(row=2, column=2, sticky = "N E W", pady = 6)
        
        #Add the first car
        #Car(self.carModelsFrame).pack(side=tk.TOP, fill=tk.X, expand = 1)

        self.root.wm_resizable(0, 0)
        
if __name__ == "__main__":
    process = OEMProjectSetup()
    #process.refreshAvailableParts()
    #process.refreshSelectedParts()
    process.root.mainloop()
