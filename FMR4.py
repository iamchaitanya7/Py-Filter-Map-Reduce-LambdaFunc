#Unnamed Function (Lambda Function)
# Name = lambda Parameters_list : Functions_logic

def Add(no1, no2):
    return no1 + no2

AddX = lambda no1, no2 : no1 + no2    #lambda function for addition 

def CheckEven(no):
    return (no % 2 == 0)

CheckEvenX = lambda no : (no % 2 == 0)        #lambda function for CheckEvenOdd 

def Increase(no):
    return no + 2

IncreaseX = lambda no : (no + 2)             #lambda function for addition of no by 2

def main():
    no1 = int(input("Enter a First Number: "))
    no2 = int(input("Enter a Second Number: "))
 
    print(Add(no1, no2))                   #calling the normal Add function
    print(AddX(no1, no2))                  #calling the Lambda Add function

    print(CheckEven(no1))                #calling the normal Checkeven function
    print(CheckEvenX(no1))               #calling the Lambda Checkeven function

    print(Increase(no1))                #calling the normal Increase function
    print(IncreaseX(no1))               #calling the Lambda Increase function

if __name__ == "__main__":
    main()