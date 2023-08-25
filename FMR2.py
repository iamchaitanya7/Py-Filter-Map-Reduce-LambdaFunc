from functools import reduce

def CheckEven(no):
    if (no % 2==0):
        return True
    else:
        return False

def Increase(no):
    return no + 2

def add(A, B):
    return A + B

def main():
    #data = [5, 4, 9, 8, 13, 17, 12, 18]     #hardcoded input list which is predefined

    no = int(input("Enter Number of elements: "))    #accept no of elements to take as input
    data = [] 
    for i in range(no):                         #accept the list values from user
        num = int(input())
        data.append(num)
    
    print(data)

    filter_output = list(filter(CheckEven, data))
    print(filter_output)

    map_output = list(map(Increase, filter_output))
    print(map_output)

    reduce_output = reduce(add, map_output)
    print(reduce_output)

if __name__ == "__main__":
    main()

#program to check even odd using filter map reduce and performing the addition of this even no
