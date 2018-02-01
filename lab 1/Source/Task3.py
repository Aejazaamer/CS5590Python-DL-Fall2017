def find_triplets(m, n):            #creating a function to find triplets for a given sequence of number
    value = True
    for i in range(0, n - 2):       #iterating i from o to n-2

        for j in range(i + 1, n - 1):   #iterating j in i

            for k in range(j + 1, n):   #iterating k in j

                if (arr[i] + arr[j] + arr[k] == 0):     #arr is array of all values of i
                    print(arr[i], arr[j], arr[k])

number = input('enter your list:')
arr = list(map(int, number.split()))
n = len(arr)
find_triplets(arr, n)
