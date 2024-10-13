import webbrowser
import pyautogui
import time
from random_word import RandomWords

# Function to open the browser, type random words, and hit Enter
def search_random_words(number_of_words=30):
    r = RandomWords()
    search_engine_url = "https://www.bing.com"  # Open the Bing homepage first

    # Open the Bing homepage in the browser
    webbrowser.open(search_engine_url)
    
    # Give the browser time to load
    time.sleep(5)  # Adjust this depending on your internet speed

    for _ in range(number_of_words):
        random_word = r.get_random_word()
        if random_word:  # If a word is generated successfully
            # Type the random word
            pyautogui.write(random_word)

            # Press 'Enter' to search
            pyautogui.press('enter')

            # Wait for search results to load before proceeding to the next word
            time.sleep(10)  # Adjust this delay if needed

            

            # Wait briefly before typing the next word
            time.sleep(2)

# Run the function to perform the searches
search_random_words()
