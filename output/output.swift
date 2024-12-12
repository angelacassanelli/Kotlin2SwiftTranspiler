# Class representing a simple Counter
class Counter {
# Variable to store the current value of the counter.
var count : Int = 0
# Function to increment the counter by 1.
# Function to reset the counter to 0.
# Function to check if the counter value is even.
# Returns true if even, false otherwise.
func checkIfEven() -> Bool { print("Check if counter is even")
return count % 2 == 0 }
/* Function to test the counter's behavior:
    1. Resets the counter;
    2. Increments the counter 5 times;
    3. Checks if the counter value is even or odd;
    4. Prints the result;
    5. Returns a string "Even" or "Odd" based on the result. */
func checkEvenOrOdd() -> String { reset()
var i : Int = 1
for i in 1 ... 5 { increment() }
let isEven : Bool = checkIfEven()
if isEven { print("Counter is even")
return "Even" } else { print("Counter is odd")
return "Odd" } }
}