# manages the room the player can move around in
class Room():
    def __init__(self, title, text, top_exit=None, bottom_exit=None, left_exit=None, right_exit=None):
        self.title = title
        self.text = text
        self.top_exit = top_exit
        self.bottom_exit = bottom_exit
        self.left_exit = left_exit
        self.right_exit = right_exit
        self.enemies = []
        self.items = []
        self.cleared = False
        self.boss = False

#spawns enemies and items into the room
    def spawn(self):
        pass