# There is a list of 26 character heights aligned by index to their letters. 
# For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string. 
# Using the letter heights given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide.

# Example
# h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 1, 1, 5, 5, 1, 5, 2, 5, 5, 5, 5, 5, 5] word = 'torn'

# The heights are t=2, o=1, r=1 and n=1. The tallest letter is 2 high and there are 4 letters. 
# The hightlighted area will be 2*4=8mm^2 so the answer is 8.

def designerPdfViewer(h, word):
    tall_word = 0
    print(word)
    
    for i in range(len(word)):
        tall_word = max(tall_word, h[ord(word[i]) - 97])
        
    return len(word)*tall_word

result_tall_word = designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'abc')
print(result_tall_word)
