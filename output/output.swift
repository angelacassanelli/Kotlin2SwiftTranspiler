class Example() {
let isCitizen = true
let age = 18
let hasPermanentResidency = false
let canVote : Bool = isCitizen || (age >= 18 && hasPermanentResidency)
}