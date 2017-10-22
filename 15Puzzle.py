from utils import *
import math, random, sys, time, bisect, string
from search import *

class Puzzle15(Problem) :
    def __init__(self ,Matrix15,ch) :
        
        if(ch==1):
            Matrix15[0] = 2
            Matrix15[1] = 6
            Matrix15[2] = 5
            Matrix15[3] = 4
            Matrix15[4] = 1
            Matrix15[5] = 10
            Matrix15[6] = 0
            Matrix15[7] = 7
            Matrix15[8] = 9
            Matrix15[9] = 11
            Matrix15[10] = 3
            Matrix15[11] = 8
            Matrix15[12] = 13
            Matrix15[13] = 14
            Matrix15[14] = 15
            Matrix15[15] = 12
        
        else: 
            count=1
            while ( count <= 15 )  :      #random starting state
                i=random.randint(0,15)    #may be unsolvable/need a lot of time to be solved
                if (Matrix15[i] ==  0) :
                    Matrix15[i] = count
                    count +=1
                
        super(Puzzle15, self).__init__(tuple(Matrix15), None)

   
    
    
    
    def actions(self, state) :
        """ actions for the empty piece 0
            1 up, 2 down ,
            3 right , 4 left    
        """
        i = state.index(0)
        if ( i == 5 or i == 6 or i == 9 or i == 10) :  
            return [ 1 , 2 , 3 , 4]
        elif ( i == 1 or i == 2 ) :
            return [ 2 , 3, 4 ]
        elif ( i == 13 or i == 14 ) :
            return [ 1 , 3 ,4 ]
        elif ( i == 4 or i == 8 ) :
            return [1 , 2 , 3 ]
        elif ( i == 7 or i == 11 ) :    
            return [ 1 , 2 , 4 ]
        elif( i == 0) :
            return [ 2 ,3 ]
        elif( i == 3) :
            return [ 2 , 4 ]
        elif( i == 12) :
            return [ 1 , 3 ]
        elif( i == 15) :
            return [ 1 , 4  ]
              
            
        
    
    
    def result(self, state, action) :
    	""" changes current state according to
    		the action selected
    	"""
        i = action;
        k = state.index(0);
        newStateList = list(state)
        tmp=newStateList[k]
        if ( i == 1) :
            newStateList[k] = newStateList[k-4]
            newStateList[k-4]=tmp  
        elif ( i == 2 ) :
            newStateList[k] = newStateList[k+4]
            newStateList[k+4]=tmp  
        elif ( i == 3) :
            newStateList[k] = newStateList[k+1]
            newStateList[k+1]=tmp  
        elif ( i == 4 ) :
            newStateList[k] = newStateList[k-1]
            newStateList[k-1]=tmp              
        return tuple(newStateList)
        
        
    def goal_test(self, state) :
        """print state"""
        if (state[15]!=0) :
            return False
        else :
            for i in range(0,14) :
                if(state[i]!=i+1) :
                    return False
                else :
                    '''print "The puzzle has been solved"
                    print state;
                    return True'''
                    continue
            print "The puzzle has been solved"
            return True        
                
        
def h1(n):
    """ manhattan distance"""
    state = n.state
    i=0
    summ = 0
   
    while (i< 15) :
        y=0
        if state[i] !=i+1 :
            a=state.index(i + 1)
            k1 = i%4
            k2 = a%4
            y1 = abs(k2-k1)
            if i == 0:
                k1 = 0
            else :
                k1 = i /4 
            if a == 0:
                k2 = 0
            else :
                k2 = a /4 
            y2 = abs (k2-k1)       
            y =y1+y2
        i = i + 1
        summ= summ + y
    if ( state[15] != 0) :
        a = state.index(0)
        k1 = 15%4
        k2 = a%4
        y1 = abs(k2-k1)
        k1 = 15/4
        if a == 0:
            y2 = 1/ 4
        else :
            y2 = a /4 
        y2 = abs (y2 - k1)               
        y =y1+y2
        summ= summ + y   
    return summ  
   
    
        
        
def h2(n) :
    """ number of wrongly placed pieces/numbers"""
    state = n.state
    n = 1
    y=0
    while (n <= 14) :
        if (state[n]!=n) :
            y=y+1
        n = n + 1    
    if ( state[15]!=0 ) :
        y=abs(y+1)      
    return y            
        
         
        
def h3(n) :
    """ number of wrongly placed pieces/numbers in wrong column"""
    state = n.state
    i=0
    y=0
    while ( i <= 15) :
        if (state[i] % 4 != 0) :
            if (state[i]%4 - 1 != i%4 ) :
                y = y+ 1
        elif (state[i]%4 != i%4)  :
            y=y+1
        i = i + 1           
    return y       
        
        
        
        
#print p.initial, type(p.initial)
#for a in p.actions(p.initial) :
#    print p.result(p.initial, a)
ch=0
ch1=0
 
if ((len(sys.argv)!=2) or (sys.argv[1]!=1 and sys.argv[1]!=2 and sys.argv[1]!=3)):
    while(ch!=1 and ch!=2 and ch!=3):
        print "Select Heuristic Func (1,2,3)"
        print " 1. Manahattan Distance"
        print " 2. # of wrong placed pieces"
        print " 3. # of placed pieces in wrong column"
        ch = input()
else:
    ch=sys.argv[1]

while(ch1!=1 and ch1!=2):
        print "Select default or random puzzle (1,2)"
        print " 1. Default"
        print " 2. Random (may take a very long time to be solved)"
        ch1 = input()
   
p = Puzzle15([0 for x in range(16)],ch1)

if ch == "1" :
    solution = astar_search(p, lambda node : h1(node))
elif ch == "2" :  
    solution = astar_search(p, lambda node : h2(node))
else :
    solution = astar_search(p, lambda node : h3(node))     
l = list(solution.state)  
