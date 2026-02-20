# 🐾 Catômetro 🐾 - Que Gato Sou Eu?

Bem-vindo ao projeto **Catômetro**! Esta é uma aplicação interativa desenvolvida para que os usuários descubram qual gatinho melhor representa sua personalidade no momento, utilizando integração com APIs externas e um design moderno.

## Índice

*   [Sobre o Projeto](#sobre-o-projeto)
*   [Tecnologias Utilizadas](#tecnologias-utilizadas)
*   [Funcionalidades Implementadas](#funcionalidades-implementadas)
*   [Como Executar o Projeto Localmente](#como-executar-o-projeto-localmente)
*   [Estrutura do Projeto](#estrutura-do-projeto)
*   [Contato](#contato)

## Sobre o Projeto

O objetivo deste projeto é criar uma experiência lúdica onde o usuário insere seu nome e recebe uma imagem aleatória de um gato vinda da **TheCatAPI**. O diferencial do projeto é a capacidade de processar o download da imagem já renomeada com o nome do usuário, além de manter o estado da aplicação através de sessões do Flask.

## Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

*   **Python:** Linguagem de programação para a lógica de back-end.
*   **Flask:** Framework web para gerenciamento de rotas e sessões.
*   **Tailwind CSS:** Framework utilitário para um design responsivo e elegante.
*   **TheCatAPI:** API pública REST para fornecimento dinâmico de fotos de felinos.
*   **Requests:** Biblioteca Python para realizar requisições HTTP.
*   **Jinja2:** Motor de templates para integração de dados no HTML.

## Funcionalidades Implementadas

*   **Identificação de Gatinho:**
    *   Formulário intuitivo para inserção do nome do usuário.
    *   Busca dinâmica de imagens via API externa.
*   **Download Inteligente:**
    *   Botão para download da imagem processado via buffer de memória (`io.BytesIO`).
    *   O arquivo baixado é automaticamente nomeado com o nome do usuário (ex: `lorena.jpg`).
*   **Design e Experiência do Usuário (UX):**
    *   Mensagens de erro (*Flash Messages*) estilizadas para campos vazios.
    *   Paleta de cores em tons de marrom e bege (estilo "Coffee & Cats").
    *   Efeito de animação (*hover*) na imagem do gatinho.
    *   Funcionalidade de "Reset" para limpar a memória do navegador e trocar de nome.

## Como Executar o Projeto Localmente

Para visualizar este projeto em sua máquina local, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/catometro.git
    cd catometro
    ```

2.  **Instale as dependências:**
    ```bash
    pip install flask requests
    ```

3.  **Execute o servidor:**
    ```bash
    python app.py
    ```

4.  **Acesse no seu navegador:**
    Abra o endereço: `http://127.0.0.1:5000`

## Estrutura do Projeto
```text
.
├── static/
│   ├── favicon.png          # Ícone da aplicação
│   └── null.webp            # Imagem de fallback
├── templates/
│   └── index.html           # Template front-end (Jinja2 + Tailwind)
├── app.py                   # Servidor Flask e rotas
└── README.md                # Documentação
```
## Contato
* Desenvolvido por: Lorena Rinaldo Moreira
* Vercel: https://cat-o-metro.vercel.app/
* GitHub: https://github.com/Lorena-Rinaldo
* LinkedIn: www.linkedin.com/in/lorena-rinaldo01
* Email: lorena.rinaldodev@gmail.com
