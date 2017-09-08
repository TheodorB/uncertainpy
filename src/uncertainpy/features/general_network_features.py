import numpy as np

try:
    import neo.core
    import quantities as pq

    prerequisites = True
except ImportError:
    prerequisites = False


from .general_features import GeneralFeatures


class GeneralNetworkFeatures(GeneralFeatures):
    def __init__(self,
                 new_features=None,
                 features_to_run="all",
                 adaptive=None,
                 labels={},
                 units=pq.ms):

        if not prerequisites:
            raise ImportError("Network features require: neo")

        super(GeneralNetworkFeatures, self).__init__(new_features=new_features,
                                                     features_to_run=features_to_run,
                                                     adaptive=adaptive,
                                                     labels=labels)

        self.units = units

    def preprocess(self, t_stop, spiketrains):
        if t_stop is None or np.isnan(t_stop):
            raise ValueError("t_stop is NaN or None. t_stop must be the time when the simulation ends.")

        neo_spiketrains = []
        for spiketrain in spiketrains:
            neo_spiketrain = neo.core.SpikeTrain(spiketrain, t_stop=t_stop, units=self.units)
            neo_spiketrains.append(neo_spiketrain)

        return None, neo_spiketrains