import comtypes.client
import os
import sys

from TSC.MSCSI.ErrorHandler import ApiReturnError

def ConnectionEtabs(ModelPath : str = None):

    #set the following flag to True to attach to an existing instance of the program
    #otherwise a new instance of the program will be started
    AttachToInstance = True

    #set the following flag to True to manually specify the path to ETABS.exe
    #this allows for a connection to a version of ETABS other than the latest installation
    #otherwise the latest installed version of ETABS will be launched
    SpecifyPath = True

    #if the above flag is set to True, specify the path to ETABS below
    path="C:\\Program Files\\Computers and Structures"
    liste = os.listdir(path)
    Versions = []
    for prog in liste:
        programName = prog.split(" ")[0]
        progVersionNo =  int(prog.split(" ")[1])
        if programName == "ETABS":
            Versions.append(progVersionNo)

    EtabsPath = "".join(f'C:\\Program Files\\Computers and Structures\\Etabs {max(Versions)}\\ETABS.exe')
    # EtabsPath = "C:\\Program Files\\Computers and Structures\\ETABS 21\\ETABS.exe"

    #create API helper object
    helper = comtypes.client.CreateObject('ETABSv1.Helper')
    helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)

    if AttachToInstance:
        #attach to a running instance of ETABS
        try:
            #get the active ETABS object
            myETABSObject = helper.GetObject("CSI.ETABS.API.ETABSObject") 
            if myETABSObject is None:
                AttachToInstance = False
        except (OSError, comtypes.COMError):
            print("No running instance of the program found or failed to attach.")
            sys.exit(-1)

    if AttachToInstance != True:
        if SpecifyPath:
            try:
                #'create an instance of the ETABS object from the specified path
                myETABSObject = helper.CreateObject(EtabsPath)
                if myETABSObject is None:
                    SpecifyPath = False
            except (OSError, comtypes.COMError):
                print("Cannot start a new instance of the program from " + EtabsPath)
                sys.exit(-1)
        if SpecifyPath != True:
            try: 
                #create an instance of the ETABS object from the latest installed ETABS
                myETABSObject = helper.CreateObjectProgID("CSI.ETABS.API.ETABSObject") 
            except (OSError, comtypes.COMError):
                print("Cannot start a new instance of the program.")
                sys.exit(-1)

        #start ETABS application
        myETABSObject.ApplicationStart()

    #create SapModel object
    SapModel = myETABSObject.SapModel

    if ModelPath != None:
        ret = SapModel.InitializeNewModel()
        if ret != 0:
            raise ApiReturnError(ret)
        
        ret = SapModel.File.OpenFile(ModelPath)
        if ret != 0:
            raise ApiReturnError(ret)
    return SapModel,myETABSObject

# if __name__ == "__main__":
#     MySapModel,myETABSObject  = ConnectionEtabs()