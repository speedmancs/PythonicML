#encoding=utf-8
class Classifier(object):
    def __init__(self, *args, **kwargs):
        self.model = None
        pass
    def SetConfig(self, *args, **kwargs):
        pass        
    def Train(self, train_data):
        pass
    def Test(self, data_set):
        sample_number = data_set.GetSize()
        cor_number = 0        
        for sample in data_set.GetSamples():
            gt_label = sample.label
            label = self.Classify(sample)
            if gt_label == label:
                cor_number = cor_number + 1
        print "accuracy: %f" % (cor_number / float(sample_number))
        
    
    def Classify(self, sample):
        pass