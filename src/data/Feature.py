#encoding=utf-8
import numpy as np
class Feature(object):
    def __init__(self, data):
        self.data = data
    def GetData(self):
        return self.data