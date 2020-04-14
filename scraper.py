import wikipediaapi as wiki
import wikipedia
import urllib.request

class Scraper(wiki.Wikipedia):
    def __init__(self, language='en'):
        super().__init__(language=language)

    def print_sections(self, sections, level=0):
            for s in sections:
                    print("%s: %s" % ("*" * (level + 1), s.title))
                    print_sections(s.sections, level + 1)

    def random_page(self):
        return wikipedia.random()

    def get_sections(self, sections, result=[]):
        for s in sections:
            result.append(s.title)
            result = self.get_sections(s.sections, result=result)
        return result

    def load_random_page(self, images=True, mind_sections=5):
        while 1:
           random_page = self.page(self.random_page()) 
           print(random_page.title)
           images = self.get_image_list(random_page.title)
           print(images)
           sections = self.get_sections(random_page.sections)
           print(sections)
           if len(sections) >= mind_sections:
               break
        return random_page

    def get_image_list(self, page_title):
        page = wikipedia.page(page_title)
        return page.images


    def download_images(self, image_list, max_images=10):
        if len(image_list < 10):
            image_list = image_list[:10]
        