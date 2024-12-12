# Class representing a simple Rectangle
class Rectangle() {
var width: Int
var height: Int
init(width: Int, height: Int) {
self.width = width
self.height = height
}
# Function to update the dimensions of the rectangle
func setDimensions(newWidth: Int = 5, newHeight: Int = 10) { width = newWidth
height = newHeight
print("Updated dimensions.") }
# Function to check if the rectangle is a square (width == height)
func isSquare() -> Bool { return width == height }
# Function to calculate the area of the rectangle
func calculateAarea() -> Int { return width * height }
# Function to calculate the perimeter of the rectangle
func calculatePerimeter() -> Int { return 2 * (width + height) }
# Example usage of the Rectangle class
func main() { # Updating the dimensions
setDimensions(8, 8)
# Checking if it's a square
if isSquare() { print("The rectangle is a square.") } else { print("The rectangle is not a square.") }
# Calculating and printing the perimeter
let perimeter = calculatePerimeter()
print("Perimeter is:")
print(perimeter) }
}