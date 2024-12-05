class TestFor {
func iterate() { let number = 1
for number in 1 ... 10 { # Error: Int is not iterable
print(number) } }
}