"""

day_menu.py
Mohsin Rizvi
Last edited: 10/19/17
Defines the Day_Menu class.

"""
import requests as req
import json

# The Day_Menu class holds menus for Dewick and Carmichael for a given date.
class Day_Menu:

    # Purpose:    Get menus for Dewick and Carmichael for a given date.
    # Parameters: A datetime instance to give the day to check for.
    # Return:     Void
    def __init__(self, date):
        # TODO: Day_Menu should not initially load both, and should only
        #       load a hall when its data is requested by the user.
        self.dew = req.get("https://tuftsdiningdata.herokuapp.com/menus/" + 
                           "dewick/%d/%d/%d" %
                           (date.day, date.month, date.year)).json()
        self.carm = req.get("https://tuftsdiningdata.herokuapp.com/menus/" + 
                            "carm/%d/%d/%d" %
                            (date.day, date.month, date.year)).json()