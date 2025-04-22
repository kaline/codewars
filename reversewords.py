def reverse_words(text):
   words = text.split(" ")
   reverse_words = ' '.join(word[::-1] for word in words)
   return reverse_words
