from TSCConfimentBarsRules import ConfimentDesign
import pytest
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


def test_Ac(MyConf):
    
    assert MyConf.GetAc(Height=30, Width=50) == 1500
    assert MyConf.GetAc(Height=40, Width=40) == 1600

def test_Ack(MyConf):
    assert MyConf.GetAck(Height=H, Width=B, Cover=ClearCoverConc) == 122500
    assert MyConf.GetAck(10,10,3) == 16