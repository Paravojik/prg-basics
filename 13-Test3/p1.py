def f(word):
    if not word:
        return ""
    
    result = []
    # Create the wave pattern
    for i in range(len(word)):
        # Construct the word: char at i is uppercase, rest are lowercase
        temp_word = word[:i].lower() + word[i].upper() + word[i+1:].lower()
        result.append(temp_word)
        
    return "-".join(result)

if __name__ == "__main__":
    print(f("water"))  # Expected: Water-water-waTer-water-water
    print(f("a"))      # Expected: A
    print(f(""))       # Expected: