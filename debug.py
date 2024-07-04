import os

def search_files(directory, search_terms):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                try:
                    contents = file.read()
                    for term in search_terms:
                        if term in contents:
                            print(f"Found '{term}' in {filepath}")
                except Exception as e:
                    print(f"Could not read {filepath}: {e}")

# Directory to search and terms to search for
directory_to_search = "" # Update this path to your project directory
search_terms = ['tensorflow', 'tflite']

search_files(directory_to_search, search_terms)