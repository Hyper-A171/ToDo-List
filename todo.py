print(" 1) Add Todo\n 2) Remove Todo \n 3) View All Todo \n press q to exit")
num = (input())
list = []
i = 1
while i <= 15:
    if i >= 6:
        print(" 1) Add Todo\n 2) Remove Todo \n 3) View All Todo \n press q to exit")
        num = (input())
    if num == "1" :
        list.append(input())
        print(list)
    elif num == "2" :
        list.remove(input())
        print(list)
    elif num == "3" :
        print("View All List :-")
        print(list)
    elif num == "q":
        print("Thankyou")
        break
    else :
        print("Not Found")
    i +=1 

    

