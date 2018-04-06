import davaleba3.Neironi as np


class SruladBmuliQseli:
    def __init__(self, list_neiron):
        self.list_neurons = list_neiron

    def shedegi(self, x):
        for i in self.list_neurons[0]:
            np.Neironi.datvale_y(i, x[self.list_neurons[0].index(i)])

        for layer in self.list_neurons:
            if self.list_neurons.index(layer) == 0:
                continue
            for neiron in self.list_neurons[self.list_neurons.index(layer) - 1]:
                prev_y = list()
                prev_y.append(neiron.y)
            for neiron in layer:
                neiron.datvale_y(prev_y)

        shedegi = list()
        for neiron in self.list_neurons[len(self.list_neurons) - 1]:
            shedegi.append(neiron.y)

        return shedegi
