class URLencode(object):
    """ Transforms a string from unicode to URL, or percent, encoding """
    def __init__(self):
        pass

    def encodeString(self,s):
        self.result = ''
        for letter in s:
            if letter is '<':
                self.result = self.result+'%3C'
            elif letter is '>':
                self.result = self.result+'%3E'

            else:
                self.result = self.result+letter


        return self.result

'''
#template
            elif letter is '>':
                self.result = self.result+'%3E'
'''
