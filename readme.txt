Program 9
Sorting Implementation and Comparison
In this assignment you are going to implement several sort
algorithms (Bubble Sort, Selection Sort, and Quick Sort). After
implementing these sort algorithms, you will analyze/compare their
performance and complexity by plotting/graphing this information.
Functions:
Your sorting algorithms will be implemented as functions using this
template:
def bubble_sort(array):
pass
def selection_sort(array):
pass
def quick_sort(array):
pass
You will also implement a function which will create an array of
random integers whose value is in the range of 0 to 50000. A call
to this function will look like:
new_array = create_array(size)
Implementing the 3 sort algorithms:
This is the first time I am every trying the following approach to a
programming assignment. Often, in the "real world", when solving a
programming problem, you will search for similar code and then
modify it to meet your needs. I am going to give you code to use
for each of the 3 searches we are looking at. You can take that
code and build the functions around it and add the complexity
tracking code.
For the plotting, I am going to give you sample code to demonstrate
the use of the matplotlib library that you can modify to meet your
needs for this program.
Information related to bubble_sort(array)
The code to start with that implements a bubble sort is:
===== bubble sort code =====
n = len(array)
# Traverse through all array elements
for i in range(n):
swapped = False
# Last i elements are already in place
for j in range(0, n-i-1):
# Traverse the array from 0 to n-i-1
# Swap if the element found is greater
# than the next element
if array[j] > array[j+1]:
array[j], array[j+1] = array[j+1], array[j]
swapped = True
if (swapped == False):
break
===== end of bubble sort code =====
For the measure of complexity for the bubble sort, add code that
counts the number of comparisons and swaps that occur.
Information related to selection_sort(array)
The code to start with that implements a selection sort is:
===== selection sort code =====
n = len(array)
# Traverse through all array elements
for i in range(n):
# Find the minimum element in remaining
# unsorted array
min_idx = i
for j in range(i+1, n):
if array[min_idx] > array[j]:
min_idx = j
# Swap the found minimum element with
# the first element
array[i], array[min_idx] = array[min_idx], array[i]
===== end of selection sort code =====
For the measure of complexity for the selection sort, add code that
counts the number of comparisons and swaps that occur.
Information related to quick_sort(array)
The code to start with that implements a quick sort is:
===== quick sort code =====
## We define our 3 arrays
less = []
equal = []
greater = []
## if the length of our array is greater than 1
## we perform a sort
if len(array) > 1:
## Select our pivot. This doesn't have to be
## the first element of our array
pivot = array[0]
## recursively go through every element
## of the array passed in and sort appropriately
for x in array:
if x < pivot:
less.append(x)
if x == pivot:
equal.append(x)
if x > pivot:
greater.append(x)
## recursively call quicksort on gradually smaller and
## smaller arrays until we have a sorted list.
return quicksort(less)+equal+quicksort(greater)
else:
return array
===== end of quick sort code =====
For the measure of complexity for the quicksort, add code that
counts the number of recursive calls and every time you place a
value into the appropriate array. Since you are solving this with a
recursive function, any function that uses your complexity counter
variable, it will need to be declared as global.
Timing Code Execution
You can get "wall clock time" and "CPU time" using function in the
time library. To make use of the time library you must:
import time
Then you would code that looks like this:
wall_start = time.time()
cpu_start = time.process_time()
#### Insert here the code you want to time ####
wall_end = time.time()
cpu_end = time.process_time()
wall_time = wall_end - wall_start
cpu_time = cpu_end - cpu_start
Plotting / Graphing
Your program should produce a graphic that looks like this:
This will be done using the matplotlib library. I will provide you
with code, execution_times.py, that brute force generates this
graph. Your program will need to gather this information and plug
your results into dictionaries that store this information and then
graph your results.
Other Misc. Information
• This program uses recursion and the default recursion limit will
not be enough for you to run some of the larger sorts. To "fix"
this you will need to "import sys" and then place this line of
code in your program:
sys.setrecursionlimit(6000)
• In Blackboard, as part of this programming assignment, there will
be a file named code_segments.txt that has code that I have shown
and/or discussed in this assignment.
• Normally when you create a graph you could call
fig.show()
to display your graph to the screen. Since you will be writing
this program on the grace server, instead of the show() function
you will be calling the savefig() function to create a PNG file
which contains your graphic. The call to do this is shown in the
code segments file and looks like:
fig.savefig('graphs.png')
Once the file is saved, you will need to use SFTP (either a local
SFTP client on your machine or the VPN web gateway) to copy the
file to your local machine and then open it there.
Main Program Output to the User
The output of your main program should look like the following but
should have the output repeated for each size array you are
processing:
Creating an array of size 1000
*** Bubble Sort ***
Execution time: 0.04690127299999999 milliseconds
Wallclock time: 0.04691600799560547 seconds
Complexity: 743519
*** Selection Sort ***
Execution time: 0.023277274 milliseconds
Wallclock time: 0.02327704429626465 seconds
Complexity: 500500
*** Quicksort (Recursive) ***
Execution time: 0.037617359 milliseconds
Wallclock time: 0.03761720657348633 seconds
Complexity: 460913
Submission Guidelines:
Your submission document should include, in the order given here:
- The code of your program
- The output of executing your code
- The graphic that your program produced