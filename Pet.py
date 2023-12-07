from Zodiac_Sign import Zodiac
from math import exp

#this will contain how much time has passed since last open
time_passed = 0

#this will contain the real life current time
true_time = 0

class Pet:

    def __init__(self):
        self.mental_health = 0
        self.mental_health_state = 0

        self.physical_health = 0
        self.physical_health_state = 0

        self.hunger = 0
        self.cleanliness = 0
        self.wildness = 0
        self.bio_age = 0  #determines age of the pet physically-wise
        self.weight = 0
        self.trust = 0
        self.attractiveness = 0
        
        self.attraction = 0
        self.IQ = 0

        self.true_age = 0 #the actual age of pet
        

    #============================================================
    #calculations - still needs 
    #============================================================

    #calculates age of the pet
    def __calc_Trueage(self):
        self.true_age += time_passed

    #calculates biological age of the pet
    def __calc_bio_age(self,star_sign):
        self.bio_age = (self.physical_health + self.mental_health + self.weight)**(-1) + self.bio_age
    
    #calculates attrctiveness of the pet
    def __calc_attractiveness(self):
        self.attractiveness = (1-1/(self.cleaniness))**self.bio_age

    #calculates mental health state, the rate will be calculated in starsign
    def __calc_mental_health(self,star_sign):
        self.mental_health = -100/(1 + exp(- star_sign.mental_health_rate * (self.mental_health_state)))

    #calculates physical health state
    def __calc_physical_health(self,star_sign):
        self.physical_health = -100/(1 + exp(- star_sign.mental_health_rate * (self.physical_health_state)))


