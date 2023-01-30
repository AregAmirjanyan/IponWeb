#Task 1 
''' 
def progression(a1,a2, n):
    d= a2 - a1
    an=a1 + d*(n-1)
    return an

print(progression(1, 6, 4))
    



# Task2   

def inputString(s):
    summ = 0
    x = ''

    for letter in s:
        if letter.isdigit() == True:
            x += letter
            
        else:
            summ += int(x)
            x='0'
            
    return summ +int(x)
        

print(inputString('1 apple, 77 oranges 1'))



#task 3 
def check(a,b,c):
    if a<b and b>c:
        print ("unsorted")
    elif a>b and b<c:
        print ("unsorted")
    else:
        print("sorted")

check(20,16,10)



#task 4  
def perfect(a):
    summ=0
    for num in range(1, a):
        if a%num == 0:
            summ += num
    if summ == a:
        print("the number is perfect")
    else: print("the num is NOT perfect")
    
perfect(28)    



#task 5  
def count_sum(l):
    summ=0
    for num in l:
        summ += num
    return summ
print(count_sum([1,9,100]))





#task 6  
def find_max(l):
    maxx=0
    for num in l:
        if num > maxx:
            maxx=num
    return maxx

print(find_max([1,9,88,4]))
            
        

#task 7 
def del_elements(l, a):
    while a in l:
        l.remove(a)
    return l

print(del_elements([1,2,3,3,3,4,3,5], 3))
    
            


#task 8 
def mult(l):
    overall_mult=1
    for num in l:
        overall_mult *= num
    return overall_mult
print(mult([1,2,3,4]))




#task 9  
def reverse(s):
    if len(s) % 4 == 0:
        s= s[::-1]
        return s
    else: print("the length is not divisible by 4")
    
print(reverse('Areg'))
    


#task 10 
def fib_recurive(n):
    if n<=1:
        return n
    else:    
        return fib_recurive(n-1) + fib_recurive(n-2)
    
print(fib_recurive(10))



def fib_iterative(n):
    a=1
    b=0
    if n==0:
        return n
    else:     
        for num in range(1,n):
            total = a+b
            b=a
            a=total
        return a
    
print(fib_iterative(10))
            
            
        

#task 11 

def lcm(a,b):
    for num in range(1, 999999):
        if num%a == 0 and num%b == 0:
            return num
      

print(lcm(11, 56))
    






#task 12 
def palindrome(n):
    s=''
    a=0
    for num in range(n, 100*n):
        a=str(num)
        a=a[::-1]
        a=int(a)
        if num==a:
            return num      
        
print(palindrome(119))
        
    
    
    
#task 13  
def robot(command):
    X=0
    Y=0
    
    for move in range(len(command)):
        # U:Up, D:Down, L;Left, R:Right
        if command[move] == 'U':
            Y += 1
            
        elif command[move] == 'D':
            if Y>0:
                Y -=1
            
        elif command[move] == 'L':
            if X>0:
                X -= 1
            
        elif command[move] == 'R':
            X += 1
        
    return (X,Y)
            
        
print(robot('RRURUULD'))          

        
    
    
    
#task 14 
def check_lists(l1, l2):
    if len(l1) != len(l2):
        return False
    
    if l1[-1] == l2[0]:
        
        for num in range(0, len(l1)-1):
        
            if l1[num] == l2[num+1]:
                continue
            
            else: return False
            
        return True
            
          
    else: return False
            
print(check_lists([1,2,3,4,5,6], [6,1,2,3,4,5]))
   
    
   

#task 15 
def delete_digit(n):
    n = str(n)
    l=[]
    for num in n:
        l.append(int(num))
        
    minn = l[0]
    
    for idx in range(len(l)):
        if l[idx] <= minn:
            minn = l[idx]
            
            
    l.remove(minn)
    var = ''
    for x in l:
        var += str(x)
    
    return int(var)

print(delete_digit(152))
    
    
    
    
#task 16   
def tuples(t):
    t_2=()
    for num in t:
        if type(num) is int:
            t_2 += (num,)
    return t_2

print(tuples((1,6,'hey', 0)))
        
    
    
    
#task 17 
def append_tuple(t, x):
    t += (x, )
    return t

print(append_tuple((1,2,'hh',88), 9))




#task 18   
def str_tuple(t):
    s = ''
    
    for element in t:
        s += str(element) 
        
    s = '-'.join(s)
    return s

print(str_tuple(("a","b","c", 9)))






    
#task 19 
def list_len(l):
    length = 0
    for num in l:
        length += 1
    return length

print(list_len([1,2,3,4,9,'ab']))
    
    
    
    
    
#task 20 works #cannot solve without lists/strings because I need to use len() function to split the number into equal parts
def is_lucky(n):
  
    s=str(n)

    half = len(s)//2
    first_half= int(s[:half])
    last_half = int(s[half:])
    sum1 = 0
    sum2 = 0 
    
    while first_half > 1:
        mod = first_half % 10
        sum1 += int(mod)
        first_half=first_half/10
        
    while last_half > 1:
        mod = last_half % 10
        sum2 += int(mod)
        last_half=last_half/10
        
    if sum1 == sum2:
        return ("The number is lucky")
    else: return False


print(is_lucky(11110004))
    
    

# task 21  
def gcd(x,y):
    if y==0:
        return x
    else: return gcd(y,x%y)


def euler(n):
    
    summ = 0
    for num in range(1,n):
        if gcd(n,num) == 1:
            summ += 1
            
    return summ

print(euler(6))
        
    

#task 22 

def remove_anagrams(words):
    
    if len(words) in range(1,101):
        
        i=0
        while i < len(words):
            
            if len(words[i]) > 10 or len(words[i])<1:
                return False
            
            if words[i].islower() is False:
                return False
            
            if sorted(words[i]) == sorted(words[i-1]):
                words.remove(words[i])
                continue
            i+=1
                    
        return words
    
    else: print("the lenght is not correct")

print(remove_anagrams(['abab','baba','aabb', 'gg', 'hey','yeh']))

'''



#task 23
def name_height(names, heights):
    
    if len(heights) != len(names):
        return False
    
    n = len(names)
    if n < 1 or n > 10**3:
        return False
    
    
    
    paired=dict()
    
    
    for i in range(len(names)):
        
        if len(names[i]) < 1 or len(names[i])>20:
            return False
        
        if  names[i].islower() or names[i].isupper():
            return False
            
        
        key = names[i]
        value = heights[i]
        paired[key] = value
        
        
    for i in range(len(heights)):
        
        if heights[i] < 1 or heights[i] > 10 ** 5:
            return False
        
    #check wheter the values in height are distinct
    set_heights = set(heights)
    if len(set_heights) != len(heights):
        return False
    
    
    l=[]
    sorted_paired = sorted(paired.items(), key=lambda item:item[1], reverse = True )
    print(sorted_paired)
    
        
        
    
name_height(['Areg','Narek','Aram'], [100,200,150])    
    
    
    
'''


#task 24 

def ranking(votes):
    d={}
    
    if len(votes) >= 1 and len(votes) <= 1000:
    
        for string in votes:
         
            for char in range(len(string)):
                
                if string[char] not in d:
                    d[string[char]] = [0] * len(string)       
                d[string[char]][char] += 1
        
        # I used online sources for this part
        l = sorted(list(d.keys()))
        final= sorted(l, key = lambda string: d[string], reverse = True)
        
        return "".join(final)

print(ranking(['ABC', "BCA", "ABC", "ACB", "ACB" ,"CAB", "ACB"]))
            
            
'''         















    



