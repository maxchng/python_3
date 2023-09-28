from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def get_eyes(self):
        """Return eye value"""
        return self.eyes

    def get_hairs(self):
        """Return hair value"""
        return self.hairs

    def set_eyes(self, value):
        """Set eye value"""
        self.eyes = value

    def set_hairs(self, value):
        """Set hair value"""
        self.hairs = value
