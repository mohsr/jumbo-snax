"""

setting.py
Mohsin Rizvi
Last edited: 10/19/17
Defines the Setting class.

"""

# The Setting class holds a dining hall code and a meal time code.
class Setting:

    # Purpose:    Create a Setting instance with a given dining hall code
    #             and meal time code.
    # Parameters: A dining hall code, which is a string that is "d" for
    #             Dewick, "c" for Carmichael, or "b" for both, and a meal
    #             time code, which is either "b" for breakfast, "l" for
    #             lunch, or "d" for dinner.
    def __init__(self, hall, meal):
        self.hall = hall
        self.meal = meal