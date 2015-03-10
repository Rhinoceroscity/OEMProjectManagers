import os, shutil

def generateDeliveriesFolder(deliveriesFolder, verbose = False):
    try: os.makedirs(os.path.join(deliveriesFolder, "product/"))
    except FileExistsError as E:
        if verbose == True: print(E)

def generateManagementFolder(managementFolder, verbose = False):
    try: os.makedirs(os.path.join(managementFolder, "01_Project_Overview/_data/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    try: os.makedirs(os.path.join(managementFolder, "02_Approvals/Round1/Production_Retouching/01_Client_Review/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "02_Approvals/Round1/Production_Retouching/02_Client_Feedback/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "02_Approvals/Round1/Production_Modeling&Post/01_Client_Review/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "02_Approvals/Round1/Production_Modeling&Post/02_Client_Feedback/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "02_Approvals/Round2/Production_Retouching/01_Client_Review/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "02_Approvals/Round2/Production_Retouching/02_Client_Feedback/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    try: os.makedirs(os.path.join(managementFolder, "02_Approvals/Round2/Production_Modeling&Post/01_Client_Review/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "02_Approvals/Round2/Production_Modeling&Post/02_Client_Feedback/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "02_Approvals/Round3/Production_Retouching/01_Client_Review/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "02_Approvals/Round3/Production_Retouching/02_Client_Feedback/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "02_Approvals/Round3/Production_Modeling&Post/01_Client_Review/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "02_Approvals/Round3/Production_Modeling&Post/02_Client_Feedback/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    try: os.makedirs(os.path.join(managementFolder, "03_Final_Deliverables/CG_Assets/Exterior_Stills/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "03_Final_Deliverables/CG_Assets/Fly_Arounds/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "03_Final_Deliverables/Photography_Assets/Exterior_Stills/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "03_Final_Deliverables/Photography_Assets/Fly_Arounds/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "03_Final_Deliverables/Photography_Assets/Panoramas_VR/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(managementFolder, "03_Final_Deliverables/Photography_Assets/Panoramas_Standard/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    try: os.makedirs(os.path.join(managementFolder, "04_Project_Recap/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    
def removeDataFolder(dataFolder, carName = "default"):
    if os.path.isdir(os.path.join(dataFolder, "%s/"%(carName))):
        shutil.rmtree(os.path.join(dataFolder, "%s/"%(carName)), True)

def generateDataFolder(dataFolder, carName = "default"):
    if not os.path.isdir(os.path.join(dataFolder, "%s"%(carName))):
        os.makedirs(os.path.join(dataFolder, "%s/01_Vehicle_Data/"%(carName)))

        os.makedirs(os.path.join(dataFolder, "%s/02_Reference_Shots/Detail_shots/"%(carName)))
        os.makedirs(os.path.join(dataFolder, "%s/02_Reference_Shots/orthos_shots/"%(carName)))
        
        os.makedirs(os.path.join(dataFolder, "%s/03_Client_Data/"%(carName)))

def generateModelingFolder(modelingFolder, verbose = False):
    try: os.makedirs(os.path.join(modelingFolder, "00_Project/data/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "00_Project/Vehicle/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    try: os.makedirs(os.path.join(modelingFolder, "01_Images/00_Orthos/Front/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "01_Images/00_Orthos/Front_34/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "01_Images/00_Orthos/Profile/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "01_Images/00_Orthos/Rear/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "01_Images/00_Orthos/Rear_34/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "01_Images/01_References/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "01_Images/Videos/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    try: os.makedirs(os.path.join(modelingFolder, "02_Scenes/00_Camera_Match/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "02_Scenes/01_Orthos_Scene/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    try: os.makedirs(os.path.join(modelingFolder, "03_Components/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "05_Clay_Complete/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    #componentsFolder = os.path.join(modelingFolder, "03_Components/")
    #clayCompleteFolder = os.path.join(modelingFolder, "05_Clay_Complete/")
    
    try: os.makedirs(os.path.join(modelingFolder, "04_Renders/_logs/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "04_Renders/maya/anim/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "04_Renders/maya/renders/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "04_Renders/maya/renderScenes/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "04_Renders/nuke/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(modelingFolder, "04_Renders/output/"))
    except FileExistsError as E:
        if verbose==True: print(E)

def generateCGIFolder(cgiFolder, cgl = "#####", verbose = False):
    try: os.makedirs(os.path.join(cgiFolder, "_dailies/date_time/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    try: os.makedirs(os.path.join(cgiFolder, "assets/_logs/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "assets/modl/CGL%s/modl/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "assets/modl/CGL%s/textures/_wrk/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "assets/ref/CGL%s"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "assets/rig/CGL%s/_wrk/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "assets/rig/CGL%s/textures/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    try: os.makedirs(os.path.join(cgiFolder, "fly/anim/CGL%s/_wrk/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "fly/cmp/CGL%s/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "fly/lgt/CGL%s/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "fly/lgt/lgtRig/_wrk/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "fly/renders/cmp/CGL%s/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "fly/renders/lgt/CGL%s/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "fly/renders/lgt/lgtRig/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "fly/textures/gobos/_wrk/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "fly/textures/HDR/_wrk/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "fly/textures/lgts/_wrk/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "fly/textures/plates/_wrk/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    try: os.makedirs(os.path.join(cgiFolder, "hStills/anim/CGL%s/_wrk/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "hStills/cmp/CGL%s/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "hStills/lgt/CGL%s/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "hStills/lgt/lgtRig/_wrk/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "hStills/renders/cmp/CGL%s/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "hStills/renders/lgt/CGL%s/"%(cgl)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "hStills/renders/lgt/lgtRig/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "hStills/textures/gobos/_wrk/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "hStills/textures/HDR/_wrk/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "hStills/textures/lgts/_wrk/"))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(cgiFolder, "hStills/textures/plates/_wrk/"))
    except FileExistsError as E:
        if verbose==True: print(E)

def generateRetouchingFolder(retouchingFolder, carName = "default", verbose = False):
    try: os.makedirs(os.path.join(retouchingFolder, "%s/01_CG_Stills/01_Use_This/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/01_CG_Stills/02_For_QA/V001/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/01_CG_Stills/02_For_QA/V002/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/01_CG_Stills/02_For_QA/V003/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/01_CG_Stills/03_Final_PSD/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/01_CG_Stills/04_Out/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    try: os.makedirs(os.path.join(retouchingFolder, "%s/02_Photo_Interior_Panos/00_Camera_Source_Files/Raw Images/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/02_Photo_Interior_Panos/00_Camera_Source_Files/Testmoviefiles/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/02_Photo_Interior_Panos/01_Use_This/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/02_Photo_Interior_Panos/02_For_QA/V001/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/02_Photo_Interior_Panos/02_For_QA/V002/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/02_Photo_Interior_Panos/02_For_QA/V003/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/02_Photo_Interior_Panos/03_Final_PSD/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/02_Photo_Interior_Panos/04_Out/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/00_Camera_Source_Files/Raw Images/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/01_Use_This/CenterStack/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/01_Use_This/DriverSeat/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/01_Use_This/HighDriver/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/01_Use_This/Highpass/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/01_Use_This/IP/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/01_Use_This/PushButton/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/01_Use_This/Radio/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/01_Use_This/RearSeat/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/01_Use_This/Shifter/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/01_Use_This/SteeringControls/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/01_Use_This/StraightSteering/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/01_Use_This/WideDash/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/02_For_QA/V001/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/02_For_QA/V002/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/02_For_QA/V003/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/03_Final_PSD/V001/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/03_Final_PSD/V002/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/03_Final_PSD/V003/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/04_Out/V001/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/04_Out/V002/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/03_Photo_Interior_Stills/04_Out/V003/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/00_Camera_Source_Files/Raw Images/CenterStack/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/00_Camera_Source_Files/Raw Images/DriverSeat/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/00_Camera_Source_Files/Raw Images/HighDriver/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/00_Camera_Source_Files/Raw Images/Highpass/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/00_Camera_Source_Files/Raw Images/IP/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/00_Camera_Source_Files/Raw Images/PushButton/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/00_Camera_Source_Files/Raw Images/Radio/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/00_Camera_Source_Files/Raw Images/RearSeat/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/00_Camera_Source_Files/Raw Images/Shifter/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/00_Camera_Source_Files/Raw Images/SteeringControls/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/00_Camera_Source_Files/Raw Images/StraightSteering/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/00_Camera_Source_Files/Raw Images/WideDash/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/01_Use_This/CenterStack/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/01_Use_This/DriverSeat/"%(carName))) 
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/01_Use_This/HighDriver/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/01_Use_This/Highpass/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/01_Use_This/IP/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/01_Use_This/PushButton/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/01_Use_This/Radio/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/01_Use_This/RearSeat/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/01_Use_This/Shifter/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/01_Use_This/SteeringControls/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/01_Use_This/StraightSteering/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/01_Use_This/WideDash/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/02_For_QA/V001/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/02_For_QA/V002/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/02_For_QA/V003/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/03_Final_PSD/V001/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/03_Final_PSD/V002/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/03_Final_PSD/V003/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/04_Out/V001/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/04_Out/V002/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)
    try: os.makedirs(os.path.join(retouchingFolder, "%s/04_Photo_Exterior_Stills/04_Out/V003/"%(carName)))
    except FileExistsError as E:
        if verbose==True: print(E)