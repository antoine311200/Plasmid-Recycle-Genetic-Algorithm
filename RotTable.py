import mathutils
import math

class RotTable:
    """Represents the rotation table"""    

    __ORIGINAL_ROT_TABLE = {\
        "AA": [35.62, 7.2, -154, 0.06, 0.6, 0],\
        "AC": [34.4, 1.1, 143, 1.3, 5, 0],\
        "AG": [27.7, 8.4, 2, 1.5, 3, 0],\
        "AT": [31.5, 2.6, 0, 1.1, 2, 0],\
        "CA": [34.5, 3.5, -64, 0.9, 34, 0],\
        "CC": [33.67, 2.1, -57, 0.07, 2.1, 0],\
        "CG": [29.8, 6.7, 0, 1.1, 1.5, 0],\
        "CT": [27.7, 8.4, -2, 1.5, 3, 0],\
        "GA": [36.9, 5.3, 120, 0.9, 6, 0],\
        "GC": [40, 5, 180, 1.2, 1.275, 0],\
        "GG": [33.67, 2.1, 57, 0.07, 2.1, 0],\
        "GT": [34.4, 1.1, -143, 1.3, 5, 0],\
        "TA": [36, 0.9, 0, 1.1, 2, 0],\
        "TC": [36.9, 5.3, -120, 0.9, 6, 0],\
        "TG": [34.5, 3.5, 64, 0.9, 34, 0],\
        "TT": [35.62, 7.2, 154, 0.06, 0.6, 0]\
        }
    """
    la data est un dictionnaire qui contient le Twist et le Wedge de tout les dinucleotide
    ainsi selon les cas , on prends les données de ORIGINAL_ROT_TABLE ou de data
    """
    def __init__(self, data={}):
        self.__Rot_Table = {}
        if(data=={}):
            for dinucleotide in RotTable.__ORIGINAL_ROT_TABLE:
                self.__Rot_Table[dinucleotide] = RotTable.__ORIGINAL_ROT_TABLE[dinucleotide][:2]

        else :
            for dinucleotide in data:
                self.__Rot_Table[dinucleotide] = data[dinucleotide]



    ###################
    # READING METHODS #
    ###################
    def getTwistVariance(self, dinucleotide): #independent
        return RotTable.__ORIGINAL_ROT_TABLE[dinucleotide][3]
    
    def getWedgeVariance(self, dinucleotide): #independent
        return RotTable.__ORIGINAL_ROT_TABLE[dinucleotide][4]

    def getTwist(self, dinucleotide): #depend on the individual
        return self.__Rot_Table[dinucleotide][0]

    def getWedge(self, dinucleotide): #depend on the individual
        return self.__Rot_Table[dinucleotide][1]

    def getDirection(self, dinucleotide): #independent
        return RotTable.__ORIGINAL_ROT_TABLE[dinucleotide][2]

    ###################
