import random
from madlibs_functions import get_prompts, inputs

input("""
Mad Libs
Instructions:
1. Pick one of the templates 1, 2, or 3.
2. Fill in the corresponding words as prompted (e.g., Write a noun --> book).
3. If you're unsure, type '?' and the game will generate a word for you.
4. You will receive the full story with your chosen words at the end.

Press Enter to start the game.
""")
print("Starting...")

# categories with their corresponding words to generate a word if needed.
categories = {
    "number": [3, 14, 27, 8, 21, 35, 50, 12, 19, 28, 33, 45, 60, 7, 25],
    "measure of time": ["second", "minute", "hour", "day", "week", "month", "year", "decade", "century", "millennium",
                        "microsecond", "millisecond", "nanosecond", "fortnight", "bimester"],
    "mode of transportation": ["car", "bicycle", "bus", "train", "airplane", "boat", "motorcycle", "scooter", "subway",
                               "tram", "helicopter", "skateboard", "rollerblades", "hot air balloon", "ferry"],
    "adjective": ["happy", "sad", "bright", "dark", "quick", "slow", "loud", "quiet", "large", "small", "hot", "cold",
                  "young", "old", "brave"],
    "noun": ["dog", "cat", "tree", "car", "house", "book", "computer", "phone", "mountain", "river", "city", "ocean",
             "flower", "bicycle", "bird"],
    "color": ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white", "gray", "cyan",
              "magenta", "lime", "teal"],
    "part of the body": ["head", "arm", "leg", "hand", "foot", "eye", "ear", "nose", "mouth", "back", "shoulder",
                         "knee", "elbow", "wrist", "ankle"],
    "verb": ["run", "jump", "swim", "dance", "eat", "sing", "write", "read", "fly", "laugh", "play", "paint", "cook",
             "sleep", "talk"],
    "silly word": ["blubber", "flibbertigibbet", "gobbledygook", "snollygoster", "lollygag", "bamboozle", "kerfuffle",
                   "hootenanny", "skedaddle", "fiddle-faddle", "jabberwocky", "dinglehopper", "widdershins",
                   "gobbledygook", "nincompoop"],
    "proper noun": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia", "Kevin",
                    "Laura", "Michael", "Nina", "Oliver"],
    "adjective (feeling)": ["happy", "sad", "angry", "excited", "nervous", "calm", "bored", "confused", "anxious",
                            "joyful", "frustrated", "relaxed", "hopeful", "scared", "content"],
    "animal": ["dog", "cat", "elephant", "lion", "tiger", "giraffe", "monkey", "bear", "rabbit", "snake", "deer", "fox",
               "penguin", "dolphin", "turtle"],
    "verb (ending in ing)": ["singing", "dancing", "eating", "drinking", "swinging", "painting", "running", "walking",
                             "sleeping", "thinking", "playing", "writing", "reading", "laughing", "crying"],
    "adverb (ending in ly)": ["quickly", "slowly", "happily", "sadly", "loudly", "quietly", "calmly", "nervously",
                              "excitedly", "carefully", "eagerly", "kindly", "boldly", "gently", "firmly"],
    "place": ["beach", "park", "mountain", "city", "forest", "desert", "lake", "river", "island", "castle",
              "countryside", "library", "cafe", "school", "hospital"],
    "magical creature (plural)": ["dragons", "unicorns", "fairies", "elves", "phoenixes", "centaurs", "mermaids",
                                  "werewolves", "griffins", "goblins", "sprites", "vampires", "sphinxes", "pegasi",
                                  "djinn"],
    "room in a house": ["kitchen", "living room", "bedroom", "bathroom", "dining room", "study", "guest room",
                        "playroom", "basement", "attic", "laundry room", "garage", "sunroom", "mudroom"],
    "noun (plural)": ["students", "teachers", "chairs", "tables", "pens", "keys", "shoes", "socks", "glasses",
                      "watches", "clouds", "stars", "fish", "horses", "butterflies"]
}

# prompts with their categories for templates 1,2 and 3 combined.
prompts_and_categories = [
    ("Enter number --> ", "number"),  # 0
    ("Enter measure of time --> ", "measure of time"),  # 1
    ("Enter mode of transportation --> ", "mode of transportation"),  # 2
    ("Enter adjective --> ", "adjective"),  # 3
    ("Enter Noun(Plural) --> ", "noun (plural)"),  # 4
    ("Enter color --> ", "color"),  # 5
    ("Enter part of the body --> ", "part of the body"),  # 6
    ("Enter verb --> ", "verb"),  # 7
    ("Enter noun --> ", "noun"),  # 8
    ("Enter silly word --> ", "silly word"),  # 9
    ("Enter Proper Noun (Person's Name) --> ", "proper noun"),  # 10
    ("Enter Adjective (Feeling) --> ", "adjective (feeling)"),  # 11
    ("Enter Animal --> ", "animal"),  # 12
    ("Enter Verb (ending in ing) --> ", "verb (ending in ing)"),  # 13
    ("Enter Adverb (ending in ly) --> ", "adverb (ending in ly)"),  # 14
    ("Enter Place --> ", "place"),  # 15
    ("Enter Magical Creature (Plural) --> ", "magical creature (plural)"),  # 16
    ("Enter Room in a House --> ", "room in a house"),  # 17
]

# separated prompts for each template.
template_mapping = {
    '1': [0, 1, 2, 3, 3, 4, 5, 6, 7, 0, 8, 8, 6, 7, 8, 3, 9, 8],
    '2': [10, 8, 11, 7, 11, 12, 7, 5, 13, 14, 0, 1, 5, 12, 0, 9, 8],
    '3': [10, 3, 5, 12, 15, 3, 16, 3, 16, 17, 4, 8, 4, 3, 4, 0, 1, 13, 3, 8]
}

# Choosing the template
template = input('Choose a template (1, 2, or 3): ')
while template not in ['1', '2', '3']:
    print('You can only choose the given templates 1, 2, or 3. Try again.')
    template = input('Choose a template (1, 2, or 3): ')


# function to get the prompts needed for a specified template
prompts = get_prompts(template_mapping, prompts_and_categories, template)

# function to give template's prompts to the user and store them in a list
user_inputs = inputs(prompts, categories)

# template 1
if template == '1':
    print(f"""
It was about [{user_inputs[0]}] [{user_inputs[1]}] ago when I arrived at the hospital in a [{user_inputs[2]}]. 
The hospital is a/an [{user_inputs[3]}] place, there are a lot of [{user_inputs[4]}] [{user_inputs[5]}] here. 
There are nurses here who have [{user_inputs[6]}] [{user_inputs[7]}]. If someone wants to come into 
my room I told them that they have to [{user_inputs[8]}] first. I’ve decorated my room with 
[{user_inputs[9]}] [{user_inputs[10]}].Today I talked to a doctor and they were wearing a [{user_inputs[11]}]
on their [{user_inputs[12]}]. I heard that all doctors [{user_inputs[13]}] [{user_inputs[14]}] everyday for
breakfast. The most [{user_inputs[15]}] thing about being in the hospital is the [{user_inputs[16]}]
[{user_inputs[17]}]!
""")


# template 2
elif template == '2':
    print(f"""
This weekend I am going camping with [{user_inputs[0]}]. I packed my lantern, 
sleeping bag, and [{user_inputs[1]}]. I am so [{user_inputs[2]}] to [{user_inputs[3]}] in a tent. I am [{user_inputs[4]}]
we might see a(n) [{user_inputs[5]}], I hear they're kind of dangerous. While we’re camping, we are going to hike,
fish, and [{user_inputs[6]}]. I have heard that the [{user_inputs[7]}] lake is great for [{user_inputs[8]}]. 
Then we will [{user_inputs[9]}] hike through the forest for [{user_inputs[10]}] [{user_inputs[11]}]. If I see
a [{user_inputs[12]}] [{user_inputs[13]}] while hiking, I am going to bring it home as a pet! At night we will tell 
[{user_inputs[14]}] [{user_inputs[15]}] stories and roast [{user_inputs[16]}] around the campfire!!
""")

# template 3
elif template == '3':
    print(f"""
Dear [{user_inputs[0]}], I am writing to you from a [{user_inputs[1]}] castle in
an enchanted forest. I found myself here one day after going for a ride on a [{user_inputs[2]}] [{user_inputs[3]}]
in [{user_inputs[4]}]. There are [{user_inputs[5]}] [{user_inputs[6]}] and [{user_inputs[7]}] [{user_inputs[8]}] here! 
In the [{user_inputs[9]}] there is a pool full of [{user_inputs[10]}]. I fall asleep each night
on a [{user_inputs[11]}] of [{user_inputs[12]}] and dream of [{user_inputs[13]}] [{user_inputs[14]}]. It feels as though
I have lived here for [{user_inputs[15]}] [{user_inputs[16]}]. I hope one day you can visit, although the only
way to get here now is [{user_inputs[17]}] on a [{user_inputs[18]}] [{user_inputs[19]}]!!
""")
