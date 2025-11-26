"""Define words on clipboard"""
import re
import urllib.request
import json
import pyperclip

def define_clipboard():
    """Define all words included in Clipboard."""
    words = pyperclip.paste()
    words = set(re.findall(r"\b\w+\b", words))
    word_count = 1
    for word in words:
        print(f"{word_count}. {word}")
        word_count += 1
        try:
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            with urllib.request.urlopen(url) as response:
                data = response.read().decode('utf-8')
                json_data = json.loads(data)[0]
                for meaning in json_data["meanings"]:
                    print(f"\t\t{meaning['partOfSpeech']}")
                    def_count = 1
                    for definition in meaning['definitions']:
                        print(f"\t\t{def_count}) {definition['definition']}")
                        def_count += 1
                    print()
                print()
        except urllib.error.URLError as e:
            print(f"Error fetching data: {e.reason}")
    return words

def main():
    """Main Function."""
    define_clipboard()

if __name__ == "__main__":
    main()
