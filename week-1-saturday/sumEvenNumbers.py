print("this is the second activity of this week")


def sum_of_even_number():
    n=input("Provide the number you want the even sum upto:")
    num=int(n)
    if(num<=0):
        print("Please provide the positive integer")
    
    sum=0
    for i in range(1,num+1):
        if(i%2==0):
            print(i)
            sum+=i
    return sum
    
if __name__ == "__main__":
   result= sum_of_even_number()
   print(f"Final sum is {result}")
