from collections import Counter, defaultdict
from bs4 import BeautifulSoup
import codecs, glob, sys, os

d = defaultdict(Counter)
prev_type = ''

# Define the infiles to parse
if len(sys.argv) > 1:
  infiles = glob.glob( os.path.join(sys.argv[1], '*') )
else:
  infiles = glob.glob('*.xml')

for c, i in enumerate(infiles):
  print(' * processed', c+1, 'of', len(infiles), 'files')
  with codecs.open(i) as f:
    f = f.read()
    soup = BeautifulSoup(f, 'lxml')
    for j in soup.find_all('token'):
      entity_type = j.find('ner').string

      # Only process non-0 entity types
      if entity_type != 'O':

        # Handle consecutive instances of the same entity type
        if entity_type == prev_type:
          if entity:
            entity += j.find('word').string + ' '
          else:
            entity = j.find('word').string + ' '

        # Increment the extant entity's count (if present)
        else:
          try:
            d[prev_type][entity] += 1
          except NameError:
            pass

          # Store the new entity word
          entity = j.find('word').string + ' '

        # Store the current entity type
        prev_type = entity_type

    # Handle the last identified entity
    try:
      if entity:
        d[prev_type][entity] += 1
        entity = ''
    except NameError:
      pass

# Write an output file
with codecs.open('ner_counts.txt', 'w', 'utf8') as out:
  out.write('\t'.join(['type', 'count', 'value']))
  for entity_type in d:
    for ner in d[entity_type]:
      out.write( '\t'.join([entity_type, str(d[entity_type][ner]), ner]) + '\n')