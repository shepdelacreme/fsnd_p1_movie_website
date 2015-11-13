import media
import yaml
import webbrowser
import os
from jinja2 import Environment, FileSystemLoader


class MediaCenter():

    def __init__(self, datafile="data/media.yml"):
        # Open the input media yaml file and process it
        with open(datafile, 'r') as f:
            self.mediadata = yaml.safe_load(f)
        # Get different types of media from file
        if self.mediadata['movies']:
            self.movies = self.get_media('movies')
        # Setup the Jinja2 template env
        self.env = Environment(loader=FileSystemLoader('templates'))
        # Render pages
        self.rendered_files = self.render_pages()

    def run(self):
        # Open the rendered files
        for page in self.rendered_files:
            webbrowser.open('file://' + os.path.realpath(page))

    def get_media(self, mediatype):
        '''
        Loop through the list of media from the
        yaml file and return a list of objects
        '''
        # Placeholder list for media items
        items = []
        # Loop through the list
        for item in self.mediadata[mediatype]:
            if mediatype == 'movies':
                items.append(media.Movie(item['title'], item['storyline'],
                             item['year'], item['poster_id'], item['trailer_id']))
        # Return the list of media objects
        return items

    def render_pages(self):
        '''
        Render all the various pages we need for the site
        and return the list of files
        '''
        # Placeholder for list of files
        rendered_pages = []
        # Make sure the media data file contained a movies section
        if self.movies is not None:
            # Get the movie template and build the page
            template = self.env.get_template('movies.html')
            with open("movies.html", 'w') as f:
                f.write(template.render(movies=self.movies))
                rendered_pages.append(f.name)
        # Return the list of files
        return rendered_pages


if __name__ == "__main__":
    app = MediaCenter()
    app.run()
