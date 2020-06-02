import numpy as np

from echochamber.esn import ESN

N_in, N, N_out = 5, 75, 3


def random_task():
    X = np.random.randn(100, N_in)
    y = np.random.randn(100, N_out)
    Xp = np.random.randn(50, N_in)
    return X, y, Xp

def assertTrue(a):
    assert a

def assertFalse(a):
    assert not(a)

def _compare( esnA, esnB, should_be):
    """helper function to see if two esns are the same"""
    X, y, Xp = random_task()
    test = assertTrue if should_be == "same" else assertFalse
    test(np.all(np.equal(esnA.W, esnB.W)))
    test(np.all(np.equal(esnA.W_in, esnB.W_in)))
    test(np.all(np.equal(esnA.W_feedb, esnB.W_feedb)))
    test(np.all(np.equal(esnA.fit(X, y), esnB.fit(X, y))))
    test(np.all(np.equal(esnA.W_out, esnB.W_out)))
    test(np.all(np.equal(esnA.predict(Xp), esnB.predict(Xp))))

def test_integer():
    """two esns with the same seed should be the same"""
    esnA = ESN(N_in, N_out, random_state=1)
    esnB = ESN(N_in, N_out, random_state=1)
    _compare(esnA, esnB, should_be="same")

def test_randomstate_object():
    """two esns with the same randomstate objects should be the same"""
    rstA = np.random.RandomState(1)
    esnA = ESN(N_in, N_out, random_state=rstA)
    rstB = np.random.RandomState(1)
    esnB = ESN(N_in, N_out, random_state=rstB)
    _compare(esnA, esnB, should_be="same")

def test_none():
    """two esns with no specified seed should be different"""
    esnA = ESN(N_in, N_out, random_state=None)
    esnB = ESN(N_in, N_out, random_state=None)
    _compare(esnA, esnB, should_be="different")





def test_inputscaling():
    """input scaling factors of different formats should be correctly intereted or rejected"""
    X, y, Xp = random_task()

    esn = ESN(N_in, N_out, input_scaling=2)
    assert(np.all(2 * X == esn._scale_inputs(X)))
    esn.fit(X, y)
    esn.predict(Xp)

    esn = ESN(N_in, N_out, input_scaling=[2] * N_in)
    assert(np.all(2 * X == esn._scale_inputs(X)))
    esn.fit(X, y)
    esn.predict(Xp)

    esn = ESN(N_in, N_out, input_scaling=np.array([2] * N_in))
    assert(np.all(2 * X == esn._scale_inputs(X)))
    esn.fit(X, y)
    esn.predict(Xp)



def test_inputshift():
    """input shift factors of different formats should be correctly interpreted or rejected"""
    X, y, Xp = random_task()
    esn = ESN(N_in, N_out, input_shift=1)
    assert(np.all(1 + X == esn._scale_inputs(X)))
    esn.fit(X, y)
    esn.predict(Xp)

    esn = ESN(N_in, N_out, input_shift=[1] * N_in)
    assert(np.all(1 + X == esn._scale_inputs(X)))
    esn.fit(X, y)
    esn.predict(Xp)

    esn = ESN(N_in, N_out, input_shift=np.array([1] * N_in))
    assert(np.all(1 + X == esn._scale_inputs(X)))
    esn.fit(X, y)
    esn.predict(Xp)


def test_IODimensions():
    """try different combinations of input & output dimensionalities & teacher forcing"""
    tasks = [(1, 1, 100, True), (10, 1, 100, True), (1, 10, 100, True), (10, 10, 100, True),
             (1, 1, 100, False), (10, 1, 100, False), (1, 10, 100, False), (10, 10, 100, False)]
    for t in tasks:
        N_in, N_out, N_samples, tf = t
        X = np.random.randn(
            N_samples, N_in) if N_in > 1 else np.random.randn(N_samples)
        y = np.random.randn(
            N_samples, N_out) if N_out > 1 else np.random.randn(N_samples)
        Xp = np.random.randn(
            N_samples, N_in) if N_in > 1 else np.random.randn(N_samples)
        esn = ESN(N_in, N_out, teacher_forcing=tf)
        prediction_tr = esn.fit(X, y)
        prediction_t = esn.predict(Xp)
        assert (prediction_tr.shape[0]== N_samples)
        assert (prediction_t.shape[0]==N_samples)

