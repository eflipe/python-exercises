# Usage: clipboard save <keyword> - Saves clipboard to keyword.
#        clipboard <keyword> - Loads keyword to clipboard.
#        clipboard list - Loads all keywords to clipboard.
import shelve, pyperclip, sys

clipShelf = shelve.open('clipC')

# save to clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    clipShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        print(list(clipShelf.items()))
        pyperclip.copy(str(list(clipShelf.keys())))
    elif sys.argv[1] in clipShelf:
        pyperclip.copy(clipShelf[sys.argv[1]])

clipShelf.close()
