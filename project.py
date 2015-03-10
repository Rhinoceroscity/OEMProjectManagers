import os, shutil, glob, project_dirs, time

variant_name_delimiter = "__"

def moveFolder(src, dst):
    try:
        for src_dir, dirs, files in os.walk(src):
            dst_dir = src_dir.replace(src, dst)
            if not os.path.exists(dst_dir):
                os.mkdir(dst_dir)
            for file_ in files:
                print("Moving file %s..."%(file_))
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    os.remove(dst_file)
                shutil.copy(src_file, dst_dir)
    except Exception as E:
        print("Error moving folder from %s to %s: %s"%(src, dst, E))

def reverse_enumerate(iterable):
    return zip(reversed(range(len(iterable))), reversed(iterable))

def generateReferenceScript(fileLocation, nameSpace):
    return ("file -rdi 1 -ns \"%s\" -rfn \"%sRN\" -op \"v=0;\"\n"%(nameSpace, nameSpace) +
         "     \"%s\";\n"%(fileLocation) +
         "file -r -ns \"%s\" -dr 1 -rfn \"%sRN\" -op \"v=0;\"\n"%(nameSpace, nameSpace) +
         "     \"%s\";\n"%(fileLocation))

def generateReferenceScript2(partName):
    return '''
createNode reference -n "%sRN";
setAttr ".ed" -type "dataReferenceEdits" 
        "%sRN"
        "%sRN" 0;
    setAttr ".lk" yes;
lockNode -l 1 ;'''%(partName, partName, partName)

def appendReferenceScriptEnd():
    return '''
createNode reference -n "sharedReferenceNode";
    setAttr ".ed" -type "dataReferenceEdits" 
        "sharedReferenceNode";'''

#The class for our cars and car related functions
class Car():
    def __init__(self, name):
        self.name = name
        #self.associated_parts = []
        self.associated_part_variants = []
        
        #Initialize our changed name variable
        self.oldName = name
    
    #Attempts to update a singular reference of Oldname to Newname
    def updateVariantReference(self, oldName, newName):
        for index, i in enumerate(self.associated_part_variants):
            if oldName == i:
                self.associated_part_variants[index] = newName
                print("Executing name replace")
                break
    
    #Attempts to update a list of Oldnames to their respective Newnames.  Both lists must be of equal length
    def updateVariantReferences(self, oldNames, newNames):
        for index, i in enumerate(self.associated_part_variants):
            for oldName, newName in zip(oldNames, newNames):
                if oldName == i:
                    self.associated_part_variants[index] = newName
                    print("Executing name replace")
                    break
    
    def removePartReferences(self, partNames):
        #Provide a list of parts to remove from the cars if they have them
        for index, x in reverse_enumerate(self.associated_part_variants):
            for y in partNames:
                if y in x:
                    self.removePartVariant(index)
    
    def removeVariantReferences(self, variantNames):
        #Provide a list of variants to remove from the cars if they have them
        for index, x in reverse_enumerate(self.associated_part_variants):
            for y in variantNames:
                if y == x:
                    self.removePartVariant(index)
    
    #Returns the associated part variants list variable
    def getPartVariants(self, indexes="all"):
        if not indexes=="all":
            try:
                return [self.associated_part_variants[x] for x in indexes]
            except IndexError as E:
                print(E)
        else:
            return self.associated_part_variants
    
    #Adds a part variant onto the end of the list
    def addPartVariant(self, partVariant):
        #The checks here go through 1) making sure this exact part is not in part variants, 2) making sure the part is not equal to None, 3) making sure multiple variants of the same part arent being added
        if all((partVariant not in self.associated_part_variants, not partVariant.lower() == "none", True not in [partVariant.split(variant_name_delimiter)[0] == x.split(variant_name_delimiter)[0] for x in self.associated_part_variants])):
            self.associated_part_variants.append(partVariant)
            return True
        else:
            return False
    
    #Remove all part variants
    def clearPartVariants(self):
        self.associated_part_variants.clear()
    
    #Removes part variants from the specified indexes
    def removePartVariants(self, indexes):
        if len(indexes)>0:
            for i in reversed(sorted(indexes)):
                self.removePartVariant(i)
                
    #Removes a singular part variant
    def removePartVariant(self, index):
        del(self.associated_part_variants[int(index)])
    
    def exists(self, dataFolder, name = ""):
        if name == "": name = self.name
        try:
            if os.path.isdir(os.path.join(dataFolder, "%s/"%(name))):
                return True
            return False
        except Exception as E:
            return False
    
    def setName(self, dataFolder, name):
        #Update the name of the car, setting both the old and new name if the car doesnt exist
        #If it does, only update the new name so the car knows to try and update the folder instead
        #Of creating a new car when saved
        if not self.exists(dataFolder, self.oldName):
            self.oldName = name
            print("Car not yet created, updating old name and new name")
        else:
            print("Car created, updating only new name")
        self.name = name
    
    def generateDataFolder(self, dataFolder, carName = ""):
        if carName == "": carName = self.name
        if not os.path.isdir(os.path.join(dataFolder, "%s"%(carName))):
            os.makedirs(os.path.join(dataFolder, "%s/01_Vehicle_Data/"%(carName)))
    
            os.makedirs(os.path.join(dataFolder, "%s/02_Reference_Shots/Detail_shots/"%(carName)))
            os.makedirs(os.path.join(dataFolder, "%s/02_Reference_Shots/orthos_shots/"%(carName)))
            
            os.makedirs(os.path.join(dataFolder, "%s/03_Client_Data/"%(carName)))
    
    #Save information about the car
    #Input the DATA folder here.
    def saveCar(self, dataFolder, componentsFolder, clayCompleteFolder, components):
        try:
            if os.path.isdir(dataFolder):
                if self.oldName==self.name:
                    print("Old name is same as new name, saving new car")
                    self.generateDataFolder(dataFolder, self.name)
                    f = open(os.path.join(dataFolder, "%s/01_Vehicle_Data/vehicle_data"%(self.name)), "w+")
                    if len(self.getPartVariants("all"))>0:
                        for part in self.getPartVariants("all"):
                            f.write(part+"\n")
                    f.close()
                    self.generatePublishedAsciiFile(componentsFolder, clayCompleteFolder, "/rendershare/LIBRARY/cg_production/00_resources/production_scripts/Modeling_Pipeline/EmptyMayaFileTemplates/empty.ma", components)
                    return True
                else:
                    print("Old name is different than new name, updating car folder and reference file")
                    if os.path.isdir(os.path.join(dataFolder, "%s"%(self.oldName))):
                        print("Old car folder found, updating to new car folder name")
                        oldName = os.path.join(dataFolder, "%s/"%(self.oldName))
                        newName = os.path.join(dataFolder, "%s/"%(self.name))
                        #Create a copy of the folder with the new name
                        moveFolder(oldName, newName)
                        #Remove the old car folder (which should also make a backup of the old one)
                        self.removeCar(dataFolder, self.oldName)
                        #Rebuild vehicle data file
                        f = open(os.path.join(dataFolder, "%s/01_Vehicle_Data/vehicle_data"%(self.name)), "w+")
                        if len(self.getPartVariants("all"))>0:
                            for part in self.getPartVariants("all"):
                                f.write(part+"\n")
                        f.close()
                        #If theres already a .ma clay complete file, rename it, otherwise create a new one
                        if self.checkReferenceFile(clayCompleteFolder, self.oldName)!=False:
                            print("Old reference file found, updating...")
                            self.renameReferenceFile(self.oldName, self.name, clayCompleteFolder)
                        else:
                            self.generatePublishedAsciiFile(componentsFolder, clayCompleteFolder, "/rendershare/LIBRARY/cg_production/00_resources/production_scripts/Modeling_Pipeline/EmptyMayaFileTemplates/empty.ma", components)
                        self.oldName = self.name
                        #shutil.rmtree(oldName)
                        return True
                    else:
                        print("Old car folder not found, creating new car folder like normal")
                        self.generateDataFolder(dataFolder, self.name)
                        f = open(os.path.join(dataFolder, "%s/01_Vehicle_Data/vehicle_data"%(self.name)), "w+")
                        if len(self.getPartVariants("all"))>0:
                            for part in self.getPartVariants("all"):
                                f.write(part+"\n")
                        f.close()
                        
                        self.generatePublishedAsciiFile(componentsFolder, clayCompleteFolder, "/rendershare/LIBRARY/cg_production/00_resources/production_scripts/Modeling_Pipeline/EmptyMayaFileTemplates/empty.ma", components)
                        self.oldName = self.name
                        return True
            else:
                return False
        except Exception as E:
            print("Error encountered when saving car %s: %s"%(self.name, E))
            return False
    
    def checkReferenceFile(self, clayCompleteFolder, name = ""):
        #Check if this car has a reference file for a specified name
        if name=="": name = self.name
        reference_file =os.path.join(clayCompleteFolder, "%s.ma"%(name))
        print("Checking for reference file %s, %s"%(reference_file, name))
        try:
            if os.path.isfile(os.path.join(clayCompleteFolder, "%s.ma"%(name))):
                print("Reference file found %s"%(os.path.join(clayCompleteFolder, "%s.ma"%(name))))
                return os.path.join(clayCompleteFolder, "%s.ma"%(name))
            else:
                print("Reference file not found")
                return False
        except Exception as E:
            print("Error checking reference file: %s"%(E))
            return False
    
    def renameReferenceFile(self, oldName, newName, clayCompleteFolder):
        try:
            if os.path.isfile(os.path.join(clayCompleteFolder, "%s.ma"%(oldName))):
                shutil.move(os.path.join(clayCompleteFolder, "%s.ma"%(oldName)), os.path.join(clayCompleteFolder, "%s.ma"%(newName)))
        except Exception as E:
            print("Error renaming reference file: %s"%(E))
    
    def removeCar(self ,dataFolder, name=""):
        #This function is called when you want to remove a car data folder
        if name=="": name = self.name
        try:
            if os.path.isdir(dataFolder):
                print("Data folder valid for removing car.")
                if os.path.isdir(os.path.join(dataFolder, "%s/"%(name))):
                    car_data = os.path.join(dataFolder, "%s/"%(name))
                    print("Car data folder found: %s"%(car_data))
                    if not os.path.isdir(os.path.join(dataFolder, "_removed/")): os.mkdir(os.path.join(dataFolder, "_removed/"))
                    #Make a copy of the folder in the removed folder with a timestamp
                    moveFolder(car_data, os.path.join(dataFolder, "_removed/%s_%s/"%(name, time.strftime("%b%d%Y_%H-%M-%S",time.localtime(time.time())))))
                    #remove the old folder
                    shutil.rmtree(os.path.join(dataFolder, "%s/"%(name)))
        except Exception as E: print("Error removing car folder: %s"%(E))
    
    #Load information about a car from an info file
    #Input the DATA folder of the project here, and it'll find the folder based on the car's name
    def loadCar(self, dataFolder):
        print("Loading Car...")
        file = os.path.join(dataFolder, "%s/01_Vehicle_Data/vehicle_data"%(self.name))
        if os.path.isfile(file):
            self.clearPartVariants()
            f = open(file, "r")
            for line in f:
                self.associated_part_variants.append(line.rstrip("\n"))
                print("Added new part to car %s"%(self.name))
            f.close()
        else:
            print("No car data folder found for %s"%(self.name))

    #Create a published ASCII file for this car in clay complete.  It needs to be passed the root directory of the project and the list of component names
    def generatePublishedAsciiFile(self, componentsFolder, clayCompleteFolder, template_file, sharedComponents):
        print("Generating Published ASCII file")
        total_components = self.associated_part_variants
        
        [total_components.append(component) for component in sharedComponents if component not in [x.split(variant_name_delimiter)[0] for x in self.associated_part_variants]]
        total_components = set(total_components)
        print(str(total_components))
        #Input a list of components to reference
        if not os.path.isdir(componentsFolder):
            print("Component folder not found")
        elif not os.path.isdir(clayCompleteFolder):
            print("Clay complete folder not found")
        elif not len(total_components)>0:
            print("Not enough components")
        elif not os.path.isfile(template_file):
            print("Template file does not exist")
        else:
            reference_string = ""
            reference_string2=""
            for component in total_components:
                print("Component: %s"%(component))
                publish_directory = os.path.join(componentsFolder, "%s/Publish/%s_publish.mb"%(component, component))
                reference_string = reference_string + generateReferenceScript(publish_directory, component.replace(" ","_"))
                reference_string2=reference_string2 + generateReferenceScript2(component.replace(" ","_"))
            else:
                reference_string2=reference_string2 + appendReferenceScriptEnd()
                print(reference_string2)
            
            #Instead of copy pasting the file, we're going to read the text data of an empty maya ASCII file into a variable, insert the text, and save out a
            #Brand new file to the proper place
            f = open(template_file, "r")
            ma_file = f.readlines()
            f.close()
            
            #Insert the reference headers while its still a list
            ma_file.insert(4, reference_string)
            #Join it all into one string so we can do a search and replace
            ma_file = "".join(ma_file)
            #Add in the locked reference node scripts
            ma_file = ma_file.replace("//..REFERENCES_HERE..//", reference_string2)
            
            f = open(os.path.join(clayCompleteFolder, "%s.ma"%(self.name)), "w")
            [f.write(x) for x in ma_file]
            f.close()
    
#The container for our parts and part related functions
class Parts():
    def __init__(self):
        #The three main variables dictating a list of available parts, selected parts, and part variants of selected parts
        #A part in selected parts cannot exist in available parts and vice versa, and a part variant cannot exist without
        #Its base part remaining selected
        self.availableParts = []
        self.selectedParts = []
        self.partVariants = []
        self.initializeDefaultPartSelection("/rendershare/LIBRARY/cg_production/00_resources/production_scripts/Modeling_Pipeline/defaultParts")
        #A list of changed parts.  This is only useful for a project that has already generated component folders.
        #This variable creates a list of parts with old names and new names, and when the project is re-saved, goes
        #through and renames the appropriate part folders and all their subdirectories and files
        #(oldName, newName), if newName == _REMOVED, the part has been deleted and will be removed when the project is saved
        self.changed_parts = []
    
    def initializeDefaultPartSelection(self, fromFile = None):
    #Clears all selected parts, part variants, and part variants assigned to cars, and repopulates the default available parts
    #If an optional file is provided, it will load the default parts from there, line by line, one part per line
        if fromFile == None:
            self.partVariants.clear()
            self.selectedParts.clear()
            #self.availableParts.clear()
            self.availableParts = ["Headlight",
                                   "Taillight",
                                   "Front Grill",
                                   "Front Bumper",
                                   "Side Mirror",
                                   "Rear Bumper",
                                   "Antenna",
                                   "Door Handle",
                                   "Front Windshield",
                                   "Front Wipers",
                                   "Rear Wipers"]
            return True
        else:
            if os.path.isfile(fromFile):
                self.partVariants.clear()
                self.selectedParts.clear()
                self.availableParts.clear()
                f = open(fromFile, "r")
                for line in f:
                    add = line.rstrip("\n")
                    if add!="" and add.replace(" ","").lower() not in [x.replace(" ","").lower() for x in self.availableParts]:
                        self.availableParts.append(add)
                f.close()
                return True
            else:
                print("Invalid file path provided, initializing from built-in array.")
                self.availableParts = ["Headlight",
                                   "Taillight",
                                   "Front Grill",
                                   "Front Bumper",
                                   "Side Mirror",
                                   "Rear Bumper",
                                   "Antenna",
                                   "Door Handle",
                                   "Front Windshield",
                                   "Front Wipers",
                                   "Rear Wipers"]
                return False
    
    #Clears all the parts.  Should probably only be used when loading a new project
    def clearAllParts(self):
        self.availableParts.clear()
        self.selectedParts.clear()
        self.partVariants.clear()
    
    #Load parts from a tab delimited file.  The core directory of the project should be entered in dir
    #This will clear all part selections and such
    def loadParts(self, dataDirectory):
        file = os.path.join(dataDirectory, "parts_data")
        if os.path.isfile(file):
            print("Loading Parts...")
            #Clear all the parts already in the project so we don't have duplicates when it reloads the lists
            self.clearAllParts()
            f = open(file, "r")
            for line in f:
                key, value = line.replace("\n", "").split(":")
                
                if key=="AP":
                    print("Available Part %s"%(value))
                    self.availableParts.append(value)
                if key=="SP":
                    print("Selected Part %s"%(value))
                    self.selectedParts.append(value)
                #if key=="PV":
                #    print("Part Variant %s"%(value))
                #    self.partVariants.append(value)
            f.close()
            return True
        else:
            print("Parts data not found")
            return False
    
    #Save a tab delimited file with all the selected, available, and part variant parts
    def saveParts(self, dir):
        try:
            if os.path.isdir(dir):
                f = open(os.path.join(dir,"parts_data"), "w+")
                for x in self.availableParts:
                    f.write("AP:"+x+"\n")
                for x in self.selectedParts:
                    f.write("SP:"+x+"\n")
                #for x in self.partVariants:
                #    f.write("PV:"+x+"\n")
                f.close()
                return True
            else:
                return False
        except Exception as E:
            print("Error saving parts: %s"%(E))
            return False
    
    #Sort the part variants list in place
    #def sortPartVariants(self):
    #    self.partVariants.sort()
    
    def sortAvailableParts(self):
        self.availableParts.sort()
        
    def sortSelectedParts(self):
        self.selectedParts.sort()
    
    #Renames part variants
    #Returns list of old parts compared to new parts
    def renamePartVariants(self, indexes, names):
        #Get all the names of the part variants as old names
        oldPartNames = [self.partVariants[int(index)] for index in indexes]
        
        indexes = [int(x) for x in indexes]
        
        for index, name in zip(indexes, names):
            #If the person didnt just leave the entry blank
            if not name=="":
                part = self.partVariants[int(index)].split(variant_name_delimiter)[0]
                newName = part+"%s"%(variant_name_delimiter)+name.replace("_", "")
                #If there isnt already a part named with the new name we're trying to insert (cant have multiple variants with the same name)
                if not newName in self.partVariants:
                    self.partVariants[int(index)]=newName
                    #self.partVariantsWidget.delete(index)
                    #self.partVariantsWidget.insert(index, newName)
        
        newPartNames = [self.partVariants[int(index)] for index in indexes]
        
        print("Old Part Names: %s\nNew Part Names: %s"%(str(oldPartNames),str(newPartNames)))
        return (oldPartNames, newPartNames)
        #Rename all the appropriate parts to new names
        #for oldName, newName in zip(oldPartNames, newPartNames):
            #self.project.renameComponentFolder(oldName, newName)
        
        #Update all the car variant references before force updating their lists and possibly deleting them
        #for car in self.cars:
        #    car.updateVariantReferences(oldPartNames, newPartNames)
    
    #Takes in a list of strings for the component names
    def generateComponentFiles(self, componentsDir, components=[]):
        if os.path.isdir(componentsDir):
            if len(components)>0:
                for x in components:
                    folder = os.path.join(componentsDir, x)
                    
                    #If the folder for this component already exists, don't try to rebuild the maya files, since it might overwrite working files
                    if not os.path.isdir(folder):
                        os.makedirs(folder)
                        
                        #Create all the necessary subfolders
                        working = os.path.join(folder, "Working")
                        if not os.path.isdir(working): os.makedirs(working)
                        qa = os.path.join(folder, "QA")
                        if not os.path.isdir(qa): os.makedirs(qa)
                        publish = os.path.join(folder, "Publish")
                        if not os.path.isdir(publish): os.makedirs(publish)
                        
                        self.generateEmptyMayaFile("%s_Created_v001"%(x), "/rendershare/LIBRARY/cg_production/00_resources/Modeler_Folders/_Lights/EmptyMayaFileTemplates/empty.mb", working)
                        self.generateEmptyMayaFile("%s_publish"%(x), "/rendershare/LIBRARY/cg_production/00_resources/Modeler_Folders/_Lights/EmptyMayaFileTemplates/empty.mb", publish)
            else:
                print("No components entered")
                return False
        
    def generateEmptyMayaFile(self, name, template_file, destination):
        if os.path.isfile(template_file):
            if os.path.isdir(destination):
                shutil.copy(template_file, destination)
                original_fname = os.path.split(template_file)[1]
                copy_fname = os.path.join(destination, original_fname)
                new_fname = copy_fname.replace(os.path.split(copy_fname)[1].split(".")[0], name)
                os.rename(copy_fname, new_fname)
                return new_fname
            else:
                print("Destination not valid")
                return False
        else:
            print("Source not valid")
            return False
    
    def moveParts(self, indexes, dir=0):
        #Remap indexes to ints
        indexes = [int(index) for index in indexes]
        #0 = Available->Selected
        #1 = Selected->Available
        #2 = Selected->Variant
        #3 = Delete Variant
        #Move items FROM available parts TO selected parts
        print("Indexes: "+str(indexes))
        if dir == 0:
            if len(indexes)>0:
                #Append all the appropriate indexes of Available Parts to Selected Parts
                [self.selectedParts.append(self.availableParts[x]) for x in indexes if self.availableParts[x] not in self.selectedParts]
                #Delete the proper indexes out of available parts
                for x in sorted(indexes, reverse = True):
                    #print(x)
                    del(self.availableParts[x])
        
        #Move items FROM selected parts TO available parts
        if dir == 1:
            if len(indexes)>0:
                #Append all the appropriate indexes of Available Parts to Selected Parts
                [self.availableParts.append(self.selectedParts[x]) for x in indexes if self.selectedParts[x] not in self.availableParts]
                
                remove_variants = []
                #Remove all reliant part variants from the part variants list
                #for index, variant in enumerate(self.partVariants):
                #    for part in indexes:
                #        if self.selectedParts[part] in variant:
                #            remove_variants.append(index)
                #            
                #remove_variants = set(remove_variants)
                #if len(remove_variants)>0:
                #    for index in sorted(remove_variants, reverse=True):
                #        del(self.partVariants[index])
                            
                #Delete the proper indexes out of available parts
                for x in sorted(indexes, reverse = True):
                    del(self.selectedParts[x])
        #Create part variants
        '''if dir == 2:
            #Check all the part variants to see if we've already added this item, and iterate it up number wise if we have
            if len(indexes)>0:
                if len(self.partVariants)>0:
                    for index in indexes:
                        max=0
                        for i in self.partVariants:
                            if self.selectedParts[index] in i:
                                count = i.split("%s"%(variant_name_delimiter))[1]
                                if not False in [x.isdigit() for x in count]:
                                    count=int(count)
                                    if count>max:
                                        max=count
                        else:
                            self.partVariants.append(self.selectedParts[index]+"%s%s"%(variant_name_delimiter, str(max+1)))
                else:
                    for index in indexes:
                        self.partVariants.append(self.selectedParts[index]+"%s1"%(variant_name_delimiter))
        #Remove part variant
        if dir == 3:
            if len(indexes)>0:
                for index in sorted(indexes, reverse=True):
                    del(self.partVariants[index])'''
                    
        print("Available Parts: " + str(self.availableParts))
        print("Selected Parts: " + str(self.selectedParts))
        #print("Variants: " + str(self.partVariants) + "\n")
        #If it makes it this far, it succeeded.  It will return out of the function with False if it fails along the way
        return True    
        
    def addNewAvailablePart(self, name):
        print("Attempting to add part %s"%(name))
        #Adds a completely new available part independent of anything
        if not name.replace(" ","").lower() in [x.replace(" ","").lower() for x in self.availableParts] and not name.replace(" ","").lower() in [x.replace(" ","").lower() for x in self.selectedParts] and not name == "" and not name==None:
            self.availableParts.append(name)
            return True
        return False

    '''def removeAvailableParts(self, indexes):
        if len(indexes)>0:
            indexes = [int(x) for x in indexes]
            for index in sorted(indexes, reverse=True):
                self.'''
class Project():
    def __init__(self):
        self.initVars()

    def initVars(self):
        #Initialize the cars for this project.  This is just a holder for a class that contains the name of the car(trim), the associated parts, and any variants of those parts.
        self.Cars = []
        #
        self.removed_cars = []
        #Initialize our parts container
        self.Parts = Parts()
        
        #Name of the project
        self.projectName = ""
        
        #Location of the project on the server (either bto-secure, or Client_Projects)
        self.coreFolderLocation = ""
        
        #All the relevant folders to the project
        self.projectDataFolder = None
        self.coreFolder = None
        self.modelingFolder = None
        self.managementFolder = None
        self.dataFolder = None
        self.cgiFolder = None
        self.retouchingFolder = None
        self.componentsFolder = None

    def initFolderStructure(self, location, createFolders = False):
    #This function initializes the folder structure and all the relevant folders for this project.  If createFolders = True, it'll create all the folders and folder structures
    #In the coreFolderLocation of this project.  Otherwise it just initializes the variables.  createFolders should only be used when creating a new project.  When loading one,
    #It should be false.
        if os.path.isdir(location):
            print("Initializing folder structure")
            self.coreFolderLocation = location
            #Create the core folder if createFolders is on
            if createFolders == True:
                self.coreFolder = os.path.join(self.coreFolderLocation, self.projectName)
                if not os.path.isdir(self.coreFolder): os.mkdir(self.coreFolder)
            
            #Generate all the core level directories, then each of the subfolders within each one with custom functions
            self.managementFolder = os.path.join(self.coreFolder, "00_Management")
            if not os.path.isdir(self.managementFolder) and createFolders == True: os.mkdir(self.managementFolder)
            #self.generateManagementFolder()
            
            self.dataFolder = os.path.join(self.coreFolder, "01_Data")
            if not os.path.isdir(self.dataFolder) and createFolders == True: os.mkdir(self.dataFolder)
            
            self.modelingFolder = os.path.join(self.coreFolder, "02_Modeling")
            #Either create the folder structure, or assign some crucial variables that this project will need if its being loaded
            if createFolders==True:
                if not os.path.isdir(self.modelingFolder): os.mkdir(self.modelingFolder)
            else:
                self.componentsFolder = os.path.join(self.modelingFolder, "03_Components/")
                self.clayCompleteFolder = os.path.join(self.modelingFolder, "05_Clay_Complete/")
            #self.generateModelingFolder()
            
            self.cgiFolder = os.path.join(self.coreFolder, "03_CGI")
            if not os.path.isdir(self.cgiFolder) and createFolders == True: os.mkdir(self.cgiFolder)
            
            self.retouchingFolder = os.path.join(self.coreFolder, "04_Retouching")
            if not os.path.isdir(self.retouchingFolder) and createFolders == True: os.mkdir(self.retouchingFolder)
            
            self.deliveriesFolder = os.path.join(self.coreFolder, "05_Deliveries")
            if not os.path.isdir(self.deliveriesFolder) and createFolders == True: os.mkdir(self.deliveriesFolder)
            #self.generateDeliveriesFolder()
            
            #Generate the folders if createFolders is on
            if createFolders == True:
                self.makeDefaultDirectories()
                
            #Create the variables for modeling components, clay complete, and the save file data folder
            self.initFolderVariables()
    
    def initFolderVariables(self):
        self.projectDataFolder = os.path.join(self.managementFolder, "01_Project_Overview/_data/")
        self.componentsFolder = os.path.join(self.modelingFolder, "03_Components/")
        self.clayCompleteFolder = os.path.join(self.modelingFolder, "05_Clay_Complete/")
    
    #Check if this project's folder structure has been created or not
    def projectCreated(self):
        try:
            if os.path.isdir(self.coreFolder):
                return True
            return False
        except TypeError as E:
            print(E)
            return False
    
    #Rename part variants in parts, then update the references in the list of cars
    def renamePartVariants(self, indexes, names):
        renamed = self.Parts.renamePartVariants(indexes, names)
        print(str(renamed))
        oldNames = [name for name in renamed[0]]
        newNames = [name for name in renamed[1]]
        print("Unzipped Old Names: %s"%(str(oldNames)))
        print("Unzipped New Names: %s"%(str(newNames)))
        for car in self.Cars:
            car.updateVariantReferences(oldNames, newNames)
        
    
    #Check to see if a modeling folder has already been created for the entered component
    def checkForComponentFolder(self, partName):
        try:
            if os.path.isdir(os.path.join(self.componentsFolder, "%s/"%(partName))):
                return True
            return False
        except TypeError as E:
            print(E)
            return False
    
    #Recursively looks through a component folder and switches all of the old component names to the new component name
    def renameComponentFolder(self, oldName, newName):
        all_component_folders = glob.glob(os.path.join(self.componentsFolder, "*"))
        list_to_rename = []
        for component in all_component_folders:
            if oldName in os.path.split(component)[1]:
                list_to_rename.append(component)
                #A current list of directories that we need to search
                current_dirs = [component,]
                #A list of the next level of search directories we need to search
                next_dirs = []
                #A recursive function that should probe deeper and deeper into a file structure looking for files and directories.  Has the potential to lock up the computer, so thats exciting
                #while (True in [x.isdir() for x in glob.glob(os.path.join(current_dir, "*"))]):
                while (len(current_dirs)>0):
                    print("Begin renaming loop, search dirs: " + str(current_dirs))
                    #next_dirs.clear()
                    for dir in current_dirs:
                        files = glob.glob(os.path.join(dir, "*"))
                        print("Files in current searching dir: " + str(files))
                        if len(files)>0:
                            for file in files:
                                if oldName in file:
                                    list_to_rename.append(file)
                                        
                                if os.path.isdir(file):
                                    next_dirs.append(file)
                            else:
                                print("Next level search dirs should contain %s"%(str(next_dirs)))
                    else:
                        #print("Next dirs: "+str(next_dirs))
                        current_dirs = [x for x in next_dirs]
                        next_dirs.clear()
                        #print("Current dirs: "+str(current_dirs))
                        print("Renaming loop finished, next level dirs: %s.\n"%(current_dirs))
                        
                if len(list_to_rename)>0:
                    for file in reversed(list_to_rename):
                        print("Rename FROM: %s\nRename TO: %s"%(file, file.replace(oldName, newName)))
                        if os.path.exists(file):
                            try:
                                os.renames(file, file.replace(oldName, newName))
                            except FileNotFoundError as E:
                                print("Error Encountered: %s"%(E))
                
    #Add a car to the list
    def addCar(self, name = "default"):
        self.Cars.append(Car(name))
        
    #Remove a car from the list at index
    def removeCar(self, index):
        self.removed_cars.append(self.Cars[index])
        del(self.Cars[index])
    
    #Remove multiple cars through a list of given indexes
    def removeCars(self, indexes):
        for index in sorted(indexes, reverse=True):
            self.removeCar(index)
    
    def carExists(self, index):
        #Check if a car exists by looking for its data folder
        try:
            return self.Cars[index].exists(self.dataFolder)
            #name = self.Cars[index].name
            #if os.path.isdir(os.path.join(self.dataFolder, "%s/"%(name))):
            #    return True
            #return False
        except IndexError:
            return False
    
    def setCarName(self, index, name):
        #Set the name of a car in this project
        self.Cars[index].setName(self.dataFolder, name)
    
    def moveToSelectedParts(self, indexes):
        self.Parts.moveParts(indexes, 0)
    
    def moveToAvailableParts(self, indexes, force = False):
        
        try:
            referenced_parts = self.getPartReferencesInCars(indexes)
            if force==True:
                if len(referenced_parts)>0:
                    [car.removePartReferences([self.Parts.selectedParts[x] for x in referenced_parts]) for car in self.Cars]
                self.Parts.moveParts(indexes, 1)
                return []
            else:
                if len(referenced_parts)==0:
                    self.Parts.moveParts(indexes, 1)
                    return[]
                return referenced_parts
        except Exception as E:
            print(E)
    
    def createPartVariants(self, indexes):
        self.Parts.moveParts(indexes, 2)
    
    def assignVariantToCars(self, variants, indexes):
        indexes = [int(x) for x in indexes]
        
        for index in indexes:
            car = self.Cars[index]
            for variant in variants:
                if variant[1]!="":
                    car.addPartVariant("%s%s%s"%(variant[0], variant_name_delimiter, variant[1]))
    
    def removePartVariants(self, indexes, force = False):
        try:
            referenced_variants = self.getVariantReferencesInCars(indexes)
            if force==True:
                if len(referenced_variants)>0:
                    [car.removeVariantReferences([self.Parts.partVariants[x] for x in referenced_variants]) for car in self.Cars]
                self.Parts.moveParts(indexes, 3)
                return []
            else:
                if len(referenced_variants)==0:
                    self.Parts.moveParts(indexes, 3)
                    return[]
                return referenced_variants
        except Exception as E:
            print(E)
    
    def getVariantReferencesInCars(self, variants):
        #Check if part variants have been referenced by cars
        #Returns a list of variant indexes that have been referenced
        #If return list is empty, none are referenced
        if len(variants)>0:
            return_referenced_variants = []
            for car in self.Cars:
                for variant in variants:
                    if variant in car.getPartVariants("all"):
                        return_referenced_variants.append(variant)
            else:
                return set(return_referenced_variants)
        else:
            return []
    
    def getPartReferencesInCars(self, indexes):
        #Check if base level parts have been referenced by cars
        #Returns a list of part indexes that have been referenced
        #If return list is empty, none are referenced
        if len(indexes)>0:
            all_parts = []
            referenced_parts = []
            for car in self.Cars:
                [all_parts.append(part.split(variant_name_delimiter)[0]) for part in car.getPartVariants("all") if part not in all_parts]
            
            if len(all_parts)>0:
                for index in indexes:
                    if self.Parts.selectedParts[int(index)] in all_parts:
                        referenced_parts.append(int(index))
                else:
                    return set(referenced_parts)
            else:
            #referenced_parts = [part.split(variant_name_delimiter)[0] for part in set([].extend([car.getPartVariants("all") for car in self.Cars]))]
                return []
        else:
            return []
    
    #Generate all data folders for all created cars
    def generateAllDataFolders(self):
        #if len(self.Cars)>0:
        [project_dirs.generateDataFolder(self.dataFolder, car.name) for car in self.Cars if len(self.Cars)>0]
    
    #Generate all retouching folders for all created cars
    def generateAllRetouchingFolders(self):
        [project_dirs.generateRetouchingFolder(self.retouchingFolder, car.name) for car in self.Cars if len(self.Cars)>0]
        
    #Initialize the default directories that don't require car names passed into it
    def makeDefaultDirectories(self):
        project_dirs.generateManagementFolder(self.managementFolder)
        project_dirs.generateModelingFolder(self.modelingFolder)
        project_dirs.generateDeliveriesFolder(self.deliveriesFolder)
    
    #Load a project and all relevant information.  This involves resetting the project info, and as such a warning should be given before doing this
    def loadProject(self, directory):
        open_file = os.path.join(directory, "00_Management/01_Project_Overview/_data/project_data")
        if not os.path.isfile(open_file):
            print("Not found project file")
            return False
        else:
            print("Resetting project")
            self.resetProject()
            f = open(open_file, "r")
            for i in f:
                key, value = i.split(":")
                value = value.replace("\n", "")
                if key=="PN":
                    print("Project name %s"%(value))
                    self.projectName = value
                if key=="CM":
                    print("Car name %s"%(value))
                    self.Cars.append(Car(value))
                if key=="CD":
                    print("Core directory %s"%(value))
                    self.coreFolder = value
                if key=="PL":
                    print("Core directory loc %s"%(value))
                    self.coreFolderLocation = value
            f.close()
            
            #Reinitialize the folder structure variables with the loaded core folder location
            self.initFolderStructure(self.coreFolderLocation, False)
            
            #Now attempt to load the parts
            self.Parts.loadParts(self.projectDataFolder)
            
            #Now attempt to load part variants for the cars
            for car in self.Cars:
                car.loadCar(self.dataFolder)
            
            return True
    
    def exists(self):
        if not self.coreFolderLocation == None and not self.coreFolder == None:
            if os.path.exists(self.coreFolder):
                return True
        return False
    
    #Save the project data to a file
    def saveProject(self):
        if not self.coreFolderLocation == None and not self.coreFolder == None:
            save_file = os.path.join(self.managementFolder, "01_Project_Overview/_data/project_data")
            if not os.path.isdir(os.path.join(self.managementFolder, "01_Project_Overview/_data/")):
                os.makedirs(os.path.join(self.managementFolder, "01_Project_Overview/_data/"))
            save = open(save_file, "w+")
            #Save the project name
            save.write("PN:%s\n"%(self.projectName))
            #Write the root directory
            save.write("CD:%s\n"%(self.coreFolder))
            #Write the project location
            save.write("PL:%s\n"%(self.coreFolderLocation))
            #Delete all car models that have been removed
            for car in self.removed_cars:
                car.removeCar(self.dataFolder)
                
            self.Parts.saveParts(self.projectDataFolder)
            
            #Generate all component files and folders
            self.Parts.generateComponentFiles(self.componentsFolder,self.Parts.selectedParts)
            self.Parts.generateComponentFiles(self.componentsFolder, self.getCarVariants())
            
            #Save all the car models
            for car in self.Cars:
                save.write("CM:%s\n"%(car.name))                    
                car.saveCar(self.dataFolder, self.componentsFolder, self.clayCompleteFolder, self.Parts.selectedParts)
                #car.generatePublishedAsciiFile(self.componentsFolder, self.clayCompleteFolder,"/rendershare/LIBRARY/cg_production/00_resources/production_scripts/Modeling_Pipeline/EmptyMayaFileTemplates/empty.ma",self.Parts.selectedParts)
            
            save.close()            
            return True
        else:
            print("Necessary project variables haven't been defined yet.")
            return False
        
    
    def getCarVariants(self):
        #Return a set of variants referenced by cars for the purposes of generating component folders
        parts=[]
        for car in self.Cars:
            parts.extend(car.getPartVariants())
        return set(parts)
    
    def resetProject(self):
    #After calling this, the folder structure must be reinitialized with self.initFolderStructure
        self.initVars()

    def retrievePublishedFilepaths(self):
        components = [x for x in glob.glob(os.path.join(self.componentsFolder, "*")) if os.path.isdir(x)==True]
        return_files = []
        if len(components)>0:
            for x in components:
                publish_dir = os.path.join(x, "Publish/")
                if os.path.isdir(publish_dir):
                    publish_file = glob.glob(os.path.join(publish_dir, "*.mb"))
                    if len(publish_file)>0:
                        #Return the name of the components as well as the path to the published file
                        return_files.append((x.split("/")[-1],publish_file[0]))
                    else:
                        print("No published maya file found")
                else:
                    print("No publish dir found for component %s at %s"%(x, publish_dir))
        else:
            print("No components found")
        
        return return_files