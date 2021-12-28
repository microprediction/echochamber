
from microprediction import MicroReader

def test_imports():
    mr = MicroReader()
    values = mr.get_lagged_values(name='three_body_x.json')
    assert len(values)>500

