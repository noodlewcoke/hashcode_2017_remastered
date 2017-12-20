import numpy as np

class cem:
    def __init__(self, initus, exitus, top):
        self.initus = initus
        self.exitus = exitus
        self.top = top
        self.mean = np.zeros((initus, exitus))
        self.std = np.ones((initus, exitus))
        self.generation = None

    def generate(self, population):
        self.generation = np.random.normal(self.mean, self.std, size=(population, self.initus, self.exitus))
        if np.random.random()>0.5:
            self.generation += np.random.normal(0.0, 1.0, size=(population, self.initus, self.exitus))
        return self.generation

    def evolution(self, scores):
        index = np.argsort(-scores)[:self.top]
        self.mean = np.mean(self.generation[index], axis=0)
        self.std = np.std(self.generation[index], axis=0)

    def run(self):
        return self.mean

    def save(self, filename):
        np.save(filename, np.array([self.mean, self.std]))

    def load(self, filename):
        self.mean, self.std = np.load(filename)