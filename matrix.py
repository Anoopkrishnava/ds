# 1 read num of rows and cols for m1 
# 2 create m1 
# 3 read num of r and c for m2  & create m2
# find dot product , transpose of m1 and m2 , trace of m1 and m2 , 
#  find rank of m1 and m2, find determinant of m1 and inverse of m2.

r1,c1 = map(int,input("Enter number of rows and cols: ").split())
m1 = []

for i in range(r1):
    rows = []
    for j in range(c1):
        el=int(input("Enter the elements :"))
        rows.append(el)
    m1.append(rows)

for row in m1:
    print(row)

# creating m2

r2,c2 = map(int,input("Enter rows and cols for m2 :").split())
m2 = []
for i in range(r2):
    rows = []
    for j in range(c2):
        el = int(input("Enter the elements :"))
        rows.append(el)
    m2.append(rows)
for rows in m2:
    print(rows)

