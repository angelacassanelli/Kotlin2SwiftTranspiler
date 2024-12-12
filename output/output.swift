class Person() {
var name: String
var age: Int
init(name: String, age: Int) {
self.name = name
self.age = age
}
func greet() {
print("Hello!")
print(name)
}
func main() {
var i : Int = 1
for i in 1 ... 5 {
greet()
}
}
}