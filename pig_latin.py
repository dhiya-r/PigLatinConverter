# Translating a sentence to lig latin
# Dhiya Ramadhar

sentence = input("Enter a sentence:\n")
sentence = sentence.lower()
word = ''
last_word = ''
z = 0

for k in range(len(sentence)):
    if sentence[k] == ' ':
        word = sentence[z:k] #Extracts each word in the sentence
        if word[0] in 'bcdfghjklmnpqrstvwxyz':
            for i in range(len(word)):
                if word[i] in 'aeiou': # to find out where the first vowel appears in the word
                    word = word[i::] + 'a' + word[:i] + 'ay'
                    break
        else:
            word = word + 'way'
        print(word, end=' ')
        z = k + 1
        k = k + 1
        
for n in range(len(sentence), z, -1):
    last_word = sentence[n - 1] + last_word#Extracts the last word in the sentence

if last_word[0] in 'bcdfghjklmnpqrstvwxyz':
    for d in range(len(last_word)):
        if last_word[d] in 'aeiou':
            last_word = last_word[d::] + 'a' + last_word[:d] + 'ay'
            #print('\n', last_word)
            break
    else:
        last_word = 'a' + last_word + 'ay' #This is used if there are no vowels in the word eg: 'fly'
else:
    last_word = last_word + 'way'#USed if the last word starts with a vowel
print(last_word)