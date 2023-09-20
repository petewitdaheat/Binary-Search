from serialsearch import *

def main():
        # set up local variables to store the list, first, size, and target
    i = 0
    a = ['E', 'B', 'E', 'F', 'A', 'F', 'C']
    list2 = ['E', 'B', 'E', 'F', 'A', 'F']
    first = 0
    size = len(a)
    target = a[i]
    identical = True

    if size != len(list2):
        print("The two lists aren't strictly identical!")
    else:
        for i in range(size):
            search(a, first, size, target)
            if a[i] != list2[i]:
                print("The two lists aren't strictly identical!")
                identical = False
                break
            
    if i == (size - 1) and identical != False:
        print("The two lists are strictly identical!")  

    print(a)
    print(list2)  

if __name__ == '__main__':
    main()