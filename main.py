import random
def Array():
    return [random.randint(0,1000)for i in range(100)]
def lineSearch(n):
    array=Array()
    for index in array:
        try:
            if array[index]==n:
                return index
        except:
            return "There doesn't exist this number!"
if __name__=="__main__":
    print(lineSearch(10))