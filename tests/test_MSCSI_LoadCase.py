import pytest
from TSC.MSCSI.Connector import ConnectionEtabs
from TSC.MSCSI.Model import SapModel
from TSC.MSCSI.LoadCases import LoadCase
ModelPath="C:\\CSi_ETABS_API_Example\\ETABS_API_Example.EDB"

@pytest.fixture(scope="class")
def MySapModel():
    MySapModel,myETABSObject  = ConnectionEtabs(ModelPath)
    return MySapModel

@pytest.fixture(scope="class")
def MyEtabs():
    etabs                   = SapModel(RefApi=MySapModel)
    if etabs.GetModelIsLocked():
        etabs.SetModelIsLocked(Lockit=False)
    return etabs

@pytest.fixture(scope="class")
def MyLoadCase():
    loadCase        = LoadCase(RefApi=MySapModel)
    return loadCase

def test_ModalRitz_SetCase(MyLoadCase):
    assert MyLoadCase.ModalRitz.SetCase(MyLoadCase.RefApi.ModalRitz,Name="Ritz1") == None