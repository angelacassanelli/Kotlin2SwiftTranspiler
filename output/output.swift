# Class representing a simple Rectangle
class Rectangle() {
var width: Int
var height: Int
init(width: Int, height: Int) {
self.width = width
self.height = height
}
# Semantic Error: variable 'depth' not declared
# Semantic Error: variable 'width' already declared
func calculateAarea() -> Int { let width = 10
return width * height * depth }
# Semantic Error: function 'printDimensions' not declared
func main() { printDimensions() }
}