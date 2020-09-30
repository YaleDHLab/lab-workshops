import matplotlib.pyplot as plt
from collections import Counter

def plot_counts(counter, n=50):
  if not isinstance(counter, Counter):
    print('Please provide a collections.Counter object')
    return
  with plt.style.context('fivethirtyeight'):
    words, counts = zip(*counter.most_common())
    plt.figure(figsize=(20,10))
    plt.bar(words[:n], counts[:n])
    plt.xticks(rotation=90)
    plt.show()
