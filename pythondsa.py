def search(array, key):
    for i in range(len(array)):
        if key == array[i]:
            print("Element is found at ",i)
            break
    else:
        print("Elemnt is not found")


array = [1,2,3,4,56,7,9]
key = int(input("Enter your desired Number"))

search(array,key)