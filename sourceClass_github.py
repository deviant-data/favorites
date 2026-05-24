

# This is very old.
# It's simple, and beautiful.
# It should be relevant as long as we have python.
# Some great things have probably been built with a similar ethos.



class Source: 
    
    def __init__(self):
        self.all = {}
        # returns stored sources as dict {key: name, value: source}
        self.changeLog = {}
        # the changeLog tracks updates to sources.
        # It is a dict with boolean values (defaults to False):
            # True: source has been updated
            # False: source has not been updated
        # used in: addSource, removeSource, updateSource, clear, reset

    def addSource(self, source, data):
        try:
            self.all.update({str(source): data})
            setattr(self, str(source), data)
            # new source names are set as attributes which return source content
            self.changeLog.update({str(source): False})
            # new sources are logged in the changeLog and set to False
        except:
            return None
    
    def removeSource(self, source):
        try:
            self.all.pop(str(source))
            delattr(self, str(source))
            self.changeLog.pop(str(source))
        except:
            return None
    # when called:
        # 1. the relevant source is removed from the internal dict containing all sources (self.all)
        # 2. the associated attribute is removed
        # 3. the source's entry is removed from the changeLog

    def updateSource(self, source, data):
        try:
            self.all.update({str(source): data})
            setattr(self, str(source), data)
            self.changeLog.update({str(source): True})
            # updated sources are set to True in the changeLog
        except:
            return None
    
    def clear(self):
        try:
            [delattr(self, i) for i in list(dict(self.all).keys())]
            self.changeLog = {}
            self.all = {}
        except:
            return None
    
    def reset(self):
        self.__init__()        










