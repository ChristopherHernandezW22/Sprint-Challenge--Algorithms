#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
assign a to 0, and for each input of 'n', the runtime will increase by that number.


b) O(n*log n)
The loop is a straight O(n) runtime, because it runs for equal to the number in a given input range (n).

The nested while loop runs while j < n. j gets multiplied by 2 each time, halving the total amount of iterations, leading to O(log n)

Since the while loop grows lower than the proportional increase in the input size, we assume O(log n) for that part.


c) O(n)
The function will run a number of times equal to the input amount given in 'bunnies', resulting in O(n) n equals the amount of bunnies passed in.


## Exercise II

get break_point = n // 2

Test eggs breaking at break_point

If egg breaks, take lower half of the array, find halfway point and repeat

If egg doesn't break, take upper half of array, find halfway point and repeat.

Repeat the process until you only move in one direction by one spot. If the egg breaks, and you move one spot down and the egg doesn't break.. The previous spot is 'f'.

If the egg doesn't break and you move up one and it does break, that last one is your 'f'

Since we are halving every time, the runtime complexity would be O(log n)

n would represent the amount of floors