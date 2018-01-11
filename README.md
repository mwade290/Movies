# Movie Trailer Website

Lists a number of Movies formatted using the Movie image above the Movie title.  
Clicking on the Movie link will play the YouTube trailer for the selected Movie.  
In the background, fresh_tomatoes.py is taking in a list of Movie objects and converting it to html syntax.

# Install

No installation requirements

# Usage

## How to run the code
1. Download the code
2. Open a terminal
3. Navigate to directory where downloaded files are located
4. Type 'python entertainment_center.py'
5. Enjoy my favourite movie trailers!

## Add new movie
1. Open entertainment_center.py with a text editor
2. Create new unique variable from movie title
3. Use the format: unique_variable = media.Movie(movie_title, movie_storyline, movie_image_url, movie_trailer_url)
4. Add unique variable to 'movies' list
5. Run program

### Example
```
v_for_vendetta = media.Movie(
    'V For Vendetta',
    (
        'In a future British tyranny, a shadowy freedom '
        'fighter, known only by the alias of "V", plots to '
        'overthrow it with the help of a young woman.'
    ),
    'https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg',
    'https://www.youtube.com/watch?v=k_13fFIrhPk')
```