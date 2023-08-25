import functools

def main():
    #data = [5, 4, 9, 8, 13, 17, 12, 18]     #hardcoded input list which is predefined

    no = int(input("Enter Number of elements: "))    #accept no of elements to take as input
    data = [] 
    for i in range(no):                         #accept the list values from user
        num = int(input())
        data.append(num)
    
    print("Input Data: ", data)

    filter_output = list(filter(lambda no : (no % 2==0), data))  #directly giving lambda function to filter which makes lambda anonymous
    print("Output after Filter: ", filter_output)

    map_output = list(map(lambda no : (no + 2), filter_output))     #directly giving lambda function to filter which makes lambda anonymous
    print("Output after Map: ", map_output)

    reduce_output = functools.reduce(lambda A, B :  (A + B), map_output)         #directly giving lambda function to filter which makes lambda anonymous
    print("Output after Reduce: ", reduce_output)

if __name__ == "__main__":
    main()