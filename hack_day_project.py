from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random
import operator
x = {1: 2, 3: 4, 4:3, 2:1, 0:0}


INTEREST_WEIGHT = 0.6
AVAILABILITY_WEIGHT = -0.2
LOCATION_WEIGHT = 0.3
CAMPUS_WEIGHT = 0.8
BUILDING_WEIGHT = 0.2
TIME_WEIGHT = 0.1
"""
   Parent class person
   
"""
class Person:
    def __init__(self,name):
        self.name = name
        self.campus = None
        self.building = None
        self.time = []
        self.list_of_target = []
        
##    def add_location(self, loc):
##        self.location.append(loc)

    def add_time(self,time):
        self.time.append(time)

    def add_target(self,target):
        self.list_of_target.append(target)

    def get_num_target(self):
        return len(self.list_of_target)
    
    def __str__(self):
        return self.name

class Mentee(Person):
    def __init__(self,name):
        Person.__init__(self,name)        
        self.interest = []
                
    def add_interest(self, topic):        
        self.interest.append(topic)    
    

class Mentor(Person):
    def __init__(self,name):
        Person.__init__(self,name)
        self.expertise = []

    def add_expertise(self, topic):
        self.expertise.append(topic)

class MatchingPool:
    def __init__(self,mentors,mentee):
        self.mentors = mentors
        self.result = {}
        self.mentee = mentee

    def match_list(self):
        for i in self.mentors:
            self.result[i.name] = CalculateScore(i, self.mentee).calculate_score()            
        if len(self.result) > 0:
            return [(w,self.result[w]) for w in sorted(self.result, key = self.result.get,reverse = True)]
                
                
            
        
        

# calculate the score between a mentor and mentee
class CalculateScore:       
    
    def __init__(self,mentor, mentee):
        self.mentor = mentor
        self.mentee = mentee
        self.score = 0
        

    def calculate_score(self):
        compare = lambda x,y : 1 if x == y else 0
        interest_score = 0
        availability_score = 0
        location_score = 0
        time_score = 0

        score, number_of_match = cal_stringArray(self.mentor.expertise, self.mentee.interest)
        
        location_score = cal_location(self.mentor, self.mentee)
        
        time_score = compare(self.mentor.time, self.mentee.time)
        availability = self.mentor.get_num_target()
        self.score = INTEREST_WEIGHT*score + LOCATION_WEIGHT*location_score + time_score*TIME_WEIGHT + availability*AVAILABILITY_WEIGHT
        return self.score
        
        
# calculate the score of matching string and number of instances matches of two arrays of string      
            
def cal_stringArray(string1, string2):
    # function to return the list with smaller length
    f = lambda x,y: y if len(x) >= len(y) else x
    clone_string1 = [i.lower() for i in string1[:]]
    clone_string2 = [i.lower() for i in string2[:]]
    score = 0
    number_of_match = 0
    for item in clone_string1:
        # stop if run out of item
        if len(clone_string2) > 0:
            temp = process.extractOne(item, clone_string2,score_cutoff=90)
            # temp can be None due to score_cutoff
            if temp != None:
                clone_string2.remove(temp[0].lower())
                score += temp[1]/float(100)
                number_of_match += 1            
    return score, number_of_match

class Campus:
    def __init__(self,name):
        self.name = name
        
    def name(self):
        return self.name
    def __cmp__(self,other):
        return self.name == other.name

class Building(Campus):
    def __init__(self,name):
        Campus.__init__(self,name)
    
    
#     
def cal_location(object1,object2):
    campus_match = 0
    building_match = 0
    if object1.campus.name == object2.campus.name:
        campus_match = 1
    if object1.building.name == object2.building.name :
        building_match = 1
    if campus_match == 1:
        return CAMPUS_WEIGHT*campus_match + BUILDING_WEIGHT*building_match
    else:
        return 0
    
"""
# test for cal_stringArray
cool = ['machine learning', 'artificial intelligent', 'R']
cooles = ['machine learning', 'artificial intelligience']
funk = ['Java','C', 'mathlab']
funkier = ['machine learning']
print cal_stringArray(cool, cooles)
print cal_stringArray(cool,funk)
print cal_stringArray(cool,funkier)
"""
        
    
skills = ['Ajax' ,'ASP' , 'ASP.NET' ,'BASIC', 'C', 'C++', 'C#', 'ColdFusion' , 'CSS', 'Flash', 'HTML', 'Java', 'Javascript', 'MySQL', 'Perl', 'PHP', 'Python', 'Ruby', 'Visual Basic','XHTML', 'XML'] 

building = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

campus= ['Corporate South', 'Research & Development (RDC)', 'OAB', 'Corporate HeadQuarter', 'TRAIL']

list_of_mentee = ['Sherie Ovitt','Reena Scheider','Clarinda Christo','Kasha Seyler','Nguyet Carignan','Cristi Paro','Romaine Rawley','Corine Slonaker','Sherise Ferdinand','Palmira Rowell']

list_of_mentor = ['Tran Nguyen','Mark Coztanzo', 'Michael', 'Melissa Piontek', 'Unknown']

# make a list of Mentee object:
random.seed = 42
mentors_objects = [Mentor(i) for i in list_of_mentor]
mentees_objects = [Mentee(i) for i in list_of_mentee]

def Generate(people_list, typ):
    for i in people_list:
        a = random.randint(2,4)
        skill = set()    
        for j in range(a):        
            skill.add(random.choice(skills))
        i.campus = Campus(random.choice(campus))
        i.building = Building(random.choice(building))
        if typ is Mentor:
            i.expertise.extend(list(skill))
            
        else:
            i.interest.extend(list(skill))
    return people_list

mentors = Generate(mentors_objects,Mentor)
mentees = Generate(mentees_objects, Mentee)
for i in mentors:
    print i.name , i.expertise, i.campus.name
    
for i in mentees:
    print i.name, MatchingPool(mentors,i).match_list()
    print i.interest, i.campus.name
    





##tran = Mentor("Tran Nguyen")
##mark = Mentee("Mark")
##tran.campus = campus("Corporate South")
##tran.building = building("K")
##tran.time.extend(["at work"])
##tran.expertise.extend(["machine learning","artificial intelligent", "R"])
##mark.campus = campus("Corporate South")
##mark.building = building("M")
##mark.time.extend(["at work"])
##mark.interest.extend(['machine learning', 'artificial intelligience'])
##michael = Mentee("Micheal")
##michael.campus = campus("Corporate South")
##michael.building = building("L")
##michael.time.extend(["at work"])
##michael.interest.extend(['Java','C', 'mathlab'])
##tran.list_of_target.extend([mark])
##print CalculateScore(tran,mark).calculate_score()
##print CalculateScore(tran,michael).calculate_score()
