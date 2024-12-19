#Cone defined in a standard form, assuming one generator is e_2 and the other generator of the cone is m e_1 -k e_2 where k and m are relatively prime and 0 <= k < m. 
#Lattice is assumed to be free integral module generated by standard basis vectors e_1 and e_2. 
#This program will be refined later when I have installed numpy packages. But for now the user has to input two integers in the standard form and we create a list out of it.
m = int(input("Enter the first co-ordinate of the second generator of the cone: "))
k = int(input("Enter the second co-ordinate of the second generator of the cone: "))
print(f"( {m}, {-k})")
while k!= 0:
    for k_1 in range(k):
        a_1 = (m + k_1)/k
        if a_1.is_integer() and a_1 >=2 :
            m = k
            k = k_1
            print(f"( {m}, {-k} )")
print(f"( 0 , 1 )")


