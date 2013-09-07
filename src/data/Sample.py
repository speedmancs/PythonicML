#encoding=utf-8
import numpy as np
class Sample(object):
    def __init__(self, feature, label):
        self.label = label
        self.feature = feature
    def GetLabel(self):
        return self.label
    def GetFeature(self):
        return self.feature
    def Distance(self, sample):
        return np.linalg.norm(self.feature.data - sample.feature.data)
