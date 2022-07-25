class stack2:
    def __init__(s,n):
        s.n=n
        s.st=[None]*n
        s.top=-1
        
    def isfull(s):
        return s.top==s.n-1
        
    def push(s):
        if s.isfull():
            print("STACK IS FULL")
        else:
            s.top+=1
            x=int(input("Enter data : "))
            s.st[s.top]=x
    def display(s):
        for i in range (s.top+1):
            print(s.st[i])
    def pop(s):
        if s.top==-1:
            print("Stack is empty")
        else:
            print("The deleted element is : ",s.st[s.top])
            s.st[s.top]=None
            s.top-=1
    def exit(s):
        print("See u soon")
        
       
        
size=int(input("Enter the size of the stack : "))
s1=stack2(size)
while (1):
    print('''1-PUSH
    2-POP
    3-DISPLAY
    4-EXIT''')
    ch=int(input("Enter your choice : "))
    if ch==1:
        s1.push()
    elif ch==2:
        s1.pop()
    elif ch==3:
        s1.display()
    elif ch==4:
        break
    else:
        print("INVALID CHOICE:")
