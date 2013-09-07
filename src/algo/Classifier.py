#encoding=utf-8
#sys.path.append(r"..\data")
#from Sample import Sample
class Classifier(object):
    def __init__(self, *args, **kwargs):
        self.model = None
        pass
#    def SetData(self, train_set, test_set):
#        self.train_set = train_set
#        self.test_set = test_set
    def SetConfig(self, *args, **kwargs):
        pass        
    def Train(self, train_data):
        pass
    def Test(self, data_set):
        sample_number = data_set.GetSize()
        cor_number = 0        
        count = 0
        for sample in data_set.GetSamples():
            print count
            count = count + 1
            gt_label = sample.label
            label = self.Classify(sample)
            if gt_label == label:
                cor_number = cor_number + 1
        print cor_number, sample_number
        print "accuracy: %f" % (cor_number / float(sample_number))
        
    
    def Classify(self, sample):
        pass