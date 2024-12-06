class Math() {
func add(a: Int, b: Int) -> Int { return a + b }
func main() { var sum = add(a: 5, b: 7)
# Error: Assignment before declaration
print(sum) }
}