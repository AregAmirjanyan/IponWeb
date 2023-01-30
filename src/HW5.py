#task 1 
'''
sample_dict = {
    'name' : 'kelly',
    'age' : 25,
    'salary' :8000,
    'city' : 'new york'
    }

keys = ['name', 'salary']
d={}

for x in keys:
    d[x] = sample_dict[x]
    
        
print(d)



    

#task 2 
sample_dict2 = {
    'physics' : 82,
    'math' : 65,
    'history' : 75
    }

min = 10000

for val in sample_dict2.values():
    if val < min:
        min = val
             
for key in sample_dict2.keys():
    if sample_dict2[key] == min:
        print(key)



#task 3 
def copy():
    with open('text.txt', 'r') as f:
        text = ''
        for string in f:
            text += string
        
        with open ('new.txt', 'w') as g:
            g.write(text)
            
        with open('new.txt', 'r') as g:
            return(g.read())

print(copy())



#task 4 
def freq():
    d = {}
    with open('/Users/areg/Documents/Iponweb/psps.txt' , 'r') as f:
       
        for line in f:
            
            words = line.split(' ')
            
            for word in words:
                
                if word in d:
                    d[word] += 1
                    
                else:
                    d[word] = 1
                
        return(d)
    
print(freq())
            


#task 5 
def bottom(n):
    with open('/Users/areg/Documents/Iponweb/text.txt', 'r') as f:
        lines = f.readlines()
        
        last_l = lines[-n:]
        return(last_l)
    
        #OR THIS WAY (prints the wanted lines as they are, not in a list)
        # x= 1
        # for line in lines:
        #     if x>len(lines)-n:
        #         print(line)
        #     else:
        #         x+=1
        
        
print(bottom(4))

'''

#task 6 

class Company:
    def __init__(self, company_name, founded_at, employees_count):
        self.company_name = company_name
        self.founded_at = founded_at
        self.employees_count = 0
        
    def __repr__(self):
        return "the name is " + self.company_name
    


iponweb=Company('iponweb', 2000, 0)

class Job:
    def __init__(self, company, salary, experience_year, position):
        self.company = iponweb
        self.salary = salary
        self.experience_year = experience_year
        self.position = position
        
    def __repr__(self):
        return "the job position is " + self.position
    
    def change_salary(self, new_salary):
        self.salary = new_salary
        return self.salary
    
    
    def change_experience_year(self, new_exp):
        self.experience_year = new_exp
        return self.experience_year
        
        
    def change_position(self, new_pos):
        self.position = new_pos
        return self.position

    
    

class Person:
    def __init__(self, name, surname, gender, age, address, friends, job):
        self.name = name
        self.surname = surname
        if gender in ['Male', 'Female','male', 'female']: self.gender = gender
        self.age =age
        self.address = address
        self.friends = []
        self.job = []    
    
    def __repr__(self):
        return "this is " +self.name +' ' + self.surname
    
    def add_friend(self, Person):
        self.friends.append(Person.name)
        
    def remove_friend(self, Person):
        self.friends.remove(Person.name)
        
    def add_job(self, job):
        self.job.append(job.position)
        job.company.employees_count += 1
        

    def remove_job(self, job):
        self.job.remove(job.position)
        job.company.employees_count -= 1
        
    def display_job(self):
        return self.job
    
    
    

# print(iponweb)

# prog = Job(iponweb, 1000, 2, 'programmer')
# prog2 = Job(iponweb, 1200, 4, 'designer')
# # print(prog.salary)
# # print(prog.change_salary(2000))
# # print(prog.salary)


# # print(prog.experience_year)
# # print(prog.change_experience_year(3))
# Vzg=Person('Vzg','yan', 'male', 20, 'hh', [], [])
# Vzg2=Person('Ar','yan', 'male', 20, 'hh', [], [])
# Vzg3=Person('Nar','yan', 'male', 20, 'hh', [], [])
# Vzg.add_friend(Vzg2)
# Vzg.add_friend(Vzg3)



# print(Vzg.friends)
# print(iponweb.employees_count)
        
        
# Vzg.add_job(prog)
# Vzg2.add_job(prog2)

# print(Vzg2.display_job())        
# print(iponweb.employees_count)        
# Vzg.remove_job(prog)
# print(prog.company.employees_count)




#task 7 
class Date:
    def __init__(self, __year, month, day):
        self.__year = __year
        self.month = int(month)
        self.day = int(day)
        self.date = str(day) +'.'+str(month) + '.' +str(__year)
        
    def __repr__(self):
        return str(self.day) + '.' + str(self.month) + '.' +str(self.year)
    
    
    
    def is_leap_year(self):
        if self.year % 4 ==0 or self.year %400 == 0:
            return True 
        else: return False
    
    
    
    def add_day(self, day):
        l= [1,3,5,7,8,10,12]  #months with 31 days
        l2=[4,6,9,11] #months with 30 days
        self.day = self.day + day
        
        if self.month in l:
            while self.day > 31:
                self.day -= 31
                self.month +=1
                if self.month > 12:
                    self.month -= 12
                    self.year +=1
                
        if self.month in l2:
            while self.day > 30:
                self.day -= 30
                self.month +=1     
                if self.month > 12:
                    self.month -= 12
                    self.year +=1
                    
        if self.month == 2 and self.is_leap_year is True:
            while self.day > 29:
                self.day -= 29
                self.month +=1     
                if self.month > 12:
                    self.month -= 12
                    self.year +=1   
                    
        elif self.month == 2 and self.is_leap_year is False:
            while self.day > 28:
                self.day -= 28
                self.month +=1     
                if self.month > 12:
                    self.month -= 12
                    self.year +=1   
            
        
    def add_month(self, month):
        
        self.month =self.month + month
        
        while self.month > 12:
            self.year +=1
            self.month -= 12
        
        
        
    def add_year(self, year):
        self.year = self.year + year
        
    # def __add__(self, val):
    #     return Date(self.date + val.date)




d=Date(2000, 11, 4)
# print(d)
# d.add_day(20)
# print(d.add_month(7))
# d.add_day(70)
# d.add_year(20)
# d.add_month(40)
# print(d)

# print(d)
# print(d.is_leap_year())
d.add_day(70000)
print(d)
d2=Date(2000, 11,4)
print(d2)

print(d+d2)

class Time:
    def __init__(self, hour, minute, second):
        if type(hour) == int and type(minute) == int and type(second) == int:
            self.hour = hour
            self.minute = minute
            self.second = second
        else: return False
        
    def __repr__(self):
        return str(self.hour) +'.' + str(self.minute) + '.' + str(self.second)
    
    def add_second(self, second):
        self.second += second
        while self.second >60:
            self.second -= 60
            self.minute += 1
            if self.minute > 60:
                self.hour +=1
                self.minute -= 60
                
                
    def add_minute(self, minute):
        self.minute += minute
        while self.minute > 60:
            self.minute -= 60
            self.hour += 1
            
    def add_hour(self, hour):
        self.hour += hour
        while self.hour > 24:
            self.hour = self.hour %24
            
    

time = Time(0,0,20)

# print(time)

# time.add_second(80)
# time.add_minute(65)
# time.add_hour(5)

# print(time)
            
    
    
    



