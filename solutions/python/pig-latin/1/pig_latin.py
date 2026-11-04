def translate(text):
    vowel_sounds = tuple(['A', 'E', 'I', 'O', 'U', 'Xr', 'Yt', 'a', 'e' 'i', 'o', 'u', 'xr', 'yt'])
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = []
    for word in text.split():
        if word.startswith(vowel_sounds):
            string.append(f'{word}ay')
        elif word.startswith(tuple(['Y', 'y'])):
            string.append(f'{word[1:]}yay')
        else:
            for letter in range(len(word)):
                if word[letter] == 'q' and word[letter+1] == 'u':
                    string.append(f'{word[letter+2:]}{word[0:letter+2]}ay')
                    break
                elif word[letter] in vowels:
                    string.append(f'{word[letter:]}{word[0:letter]}ay')
                    break
                elif word[letter] == 'y':
                    string.append(f'{word[letter:]}{word[0:letter]}ay')
    return ' '.join(string)
