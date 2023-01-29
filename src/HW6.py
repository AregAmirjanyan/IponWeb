
class DateError(Exception):
    def __init__(self, message):
        pass


class Date:
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day
        
        
        if type(year) != int or type(month) != int or type(day) != int:
            raise DateError('year, month and day must be integers')
        
    def __repr__(self):
        return str(self.__day) + '.' + str(self.__month) + '.' +str(self.__year)
    
    
    
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, year):
        self.__year = year
        
        
    @property
    def month(self):
        return self.__month
    
    @month.setter
    def month(self, month):
        self.__month = month
        
    @property
    def day(self):
        return self.__day
    
    @day.setter
    def day(self, day):
        self.__day = day
        
        
    
    
    def is_leap_year(self):
        if self.__year % 4 ==0 or self.__year %400 == 0:
            return True 
        else: return False
    
    
    
    def add_day(self, day):
        l= [1,3,5,7,8,10,12]  #months with 31 days
        l2=[4,6,9,11] #months with 30 days
        self.__day = self.__day + day
        
        if self.__month in l:
            while self.__day > 31:
                self.__day -= 31
                self.__month +=1
                if self.__month > 12:
                    self.__month -= 12
                    self.__year +=1
                
        if self.__month in l2:
            while self.__day > 30:
                self.__day -= 30
                self.__month +=1     
                if self.__month > 12:
                    self.__month -= 12
                    self.__year +=1
                    
        if self.__month == 2 and self.is_leap_year is True:
            while self.__day > 29:
                self.__day -= 29
                self.__month +=1     
                if self.__month > 12:
                    self.__month -= 12
                    self.__year +=1   
                    
        elif self.__month == 2 and self.is_leap_year is False:
            while self.__day > 28:
                self.__day -= 28
                self.__month +=1     
                if self.__month > 12:
                    self.__month -= 12
                    self.__year +=1   
            
        
    def add_month(self, month):
        
        self.__month =self.__month + month
        
        while self.__month > 12:
            self.__year +=1
            self.__month -= 12
        
        
        
    def add_year(self, year):
        self.__year = self.__year + year
        
        
    def sub_year(self, year):
        self.__year = self.__year - year
        if self.__year<0:
            return False
    
    
    
    def sub_month(self, month):
        self.__month -= month
        while self.__month <0:
            self.__month += 12
            self.__year -= 1
            
            
    def sub_day(self, day):
        l= [1,3,5,7,8,10,12]  #__months with 31 __days
        l2=[4,6,9,11] #__months with 30 __days
        self.__day -= day
        while self.__day < 1:
            if self.__month in l:
                self.__day += 31
                self.__month -= 1
                if self.__month < 1:
                    self.__month +=12
                    self.__year -=1
                
            if self.__day < 1 and self.__month in l2:
                self.__day += 30
                self.__month -= 1
                if self.__month < 1:
                    self.__month +=12
                    self.__year -=1
                
                
                
            if self.__day <1 and self.__month ==2:
                self.__day +=29
                self.__month -= 1
                if self.__month < 1:
                    self.__month +=12
                    self.__year -=1
                    

            


d=Date(2000, 6, 1)
# # print(d)
# # d.add_day(20)
# # d.add_month(7)
# # d.add_day(70)
# # d.add_year(20)
# # d.add_month(40)

# # print(d)

# # d.sub_year(20)
# # d.sub_month(11)
# # d.sub_day(44)
# # d.sub_day(480)
# print(d)
# print(d.year)

# d.year = 2022
# print(d.year)
# d.month = 11

# print(d.day)
# d.day = 20
# print(d)

# print(d.is_leap_year())

class TimeError(Exception):
    def __init__(self, message):
        pass

class Time:
    def __init__(self, hour, minute, second):
       
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        
        if type(hour) != int or type(minute) != int or type(second) != int:
            raise TimeError('hour, minute and second must be integers')
        
        
    def __repr__(self):
        return str(self.__hour) +'.' + str(self.__minute) + '.' + str(self.__second)
    
    
    @property
    def hour(self):
        return self.__hour
    
    
    @hour.setter
    def hour(self, hour):
        self.__hour = hour
        
    
    @property
    def minute(self):
        return self.__minute
    
    @minute.setter
    def minute(self, minute):
        self.__minute = minute
        
        
    @property
    def second(self):
        return self.__second
    
    @second.setter
    def second(self, second):
        self.__second = second 
        
    
    
    def add_second(self, second):
        self.__second += second
        while self.__second >60:
            self.__second -= 60
            self.__minute += 1
            if self.__minute > 60:
                self.__hour +=1
                self.__minute -= 60
                
                
    def add_minute(self, minute):
        self.__minute += minute
        while self.__minute > 60:
            self.__minute -= 60
            self.__hour += 1
            if self.__hour >24:
                self.__hour -=24
                
                
    def add_hour(self, hour):
        self.__hour += hour
        while self.__hour > 24:
            self.__hour %= 24
                

    

time = Time(0,0,20)

# time.add_second(80)
# time.add_minute(68)
# time.add_hour(23)
# # print(time.hour)
# time.add_hour(20)

# time.add_hour(12)
# time.minute = 44
# print(time.minute)

# time.second= 50
# print(time.second)

# print(time)


# print(time)
# time.hour = 23
# print(time.hour)
# time.add_hour(11)
# print(time)



class DateTime(Date, Time):
    def __init__(self, year, month, day, hour, minute, second):
        Date.__init__(self, year, month, day)
        Time.__init__(self, hour, minute, second)
        
        
    def __repr__(self):
        return 'the date is ' + str(self.day) + '.' + str(self.month) + '.' +str(self.year) + '\n' + 'the time is '+ str(self.hour) +'.' + str(self.minute) + '.' + str(self.second) + '\n' 
        
    def get_date(self):
        return str(self.day) + '.' + str(self.month) + '.' +str(self.year)
        
    def set_date(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    def get_time(self):
        return str(self.hour) +'.' + str(self.minute) + '.' + str(self.second)
    
    def set_time(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second      
        
    
    def add_hour(self, hour):
        self.hour += hour
        while self.hour > 24:
            self.hour -= 24
            self.day += 1
            if self.day >31:
                self.day -=31
                self.month +=1
                if self.month >12:
                    self.month -=12
                    self.year +=1
    
    
    #(sub)add_day, year, month  are implemented in their own classes
    def sub_hour(self, hour):
        self.hour -= hour
        while self.hour < 1:
            self.hour +=24
            self.day -=1
            if self.day < 1:
                self.day +=30
                self.month -= 1
                if self.month <1:
                    self.year -=1
                    self.month+=12
                    
                    
                    
    def sub_minute(self, minute):
        self.minute -= minute
        while self.minute < 1:
            self.minute += 60
            self.hour -=1
            if self.hour <1:
                self.hour +=24
                self.day -=1
                
                
    def sub_second(self, second):
        self.second -= second
        while self.second <1:
            self.second +=60
            self.minute -=1
            if self.minute <1:
                self.minute += 60
                self.hour -=1
                if self.hour <1:
                    self.hour +=24
                    self.day -=1
                    
                    
    def add_minute(self, minute):
        self.minute += minute
        while self.minute > 60:
            self.minute -= 60
            self.hour += 1
            if self.hour >24:
                self.hour -=24
                self.day += 1
                if self.day >31:
                    self.day -=31
                    self.month +=1
                    if self.month >12:
                        self.month -=12
                        self.year +=1
            
            
            
    def __add__(self, val):
        return self.year +val.year
    
    
    def __sub__(self, val):
        if self.year > val.year:
            return self.year - val.year
        else: 
            return val.year - self.year
        
    
    
    
            
        
    
dt=DateTime(2000, 11, 4, 21, 11, 40)
# dt.hour=4
# print(dt.hour)
# print(dt)
# dt2 = DateTime(200, 1, 1, 1, 1, 1)
# dt.add_second(40)

# print(dt)

# print(dt.get_date())

# dt.set_date(2011, 4, 4)
# print(dt.get_date())

# print(dt)

# dt.set_time(1, 30, 55)
# print(dt.get_time())

# dt.add_year(22)

# dt.add_minute(80)



# dt.sub_year(200)
# dt.sub_day(59)

# dt.sub_hour(600)
# dt.sub_minute(39)
# dt.sub_second(6000)
# dt.sub_month(2)
# dt.add_hour(90)
# dt.add_minute(600)

# print(dt)
# print(dt-dt2)
# print(dt+dt2)



class MoneyError(Exception):
    def __init__(self, amount, currency, message = 'amaount must be an integer, currency a string'):
        self.amount = amount
        self.currency = currency
        self.message = message
        super().__init__(self.message)
        

class Money:
    
    exchange = {'AMD':1, 'RUB' :5.8, 'USD':400, 'EUR':430}
    
    def __init__(self, amount, currency):
    
            
        self.amount = amount
        
        self.exchange = {'AMD':1, 'RUB' :5.8, 'USD':400, 'EUR':430}
        if currency in self.exchange.keys():
            self.currency = currency
            
        if type(currency) != str or type(amount) != int:
            raise MoneyError(amount, currency)
     
        
    def __repr__(self):
        return 'we have ' +str(self.amount) + ' in ' +self.currency
    
    def get_amount(self):
        return self.amount
    
    def set_amount(self, amount):
        self.amount = amount
        
    def get_currency(self):
        return self.currency
    
    def set_currency(self, currency):
        if currency in self.exchange.keys():
            self.currency = currency
        else: print('invalid currency')
        
        
    def convert(self, currency):
        if currency != self.currency:
            self.amount = self.amount * (self.exchange[self.currency] / self.exchange[currency])
            self.currency = currency
            

        
        
    def __add__(self, val):                       
        if val.currency == self.currency:
            return self.amount + val.amount
        
        else: 
            a= val.amount *self.exchange[val.currency] / self.exchange[self.currency]
            val.currency = self.currency
            return self.amount+a

        
        
    def __sub__(self, val):     
        if val.currency == self.currency:
            return self.amount - val.amount  
        else: 
            a= val.amount *self.exchange[val.currency] / self.exchange[self.currency]
            val.currency = self.currency
            if self.amount-a <0:
                return False
            else:
                return self.amount-a
            
            
    def __truediv__(self,val):
        
        if val.currency == self.currency:
            return self.amount / val.amount
        
        else: 
            a= val.amount *self.exchange[val.currency] / self.exchange[self.currency]
            val.currency = self.currency
            return self.amount/a      
        
        
        
    def __eq__(self, val):
        if val.currency == self.currency and val.amount == self.amount:
            return self.amount == val.amount
            
        else: 
            a= val.amount *self.exchange[val.currency] / self.exchange[self.currency]
            val.currency = self.currency
            if a == self.amount:
                return 'the two instances are equal'
        return False
    
    
    
    def __ne__(self, val):
        return self.amount != val.amount
    
    
    def __lt__(self, val):
       
        return self.amount < val.amount
        
      
    def __gt__(self, val):
        
        return self.amount > val.amount
    
    def __le__(self, val):
       
        return self.amount <= val.amount 
    
    def __ge__(self, val):
        
        return self.amount >= val.amount
    
    
# Checking MoneyError
# # money = Money('a', 'AMD')
# # print(money)


    
# mo = Money(1, 'AMD')
# mo2 = Money(100, 'AMD')
# print(mo/mo2)
        
     
# m=Money(100,'RUB')
# print(m)
# m.set_amount(100)
# print(m.get_amount())

# m.set_currency('USD')
# print(m.get_currency())



# print(m)
# m.convert('AMD')
# print(m)


# m2 = Money(300, 'USD')
# m2.convert('AMD')


# print(m+m2)
# # print(m-m2)
# # b=m2/m
# # print(b)
# print(m!=m2)
# print(m<m2)
# print(m>m2)
# print(m<=m2)
# print(m>=m2)
   
        
        
class MyRangeError(Exception):
    def __init__(self, current, end, step, message = 'current, end and step must be integers'):
        self.current = current
        self.end = end
        self.step = step
        self.message = message
        super().__init__(self.message)      
        
    
class MyRange:
    def __init__(self, current, end, step):
        self.current = current
        self.end= end
        self.step = step
        
        if type(current) != int or type(end) != int or type(step) != int:
            raise MyRangeError(current, end, step)
        
    def __repr__(self):
        return 'we are currently at ' + str(self.current) +' the end is at ' +str(self.end)
    
    
    def __iter__(self):
        self.n = self.current
        self.l= [self.current]
        return self
    
    
    def __next__(self):
        
        
        if self.n > self.end - self.step:
            raise StopIteration
            
        else:
            self.n += self.step
            self.l.append(self.n)
            return self.n
        
        
    def __len__(self):
        return len(self.l)
    
    
    def __getitem__(self, key):
        return self.l[key]


    def __reversed__(self):
        print('in reverse order')
        for num in self.l[::-1]:
            print(num)
    
    
            
#checking MyRangeError
# rangee = MyRange(1, 1, '')




    
# ran1 = MyRange(1, 10, 3)
# print(ran1)

# i = iter(ran1)
# print(i.current)
# print(next(i))
# print(next(i))
# print(next(i))

# print(len(ran1))


# print(ran1[2])
# print(reversed((ran1)))


class Company:
    def __init__(self, company_name, founded_at, employees_count):
        self.__company_name = company_name
        self.__founded_at = founded_at
        self.__employees_count = 0
        
    def __repr__(self):
        return "the name is " + self.__company_name
    
    
    @property
    def company_name(self):
        return self.__company_name
    
    @company_name.setter
    def company_name(self, val):
        self.__company_name = val
        
    @property
    def founded_at(self):
        return self.__founded_at
    
    @founded_at.setter
    def founded_at(self, founded_at):
        self.__founded_at = founded_at
        
        
    @property
    def employees_count(self):
        return self.__employees_count
    
    @employees_count.setter
    def employees_count(self, employees_count):
        self.__employees_count = employees_count
        
        



class Job:
    def __init__(self, company:Company, salary, experience_year, position):
        self.__company = company
        self.__salary = salary
        self.__experience_year = experience_year
        self.__position = position
        
    
    @property
    def company(self):
        return self.__company
    
    @company.setter
    def company(self, company):
        self.__company = company
        
    @property
    def salary(self):
        return self.salary
    
    @salary.setter
    def salary(self, salary):
        self.__salary = salary
        
    @property
    def experience_year(self):
        return self.__experience_year
    
    @experience_year.setter
    def experience_year(self, experience_year):
        self.__experience_year = experience_year
        
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, position):
        self.position = position
        
        
        
    
    def __repr__(self):
        return "the job position is " + self.__position
    
    def change_salary(self, new_salary):
        self.__salary = new_salary
        return self.__salary
    
    
    def change_experience_year(self, new_exp):
        self.__experience_year = new_exp
        return self.__experience_year
        
        
    def change_position(self, new_pos):
        self.__position = new_pos
        return self.__position




class Person:
    def __init__(self, name, surname, gender, age, address, friends, job):
        self.__name = name
        self.__surname = surname
        if gender in ['Male', 'Female','male', 'female']: self.__gender = gender
        self.__age =age
        self.__address = address
        self.__friends = []
        self.__job = []    
        
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self, surname):
        self.__surname = surname
    
    
    @property
    def gender(self):
        return self.__gender
    
    @gender.setter
    def gender(self, gender):
        self.__gender = gender
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
        
        
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address):
        self.__address = address
        
        
    @property
    def friends(self):
        return self.__friends
    
    @friends.setter
    def friends(self, friends):
        self.__friends = friends
        
    @property
    def job(self):
        return self.__job
    
    @job.setter
    def job(self, job):
        self.__job = job
    
    
    def __repr__(self):
        return  self.__name +' ' + self.__surname
    
    def add_friend(self, Person):
        self.__friends.append(Person.__name)
        
    def remove_friend(self, Person):
        self.__friends.remove(Person.__name)
        
    def add_job(self, job):
        self.__job.append(job.position)
        job.company.employees_count += 1
        

    def remove_job(self, job):
        self.__job.remove(job.position)
        job.company.employees_count -= 1
        
    def display_job(self):
        return self.__job      
    
    
# iponweb=Company('iponweb', 2000, 0)
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


class DoctorError(Exception):
    def __init__(self, message):
        pass

class Doctor(Person):
    def __init__(self, name, surname, gender, age, address, friends, job, department, profession, patronymic, salary ):
        super().__init__(name, surname, gender, age, address, friends, job)
        self.department = department
        self.profession = profession
        self.patronymic = patronymic
        self.salary = salary
        
        if type(department) != str or type(profession) != str or type(patronymic) != str or type(salary) != int:
            raise DoctorError("salary must be an integer, all the other vars must be strings")
        
    def __repr__(self):
        return "this is Doctor " + str(self.name) + ' ' +str(self.surname) 
    
    
    def set_department(self, department):
        self.department = department
        
    def get_department(self):
        return self.department
    
    
    def set_profession(self, profession):
        self.profession = profession
        
    def get_profession(self):
        return self.profession
    
    
    def get_patronymic(self):
        return self.patronymic
    
    
    def set_salary(self, salary):
        self.salary = salary
        
    def get_salary(self):
        return self.salary
    


# d1 = Doctor('AR', 'Mar', 'Male', 12, 1, None, 'job', 'department', 'profession', 'HM', 1000)

# d1.set_department('idk')

# print(d1)

# print(d1.get_department())
# print(d1.get_patronymic())

# d1.set_salary(2000)
# print(d1.get_salary())

        

class CityError(Exception):
    def __init__(self, message):
        pass

class City:
    def __init__(self, name, population, language, mayor:Person ):
        self.name = name
        self.population = population
        self.language = language 
        self.mayor = mayor
        
        if type(name) != str or type(language) != str or type(population) != int:
            raise CityError('name and langauge must be string, population must be an integer')
        
    
    def __repr__(self):
        return "this is city " + str(self.name) + ' and its mayor is ' +str(self.mayor)
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
        
    def get_population(self):
        return self.population
    
    def set_population(self, population):
        self.population = population
        
        
    
    def get_mayor(self):
        return self.mayor
    
    
    def set_mayor(self, mayor):
        self.mayor = mayor
        
    def get_language(self):
        return self.language
    
    
p1=Person('Areg','yan', 'male', 20, 'hh', [], [])
p2=Person('Nar','Tadevosyan', 'male', 30, 'k', [], [])


c=City('Arm', 1000, 'arm', p1)

# print(c.get_mayor())
# c.set_mayor(p2)
# print(c.get_mayor())

# print(c.get_name())
# c.set_name('America')
# print(c.get_name())

# print(c.get_population())



# # print(c.mayor.address)


# # print(c)

class UniversityError(Exception):
    def __init__(self, message):
        pass

class University():
    def __init__(self, name, founded_at : Date, rector : Person, city :City):
        self.name = name
        self.founded_at = founded_at
        self.rector = rector
        self.city = city
        
        if type(name) != str: 
            raise CityError('name must be a str')
        
        if not isinstance(founded_at, Date) or not isinstance(rector, Person) or not isinstance(city, City):
            raise CityError('name must be a str, other variables must be instances of respective classes')
        
    def __repr__(self):
        return "the university " + str(self.name) +', founded at ' +str(self.founded_at) 
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_founded_at(self):
        return self.founded_at

    def get_rector(self):
        return self.rector
    
    def set_rector(self, rector):
        self.rector = rector
        
    def get_city(self):
        return self.city



uni_date = Date(1980, 1, 28)
uni_rec = Person('Hamlet', 'idk', 'male', 80, 'address', [], [])
uni = University('AUA', uni_date, uni_rec, c)


# print(uni)
# print(uni.get_founded_at())
# print(uni.get_rector())
# uni.set_rector(p2)
# print(uni.get_rector())


class TeacherError(Exception):
    def __init__(self, message):
        pass

class Teacher(Person):
    def __init__(self, name, surname, gender, age, address, friends, job, university: University, facultet, experience, start_work_at : Date, subject, salary):
        super().__init__(name, surname, gender, age, address, friends, job)
        self.university = university
        self.facultet = facultet
        self.experience = experience
        self.start_work_at = start_work_at
        self.subject = subject
        self.salary = salary
        
        if type(facultet) != str or type(subject) != str or type(experience) != int or type(salary) !=int:
            raise TeacherError('This Hw is boaring')
        
        
    def __repr__(self):
        return f"the teacher's name is {self.name} {self.surname} "
    
    
    def get_experience(self):
        return self.experience
    
    def set_experience(self, experience):
        self.experience = experience
        
    def get_start_work_at(self):
        return self.start_work_at
    
    def get_subject(self):
        return self.subject
    
    def get_facultet(self):
        return self.facultet
    
    def set_facultet(self, facultet):
        self.facultet = facultet
        
    def get_salary(self):
        return self.salary
    
    def set_salary(self, salary):
        self.salary = salary
        
    
        
        
        
    
    
    
    
w_date = Date(2009, 3, 24)
teacher = Teacher('Hasmik', 'Martirosyan', 'female', 28, 'address', [], [], uni, 'science', 10, w_date, 'english', 9000)
## m=Money(100,'RUB')
##teacher.salary = m.amount
## print(teacher.get_salary())


# print(teacher)
# print(teacher.get_experience())
# print(teacher.get_start_work_at())
# teacher.set_facultet('engineer')
# print(teacher.get_facultet())

class StudentError(Exception):
    def __init__(self, message):
        pass



class Student(Person):
    def __init__(self, name, surname, gender, age, address, friends, job, university: University, faculty, course, started_at :Date):
        super().__init__(name, surname, gender, age, address, friends, job)
        self.university = university
        self.faculty = faculty
        self.course = course
        self.started_at = started_at
        
        if type(faculty) != str or type(course) != int:
            raise StudentError('facultey must be a str, course an int')
        
        
    def __repr__(self):
        return f"This student is {self.name} {self.surname}  "
    
    def get_university(self):
        return self.university
    
    def set_university(self, university):
        self.university = university
        
        
    def get_faculty(self):
        return self.faculty
    
    def set_faculty(self, faculty):
        self.faculty = faculty
        
    def get_course(self):
        return self.course
    
    def set_course(self, course):
        self.course = course
        
        
    def get_start_at(self):
        return self.started_at
        
        
    
    
    


# stu = Student('Anna', 'Hakobyan', 'Female', 21, 'address', [], [], uni.name, 'DS', 'Calculus', w_date)
# print(stu.get_university())
# stu.set_university('EPH')
# print(stu.get_university())
# print(stu.get_faculty())
# print(stu.get_start_at())




#task 10
def times_called(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    
    helper.calls = 0 
    helper.__name__= func.__name__
    return helper

@times_called
def function():
    return 'hi'
    
print(function())
print(function())
    
function.calls



    









            
    