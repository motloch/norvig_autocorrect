from collections import Counter
import re

words = []

# Get a set of all words
with open('moby_dick.txt', 'r') as f:
    data = f.read()
    data = data.lower()
    words = re.findall('\w+', data)

corpus = Counter(words)

from spell_corrector import SpellCorrector

spell_corrector = SpellCorrector(dictionary=corpus, verbose=0)
print('Correction to eddwardd is:')
print(spell_corrector.correction('edwardd'))
print()
print('Correction to edwardhas is:')
print(spell_corrector.correction('edwardhas'))
