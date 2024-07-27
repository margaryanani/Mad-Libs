import random

user_inputs = []
# collecting words for templates
def inputs():
    for prompt, category in prompts_and_categories:
        word = input(prompt)
        if word == '?':
            word = str(random.choice(categories[category]))
        user_inputs.append(word)

# The rules of the game
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

# words to generate
categories = {
    "number": [3, 14, 27, 8, 21, 35, 50, 12, 19, 28, 33, 45, 60, 7, 25],
    "measure of time": ["second", "minute", "hour", "day", "week", "month", "year", "decade", "century", "millennium", "microsecond", "millisecond", "nanosecond", "fortnight", "bimester"],
    "mode of transportation": ["car", "bicycle", "bus", "train", "airplane", "boat", "motorcycle", "scooter", "subway", "tram", "helicopter", "skateboard", "rollerblades", "hot air balloon", "ferry"],
    "adjective": ["happy", "sad", "bright", "dark", "quick", "slow", "loud", "quiet", "large", "small", "hot", "cold", "young", "old", "brave"],
    "noun": ["dog", "cat", "tree", "car", "house", "book", "computer", "phone", "mountain", "river", "city", "ocean", "flower", "bicycle", "bird"],
    "color": ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white", "gray", "cyan", "magenta", "lime", "teal"],
    "part of the body": ["head", "arm", "leg", "hand", "foot", "eye", "ear", "nose", "mouth", "back", "shoulder", "knee", "elbow", "wrist", "ankle"],
    "verb": ["run", "jump", "swim", "dance", "eat", "sing", "write", "read", "fly", "laugh", "play", "paint", "cook", "sleep", "talk"],
    "silly word": ["blubber", "flibbertigibbet", "gobbledygook", "snollygoster", "lollygag", "bamboozle", "kerfuffle", "hootenanny", "skedaddle", "fiddle-faddle", "jabberwocky", "dinglehopper", "widdershins", "gobbledygook", "nincompoop"],
    "proper noun": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia", "Kevin", "Laura", "Michael", "Nina", "Oliver"],
    "adjective (feeling)": ["happy", "sad", "angry", "excited", "nervous", "calm", "bored", "confused", "anxious", "joyful", "frustrated", "relaxed", "hopeful", "scared", "content"],
    "animal": ["dog", "cat", "elephant", "lion", "tiger", "giraffe", "monkey", "bear", "rabbit", "snake", "deer", "fox", "penguin", "dolphin", "turtle"],
    "verb (ending in ing)": ["singing", "dancing", "eating", "drinking", "swinging", "painting", "running", "walking", "sleeping", "thinking", "playing", "writing", "reading", "laughing", "crying"],
    "adverb (ending in ly)": ["quickly", "slowly", "happily", "sadly", "loudly", "quietly", "calmly", "nervously", "excitedly", "carefully", "eagerly", "kindly", "boldly", "gently", "firmly"],
    "place": ["beach", "park", "mountain", "city", "forest", "desert", "lake", "river", "island", "castle", "countryside", "library", "cafe", "school", "hospital"],
    "magical creature (plural)": ["dragons", "unicorns", "fairies", "elves", "phoenixes", "centaurs", "mermaids", "werewolves", "griffins", "goblins", "sprites", "vampires", "sphinxes", "pegasi", "djinn"],
    "room in a house": ["kitchen", "living room", "bedroom", "bathroom", "dining room", "study", "guest room", "playroom", "basement", "attic", "laundry room", "garage", "sunroom", "mudroom"],
    "noun (plural)": ["students", "teachers", "chairs", "tables", "pens", "keys", "shoes", "socks", "glasses", "watches", "clouds", "stars", "fish", "horses", "butterflies"]
}

# Choosing the template

template = input('Choose a template (1, 2, or 3): ')
while template not in ['1', '2', '3']:
    print('You can only choose the given templates 1, 2, or 3. Try again.')
    template = input('Choose a template (1, 2, or 3): ')

if template =='1':
    # Define prompts and their categories for template 1
    prompts_and_categories = [
        ("Enter number --> ", "number"),
        ("Enter measure of time --> ", "measure of time"),
        ("Enter mode of transportation --> ", "mode of transportation"),
        ("Enter adjective --> ", "adjective"),
        ("Enter adjective --> ", "adjective"),
        ("Enter Noun(Plural) --> ", "noun (plural)"),
        ("Enter color --> ", "color"),
        ("Enter part of the body --> ", "part of the body"),
        ("Enter verb --> ", "verb"),
        ("Enter number --> ", "number"),
        ("Enter noun --> ", "noun"),
        ("Enter noun --> ", "noun"),
        ("Enter part of the body --> ", "part of the body"),
        ("Enter verb --> ", "verb"),
        ("Enter noun --> ", "noun"),
        ("Enter adjective --> ", "adjective"),
        ("Enter silly word --> ", "silly word"),
        ("Enter noun --> ", "noun")
    ]
    inputs()
    print( f"""
It was about [{user_inputs[0]}] [{user_inputs[1]}] ago when I arrived at the hospital in a [{user_inputs[2]}]. 
The hospital is a/an [{user_inputs[3]}] place, there are a lot of [{user_inputs[4]}] [{user_inputs[5]}] here. 
There are nurses here who have [{user_inputs[6]}] [{user_inputs[7]}]. If someone wants to come into 
my room I told them that they have to [{user_inputs[8]}] first. I’ve decorated my room with 
[{user_inputs[9]}] [{user_inputs[10]}].Today I talked to a doctor and they were wearing a [{user_inputs[11]}]
on their [{user_inputs[12]}]. I heard that all doctors [{user_inputs[13]}] [{user_inputs[14]}] everyday for
breakfast. The most [{user_inputs[15]}] thing about beingin the hospital is the [{user_inputs[16]}]
[{user_inputs[17]}]!
""")



elif template == '2':
    prompts_and_categories = [
        ("Enter Proper Noun (Person's Name) --> ", "proper noun"),
        ("Enter Noun --> ", "noun"),
        ("Enter Adjective (Feeling) --> ", "adjective (feeling)"),
        ("Enter Verb --> ", "verb"),
        ("Enter Adjective (Feeling) --> ", "adjective (feeling)"),
        ("Enter Animal --> ", "animal"),
        ("Enter Verb --> ", "verb"),
        ("Enter Color --> ", "color"),
        ("Enter Verb (ending in ing) --> ", "verb (ending in ing)"),
        ("Enter Adverb (ending in ly) --> ", "adverb (ending in ly)"),
        ("Enter Number --> ", "number"),
        ("Enter Measure of time --> ", "measure of time"),
        ("Enter Color --> ", "color"),
        ("Enter Animal --> ", "animal"),
        ("Enter Number --> ", "number"),
        ("Enter Silly Word --> ", "silly word"),
        ("Enter Noun --> ", "noun")
    ]
    inputs()
    print(f"""
This weekend I am going camping with [{user_inputs[0]}]. I packed my lantern, 
sleeping bag, and [{user_inputs[1]}]. I am so [{user_inputs[2]}] to [{user_inputs[3]}] in a tent. I am [{user_inputs[4]}]
we might see a(n) [{user_inputs[5]}], I hear they're kind of dangerous. While we’re camping, we are going to hike,
fish, and [{user_inputs[6]}]. I have heard that the [{user_inputs[7]}] lake is great for [{user_inputs[8]}]. 
Then we will [{user_inputs[9]}] hike through the forest for [{user_inputs[10]}] [{user_inputs[11]}]. If I see
a [{user_inputs[12]}] [{user_inputs[13]}] while hiking, I am going to bring it home as a pet! At night we will tell [{user_inputs[14]}]
[{user_inputs[15]}] stories and roast [{user_inputs[16]}] around the campfire!!
""")

elif template == '3':
# Define prompts and their categories for template 3
    prompts_and_categories = [
        ("Enter Proper Noun (Person's Name) --> ", "proper noun"),
        ("Enter Adjective --> ", "adjective"),
        ("Enter Color --> ", "color"),
        ("Enter Animal --> ", "animal"),
        ("Enter Place --> ", "place"),
        ("Enter Adjective --> ", "adjective"),
        ("Enter Magical Creature (Plural) --> ", "magical creature (plural)"),
        ("Enter Adjective --> ", "adjective"),
        ("Enter Magical Creature (Plural) --> ", "magical creature (plural)"),
        ("Enter Room in a House --> ", "room in a house"),
        ("Enter Noun(Plural) --> ", "noun (plural)"),
        ("Enter Noun --> ", "noun"),
        ("Enter Noun(Plural) --> ", "noun (plural)"),
        ("Enter Adjective --> ", "adjective"),
        ("Enter Noun(Plural) --> ", "noun (plural)"),
        ("Enter number --> ", "number"),
        ("Enter measure of time --> ", "measure of time"),
        ("Enter Verb (ending in ing) --> ", "verb (ending in ing)"),
        ("Enter Adjective --> ", "adjective"),
        ("Enter Noun --> ", "noun")
    ]
    inputs()
    print(f"""
Dear [{user_inputs[0]}], I am writing to you from a [{user_inputs[1]}] castle in
an enchanted forest. I found myself here one day after going for a ride on a [{user_inputs[2]}] [{user_inputs[3]}]
in [{user_inputs[4]}]. There are [{user_inputs[5]}] [{user_inputs[6]}] and [{user_inputs[7]}] [{user_inputs[8]}] here! 
In the [{user_inputs[9]}] there is a pool full of [{user_inputs[10]}]. I fall asleep each night
on a [{user_inputs[11]}] of [{user_inputs[12]}] and dream of [{user_inputs[13]}] [{user_inputs[14]}]. It feels as though
I have lived here for [{user_inputs[15]}] [{user_inputs[16]}]. I hope one day you can visit, although the only
way to get here now is [{user_inputs[17]}] on a [{user_inputs[18]}] [{user_inputs[19]}]!!
""")


