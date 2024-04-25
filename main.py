from summarizer import Summarizer
from translator import Translator
print('Starting app')
summarizer = Summarizer.bind(Translator.bind())
