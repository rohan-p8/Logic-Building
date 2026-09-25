# Print pattern -> (A,BC,DEF,GHIJ)

n = int(input("Enter number of rows: "))

alpha = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"

CHAR = alpha.split(",")
char = "A"

for i in range(1, n + 1):

	for j in range(i):
		print(char, end = " ")
		char ++

	print()

