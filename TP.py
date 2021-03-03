import numpy as np
import random as rd


#-----Question 1-----#

     
def ReductionGauss(Aaug):          #On applique le pseudo-code donné en cours au format Python 
    
    n,m=Aaug.shape
    
    for k in range (n-1):
        pivot=Aaug[k,k]
        
        if (pivot==0):
            print('le pivot est nul')
            
        elif (pivot!=0):
            
            for i in range(k+1,n):  
                Aaug[i,:]=Aaug[i,:]-(Aaug[i,k]/pivot)*Aaug[k,:]

    return(Aaug)


A=np.array([[1,5,12],
            [4,11,9],
            [-2,-8,7]])

print(ReductionGauss(A))

#-----Question 2------#

def ResolutionSystTriSup(Taug):
    #Taug=ReductionGauss(Taug)        #Au cas ou la matrice ne serait pas reduite 
    n,m=Taug.shape                    # Mesure de la Matrice de taille n,m
    X=[0]*n                           # on pose un vecteur colonne de taille n
    

    for i in range(n-1,-1,-1):
        X[i]=Taug[i][n]               # On initialise les valeurs du vecteur colonne par la méthode de la remontée

        for j in range(i+1,n):        # On applique ensuite le théorème mathématique 'par récurrence descendante' 
            X[i]=X[i]-Taug[i][j]*X[j]
        X[i]=X[i]/Taug[i][i]
    return(X)


#-----Question 3-----#
def Gauss(A,B):
    n,m=A.shape
    C = np.array([],[],[])
    for i in range (n):
        C.append(A,B,axis=1)      # Rajout du vecteur colonne B à la matrice carré A pour avoir Aaug  
        
    C=ReductionGauss(C)
    
    C=ResolutionSystTriSup(C)
    
    return (C)
    
    
C=np.array([[2,5,6],
            [4,11,9],
            [-2,-8,7]])
D=np.array([[7],
            [12],
            [3]])
print (Gauss(C,D))               #test



A = np.array([[],[],[]])

for i in range(0,10) :
    a = rd.random()
    A[0,i].append(a)

for i in range(0,10) :
    a = rd.random()
    A[1,i].append(a)

for i in range(0,10) :
    a = rd.random()
    A[2,i].append(a)


B = np.array([1],
             [2],
             [3])

print("A =\n",A,"--------")
I =  identity(3, int)
print("I =\n",I,"-----")


#print("A initiale :\n",A,"\n------")
#compteur = 0

#A = ReductionGauss(Aaug)
#print("\nA terminée :\n",A)

