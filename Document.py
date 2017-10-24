'''
Created on Oct 15, 2017
@author: jiajieyan
'''
# A class representing the instance characteristics for the MaxEnt model.

class Document():
    
    def __init__(self, data, label):
        self.label = label
        self.features = self.process_feature(data)
        self.feature_vector = []
        
    def process_feature(self, data):
        '''A bag-of-word approach to process raw data, more fancy methods can be applied.
        '''
        return data.split() 
