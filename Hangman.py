import random

def hangman():
    words=[
    'apple', 'river', 'cloud', 'stone', 'light', 'bread', 'music', 'ocean',
    'forest', 'paper', 'glass', 'fire', 'water', 'earth', 'wind', 'flower',
    'mountain', 'valley', 'desert', 'island', 'bridge', 'tower', 'castle',
    'garden', 'kitchen', 'bedroom', 'library', 'school', 'market', 'hospital',
    'doctor', 'teacher', 'artist', 'writer', 'singer', 'dancer', 'player',
    'summer', 'winter', 'spring', 'autumn', 'morning', 'evening', 'midnight',
    'sunset', 'sunrise', 'thunder', 'lightning', 'rainbow', 'snowflake',
    'butterfly', 'elephant', 'dolphin', 'eagle', 'tiger', 'lion', 'bear',
    'rabbit', 'turtle', 'monkey', 'penguin', 'kangaroo', 'giraffe', 'zebra',
    'banana', 'orange', 'grape', 'lemon', 'cherry', 'peach', 'melon',
    'potato', 'carrot', 'onion', 'garlic', 'tomato', 'lettuce', 'corn',
    'chicken', 'beef', 'pork', 'fish', 'shrimp', 'cheese', 'butter',
    'coffee', 'tea', 'juice', 'soda', 'water', 'wine', 'beer',
    'chair', 'table', 'sofa', 'bed', 'lamp', 'clock', 'mirror',
    'phone', 'laptop', 'tablet', 'camera', 'radio', 'television', 'watch',
    'shirt', 'pants', 'dress', 'shoes', 'hat', 'coat', 'gloves',
    'book', 'pen', 'pencil', 'notebook', 'scissors', 'ruler', 'eraser',
    'car', 'bus', 'train', 'plane', 'boat', 'bicycle', 'motorcycle',
    'road', 'street', 'avenue', 'highway', 'tunnel', 'park', 'station',
    'happy', 'sad', 'angry', 'excited', 'tired', 'hungry', 'thirsty',
    'fast', 'slow', 'loud', 'quiet', 'hot', 'cold', 'warm',
    'big', 'small', 'tall', 'short', 'wide', 'narrow', 'deep',
    'red', 'blue', 'green', 'yellow', 'purple', 'orange', 'black',
    'white', 'gray', 'brown', 'pink', 'gold', 'silver', 'bronze'   
                          ]
    word = random.choice(words).lower()
    progress = list("_"* len(word))
    up_word = list(word)

    while "".join(progress) != word:
        guess = input('Guess a character from a-z: ').lower()

        if guess in word and guess.isalpha() and len(guess)==1:
            progress[word.find(guess)] = guess
            
            
            up_word[word.find(guess)] = "_"
            while guess in up_word:
                progress[up_word.index(guess)] = guess
                up_word[up_word.index(guess)] = "_"
            print(" ".join(progress))

        elif guess.isalpha() == False:
            print("Only enter alphabets!")
        elif len(guess)!=1:
            print("Guess one character at a time.")
        else:
            print(f'Try a different character. {guess} is incorrect', end='\n')
            print(" ".join(progress))

        if "".join(progress).lower() == word.lower():
            print(f"You Won! The name is {progress}")

hangman()
