"""
Import text file and check for bad words
Submit text to wdylike website and receive a True/False response
"""


from urllib import request, parse


def read_text():
    """ Read text file """

    file_path = r'C:\Users\Mikele\Desktop\cv.txt'
    with open(file_path) as f:
        text_content = f.read()

        """ Call method check_profanity to check if there is a bad word in selected text document """
        check_profanity(text_content)


def check_profanity(text_to_check):
    """ Check for bad words in text """

    """ Access 'wdylike' website to provide a binary response if there is a curse word in a provided text """
    url = "http://www.wdylike.appspot.com/?q="
    """ Parse the text along with a url to fix spaces between text """
    url = url + parse.quote(text_to_check)

    with request.urlopen(url) as profanity:
        """ Read the response from the website"""
        output = profanity.read()

    """ Check the output """
    if b'true' in output:
        print('Profanity alert')
    elif b'false' in output:
        print('No bad words')
    else:
        print('There was a problem')


read_text()

