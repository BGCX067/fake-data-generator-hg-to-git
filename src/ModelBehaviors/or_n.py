
"""
Created on Feb 27, 2012

@author: trobinso

Plugin IModelBehavior that implements the or operator.

"""

from fakeDataGenerator.model import IModelBehavior
import math

class OrValues(IModelBehavior):
    arity=(2,None)
    isNoise = False
    def calculate(self, *values):
        if True in [math.isnan(value) or math.isinf(value) for value in values]:
            return float('nan')
        ret = int(values[0]*131072.0) #power of 2 rounds ints cleanly
        for s in values[1:]:
            ret |= int(s*131072.0)
        return ret/131072.0
    def generate_name(self, *names):
        return 'OR({0})'.format(", ".join(names))

