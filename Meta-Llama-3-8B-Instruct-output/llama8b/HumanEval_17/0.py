from typing import List

def parse_music(music_string: str) -> List[int]:
    """ Parse a string representing musical notes and return a list of integers corresponding to how many beats each note lasts."""
    
    # Create a dictionary to map note symbols to their corresponding beat lengths
    note_lengths = {'o': 4, 'o|': 2, '.|': 1}
    
    # Initialize an empty list to store the parsed notes
    parsed_notes = []
    
    # Loop through the input string, and for each note symbol, append the corresponding beat length to the list
    for note in music_string.split():
        parsed_notes.append(note_lengths[note])
    
    # Return the list of parsed notes
    return parsed_notes