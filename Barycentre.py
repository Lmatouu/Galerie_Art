class Barycentre():


    def __init__(self,A1,A2,B1,B2):
        self.A1 = A1
        self.A2 = A2
        self.B1 = B1
        self.B2 = B2
    
    def __str__ (self):
        I=self.barycentre()
        if I == [99999,99999]:
            return f'Les droites passant par ({self.A1};{self.A2}) et ({self.B1};{self.B2}) sont parralleles'
        else:
            return f'Les droites passant par ({self.A1};{self.A2}) et ({self.B1};{self.B2}) sont sécantes en {I}.'
    
    def determinant(self,M,N,P):
        return (M[0]-P[0])*(N[1]-P[1])-(M[1]-P[1])*(N[0]-P[0])


    def barycentre(self):
        I=[0,0]
        if self.A1[0]-self.A2[0] == 0 or self.B1[0]-self.B2[0] == 0 :
            if (self.determinant(self.B1,self.B2,self.A2)+self.determinant(self.B2,self.B1,self.A1)) != 0 :
                I[0]=float("{:.4f}".format((self.determinant(self.B1,self.B2,self.A2)*self.A1[0]+self.determinant(self.B2,self.B1,self.A1)*self.A2[0])/(self.determinant(self.B1,self.B2,self.A2)+self.determinant(self.B2,self.B1,self.A1))))    #permet d'avoir 4 chiffres apres la virgule
                I[1]=float("{:.4f}".format((self.determinant(self.B1,self.B2,self.A2)*self.A1[1]+self.determinant(self.B2,self.B1,self.A1)*self.A2[1])/(self.determinant(self.B1,self.B2,self.A2)+self.determinant(self.B2,self.B1,self.A1))))
            else:
                I=[99999,99999]
        else:
            a=(self.A1[1]-self.A2[1])/(self.A1[0]-self.A2[0])
            b=(self.B1[1]-self.B2[1])/(self.B1[0]-self.B2[0])
            if a==b:
                I=[99999,99999]
            else:
                x=float("{:.4f}".format((self.B1[1]-self.A1[1]+a*self.A1[0]-b*self.B1[0])/(a-b)))
                y=float("{:.4f}".format(a*x+self.A1[1]-a*self.A1[0]))
                I=[x,y]
        return I