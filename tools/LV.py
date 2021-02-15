import numpy as np
from itertools import product

class LorentzVector(object):
    def __init__(self,E,*args):
        self.p4 = np.array(E)
        if len(args) == 3:
            self.p4 = np.append(self.p4,args)
        if np.size(self.p4) != 4:
            print('Invalid LV construction')
        self.initialize()
           
    def initialize(self):
        self.metric = np.array([1.,-1.,-1.,-1.])

    ##
    ## basic accessors and methods
    ##

    def E(self):
        return self.p4[0]
    def px(self):
        return self.p4[1]
    def py(self):
        return self.p4[2]
    def pz(self):
        return self.p4[3]
    def vec(self):
        return self.p4[1:]
    def p(self):
        return np.sqrt(np.sum(self.vec()*self.vec()))
    def p2(self):
        return np.sum(self.p4*self.metric*self.p4)
    def m(self):
        ret = np.sum(self.p4*self.metric*self.p4)
        return np.sign(ret)*np.sqrt(np.abs(ret))

    def dot(self,other):
        return np.sum(self.p4*self.metric*other.p4)
    def beta(self):
        if np.abs(self.E()) < 1.e-6:
            if np.abs(self.p()) < 1.e-6:
                return 0.
            print('Cannot compute beta for LorentzVector with t = 0. Returning infinite result.')
            return np.Inf
        elif self.p2() < 0.:
            print('Cannot compute beta for non-timeline LorentzVector.  Returning non-physical result.')
        return self.p()/self.E() 
    def gamma(self):
        beta = self.beta()
        if beta == np.Inf: return 0.
        elif self.p2() < 0. or beta > 1.:
            print('Cannot compute gamma for a spacelike LorentzVector.  Returning imaginary result.') 
            return complex(0.,1./np.sqrt(np.abs(1.-beta*beta)))
        elif abs(beta-1.) < 1.e-6:
            print('Cannot compute gamma for a lightlike LorentzVector.  Returning infinte result.')
            return np.Inf
        return 1./np.sqrt(1.-beta*beta)
    def boostToCM(self):
        ret = np.array([0., 0., 0.])
        if np.amax(np.abs(self.p4)) < 1.e-6: return ret
        elif self.p2() < 0.:
            print('Cannot compute boost to CM for spacelike LorentzVector.')
            return None
        return self.vec()/self.E()
    def boostTo(self, vec):
        b = LorentzVector(np.append(1,vec))
        transform = np.zeros((4,4)) 
        transform[0,] = b.gamma() * (b.p4 * self.metric)
        transform[:,0] = b.gamma() * (b.p4 * self.metric)
        kdelta = lambda i,j: (i==j)*1.  
        for (i,j) in product([1,2,3],repeat=2):
            transform[i][j] = kdelta(i,j) + (b.gamma()-1)*b[i]*b[j]/(b.p()*b.p())
        #print transform
        #return LorentzVector(transform.dot(self.p4))
        return LorentzVector(np.dot(transform,self.p4))
    
    ##
    ## operators
    ##
    def __add__(self,other):
        return LorentzVector(self.p4+other.p4)
    def __sub__(self,other):
        return LorentzVector(self.p4-other.p4)
    def __mul__(self,other):
        if type(self) == type(other):
            return np.sum(self.p4*self.metric*other.p4)
        else:
            self.p4 *= other 
    def __rmul__(self,other):
        return self.__mul__(other)
    def __neg__(self):
        self.p4 *= -1.
    def __eq__(self,other):
        return (np.amax(np.abs(self.p4-other.p4)) < 1.e-6)
    def __getitem__(self,key):
        if key < np.size(self.p4): return self.p4[key]
        else:
            print('Index out of range.  Returning None.')
            return None

    ##
    ## alternate accessors
    ##
    def energy(self):
        return self.E()
    def mass(self):
        return self.m()
    def momentum(self):
        return self.p()

    ##
    ## other methods
    ##
    def get_metric(self):
        return self.metric
    def set_metric(self, metric):
        self.metric = metric
    def invert(self):
        self.p4 = self.p4 * self.metric
    def _rep(self):
        return '(%s, %s, %s, %s)' % (self.p4[0], self.p4[1], self.p4[2], self.p4[3])
    __str__ = _rep
    __repr__ = _rep
        
if __name__ == '__main__':
    a = LorentzVector(np.array([90,0,0,0]))
    b = LorentzVector(np.array([np.sqrt(45**2+0.1**2),45,0,0]))  
    c = LorentzVector(np.array([np.sqrt(45**2+0.1**2),-45,0,0]))  
    print('a: ', a)
    print('b: ', b)
    print('b+c: ', b+c)
    d = LorentzVector(np.array([np.sqrt(90**2+45**2),45,0,0]))
    print('d: ', d)
    print('E,px,py,pz,m: ', d.E(), d.px(), d.py(), d.pz(), d.m())
    print('(b+c).(b+c): ', (b+c).dot(b+c))
    print('d.p(): ', d.p())
    print('E,px,py,pz: ', d[0], d[1], d[2], d[3]) 
    vecs = list([a,b,c,d])
    for vec in vecs:
        print(vec)
    e = LorentzVector([np.sqrt(90**2+45**2+45**2),45,45,0])
    print('e: ', e)
    print('boost to CM: ', e.boostToCM())
    f = e.boostTo(e.boostToCM())
    print('boost e to CM: ', f)
    print('boost f: ', f.boostTo(-1.*e.boostToCM()))
    
