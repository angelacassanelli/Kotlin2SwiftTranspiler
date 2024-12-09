from enum import Enum

class KotlinTypes(Enum):
    """
    KotlinTypes(Enum):
        An enumeration representing Kotlin data types.

        Members:
            INT (str): Represents the Kotlin 'Int' type.
            STRING (str): Represents the Kotlin 'String' type.
            BOOLEAN (str): Represents the Kotlin 'Boolean' type.
    """

    INT = "Int"
    STRING = "String"
    BOOLEAN = "Boolean"


class SwiftTypes(Enum):
    """
    SwiftTypes(Enum):
        An enumeration representing Swift data types.

        Members:
            INT (str): Represents the Swift 'Int' type.
            STRING (str): Represents the Swift 'String' type.
            BOOLEAN (str): Represents the Swift 'Bool' type.
    """

    INT = "Int"
    STRING = "String"
    BOOLEAN = "Bool"