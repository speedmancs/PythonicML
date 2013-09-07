#encoding=utf-8
import os
import numpy as np
from DataSet import DataSet
from Sample import Sample
from Feature import Feature
class DigitDataSet(DataSet):
    def __init__(self, *args, **kwargs):
        super(DigitDataSet, self).__init__(*args, **kwargs)
        
    def LoadFromFile(self, src_path):
        pass
    
    def LoadFromFolder(self, src_path):
        self.samples = []
        for root, dirs, files in os.walk(src_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    label = int(file_name.split("_")[0])
                except Exception:
                    raise Exception("input format error!")
                feature = self.LoadDigitData(file_path)
                self.samples.append(Sample(feature, label))
        
                
                
    def LoadDigitData(self, file_path):
        feature = []
        for line in open(file_path):
            line = line.strip()
            line_feature = [ord(ch) - ord('0') for ch in line]
            feature.extend(line_feature)
        self.dim = len(feature)
        return Feature(np.array(feature))

