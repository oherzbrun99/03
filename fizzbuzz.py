fizzbuzz = []

start = int(input("Start Value:"))    #indicates to input start/end values
end = int(input("End Value:"))

for i in range(start,end+1):    #based on values inputted      
    entry = ''
    if i%3 == 0:
        entry += "fizz"
    if i%5 == 0:
        entry += "buzz"
    if i%3 != 0 and i%5 != 0:
        entry = i

    fizzbuzz.append(entry)

for i in fizzbuzz:         # 
    print(i)
    
# ref from
# https://codereview.stackexchange.com/questions/763/two-fizzbuzz-solutions
#simplest code I could find though it still doesn't make much sense to me