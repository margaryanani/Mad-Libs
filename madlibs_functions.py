import random


def get_prompts(template_mapping, prompts_and_categories, num):
    """Returns a list of prompts based on the selected template number.
    Args:
        template_mapping (dict): A dictionary mapping template numbers (str) to
                                 lists of indices that correspond to specific prompts.
        prompts_and_categories (list): A list of tuples, where each tuple has
                                       a prompt with its corresponding category.
        num (str): The template number, that determines the set of prompts.
    returns:
        list: list of tuples, where each tuple has its prompt and category based on
              the chosen template.
    """
    tpl_number = template_mapping[num]
    return [prompts_and_categories[i] for i in tpl_number]


def inputs(prompts, categories):
    """Displays prompts to the user, allowing the user to input words for the game,
    if the user enters '?' a random word is chosen from the corresponding category.
    Prevents blank inputs by prompting the user to re-enter a valid input.
    Args:
        prompts (list): contains tuples, where each prompt has its own category.
        categories (dict): contains keys that are the category names and their values
                            are a list of words within that category.
    returns:
           list: A list of user's entered words or randomly generated words
                  corresponding to the prompts
    """
    user_inputs = []
    for prompt, category in prompts:
        while True:
            word = input(prompt)
            if word == '?':
                word = str(random.choice(categories[category]))
                break
            elif word == '':
                print("Input cannot be blank. Try Again.")
            else:
                break
        user_inputs.append(word)
    return user_inputs
