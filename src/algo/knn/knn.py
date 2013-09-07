# -*- coding: utf-8 -*-
import sys
sys.path.append(r"..\..")
from algo.Classifier import Classifier

class KNNClassifier(Classifier):
    def __init__(self, *args, **kwargs):
        self.K = 1
        pass
    def SetConfig(self, *args, **kwargs):
        if "K" in kwargs:
            self.K = int(kwargs["K"])
    def Train(self, train_dataset):
        self.train_dataset = train_dataset
        #no training in KNN
        pass
    
    def Classify(self, test_sample):
        distances = []
        for sample in self.train_dataset.GetSamples():
            distances.append((sample.Distance(test_sample), sample.label))
        label_map = {}
        for dis, label in sorted(distances)[0:self.K]:
            label_map[label] = label_map.get(label, 0) + 1
        predicted = sorted(label_map.items(),key = lambda x: -x[1])[0][0]
        return predicted