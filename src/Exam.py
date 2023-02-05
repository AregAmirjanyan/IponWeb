#1 continue
class Time:
    def __init__(self, hour, minute, second):
        if type(hour) == int and type(minute) == int and type(second) == int:
            self.hour = hour
            self.minute = minute
            self.second = second
        else: return False
        
    def __repr__(self):
        return str(self.hour) +'.' + str(self.minute) + '.' + str(self.second)
    
    def __add__(self, other):
        a= self.minute + other.minute
        while a>60:
            self.hour +=1
            a -= 60
        return a
        
    
    def add_second(self, second):
        self.second += second
        while self.second >60:
            self.second -= 60
            self.minute += 1
            if self.minute > 60:
                self.hour +=1
                self.minute -= 60
                if self.hour >=8:
                    self.hour = 0
                
                
    def add_minute(self, minute):
        self.minute += minute
        while self.minute > 60:
            self.minute -= 60
            self.hour += 1
            if self.hour >=8:
                self.hour = 0
            
    def add_hour(self, hour):
        self.hour += hour
        if self.hour >=8:
            return 'not enough time'
        


class Error(Exception):
    def __init__(self, message):
        pass
    
    
class Patient:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        if type(name) != str or type(surname) != str or age not in range(18,101) or gender not in ['M', 'F']:
            raise Error('name and surname must be str, age must be between 18,100 gender must be valid')
        
    def __repr__(self):
        return f"{self.name} {self.surname} - {self.gender}, {self.age} years old "
    
    
    def __ne__(self, other):
        return self.name != other.name or self.surname != other.surname or self.age != other.age
    
    
p1 = Patient('Ar', "b", 20, "M")
p2 = Patient('Nar', "a", 20, "M")
print(p1 != p2)



class Doctor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.schedule = {} #{Time: Patient}
   
        if len(self.schedule) > 16:
            raise ValueError
        
    def __repr__(self):
        return f"Doctor {self.name} {self.surname} schedule {self.schedule}"
    
    
    def is_free(self, time:Time):
        if time not in self.schedule.keys():
            return "the doctor is free at the given time"
        
        else: return "the doc is busy"
            
            
    def is_registered(self, patient:Patient):
        if patient in self.schedule.values():
            return "this patient is already registered"
        return 'this patient is not registered'
        
    
    
    def register_patient(self, patient:Patient, time:Time):
        
        if patient in self.schedule.values():
            return f"{patient} already registered"
        
        
        if time in self.schedule.keys():
            return f"{time} already taken for {patient}"
        
        
        start_time = time
        end_time = start_time + time.add_minute(30)
        self.schedule[time] = patient
        print( f"Patient {patient} successfully registered at {time}")
        
        
    
# time1 = Time(0,0,0)
# time2 = Time(1,0,0)
# time3 = Time(4,0,0)

# p3 = Patient('name', 'surname', 98, 'F')
        
# d = Doctor('name', 'surname')  
# d.register_patient(p1, time1) 
# d.register_patient(p2, time2)
# # print(d.is_free(time3))
# # print(d.is_registered(p3))
# print(d.is_registered(p1))

# # print(d.register_patient(p1, time3))
# print(d.register_patient(p3, time1))
# d.register_patient(p3, time3)


# # print(d)
# print(d.schedule)



#2
class Product:
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity
        
    def __repr__(self):
        return f"the price is {self.price}, id: {self.id}, quantity : {self.quantity}"
    
    def buy(self, count):
        self.quantity -= count
        if count > self.quantity:
            raise ValueError
            
        
        

prod1 = Product(1000, 12, 10)
prod2 = Product(300, 90, 44)

print(prod1)
prod1.buy(4)
# prod1.buy(19)
print(prod1)

        

class Inventory():
    def __init__(self):
        self.list = [prod1, prod2]    
        
    def __repr__(self):
        return f"{self.list}"
    
    def sum_of_products(self):  
        summ = 0 
        for prod in self.list:
            summ += prod.quantity
        return summ
    

    def get_by_id(self, id):
        for prod in self.list:  
            if prod.id == id:
                return prod
            
        else: return "No such item"
    

inv =Inventory()
print(inv) 
# print(inv.get_by_id(12))
print(inv.sum_of_products())
print(inv.get_by_id(12))
        




#3
class Hotel:
    def __init__(self, city):
        self.city = city 
        
        self.rooms= {"penthouse" : 10,
                     'single' : 16,
                         'double' : 10}
                
    def __repr__(self):
        return f"{self.city}, {self.rooms}"
    
    
    def get_city(self):
        return self.city
    
    
    def free_rooms_list(self, r_type):
        for a in self.rooms.keys():
            if a == r_type:
                return self.rooms[a]
            
            
    def reserve_rooms(self, r_type, count):
        if count <= self.rooms[r_type]:
            self.rooms[r_type] -= count
            return "You have succesfully reserved the room"
            
        else: return "Not so many free rooms"
    
    
h=Hotel('Arm')
# print(h)
# print(h.get_city())
# print(h.free_rooms_list('single'))
# print(h.reserve_rooms('double', 2))
# print(h.free_rooms_list('double'))

# print(h.reserve_rooms('single', 20))

    
    
class Passenger:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.room_types = ['penthouse', 'single', 'double']
      
        
        
        
    def __repr__(self):
        return f" {self.name},  {self.city}, "
    
    def get_name(self):
        return self.name
    
    def get_city(self):
        return self.city
    
    def get_rooms(self):
        return self.rooms
    
passenger = Passenger('AR', 'Arm')



def book(passenger: Passenger, h : Hotel):
    if passenger.city == h.city:
        print(h.reserve_rooms('double', 1))
        
print(book(passenger, h))
        
    
        
    
    
    

            
        
    


    
        
    
    
        








