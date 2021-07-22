"""
Though this module is never gonna let you down, it's a total joke.
Features:
    The RickRollException for your memelike error needs,
    the rickroll function for classic rickrolling,
    the rickroll_text function for rickrolls via text,
    and the subtle_rickroll function for some more hidden rickrolls.
"""
import webbrowser as wb
from random import choice


class RickRollException(Exception):
    """
    The RickRollException, can be raised by the user.
    A custom message can be used but there are also defaults.
    """
    def __init__(self, message=None):
        if message is not None:
            self.message = message
        else:
            self.message = choice([
                "The code seems to be giving you up",
                "The code's letting you down",
                """If you ask Rick Astley for his copy of the movie Up,
                 he can't give it to you as he is never gonna give you up.
                  But in doing so, he lets you down...""",
                "We're no strangers to Python. You know the rules and sO dO i"
                ])
        super().__init__(self.message)


def rickroll():
    """Directs the user to the classic rickroll"""
    try:
        wb.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    except Exception as err:
        raise RickRollException from err


def rickroll_text(lines=55):
    """
    Gets the lyrics of Never Gonna Give You Up
    Args:
        lines (int): how many lines of lyrics. Defaults to all.

    Returns:
        lyrics (str): A string of the number of lines of lyrics requested.
    """
    lyrics = """We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give, never gonna give
(Give you up)
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye"""

    if lines > 55:
        raise RickRollException("you only wish the song was that long")
    lyrics = lyrics.split("\n")
    return "\n".join(lyrics[:lines])


def subtle_rickroll():
    """Opens a random link from a list of more subtle rickrolls."""
    try:
        urls = ["https://www.youtube.com/watch?v=42OleX0HR4E",
                "https://youtu.be/fabiBsQWDTY",
                "https://youtu.be/nHRbZW097Uk",
                "https://youtu.be/cqF6M25kqq4",
                "https://youtu.be/fMnIpIMuBJI"]
        wb.open(choice(urls))
    except Exception as err:
        raise RickRollException from err
