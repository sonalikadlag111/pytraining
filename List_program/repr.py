class build1:
    def _init_(self,bed):
        self.bed=bed
        # self.hall=hall
        # self.bath=bath
    def __repr__(self):
        return repr('a'+self.bed)
        # return repr('a'+self.hall)
        # return repr('a'+self.bath)
ddd=build1('ddd')
repr(ddd)

