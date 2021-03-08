# Optional Parameters Tutorial #1

class car(object):

     # Initial conditions are NEW and with 0 Kms

    def __init__ (self, maker, model, year, condition="New", kms=0):
        self.maker = maker
        self.model = model
        self.year = year 
        self.condition = condition
        self.kms = kms
    
    def display(self, showAll = True):

        if showAll:
            print("\nThis is a %s %s from %s, it is %s and has %s kms" %(self.maker, self.model, self.year, self.condition, self.kms))
        else:
            print("\nThis is a %s %s from %s" %(self.maker, self.model, self.year))

whip = car('Ford','F150', 2015)
whip.display(False)