from calculo.medias import media_aritmetica

class TestMedias:
    def test_media_com_lista_numerica(self):
        """ Valida o cálculo da média. """
        assert media_aritmetica([1, 1]) == 1.0

    def test_media_com_lista_vazia(self):
        """ Valida o envio de 'None' para listas vazias. """
        assert media_aritmetica([]) == None
