class calculator:
    """Calculator for ex04"""
    def __init__(self, V1, V2):
        """Constructor"""
        self.V1 = V1
        self.V2 = V2

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Multiply and sum it"""
        print("Dot product is: ", end="")
        print(sum([V1[i] * V2[i] for i in range(len(V1))]))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add 2 vectors"""
        print("Add vector is : ", end="")
        print([float(V1[i]) + float(V2[i]) for i in range(len(V1))])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract 2 vectors"""
        print("Sous vector is: ", end="")
        print([float(V1[i]) - float(V2[i]) for i in range(len(V1))])
