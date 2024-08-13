# Mini-project for the game of Mad Libs
## Introduction
The game provides 3 templates to choose from, after choosing a template, it gives the corresponding prompts to the user. The user can either enter the words by themselves or
let the game generate a random word. At the end, the game gives a story to the user with their chosen words.

## How to download files

- ### Downloading Individual Files
  - Click on the file that you want to download.
  - Click the download icon, which lets you download the raw file or right-click the "Raw" button and select "Save link as..." to download the file.
- ### Cloning the Repository
  If you want to work with the entire repository and want to make changes, cloning is the best option.
  
  - 1st make sure that you have Git installed on your computer.
  - Open a terminal.
  - Navigate to the directory where you want to clone the repository.
  - Run this command. ` git clone https://github.com/margaryanani/Mad-Libs.git `
    
## Usage

You need 'madlibs_functions.py', 'madlibs.py' files for this project. 
The 'madlibs_functions.py' file contains all the functions needed for the main file ('madlibs.py') to be executed. 

## Code Structure
  'madlibs.py' is the main script that runs the game. It interacts with the user, gathers input, and generates the final story.
  
  - The `categories` dictionary contains categories as keys and their values are a list of words within that category. This is for generating a random word if the user enters '?'.
  - To connect the categories with prompts we have the list `prompts_and_categories`, which consists of tuples, where each tuple has
            a prompt with its corresponding category.
  - the `template_mapping` dictionary maps template numbers to lists of indices that correspond to specific prompts.
  - Then we have a `template` input that lets the user choose one of the three templates. If the user enters anything besides 1,2 or 3, the program keeps asking the user for the right input.
    
After entering a template number, there are two functions that are being executed:

`prompts = get_prompts(template_mapping, prompts_and_categories, template)`

and `user_inputs = inputs(prompts, categories)`.

These functions are in the 'madlibs_functions.py' file.

#### - The overview of the  `get_prompts(template_mapping, prompts_and_categories, num)` function

 Based on the chosen template number (parameter `num`), it finds the template number in the `template_mapping`, takes the list of numbers corresponding to that number, and since those list of numbers are the indices of `prompts_and_categories`, uses them as indices to get the prompts and their categories for the chosen template from `prompts_and_categories` and stores them in a list.

So now we have the prompts ready for the user.

#### - The overview of the  `user_inputs = inputs(prompts, categories)` function

The function gives the prompts to the user one by one. When the user types '?' to any of the given prompts, the function goes to the `categories` dictionary, finds the corresponding key category for that prompt and from that key category's value that contains list of words within that category, generates a random word.
Also the `while True` loop prevents the user to leave blank inputs. for Each entered word, it is appeneded to the `user_inputs` list, which was empty at the begining of the function. 

After those functions are executed the `if` part is used to print the chosen template.

Since the order of the words in the `user_inputs` list are the same as the prompts' order, I just put them in the text based on the indices of the list.
