CheckEven = lambda no : (no % 2==0)                   #cheking even odd without if-else 
Increase = lambda no : (no + 2)                             #lambda Function used for this code FMR
add = lambda A, B :  (A + B)

def filterX(Task, Elements):                               #task = NameofFucntion  ,  Elements == List of data elements
    result = []
    for no in Elements:                                    #user defined filter function
        if (Task(no)==True):
            result.append(no)
    return result

def mapX(Task, Elements):
    result = []
    for no in Elements:                                    #user defined Map function
        Ret = Task(no)
        result.append(Ret)
    return result

def reduceX(Task, Elements):
    Sum = 0
    for no in Elements:                                    #user defined Reduce function
        Sum = Task(Sum, no)
    return Sum

def main():
    no = int(input("Enter Number of elements: "))    #accept no of elements to take as input
    data = [] 
    for i in range(no):                         #accept the list values from user
        num = int(input())
        data.append(num)
    
    print("Input Data: ", data)

    filter_output = list(filterX(CheckEven, data))
    print("Output after Filter: ", filter_output)

    map_output = list(mapX(Increase, filter_output))
    print("Output after Map: ", map_output)

    reduce_output = reduceX(add, map_output)
    print("Output after Reduce: ", reduce_output)

if __name__ == "__main__":
    main()


#Completly user defined FMR functions and Lambda