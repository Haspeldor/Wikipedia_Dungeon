from room import Room
from scraper import Scraper

class Level():
    def __init__(self, page_name=None):
        self.rooms = []
        self.load_page(page_name)
        self.load_rooms()

# loads in the requested page
    def load_page(self, page_name=None):
        self.scraper = Scraper()
        if page_name:
            self.page = self.scraper.page(page_name)
        else:
            self.page = self.scraper.load_random_page()
        if not self.page.exists():
           self.page = self.scraper.page("Wikipedia")
        
# is called to generate a room structure 
    def load_rooms(self):
        self.starting_room = Room(self.page.title, self.page.summary)
        self.rooms.append(self.starting_room)
        if self.page.sections:
            self.starting_room.bottom_exit = self.load_room(self.page.sections, 0, top_exit=self.starting_room)

# is called by the main function, to recursively create
    def load_room(self, sections, number, top_exit=None, left_exit=None):
        section = sections[number]
        room = Room(section.title, section.text, top_exit=top_exit, left_exit=left_exit)
        if number + 1 < len(sections):
            room.right_exit = self.load_room(sections, number + 1, top_exit=top_exit, left_exit=room)
        if len(section.sections) > 0:
            room.bottom_exit = self.load_room(section.sections, 0, top_exit=room)
        self.rooms.append(room)
        return room
