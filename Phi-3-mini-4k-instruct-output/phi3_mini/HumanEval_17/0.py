from typing import List

def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    note last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Create a dictionary to map the note symbols to their corresponding beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string by spaces to get a list of notes
    notes = music_string.split()

    # Initialize an empty list to store the beats
    beats = []

    # Loop through the list of notes, and for each note, get its corresponding beats from the dictionary
    for note in notes:
        beats.append(note_to_beats[note])

    # Return the result list
    return beats