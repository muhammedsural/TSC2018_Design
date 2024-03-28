import pytest
import math
from TSC.Design.ConfimentBarsRules import ConfimentDesign

"""Units N,mm"""
Nd                      = 16000 
B                       = 400
H                       = 400
s                       = 80
TieRebarDiameter        = 8
LongnitRebarDiameter    = 14
ClearCoverConc          = 25
NumBarsTop              = 2
NumBarsInterior         = 1
NumBarsBot              = 2
X_tiebars               = 2
Y_tiebars               = 3
fsy                     = 220
fywe                    = 220
eps_su                  = 0.08
f_co                    = 25
f_ce                    = 25
Fctd                    = 10
Ln                      = 2600

@pytest.fixture(scope="class")
def MyConf():
    
    return ConfimentDesign(Nd,fsy,Fctd,Ln,B,H,ClearCoverConc,X_tiebars,Y_tiebars,f_co,fywe,TieRebarDiameter,LongnitRebarDiameter)

# def test_invalid_input_raises_error():
#     # Geçersiz girdi durumunu test edin (örneğin, negatif değerler)
#     with pytest.raises(ValueError):
#         invalid_confiment_design = ConfimentDesign(
#             Nd=-50,
#             Fsy=400,
#             Fctd=30,
#             Ln=500,
#             Width=300,
#             Height=800,
#             Cover=40,
#             Xkol=4,
#             Ykol=4,
#             Fck=25,
#             Fywk=500,
#             ConfimentRebarDiameter=16,
#             LongnitudeRebarDiameter=12,
#         )

def test_Ac(MyConf):
    assert math.isclose(MyConf.GetAc(Height=30, Width=50), 1500, rel_tol=1e-2)
    assert MyConf.GetAc(Height=40, Width=40) == 1600

def test_Ack(MyConf):
    assert MyConf.GetAck(Height=H, Width=B, Cover=ClearCoverConc) == 122500
    assert MyConf.GetAck(10,10,3) == 16

def test_Bk(MyConf):
    assert MyConf.Get_bk(Dimension=300,Cover=30) == 240

def test_Ai(MyConf):
    assert MyConf.Get_a_i(bk = 240, koladet=3) == 80

# def test_invalid_input_raises_error():
# #     # Geçersiz girdi durumunu test edin (örneğin, negatif değerler)
#     with pytest.raises(ValueError):
#         assert MyConf.Get_a_i(bk = -240, koladet=3)

def test_Ash(MyConf):
    pass

def test_EndLength(MyConf):
    pass
