#!/usr/bin/python
#import pi
import sys
l=3.1415926535897931159979634685441852
def pi(n):
  pi=0
  
  for i in range (1,n+1):
    x=(i-.5)/ float (n)
  #print x
    fx=4/(1+(x*x))
  #print fx  
    pi=pi+(fx)/n
    #print 'subintervalo: [%3.2f,%3.2f] x: %f fx: %6.5f ' % ((i-1)/float(n),i/float(n), x, fx)
  return pi
if (__name__=="__main__"):
  if(len(sys.argv)==3):
    n=int(sys.argv[1])
    veces=int(sys.argv[2])
  else:
    print 'la longitud no es correcta'
    n=0;
    veces=0;
k=[]
i=1
print      'i           pi35                      Lista i                    pi35 - lista i'  
for i in range(1,veces+1):  
  s=pi(i*n)
  print   '%i           %.10f              %.10f               %.10f'  %(i,l,s,s-l)      
  n=n+1
  k=k+[s]
print 'la lista de las aproximaciones es:'
print k