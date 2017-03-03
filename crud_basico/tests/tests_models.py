from django.test import TestCase
from crud_basico.lib.basic_models import Filme, CategoriaFilme
from crud_basico.lib.basic_models_dao import FilmeDAO

# Create your tests here.
class FilmeTestCase(TestCase):
    def setUp(self):
        categoria = CategoriaFilme()
        categoria.set_id_categoria(1)
        categoria.set_categoria("Comédia")
        self.__filme_teste = Filme()
        self.__filme_teste.set_id_filme(1)
        self.__filme_teste.set_titulo('Teste Filme')
        self.__filme_teste.set_categoria(categoria)
        self.__filme_teste.set_avaliacao(4.5)


    def test_objeto_filme_categoria(self):
        """Insere um filme no banco"""
        self.assertIsInstance(self.__filme_teste, Filme)
        self.assertEqual(self.__filme_teste.get_titulo(), "Teste Filme")
        self.assertEqual(self.__filme_teste.get_categoria().get_categoria(), "Comédia")

    def test_insere_filme(self):
        """Insere um filme no banco"""
        dao_filme = FilmeDAO()
        self.assertGreater(dao_filme.insere_filme(self.__filme_teste), 0)