#encoding=utf-8
class DataSet(object):
    def __init__(self, *args, **kwargs):
        self.samples = []
        self.dim = None
        self.Load(*args, **kwargs)
        
    def Load(self, *args, **kwargs):
        if "file_path" in kwargs.keys():
            self.LoadFromFile(kwargs["file_path"])
            return
        if "folder_path" in kwargs.keys():
            self.LoadFromFolder(kwargs["folder_path"])
            return
    def GetSamples(self):
        for sample in self.samples:
            yield sample
    def LoadFromFile(self, src_path):
        print "DataSet LoadFromFile from %s" % (src_path)
    def LoadFromFolder(self, src_path):
        print "DataSet LoadFromFolder from %s" % (src_path)
    def GetDim(self):
        return self.dim
    def GetSize(self):
        return len(self.samples)

