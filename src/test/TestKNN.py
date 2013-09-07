# -*- coding: utf-8 -*-
import sys
sys.path.append(r"..")

from data.DigitDataSet import DigitDataSet
from algo.knn.knn import KNNClassifier
path = r"../../data/digits/trainingDigits"
train_dataset = DigitDataSet(folder_path=path)

path = r"../../data/digits/testDigits"
test_dataset = DigitDataSet(folder_path=path)

classifier = KNNClassifier()
classifier.SetConfig(K = 7)
classifier.Train(train_dataset)
classifier.Test(train_dataset)
classifier.Test(test_dataset)
