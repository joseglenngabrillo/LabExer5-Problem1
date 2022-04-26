#Problem NO 1

id=[]
n=[]
a=[]
r=[]
def encode():
    print("ID:")
    ID = int(input())
    id.append(ID)
    print("Name:")
    name = str(input())
    n.append(name)
    print("Quiz 1")
    Q1 = int(input())
    print("Quiz 2")
    Q2 = int(input())
    print("Quiz 3")
    Q3 = int(input())
    ave = (Q1 + Q2 + Q3) / 3
    a.append(ave)
    if ave >= 75:
        r.append("Passed")
    else:
        r.append("Failed")
def check():
    print("ID:")
    Id=int(input())
    if Id in id:
        I=id.index(Id)
        print("Name: ", n[I])
        print("Grades: ", a[I])
        print("Remarks: ", r[I])
        input()
    else:
        print("ID does not exist")
        
    while True:
        print("[1] - Enter grades", "\n[2] - Check grades")
        print("Enter your choice:")
        choice=int(input())
        if choice ==1:
            print ("Enter Student Record:")
            encode()
        if choice ==2:
            print ("Student Record:")
            check()

