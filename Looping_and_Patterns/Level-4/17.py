# Print pattern -> (A,BC,DEF,GHIJ,JKLMN)

n = int(input("Enter number of rows: "))

alpha = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"

CHAR = alpha.split(",")
count = 0

for i in range(1, n + 1):

	for j in range(i):
		print(CHAR[count], end = " ")
		count += 1

	print()

