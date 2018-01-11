import media
import fresh_tomatoes

# Create movie object - see media.py
toy_story = media.Movie(
    'Toy Story',
    (
        'A cowboy doll is profoundly threatened and jealous '
        'when a new spaceman figure supplants him as top toy '
        'in a boy\'s room.'
    ),
    'https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg',  # NOQA
    'https://www.youtube.com/watch?v=KYz2wyBy3kc')

v_for_vendetta = media.Movie(
    'V For Vendetta',
    (
        'In a future British tyranny, a shadowy freedom '
        'fighter, known only by the alias of "V", plots to '
        'overthrow it with the help of a young woman.'
    ),
    'https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg',
    'https://www.youtube.com/watch?v=k_13fFIrhPk')

the_matrix = media.Movie(
    'The Matrix',
    (
        'A computer hacker learns from mysterious rebels '
        'about the true nature of his reality and his role in '
        'the war against its controllers.'
    ),
    'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg',
    'https://www.youtube.com/watch?v=m8e-FF8MsqU')

gladiator = media.Movie(
    'Gladiator',
    (
        'When a Roman General is betrayed, and his family '
        'murdered by an emperor\'s corrupt son, he comes to Rome '
        'as a gladiator to seek revenge.'
    ),
    'https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg',
    'https://www.youtube.com/watch?v=Q-b7B8tOAQU')

the_last_samurai = media.Movie(
    'The Last Samurai',
    (
        'An American military advisor embraces the '
        'Samurai culture he was hired to destroy after '
        'he is captured in battle.'
    ),
    'https://upload.wikimedia.org/wikipedia/en/c/c6/The_Last_Samurai.jpg',
    'https://www.youtube.com/watch?v=T50_qHEOahQ')

irobot = media.Movie(
    'I, Robot',
    (
        'In 2035, a technophobic cop investigates a crime that '
        'may have been perpetrated by a robot, which leads to a '
        'larger threat to humanity.'
    ),
    'https://upload.wikimedia.org/wikipedia/en/3/3b/Movie_poster_i_robot.jpg',
    'https://www.youtube.com/watch?v=rL6RRIOZyCM')

elf = media.Movie(
    'Elf',
    (
        'After inadvertently wreaking havoc on the elf community due '
        'to his ungainly size, a man raised as an elf at the North '
        'Pole is sent to the U.S. in search of his true identity.'
    ),
    'https://upload.wikimedia.org/wikipedia/en/d/df/Elf_movie.jpg',
    'https://www.youtube.com/watch?v=gW9wRNqQ_P8')

hacksaw_ridge = media.Movie(
    'Hacksaw Ridge',
    (
        'WWII American Army Medic Desmond T. Doss, who '
        'served during the Battle of Okinawa, refuses to '
        'kill people, and becomes the first man in American '
        'history to receive the Medal of Honor without '
        'firing a shot.'
    ),
    'https://upload.wikimedia.org/wikipedia/en/8/8a/Hacksaw_Ridge_poster.png',
    'https://www.youtube.com/watch?v=s2-1hz1juBI')

transformers = media.Movie(
    'Transformers',
    (
        'An ancient struggle between two Cybertronian races, '
        'the heroic Autobots and the evil Decepticons, comes '
        'to Earth, with a clue to the ultimate power held '
        'by a teenager.'
    ),
    'https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg',
    'https://www.youtube.com/watch?v=zX81c2vycKo')

# Create list of movie objects
movies = [
    toy_story,
    v_for_vendetta,
    the_matrix,
    gladiator,
    the_last_samurai,
    irobot,
    elf,
    hacksaw_ridge,
    transformers
    ]

# fresh_tomatoes.py creates an html page from a list of movie objects
fresh_tomatoes.open_movies_page(movies)
