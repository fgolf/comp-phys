class Coordinate:
    "A simple class to store and manipulate coordinates in two dimension."
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
    def __str__(self):
        return '({:.2f},{:.2f})'.format(self.x,self.y)
    def __repr__(self):
        return 'Coordinate({:.2f},{:.2f{)'.format(self.x,self.y)
    def __add__(self,other):
        return Coordinate(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Coordinate(self.x-other.x,self.y-other.y)
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def invert(self,axis):
        if 'x' in axis or 'X' in axis: self.x *= -1
        if 'y' in axis or 'Y' in axis: self.y *= -1
    def invertX(self):
        self.invert('x')
    def invertY(self):
        self.invert('y')
    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)
    def __iter__(self):
        yield self.x
        yield self.y
    
class Measurement:
    "A simple class to store a measurement: a label and (x,y) coordinates"
    def __init__(self,label,coordinate):
        self.label = label
        self.coord = coordinate
    @classmethod
    def fromXY(self,label,x,y):
        return Measurement(label,Coordinate(x,y))
    def __str__(self,):
        return '{}: {}'.format(self.label,self.coord)
    def __repr__(self):
        return 'Measurement: {}, {}'.format(self.label,self.coord)
    def __add__(self,other):
        return Measurement(self.label,self.coord+other.coord)
    def __sub__(self,other):
        return Measurement(self.label,self.coord-other.coord)
    def __eq__(self,other):
        return self.label == other.label and self.coord == other.coord
    def x(self):
        return self.coord.x
    def y(self):
        return self.coord.y
    def invert(self,axis):
        self.coord.invert(axis)
    def invertX(self):
        self.invert('x')
    def invertY(self):
        self.invert('y')
    def __iter__(self):
        yield self.label
        yield self.coord
    
class Board:
    "A simple class for storing measurements from a TFPX rev2 module mockup"
    def __init__(self,label, list_of_measurements = []):
        self.label = label
        self.measurements = {m.label:m.coord for m in list_of_measurements}
    def __str__(self):
        return '{}: {}'.format(self.label,self.measurements.keys())
    def __repr__(self):
        return 'Measurement: {}, {}'.format(self.label,self.measurements.keys())
    def addMeasurement(self,measurement):
        self.measurements[measurement.label] = measurement.coord
    def addMeasurementFromCoordinate(self,label,coordinate):
        self.measurements[label] = coordinate
    def addMeasurementFromXY(self,label,x,y):
        self.measurements[label] = Coordinate(x,y)
    def removeMeasurement(self,label):
        del self.measurements[label]
    def shiftMeasurements(self,coord):
        for key in self.measurements.keys(): self.measurements[key] -= coord
    def shiftMeasurementsFromXY(self,x,y):
        self.shiftMeasurements(Coordinate(x,y))
    def getMeasurements(self):
        return [Measurement(key,val) for key,val in self.measurements.items()]
    def getMeasurement(self,label):
        return Measurement(label,self.measurements[label])
    def invertMeasurement(self,label,axis):
        self.measurements[labl].invert(axis)
    def invertMeasurements(self,axis):
        for key in self.measurements.keys(): self.measurements[key].invert(axis)
    def __getitem__(self,key):
        return self.measurements[key]
