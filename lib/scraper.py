import wikipediaapi as wiki
import wikipedia

class Scraper(wiki.Wikipedia):
    def __init__(self, language='en'):
        super().__init__(language=language)

    def print_sections(self, sections, level=0):
            for s in sections:
                    print("%s: %s" % ("*" * (level + 1), s.title))
                    print_sections(s.sections, level + 1)

    def random_page(self):
        return wikipedia.random()