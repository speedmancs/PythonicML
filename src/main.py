#encoding=utf-8
import numpy as np
#import algo.knn.knn
from data.DataSet import DataSet
from data.DigitDataSet import DigitDataSet

dataset = DataSet(file_path = "gaofeng_file")
dataset2 = DataSet(folder_path = "gaofeng_folder")

digit_dataset = DigitDataSet(
                file_path="gaofeng_file")
digit_dataset2 = DigitDataSet(folder_path = "gaofeng_folder")



    