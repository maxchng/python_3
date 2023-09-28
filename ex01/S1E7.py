from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Default attribute for beratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Change is_alive status to False"""
        self.is_alive = False

    def __str__(self):
        """When str function is called on this object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string representation of an object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    def __init__(self, first_name, is_alive=True):
        """Default attribute for beratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Change is_alive status to False"""
        self.is_alive = False

    def __str__(self):
        """When str function is called on this object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string representation of an object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Class method for lannister"""
        return cls(first_name, is_alive)
