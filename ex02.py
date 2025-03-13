import nltk
from nltk.tokenize import word_tokenize

# Baixar recursos necessários
import nltk
nltk.download('punkt_tab')
nltk.download('punkt')

# Texto para tokenização
text = "Eu adoro aprender sobre Inteligência Artificial!"

# Tokenizando o texto
tokens = word_tokenize(text)
print(tokens)

