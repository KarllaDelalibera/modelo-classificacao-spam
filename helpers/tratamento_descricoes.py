import re
from unicodedata import normalize


class TratamentoTexto():
    
    def remove_pontuacao(self, text):
        '''
        Remove pontuacao de uma string
        '''
        return re.sub(r'[^\w\s]',' ',text)

    def remove_acentuacao(self, text):
        '''
        Remove acentuacao de uma string
        '''
        return normalize('NFKD', text).encode('ASCII','ignore').decode('ASCII')

    def remove_space(self, text):
        '''
        Remove os espacos no inicio e no fim de uma string
        '''
        sentence = text.rstrip()
        sentence = sentence.lstrip()
        return sentence 

    def remove_space_duplicado(self, text):
        '''
        Remove espaços duplicados da string
        '''
        sentence = " ".join(re.split("\s+", text, flags=re.UNICODE))
        return sentence    

