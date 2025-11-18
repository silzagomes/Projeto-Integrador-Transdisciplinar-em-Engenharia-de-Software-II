import unittest
from app import app # Importa a instância do seu aplicativo Flask
import models # Importa seu módulo de dados simulados

class LojaCupcakesTestCase(unittest.TestCase):

    def setUp(self):
        # 1. Configura um cliente de teste
        self.app = app.test_client()
        # 2. Ativa o modo de rastreamento de cookies de sessão
        self.app.testing = True

    def test_a_pagina_produtos_carrega(self):
        """Verifica se a rota /produtos retorna HTTP 200 (Sucesso)"""
        resposta = self.app.get('/produtos')
        self.assertEqual(resposta.status_code, 200)
        self.assertIn(b'Nossos Cupcakes', resposta.data) # Verifica se a view renderizou corretamente

    def test_b_adicionar_ao_carrinho(self):
        """Testa se a adição de um produto funciona e redireciona corretamente"""
        
        # Simula o POST de adição, usando um ID conhecido do models.py (ex: id=1)
        resposta_post = self.app.post('/carrinho/adicionar', data={
            'id_produto': '1', 
            'quantidade': '2'
        }, follow_redirects=True)
        
        # Verifica se houve sucesso e redirecionamento
        self.assertEqual(resposta_post.status_code, 200)
        # Verifica se a mensagem de sucesso está presente na página de destino (carrinho.html)
        self.assertIn(b'adicionado(s) ao seu carrinho', resposta_post.data)

    def test_c_checkout_sem_itens_falha(self):
        """Testa se a tentativa de checkout sem itens redireciona com mensagem de erro"""
        
        # Garante que a sessão está limpa (simula um novo usuário)
        with self.app.session_transaction() as sessao:
            sessao['cart'] = []
            
        resposta = self.app.get('/checkout', follow_redirects=True)
        
        self.assertEqual(resposta.status_code, 200)
        # Verifica se foi redirecionado para o carrinho com a mensagem de erro
        self.assertIn(b'Seu carrinho est\xc3\xa1 vazio', resposta.data) # O \xc3\xa1 representa o 'á' acentuado
        
if __name__ == '__main__':
    unittest.main()