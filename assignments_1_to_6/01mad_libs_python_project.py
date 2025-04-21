def mad_libs():
    print("Welcome to Mad Libs! Please provide the following words:")

    # Get input from the user
    adjective = input("Adjective: ")
    noun = input("Noun: ")
    verb = input("Verb (past tense): ")
    adverb = input("Adverb: ")
    place = input("Place: ")
    emotion = input("Emotion: ")

    # Create the Mad Lib using an f-string
    story = f"""
    One day, I was walking through the {place} when I saw a very {adjective} {noun}.
    I {verb} at it {adverb} and it looked at me with {emotion}.
    It was the strangest day of my life!
    """

    # Print the final story
    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    mad_libs()
