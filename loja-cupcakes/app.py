from flask import Flask, render_template, request, redirect, url_for, session, g
import models
from datetime import datetime

app = Flask(__name__)

# CHAVE SECRETA: CRÍTICO para usar sessões
app.secret_key = 'chave_secreta_cupcake_python' 

# Middleware para injetar variáveis globais (cliente e carrinho) em todas as views
@app.before_request
def load_user_and_cart():
    g.cliente = session.get('cliente')
    g.cart = session.get('cart', [])
    
    # Injeta variáveis no contexto do Jinja para todas as renderizações
    app.jinja_env.globals['cliente'] = g.cliente
    app.jinja_env.globals['cart'] = g.cart

# ----------------------------------------------------
# ROTAS DE PRODUTOS
# ----------------------------------------------------
@app.route('/')
@app.route('/produtos')
def listar_produtos():
    produtos = models.Produto.get_todos()
    
    msg_tipo = request.args.get('msgTipo')
    msg_texto = request.args.get('msgTexto')
    mensagem = {'tipo': msg_tipo, 'texto': msg_texto} if msg_tipo and msg_texto else None

    # CORREÇÃO: Removido o .txt daqui
    return render_template('produtos.html', 
                           titulo="Nossos Cupcakes", 
                           produtos=produtos, 
                           mensagem=mensagem)

# ----------------------------------------------------
# ROTAS DE CARRINHO
# ----------------------------------------------------
@app.route('/carrinho')
def ver_carrinho():
    cart = g.cart 
    total = sum(item['preco'] * item['quantidade'] for item in cart)
    
    msg_tipo = request.args.get('msgTipo')
    msg_texto = request.args.get('msgTexto')
    mensagem = {'tipo': msg_tipo, 'texto': msg_texto} if msg_tipo and msg_texto else None

    # CORREÇÃO: Removido o .txt daqui
    return render_template('carrinho.html', 
                           titulo="Seu Carrinho", 
                           total=total,
                           mensagem=mensagem)

@app.route('/carrinho/adicionar', methods=['POST'])
def adicionar_item():
    id_produto = int(request.form.get('id_produto'))
    quantidade = int(request.form.get('quantidade'))
    produto = models.Produto.buscar_por_id(id_produto)
    
    if not produto:
        return redirect(url_for('listar_produtos', msgTipo='erro', msgTexto='Produto não encontrado.'))

    cart = session.get('cart', [])
    item_existente = next((item for item in cart if item['id_produto'] == id_produto), None)

    if item_existente:
        item_existente['quantidade'] += quantidade
    else:
        cart.append({
            'id_produto': id_produto,
            'nome': produto.nome,
            'preco': produto.preco,
            'imagemUrl': produto.imagemUrl,
            'quantidade': quantidade
        })

    session['cart'] = cart
    msg = f"🎉 {quantidade}x {produto.nome} adicionado(s) ao seu carrinho!"
    return redirect(url_for('ver_carrinho', msgTipo='sucesso', msgTexto=msg))

# ----------------------------------------------------
# ROTAS DE CHECKOUT
# ----------------------------------------------------
@app.route('/checkout')
def iniciar_checkout():
    cart = g.cart
    if not cart:
        return redirect(url_for('ver_carrinho', msgTipo='erro', msgTexto='Seu carrinho está vazio. Adicione itens para finalizar a compra.'))

    total = sum(item['preco'] * item['quantidade'] for item in cart)
    
    # CORREÇÃO: Removido o .txt daqui
    return render_template('checkout.html', 
                           titulo="Concluir Compra", 
                           total=total)

@app.route('/checkout/concluir', methods=['POST'])
def concluir_compra():
    cart = g.cart
    total = sum(item['preco'] * item['quantidade'] for item in cart)
    
    session.pop('cart', None)
    
    # CORREÇÃO: Removido o .txt daqui
    return render_template('conclusao.html', 
                           titulo="Compra Concluída!", 
                           total=total,
                           data_pedido=datetime.now().strftime("%d/%m/%Y"))

# ----------------------------------------------------
# ROTAS DE CLIENTE E LOGIN
# ----------------------------------------------------
@app.route('/cadastro')
def cadastro():
    # CORREÇÃO: Removido o .txt daqui
    return render_template('cadastro.html', titulo="Crie sua Conta")

@app.route('/cadastro', methods=['POST'])
def processar_cadastro():
    return redirect(url_for('login', msgTipo='sucesso', msgTexto='Cadastro realizado com sucesso! Faça login.'))

@app.route('/login')
def login():
    # CORREÇÃO: Removido o .txt daqui
    return render_template('login.html', titulo="Acesso do Cliente")

@app.route('/login', methods=['POST'])
def processar_login():
    email = request.form.get('email')
    
    if email:
        nome_cliente = email.split('@')[0].capitalize()
        
        session['cliente'] = {
            'id': 1, 
            'nome': nome_cliente, 
            'email': email
        }

        return redirect(url_for('listar_produtos', msgTipo='sucesso', msgTexto=f"Bem-vindo(a), {nome_cliente}!"))
    
    return redirect(url_for('login', msgTipo='erro', msgTexto='Credenciais inválidas.'))

@app.route('/logout')
def logout():
    session.pop('cliente', None)
    return redirect(url_for('listar_produtos', msgTipo='sucesso', msgTexto='Você foi desconectado com sucesso.'))


if __name__ == '__main__':
    app.run(debug=True)