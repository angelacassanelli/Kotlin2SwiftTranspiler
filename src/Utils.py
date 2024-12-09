from Types import *

"""
KOTLIN_2_SWIFT_TYPES:
    A dictionary mapping Kotlin data types to their equivalent Swift types.

    Keys:
        KotlinTypes.INT: Corresponds to the Swift type SwiftTypes.INT.
        KotlinTypes.STRING: Corresponds to the Swift type SwiftTypes.STRING.
        KotlinTypes.BOOLEAN: Corresponds to the Swift type SwiftTypes.BOOLEAN.

"""

KOTLIN_2_SWIFT_TYPES = {
    KotlinTypes.INT: SwiftTypes.INT,
    KotlinTypes.STRING: SwiftTypes.STRING,
    KotlinTypes.BOOLEAN: SwiftTypes.BOOLEAN
}


"""
RESERVED_KEYWORDS:
    A set of keywords and symbols reserved in Kotlin and Swift. These keywords are not allowed 
    to be used as variable or function names in either language.

    Contains:
        Common keywords like "if", "else", "for", "class", "fun", "return", etc.
        Operators such as "+", "-", "*", "/", "%", and comparison operators like "==", ">", "<", etc.
        Brackets and punctuation like ",", ";", ":", ".", "(", ")", "{", "}", "[", "]", etc.
"""

RESERVED_KEYWORDS = {
    "readLine", "println", "val", "var", "Boolean", "Int", "String", 
    "if", "else", "for", "class", "fun", "return", "true", "false", 
    "+", "-", "*", "/", "%", "=", "==", "!=", ">", ">=", "<", "<=",
    ",", ";", ":", ".", "(", ")", "{", "}", "[", "]", "&&", "||",
    "!", "..", "\"", "\'"
}


