from summarizer import Summarizer
from translator import Translator

summarizer = Summarizer.bind(Translator.bind())
