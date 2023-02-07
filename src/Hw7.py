#task 1

class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def print_tree(self):
       if self.left:
          self.left.print_tree()
          
       print( self.data)
       
       if self.right:
          self.right.print_tree()
    
        
    
    def insert(self, data):
        if self.data:
            
            if data < self.data:
                if self.left is None:
                    self.left = BST(data)
                else:
                    self.left.insert(data)
                 
            elif data > self.data:
                if self.right is None:
                    self.right = BST(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
   
                
                
    def delete(self, data):
        
        if data <self.data:
            temp = self.left
            while temp.data != data:
                temp = temp.left    
                if temp == None:
                    continue
            
        if data > self.data:
            temp = self.right
            while temp.data != data:
                temp = temp.right
                if temp == None:
                    continue
                
        if data == self.data:
            self.data = self.right.data
            self.delete(self.right.data)
        
        
                
        
            
            
            
    def search(self, data):
        if data == self.data:
            return True

        if data < self.data:
            if self.left == None:
                return False
            return self.left.search(data)

        if self.right == None:
            return False
        return self.right.search(data)
    
      
            
bst = BST(10)
bst.insert(20)
bst.insert(5)
bst.insert(100)
bst.insert(6)

print(bst.print_tree())
# print(bst.delete(5))
print(bst.search(10))          
            
            
            
            
#Task 2
# I googled most part of this problem
class Node():
    def __init__(self,val):
        self.val = val                                  
        self.parent = None                               
        self.left = None                               
        self.right = None                               
        self.color = 1                                   


class RBTree():
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL


   
    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                 

        y = None
        x = self.root

        while x != self.NULL:                          
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.parent = y                                 
        if y == None:                                  
            self.root = node
        elif node.val < y.val:                          
            y.left = node
        else:
            y.right = node

        if node.parent == None:                         
            node.color = 0
            return

        if node.parent.parent == None:                 
            return

        self.fixInsert(node)                        


    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node


   
    def LR (self, x):
        y = x.right                                    
        x.right = y.left                                 
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent                            
        if x.parent == None:                      
            self.root = y                               
        elif x == x.parent.left:
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y


   
    def RR (self, x):
        y = x.left                                      
        x.left = y.right                               
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent                            
        if x.parent == None:                           
            self.root = y                              
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y



    def fixInsert(self, k):
        while k.parent.color == 1:                       
            if k.parent == k.parent.parent.right:        
                u = k.parent.parent.left   
                
                if u.color == 1:                        
                    u.color = 0                          
                    k.parent.color = 0
                    k.parent.parent.color = 1           
                    k = k.parent.parent     
                    
                else:
                    if k == k.parent.left:              
                        k = k.parent
                        self.RR(k)                       
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
                    
            else:                                        
                u = k.parent.parent.right                
                if u.color == 1:                         
                    u.color = 0                         
                    k.parent.color = 0
                    k.parent.parent.color = 1           
                    k = k.parent.parent 
                    
                else:
                    if k == k.parent.right:             
                        k = k.parent
                        self.LR(k)                    
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent) 
                    
            if k == self.root:                          
                break
            
        self.root.color = 0                             


  
    def fixDelete (self, x):
        while x != self.root and x.color == 0:          
            if x == x.parent.left:                    
                s = x.parent.right   
                    
                if s.color == 1:                       
                    s.color = 0                           
                    x.parent.color = 1                
                    self.LR(x.parent)                 
                    s = x.parent.right
             
                if s.left.color == 0 and s.right.color == 0 :
                    s.color = 1                       
                    x = x.parent
                    
                else :
                    if s.right.color == 0:          
                        s.left.color = 0                
                        s.color = 1                
                        self.RR(s)                    
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0               
                    s.right.color = 0
                    self.LR (x.parent)              
                    x = self.root
            else:                                      
                s = x.parent.left                        
                if s.color == 1:                    
                    s.color = 0                         
                    x.parent.color = 1                
                    self.RR (x.parent)                
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else :
                    if s.left.color == 0:            
                        s.right.color = 0              
                        s.color = 1
                        self.LR(s)                   
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.RR(x.parent)
                    x = self.root
        x.color = 0


  
    def __rb_transplant(self,u,v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else :
            u.parent.right = v
        v.parent = u.parent


 
    def delete_node_helper(self,node,key):
        z = self.NULL
        while node != self.NULL:                          
            if node.val == key:
                z = node

            if node.val <= key:
                node = node.right
            else:
                node = node.left

        if z == self.NULL:                             
            print ( "Value not present in Tree !!" )
            return

        y = z
        y_original_color = y.color   
                    
        if z.left == self.NULL:                          
            x = z.right                                   
            self.__rb_transplant (z, z.right)    
            
        elif (z.right == self.NULL):                     
            x = z.left                                    
            self.__rb_transplant (z, z.left)  
            
        else:                                           
            y = self.minimum (z.right)                  
            y_original_color = y.color                
            x = y.right
            if y.parent == z:                             
                x.parent = y                               
            else :
                self.__rb_transplant (y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant (z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:                       
            self.fixDelete ( x )


    
    def delete_node (self, val) :
        self.delete_node_helper ( self.root , val)      


  
    def __printCall (self,node, indent, last) :
        if node != self.NULL :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.val ) + "(" + s_color + ")" )
            self.__printCall ( node.left , indent , False )
            self.__printCall ( node.right , indent , True )


    def print_tree ( self ) :
        self.__printCall ( self.root , "" , True )


if __name__ == "__main__":
    bst = RBTree()

    bst.insertNode(10)
    bst.insertNode(15)
    bst.insertNode(30)
    bst.insertNode(4)
    bst.insertNode(1)
    bst.insertNode(3)

    bst.print_tree()

  
    # bst.delete_node(2)
    print('after delete')
    bst.delete_node(15)
    bst.print_tree()








#task 3
def merge_sort(arr):
    if len(arr) > 1:
        mid = (len(arr)) // 2     
        l = arr[:mid]             
        r = arr[mid:]
        merge_sort(l)            
        merge_sort(r)            
        i=j=k=0
        #copy data to temp arrays l[] and r[]
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        #checking if any element was left
        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
    return arr
            
# print(merge_sort([8,1,2,5,7,0]))  
# print(merge_sort([89,119,20,5,7,9]))  



#task 4
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# print(insertion_sort([1,6,4,8,5,2,3]))
# print(insertion_sort([8,1,2,5,7,0]))  




#task 5

def count_sort(arr):
    s = len(arr)
    out = [0] * s
    count = [0] * 10
    for m in range(0, s):
        count[arr[m]] += 1

    for m in range(1, 10):
        count[m] += count[m - 1]

    m = s - 1
    while m >= 0:
        out[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1

    for m in range(0, s):
        arr[m] = out[m]
        
    return arr

# print(count_sort([8,1,2,5,7,0]))
# print(count_sort([1,6,4,8,5,2,3]))
    


                
            
                
                
            
            
            
            
 
        
        
        
        
        
        
        
        














