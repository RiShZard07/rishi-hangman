import random
import time

def main():
    # gets input from user for size of the list
    number = int(input("N: "))
    # creates list of random numbers from -500 to 500
    original_list = []
    for i in range(number):
        num = random.randrange(-500, 501)
        original_list.append(num)
    # makes copy of the original list
    unsorted_list = original_list[:]
    sorted_list = []
    print("Original list (first 20 elements):")
    # prints the first 20 numbers from original list
    print(original_list[:20])
    # starts the timer for the entire sort duration
    start = time.time()
    # starts doing the selection sort, removing the smallest value and adding it to new sorted list continuosly
    for i in range(number):
        y = min(unsorted_list)
        unsorted_list.remove(y)
        sorted_list.append(y)
    # stops the timer and calculates the total duration through stop - start
    stop = time.time()
    print("Time to sort:", stop - start)
    print("Sorted list (first 20 elements):")
    # prints first 20 elements of sorted list
    print(sorted_list[:20])

main()

"""
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject7 % python3 main.py 
N: 5
Original list (first 20 elements):
[-65, 195, -111, 76, -122]
Time to sort: 4.410743713378906e-05
Sorted list (first 20 elements):
[-122, -111, -65, 76, 195]
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject7 % 
"""

"""
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject7 % python3 main.py 
N: 10
Original list (first 20 elements):
[-111, 248, -212, 23, -264, -85, 92, -380, -271, 39]
Time to sort: 1.0251998901367188e-05
Sorted list (first 20 elements):
[-380, -271, -264, -212, -111, -85, 23, 39, 92, 248]
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject7 %
"""

"""
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject7 % python3 main.py
N: 50
Original list (first 20 elements):
[-450, 206, 26, 316, -10, 72, 272, 304, -476, -107, -184, 40, -29, -288, -75, 211, -61, -401, 193, -42]
Time to sort: 3.719329833984375e-05
Sorted list (first 20 elements):
[-498, -485, -476, -450, -448, -401, -351, -323, -306, -288, -284, -274, -216, -184, -127, -107, -105, -87, -75, -73]
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject7 % 
"""

"""
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject7 % python3 main.py
N: 500
Original list (first 20 elements):
[-131, 117, 65, -165, -170, -9, -390, -130, -494, 63, -372, 99, -309, -380, -175, -153, 424, 331, -333, -487]
Time to sort: 0.003159046173095703
Sorted list (first 20 elements):
[-499, -498, -497, -497, -496, -496, -494, -491, -490, -488, -487, -485, -484, -483, -483, -478, -477, -477, -471, -468]
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject7 %
"""

"""
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject7 % python3 main.py
N: 5000
Original list (first 20 elements):
[-191, -468, 43, -256, 102, 277, -449, -246, 101, -443, 498, -198, -99, 426, -400, 287, -401, 177, 264, -183]
Time to sort: 0.1721348762512207
Sorted list (first 20 elements):
[-500, -500, -500, -500, -500, -500, -499, -499, -499, -499, -499, -499, -499, -499, -499, -499, -498, -498, -498, -498]
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject7 % 
"""

"""
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject7 % python3 main.py
N: 50000
Original list (first 20 elements):
[216, 146, -36, -177, 317, -419, 254, -36, 292, -187, 309, 125, 491, -346, -28, -342, -167, -44, 447, -409]
Time to sort: 15.5903799533844
Sorted list (first 20 elements):
[-500, -500, -500, -500, -500, -500, -500, -500, -500, -500, -500, -500, -500, -500, -500, -500, -500, -500, -500, -500]
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject7 % 
"""

"""
the time to sort is increasing quadratically O(n2), based on the size of N(input list), if it is smaller then 
it is quicker time, if it is larger then longer time, when N = 50000 it took a while for everything to be sorted
this is probably because it takes longer to find the next minimum value continuosly in a much longer list 
"""
