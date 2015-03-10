'''
Created on Jan 28, 2015

@author: cgi-28
'''
import tkinter as tk
from tkinter import messagebox, filedialog
import project


def reverse_enumerate(iterable):
    """
    Enumerate over an iterable in reverse order while retaining proper indexes
    """
    return zip(reversed(range(len(iterable))), reversed(iterable))

class AddNewPartWindow(tk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        tk.Toplevel.__init__(self, master, *args, **kwargs)
        
        self.var = tk.StringVar()
        
        f = tk.Frame(self)
        f.pack(side=tk.TOP, fill=tk.BOTH, expand = 1, padx = 10, pady = 10)
        
        tk.Label(f, text = "Enter name of new part").grid(column=0, row=0)
        
        #Create a variable for this entry so we can bind the return key
        self.entry = tk.Entry(f, textvariable = self.var)
        self.entry.grid(column=1, row=0)
        
        #Create a variable for this button so we can bind it externally
        self.addButton = tk.Button(f, text = "Add")
        self.addButton.grid(column=0, row=1)
        
        tk.Button(f, text = "Cancel", command = lambda: self.destroy()).grid(column=1, row=1)
    
    def returnValue(self):
        self.destroy()
        return self.var.get()

class AssignPartVariantsWindow(tk.Toplevel):
    def __init__(self, master, names,  *args, **kwargs):
        
        self.stringVars = []
        self.baseNames = []
        
        
        tk.Toplevel.__init__(self, master, *args, **kwargs)
        
        self.masterFrame = tk.Frame(self)
        self.masterFrame.pack(side=tk.TOP, fill=tk.BOTH, expand = 1)
        
        for x in names:
            self.addRenameFrame(x)
        
        frame = tk.Frame(self.masterFrame)
        frame.pack(side=tk.TOP, fill=tk.X, expand = 1)
        self.setButton = tk.Button(frame, text = "Add")
        self.setButton.pack(side=tk.LEFT, fill=tk.BOTH, expand = 1)
        tk.Button(frame, text = "Cancel", command = lambda: self.destroy()).pack(side=tk.LEFT, fill=tk.BOTH, expand = 1)
    
    def addRenameFrame(self, partName):
        self.stringVars.append(tk.StringVar())
        self.baseNames.append(partName)
        #self.stringVars[-1].set(partName)
        
        frame = tk.Frame(self.masterFrame)
        frame.pack(side=tk.TOP, fill=tk.X, expand = 1)
        
        tk.Label(frame, text = "Enter a suffix for %s: "%(partName)).pack(side=tk.LEFT)
        tk.Entry(frame, textvariable = self.stringVars[-1]).pack(side=tk.RIGHT)
        
    def returnValues(self):
        #self.delayedDestroy()
        return_vals = []
        
        for x, y in zip(self.baseNames, self.stringVars):
            if not y=="":
                return_vals.append([x, y.get()])
        
        self.destroy()
        return return_vals
        
        
class RenamePartVariantWindow(tk.Toplevel):
    def __init__(self, master, indexes, names,  *args, **kwargs):
        
        self.stringVars = []
        
        tk.Toplevel.__init__(self, master, *args, **kwargs)
        
        self.masterFrame = tk.Frame(self)
        self.masterFrame.pack(side=tk.TOP, fill=tk.BOTH, expand = 1)
        
        for x in names:
            self.addRenameFrame(x)
        
        frame = tk.Frame(self.masterFrame)
        frame.pack(side=tk.TOP, fill=tk.X, expand = 1)
        self.setButton = tk.Button(frame, text = "Set")
        self.setButton.pack(side=tk.LEFT, fill=tk.BOTH, expand = 1)
        tk.Button(frame, text = "Cancel", command = lambda: self.destroy()).pack(side=tk.LEFT, fill=tk.BOTH, expand = 1)
    
    def addRenameFrame(self, partName):
        self.stringVars.append(tk.StringVar())
        self.stringVars[-1].set(partName.split("_")[1])
        
        frame = tk.Frame(self.masterFrame)
        frame.pack(side=tk.TOP, fill=tk.X, expand = 1)
        
        tk.Label(frame, text = "Enter new suffix for %s: "%(partName)).pack(side=tk.LEFT)
        tk.Entry(frame, textvariable = self.stringVars[-1]).pack(side=tk.RIGHT)
        
    def returnValues(self):
        #self.delayedDestroy()
        self.destroy()
        return [x.get() for x in self.stringVars]
    
class Car(tk.LabelFrame):
    def __init__(self, master, name, *args, **kwargs):
        self.images = {"FolderImage":tk.PhotoImage(file = "folder.pbm"),
               "FolderImageSmall":tk.PhotoImage(file = "folder_small.pbm"),
               "ArrowRight":tk.PhotoImage(file = "arrow_right.pbm"),
               "ArrowLeft":tk.PhotoImage(file = "arrow_left.pbm"),
               "ArrowLeftShort":tk.PhotoImage(file = "arrow_left_short.pbm"),
               "ArrowRightShort":tk.PhotoImage(file = "arrow_right_short.pbm"),
               "ExitIcon":tk.PhotoImage(file = "exit_icon.pbm"),
               "AddIcon":tk.PhotoImage(file = "add_icon.pbm"),
               "MinusIcon":tk.PhotoImage(file = "minus_icon.pbm"),
               "ArrowRightDown":tk.PhotoImage(file = "arrow_right_down.pbm"),
               "ArrowLeftTiny":tk.PhotoImage(file = "arrow_left_tiny.pbm"),
               "ArrowRightTiny":tk.PhotoImage(file = "arrow_right_tiny.pbm"),}
        
        #color="gray90"
        #self.partVariants = []
        #self.name = name
        self._selected = tk.IntVar()
        self._selected.set(0)
        self.observer=None
        
        tk.LabelFrame.__init__(self, master, text = name, *args, **kwargs)
        color=self["background"]
        interiorFrame = tk.Frame(self, width=200, height=60, bg = color)
        interiorFrame.pack(side=tk.TOP)
        interiorFrame.pack_propagate(0)
        
        buttonsFrame = tk.Frame(interiorFrame, bg = color)
        buttonsFrame.pack(side=tk.LEFT, fill=tk.Y)
        
        tk.Checkbutton(buttonsFrame, variable = self._selected).pack(side=tk.TOP)
        #self.addPartVariantButton = tk.Button(buttonsFrame, image = self.images["ArrowRightTiny"], width = 20, height = 20, bg = color)#, command = lambda: self.addPartVariants(self.selectedPartVariant.get()))
        #self.addPartVariantButton.pack(side=tk.TOP)
        
        self.deletePartVariantButton = tk.Button(buttonsFrame, image = self.images["MinusIcon"], width = 20, height = 20, bg = color)#, command = lambda: self.removePartVariants())
        self.deletePartVariantButton.pack(side=tk.TOP)
        
        #tk.Label(interiorFrame, text = "Part Variants:", bg = color).pack(side=tk.TOP, fill=tk.X)
        
        self.partVariationsWidget = tk.Listbox(interiorFrame, selectmode = tk.EXTENDED, bg = color)
        self.partVariationsWidget.pack(side=tk.RIGHT, fill=tk.BOTH, expand = 1)
    
    def deselect(self):
        self._selected.set(0)
    
    def selected(self):
        if self._selected.get()==1:
            return True
        return False
    
    def refreshUI(self, selected_variants):
        self.partVariationsWidget.delete(0, tk.END)
        [self.partVariationsWidget.insert(tk.END, v) for v in selected_variants]

        #self.addPartVariantSelector['menu'].delete(0, tk.END)
        #for v in part_variants:
        #    self.addPartVariantSelector['menu'].add_command(label = v, command = tk._setit(self.selectedPartVariant, v))
            
    def removeTrace(self):
        if self.observer!=None:
            self.selectedPartVariant.trace_vdelete("w", self.observer)

class OEMProjectSetup():
    def __init__(self):
        self.initVars()
        self.initImages()
        self.initGUI()
        self.refreshUI()
    
    def initVars(self):
        self.project = project.Project()
        #Set the root variable
        self.root = tk.Tk()
        
        #Set the necessary control variables
        self.selectedPartsFrame = None
        self.availablePartsFrame = None
        
        #TKinter variables
        #self.projectCreateDirectory = tk.StringVar()
        self.projectName = tk.StringVar()
        #self.carName = tk.StringVar()

    def refreshUI(self):
        #Refresh the UI, properly relinking things to changes made to the project class
        
        if self.project.projectName!=None and self.project.projectName!="":
            self.projectName.set("Project: %s"%(self.project.projectName))
        else:
            self.projectName.set("Project: None")
        
        #Rebuild the list of available parts
        self.availablePartsWidget.delete(0, tk.END)
        [self.availablePartsWidget.insert(tk.END, x) for x in self.project.Parts.availableParts]
        #Rebuild the list of selected parts
        self.selectedPartsWidget.delete(0, tk.END)
        [self.selectedPartsWidget.insert(tk.END, x) for x in self.project.Parts.selectedParts]
        #Rebuild the list of part variants
        '''self.partVariantsWidget.delete(0, tk.END)
        [self.partVariantsWidget.insert(tk.END, x) for x in self.project.Parts.partVariants]'''
        
        #Equalize car widgets
        while len(self.carsFrame.winfo_children())<len(self.project.Cars):
            self.addCar()
        
        while len(self.carsFrame.winfo_children())>len(self.project.Cars):
            self.carsFrame.winfo_children()[-1].destroy()
            
        if len(self.project.Cars)>0:
            for index, car in enumerate(self.project.Cars):
                widget = self.carsFrame.winfo_children()[index]
                #Update the widgets UI
                widget.removeTrace()
                widget.refreshUI(self.project.Cars[index].associated_part_variants)
                #Relink the buttons and dropdowns from outside the widget so they tie back to the variables in this class
                def addPartVariantCommand(index = index):
                    selection = self.partVariantsWidget.curselection()
                    if len(selection)>0:
                        for s in selection:
                            self.project.Cars[index].addPartVariant(self.project.Parts.partVariants[int(s)])
                    self.refreshUI()
                
                def removePartVariantCommand(index = index, widget = widget):
                    print("Executing remove callback")
                    selection = widget.partVariationsWidget.curselection()
                    print(str(selection))
                    if len(selection)>0:
                        self.project.Cars[index].removePartVariants(selection)
                    self.refreshUI()
                #widget.name = car.name
                widget.config(text = car.name)
                #widget.addPartVariantButton.config(command = addPartVariantCommand)
                widget.deletePartVariantButton.config(command = removePartVariantCommand)

    def loadProject(self):
        if not self.project.projectCreated() or messagebox.askokcancel("Project already loaded", "Would you like to load a new project?  There may be unsaved changes with this one."):
            dir = filedialog.askdirectory()
            try:
                if not dir == "":                    
                    if self.project.loadProject(dir)==False:
                        return False
                    self.refreshUI()
                else:
                    print("Load Aborted")
            except TypeError as E:
                print("Error encountered while loading project: %s"%(E))

    def saveProject(self):
        self.project.saveProject()
    
    def initImages(self):
        self.images = {"FolderImage":tk.PhotoImage(file = "folder.pbm"),
                       "FolderImageSmall":tk.PhotoImage(file = "folder_small.pbm"),
                       "ArrowRight":tk.PhotoImage(file = "arrow_right.pbm"),
                       "ArrowLeft":tk.PhotoImage(file = "arrow_left.pbm"),
                       "ArrowLeftShort":tk.PhotoImage(file = "arrow_left_short.pbm"),
                       "ArrowRightShort":tk.PhotoImage(file = "arrow_right_short.pbm"),
                       "ExitIcon":tk.PhotoImage(file = "exit_icon.pbm"),
                       "Hamburger":tk.PhotoImage(file = "hamburger_icon.pbm"),
                       "Lock":tk.PhotoImage(file = "lock_icon.pbm"),
                       "AddIcon":tk.PhotoImage(file = "add_icon.pbm"),
                       "FloppyDisk":tk.PhotoImage(file = "floppy_disc.pbm"),
                       "ArrowLeftTiny":tk.PhotoImage(file = "arrow_left_tiny.pbm"),
                       "ArrowRightTiny":tk.PhotoImage(file = "arrow_right_tiny.pbm"),}
    
    def addPartToSelected(self, indexes):
        self.project.moveToSelectedParts(indexes)
        self.refreshUI()
    
    def addPartToAvailable(self, indexes):
        try:
            if all((not indexes==None, len(indexes)>0)):
                r = self.project.moveToAvailableParts(indexes)
                if len(r)>0 and messagebox.askokcancel("Parts are Referenced!", "You are trying to remove parts that have been referenced by cars, are you sure you want to continue?"):
                    self.project.moveToAvailableParts(indexes, True)
                self.refreshUI()
        except Exception as E:
            print(E)
    
    def createPartVariants(self, indexes):
        self.project.createPartVariants(indexes)
        self.refreshUI()
    
    def getSelectedCarIndexes(self):
        return [x for x in range(len(self.carsFrame.winfo_children())) if self.carsFrame.winfo_children()[x].selected()]
    
    def assignPartVariantsWindow(self, names):
        if len(self.getSelectedCarIndexes())>0:
            assign = AssignPartVariantsWindow(self.root, names)
            assign.setButton.config(command = lambda: self.assignPartVariants(assign.returnValues(), self.getSelectedCarIndexes()))
    
    def assignPartVariants(self, variants, car_indexes):
        self.project.assignVariantToCars(variants, car_indexes)
        for x in self.carsFrame.winfo_children():
            x.deselect()
        self.refreshUI()
        
    def removePartVariants(self, indexes):
        try:
            if all((not indexes==None, len(indexes)>0)):
                r = self.project.removePartVariants(indexes)
                if len(r)>0 and messagebox.askokcancel("Parts are Referenced!", "You are trying to remove part variants that have been referenced by cars, are you sure you want to continue?"):
                    self.project.removePartVariants(indexes, True)
                self.refreshUI()
        except Exception as E:
            print(E)
    
    def renamePartVariantsWindow(self):
        selection = self.partVariantsWidget.curselection()
        if len(selection)>0:
            rename = RenamePartVariantWindow(self.root, selection, [self.partVariantsWidget.get(x) for x in self.partVariantsWidget.curselection()])
            rename.setButton.config(command = lambda: self.renamePartVariants(selection, rename.returnValues()))
    
    def addAvailablePartWindow(self):
        add = AddNewPartWindow(self.root)
        add.addButton.config(command = lambda: self.addNewAvailablePart(add.returnValue()))
        add.entry.bind("<Return>", lambda event: self.addNewAvailablePart(add.returnValue()))
        add.entry.focus()
    
    def renamePartVariants(self, indexes, names):
        self.project.renamePartVariants(indexes, names)
        self.refreshUI()
    
    def addNewAvailablePart(self, name):
        self.project.Parts.addNewAvailablePart(name)
        self.refreshUI()
        
    def sortPartVariants(self):
        self.project.Parts.sortPartVariants()
        self.refreshUI()
    
    #Trigger an update to refresh which variant parts cars can select
    #def updateAllCarPartVariantLists(self):
    #    if len(self.cars)>0:
    #        for car in self.cars:
    #            car.updateVariantsList(self.project.Parts.partVariants)
    
    def addCar(self, name = "default"):
        new = Car(self.carsFrame, name, font = (None, 12, "bold"))#, bg = "gray90")
        new.pack(side=tk.TOP, pady = 2)        
        #self.cars.append(new)
    
    def getAvailableParts(self):
        return self.availablePartsWidget.get(0, tk.END)
    
    def getSelectedParts(self):
        return self.selectedPartsWidget.get(0, tk.END)
    
    def getPartVariants(self):
        return self.partVariantsWidget.get(0, tk.END)
    
    def sortAvailableParts(self):
        self.project.Parts.sortAvailableParts()
        self.refreshUI()
    
    def sortSelectedParts(self):
        self.project.Parts.sortSelectedParts()
        self.refreshUI()
    
    def initGUI(self):
        self.root.title("OEM Project Creator")
        
        #Main frame for everything.
        mainFrame = tk.Frame(self.root, padx = 0, pady = 0)
        mainFrame.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
        
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Quit", command=lambda: self.root.destroy())
        
        self.root.config(menu = menubar)
        
        projectInfoFrame = tk.Frame(mainFrame)
        projectInfoFrame.pack(side=tk.TOP, fill=tk.X, expand = 1)
        
        tk.Label(projectInfoFrame, textvariable = self.projectName, font = (None, 16, "bold")).pack(side=tk.LEFT, fill=tk.X)
        
        internalFrame = tk.Frame(mainFrame, padx = 4, pady = 4)
        internalFrame.pack(side = tk.RIGHT, fill=tk.BOTH, expand = 1)
        
        toolbarFrame = tk.Frame(internalFrame,padx = 4, pady = 4)
        toolbarFrame.pack(side=tk.LEFT, fill=tk.Y)
        
        tk.Button(toolbarFrame, image=self.images["FolderImageSmall"], command = lambda: self.loadProject()).pack(side=tk.TOP)
        tk.Button(toolbarFrame, image=self.images["FloppyDisk"], command=lambda: self.saveProject()).pack(side=tk.TOP)
        tk.Button(toolbarFrame, image=self.images["AddIcon"], command = lambda: self.addAvailablePartWindow()).pack(side=tk.BOTTOM)
        
        #Create the available parts frame
        self.availablePartsFrame = tk.LabelFrame(internalFrame, text = "Available Parts",font = (None, 14, "bold") ,padx = 4, pady = 4, width=210, height = 400)
        self.availablePartsFrame.pack(side = tk.LEFT, padx = 4)#, fill = tk.Y)
        self.availablePartsFrame.pack_propagate(0)
        
        #Create the selected Parts Frame
        self.selectedPartsFrame = tk.LabelFrame(internalFrame, text = "Common Parts",font = (None, 14, "bold"),padx = 4, pady = 4, width=210, height = 400)
        self.selectedPartsFrame.pack(side = tk.LEFT, padx = 4)#, fill = tk.Y)
        self.selectedPartsFrame.pack_propagate(0)
        
        #Create the Part Variants frame
        '''self.partVariantsFrame = tk.LabelFrame(internalFrame, text = "Part Variants",font = (None, 14, "bold"),padx = 4, pady = 4, width=210, height = 400)#, height=200)
        self.partVariantsFrame.pack(side=tk.LEFT, padx = 4)#, fill=tk.Y)
        self.partVariantsFrame.pack_propagate(0)'''
        #self.partVariantsFrame.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)

        #Make the cars widget frame and canvas stuff
        self.partAssignmentFrame = tk.LabelFrame(internalFrame, text = "Trim Level Variations",font = (None, 14, "bold"),padx = 0, pady = 0, height = 400, width = 250)
        self.partAssignmentFrame.pack(side=tk.LEFT, padx = 8)#, fill=tk.BOTH, expand = 1)
        self.partAssignmentFrame.pack_propagate(0)

        ## 
        #Create the available parts listbox
        f = tk.Frame(self.availablePartsFrame)
        f.pack(side=tk.TOP, fill=tk.X)
        tk.Button(f, image = self.images["Hamburger"], command=lambda: self.sortAvailableParts(),height=20).pack(side=tk.LEFT)
        tk.Button(f, image = self.images["ArrowRight"], height=20, width = 100, command = lambda: self.addPartToSelected(self.availablePartsWidget.curselection())).pack(side=tk.RIGHT)
        
        self.availablePartsWidget = tk.Listbox(self.availablePartsFrame, selectmode = tk.EXTENDED)
        self.availablePartsWidget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        ##
        #Create the selected parts list box
        f = tk.Frame(self.selectedPartsFrame)
        f.pack(side=tk.TOP, fill=tk.X)
        tk.Button(f, image = self.images["ArrowLeftShort"], height=20,command = lambda: self.addPartToAvailable(self.selectedPartsWidget.curselection())).pack(side=tk.LEFT)
        tk.Button(f, image = self.images["Hamburger"], height=20, command=lambda: self.sortSelectedParts()).pack(side=tk.LEFT, fill=tk.X, expand = 1)
        #tk.Button(f, image = self.images["Lock"], height=20).pack(side=tk.LEFT, fill=tk.X, expand = 1)
        tk.Button(f, image = self.images["ArrowRightShort"], height=20, command = lambda: self.assignPartVariantsWindow(self.selectedPartsWidget.curselection())).pack(side=tk.LEFT)

        self.selectedPartsWidget = tk.Listbox(self.selectedPartsFrame, selectmode = tk.EXTENDED)
        self.selectedPartsWidget.pack(side=tk.TOP, fill=tk.BOTH, expand = 1)
        
        ##
        #Create the part variants listbox
        ''''f=tk.Frame(self.partVariantsFrame)
        f.pack(side=tk.TOP, fill=tk.X)
        tk.Button(f, image = self.images["ArrowLeftShort"], height=20, width = 40, command = lambda: self.removePartVariants(self.partVariantsWidget.curselection())).pack(side=tk.LEFT)
        tk.Button(f, image = self.images["ArrowRightShort"], command = lambda: self.renamePartVariantsWindow()).pack(side=tk.RIGHT)
        tk.Button(f, image = self.images["Hamburger"], height=20, width = 20, command = lambda: self.sortPartVariants()).pack(side=tk.RIGHT)
        tk.Button(f, text="Rename", command = lambda: self.renamePartVariantsWindow()).pack(side=tk.RIGHT)

        #Make the Parts Variant Frame
        self.partVariantsWidget = tk.Listbox(self.partVariantsFrame, selectmode = tk.EXTENDED)
        self.partVariantsWidget.pack(side=tk.TOP, fill=tk.BOTH, expand = 1)'''

        #Frame for the car widgets  
        s = tk.Scrollbar(self.partAssignmentFrame, orient=tk.VERTICAL)#, command = canvas.yview)
        s.pack(side=tk.RIGHT, fill=tk.BOTH, expand = 1)
              
        canvas = tk.Canvas(self.partAssignmentFrame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
        s.config(command = canvas.yview)
        
        self.carsFrame = tk.Frame(canvas, padx=4, pady=4)
        self.carsFrame.pack(side=tk.TOP, fill=tk.BOTH, expand = 1)
        
        
        canvas.configure(yscrollcommand=s.set)
        canvas.create_window((0,0), window=self.carsFrame, anchor='nw')
        self.carsFrame.bind("<Configure>",lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
                
        self.root.wm_resizable(0, 0)
        
if __name__ == "__main__":
    process = OEMProjectSetup()
    process.root.mainloop()
