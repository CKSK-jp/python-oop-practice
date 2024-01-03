from wordfinder import WordFinder
    
class SpecialWordFinder(WordFinder):
  def __init__(self, path_name):
    super().__init__(path_name)

  def check_list(self):
    """Remove empty spaces and commented out words in the word_list"""
    checked_list = super().count_words()
    checked_list.remove('')
    checked_list = [word for word in checked_list if '#' not in word]
    print(checked_list) 

if __name__ == "__main__":
    swf = SpecialWordFinder("words.txt")
    swf.check_list()