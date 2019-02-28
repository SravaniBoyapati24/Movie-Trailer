import webbrowser
class MovieTrailer():
    def __init__(self,movie_name,movie_story,movie_image_url,trailer_url):
        self.moviename=movie_name
        self.moviestory=movie_story
        self.image_url=movie_image_url
        self.youtube_url=trailer_url
    def show_trailer(self):
        webbrowser.open(self.youtube_url)

    
