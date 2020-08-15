from helpers import tratamento_descricoes


class TestTratamentoTexto:
    
    def test_remove_pontuacao(self):
        tratamento_texto = tratamento_descricoes.TratamentoTexto()
        texto = 'olá!'
        result = tratamento_texto.remove_pontuacao(texto)

        assert result == 'olá '
    

    def test_remove_acentuacao(self):
        tratamento_texto = tratamento_descricoes.TratamentoTexto()
        texto = 'olá!'    
        result = tratamento_texto.remove_acentuacao(texto)

        assert result == 'ola!'


    def test_remove_space(self):
        tratamento_texto = tratamento_descricoes.TratamentoTexto()
        texto = ' olá! ' 
        result = tratamento_texto.remove_space(texto)

        assert result == 'olá!'
    

    def test_remove_space_duplicado(self):
        tratamento_texto = tratamento_descricoes.TratamentoTexto()
        texto = 'Olá     mundo'
        result = tratamento_texto.remove_space_duplicado(texto)

        assert result == 'Olá mundo'




