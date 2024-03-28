


import pytest

from TSC.Design.Frp import FRPMaterial


@pytest.fixture(scope="class")
def LP():
    
    return FRPMaterial("aaa",252000,.35,0.01)

def test_invalid_input_raises_error():
    # Geçersiz girdi durumunu test edin (örneğin, negatif değerler)
    with pytest.raises((TypeError,ValueError)):
        invalid_confiment_design = FRPMaterial(
            Name="aaa",
            Ef=None,
            tf=5,
            eps_fu=0.5,
            eps_f=0.01
        )