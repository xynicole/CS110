#function that performs + operation
def addThem (num1, num2):
    return num1 + num2

def main():
    firstStr = input("please enter a whole number:  ")
    print("firstStr =", firstStr, "and is type", type(firstStr)) # for debug only
    secondStr = input("please enter another whole number:  ")
    print("secondStr =", secondStr, " and is type", type(secondStr)) # for debug(
    first = int(firstStr)
    print("firstStr =", firstStr, "and is type", type(firstStr)) # for debug only
    second = int(secondStr)
    print("secondStr =", secondStr, " and is type", type(secondStr)) # for debug(
    theSum =  addThem (first, second)
    print("The sum of your numbers is", theSum)
    print("The sum of your numbers is", addThem(first, second))
    
main()


    
