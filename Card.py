class Card:
    def __init__(self, number):
        self.number = number
        self.dimensions = (6, 5)

    def get_representation(self, show_number=True):
        """
        Cards look like this:
         ____
        |   2|
        |    |
        |    |
        |____|
        """
        character_to_show = str(self.number) if show_number else "*"
        representation = " ____\n|  {:>2}|\n|    |\n|    |\n|____|".format(character_to_show)
        return representation
