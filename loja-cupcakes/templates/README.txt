# 🧁 Loja de Cupcakes

Este é um projeto de e-commerce simples desenvolvido em **Python** utilizando o micro-framework **Flask** e o sistema de templates **Jinja2**.

Ele simula uma loja online de cupcakes, permitindo a listagem de produtos, adição ao carrinho e simulação de checkout e login de cliente.

## 1. Início Rápido

Siga os passos abaixo para baixar, configurar e executar o projeto em seu ambiente local.

### 1.1. Pré-requisitos

* **Python 3.x** instalado.
* **VS Code** (ou qualquer editor de texto) com acesso ao terminal.

### 1.2. Estrutura de Pastas

Certifique-se de que a estrutura do seu projeto esteja organizada da seguinte forma:

├── app.py # Lógica principal (servidor Flask)

├── models.py # Simulação da camada de dados

├── static/

│ └── css/

│ └── style.css # Arquivo de estilos CSS

├── templates/

│ ├── base.html # Template principal (layout)

│ ├── produtos.html # Listagem de produtos

│ └── ... (outros .html)

└── venv/ # Ambiente Virtual (criado no passo 2)

## 2. Configuração e Instalação

Abra o projeto no terminal do VS Code e execute os comandos na ordem:

### Passo 1: Criar e Ativar o Ambiente Virtual (`venv`)

Crie e ative um ambiente virtual para isolar as dependências do projeto.

| Sistema Operacional | Comando de Criação | Comando de Ativação |
| :--- | :--- | :--- |
| **Windows (PowerShell)** | `python -m venv venv` | `.\venv\Scripts\activate` |
| **macOS/Linux** | `python3 -m venv venv` | `source venv/bin/activate` |

> 💡 Após a ativação, você verá **`(venv)`** no início da linha de comando.

### Passo 2: Instalar o Flask

Instale a biblioteca Flask dentro do ambiente virtual ativo:

```bash
pip install Flask

## 3. Como Rodar a Aplicação

Com o ambiente virtual ativo e o Flask instalado, execute o arquivo principal:

```bash
python app.py

Acesso
A aplicação será iniciada no modo de desenvolvimento. Copie e cole o endereço abaixo no seu navegador:

http://127.0.0.1:5000

4. Como Encerrar
Para parar o servidor Flask, pressione a combinação de teclas Ctrl + C no terminal.

Para sair do ambiente virtual (e voltar ao ambiente normal do sistema):

Bash

deactivate