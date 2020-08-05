import arabic_reshaper
from pyarabic.araby import tokenize
from pyarabic.unshape import unshaping_text
from pyarabic import araby
from wordcloud import WordCloud, STOPWORDS


'''
# you can use path and read file as follow

path = "path.txt"
text = open(path, encoding='utf-8')
new_text = text.read()
'''

text = '⁭الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ  الرَّحْمَٰنِ الرَّحِيمِ  مَالِكِ يَوْمِ الدِّينِ  إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ  اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ  صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ '

# Interpreter reads left to right while Arabic reads right to left so I reshaped the text to make it in readable format without backward words or cutted off letters

text_to_be_reshaped = text
reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
rev_text = reshaped_text[::-1]  

# Iterate through text and count words frequencies

dictionary = {}
lst = tokenize(rev_text)
for elements in lst:  
    if elements in dictionary: 
        dictionary[elements] += 1
    else: 
        dictionary.update({elements: 1})
print(dictionary)     # check successful function

# wordcloud to generate PNG from dictionary

cloud = WordCloud(background_color = "white", font_path = 'arial.ttf', max_words = 5000, stopwords = set(STOPWORDS))

cloud.generate_from_frequencies(dictionary)

cloud.to_file("ArabicWordCloud.png")      # png will be found in your current folder or workspace
