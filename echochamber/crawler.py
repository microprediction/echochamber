from microprediction.crawler import MicroCrawler
from microprediction.samplers import differenced_bootstrap
from microprediction.samplers import approx_mode
from echochamber.esn import ESN
import numpy as np

# Example of adapting a time series method to make a crawler. Not much to this.

class EchoCrawler(MicroCrawler):

    def __init__(self, write_key, **esn_params):
        """
        :param write_key:        str
        :param esn_params:       parameters passed to ECN as below

        -- ESN_PARAMS --
        n_reservoir: nr of reservoir neurons
        spectral_radius: spectral radius of the recurrent weight matrix
        sparsity: proportion of recurrent weights set to zero
        noise: noise added to each neuron (regularization)
        input_shift: scalar or vector of length n_inputs to add to each
                    input dimension before feeding it to the network.
        input_scaling: scalar or vector of length n_inputs to multiply
                    with each input dimension before feeding it to the netw.
        teacher_forcing: if True, feed the target back into output units
        teacher_scaling: factor applied to the target signal
        teacher_shift: additive term applied to the target signal
        out_activation: output activation function (applied to the readout)
        inverse_out_activation: inverse of the output activation function
        random_state: positive integer seed, np.rand.RandomState object,
                      or None to use numpy's builting RandomState.
        silent: suppress messages

        """
        super().__init__(write_key=write_key)
        self.ecn_params = esn_params or dict()
        print("Let's do this ...",flush=True )

    def candidate_streams(self):
        return ['three_body_x.json','three_body_y.json','three_body_z.json']

    def sample(self, lagged_values, lagged_times=None, name=None, delay=None):
        """ Fit an echo-state machine to predict the mean, then use standard scattering for sampling """
        dt = approx_mode(np.diff(lagged_times))
        try:
            k  = max(1,int( delay/(0.01+dt) ))
        except:
            k = 1
        num_lagged = len(lagged_values)
        inputs = np.ones(num_lagged)          # Exogenous inputs
        outputs = np.array(list(reversed(lagged_values)))
        esn = ESN(n_inputs=1,n_outputs=1,**self.ecn_params)
        esn.fit(inputs=inputs, outputs=outputs)
        future = [ v[0] for v in esn.predict(np.ones(k)) ]
        center = future[-1]
        offset = center-lagged_values[0]
        scenarios = differenced_bootstrap(lagged=lagged_values,  decay=0.01, num=self.num_predictions)
        samples = [ offset+s for s in scenarios ]
        return samples




