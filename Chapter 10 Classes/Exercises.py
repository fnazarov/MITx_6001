class Int_set(object):
    '''
    Same Set Implementation as Python Set
    '''
    def __init__(self):
        self.u = None
        self._vals=[]
    def insert(self,e):
        if e not in self._vals:
            self._vals.append(e)
    def member(self,e):
        return e in self._vals
    def remove(self,e):
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e), ' is not in self')
    def get_member(self):
        return self._vals[:]

    def union(self, other):
        u=other()
        for i in other:
            if i not in self._vals:
                u+=i
        return u
    def add(self,new_elems):
        '''new_elems is a list'''
        self._vals+=new_elems
    def __add__(self,other):
        new_set=Int_set()
        new_set._vals = self._vals + other._vals
        return new_set
    def __hash__(self):
        return id(self)
    def __str__(self):
        if self._vals==[]:
            return {}
        self._vals.sort()
        result=''
        for e in self._vals:
            result=result+str(e)+','
        return f'{{{result[:-1]}}}'