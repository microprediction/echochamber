from echochamber.train import example_lagged_values

def test_lagged_values():
    lv = example_lagged_values()
    assert len(lv)>500