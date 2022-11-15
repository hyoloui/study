class LinkedTuple:
    def __init__(self):
        self.items = list()
        
    # [("ksdfksdf8", "test")] -> [("ksdfksdf", "test33")]
    def add(self, key, value): # .add("ksdfksdf8", "test")
                                # .add("ksdfksdf", "test33")
        # [(("ksdfksdf8", "test"))]
        # [("ksdfksdf8", "test")][("ksdfksdf", "test33")]
        self.items.append((key, value))
        
    def get(self,key):
        # ksdfksdf8
        # [("ksdfksdf8", "test"), ("ksdfksdf", "test33")]
        for k, v in self.items:
            if key == k:
                return v
            
class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())
            
    def put(self, key, value):
        return
    
    def get(self, key, value):
        index = hash(key) % len(self.items)
        # LinkedTuple
        # []
        # [(key, value)]
        return self.items[index].get(key)
        
    