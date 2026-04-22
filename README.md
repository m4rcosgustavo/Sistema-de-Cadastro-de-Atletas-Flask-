# Sistema de Cadastro de Atletas (Flask)

## 1. Introdução

Este projeto consiste no desenvolvimento de uma aplicação web utilizando o framework Flask, com o objetivo de aplicar na prática os principais conceitos de desenvolvimento web estudados em sala de aula.

A aplicação foi construída com foco na organização e gerenciamento de dados de atletas, permitindo que usuários realizem cadastro, autenticação e operações completas de manipulação de dados (CRUD).

---

## 2. Objetivo Geral

Desenvolver uma aplicação web funcional que utilize os recursos do Flask, como rotas, templates, formulários, métodos HTTP e manipulação de dados, com o propósito de resolver um problema simples do cotidiano.

---

## 3. Objetivos Específicos

* Implementar sistema de cadastro e login de usuários
* Criar rotas para navegação entre páginas
* Utilizar templates para padronização de layout
* Aplicar formulários com métodos GET e POST
* Desenvolver um CRUD completo para gerenciamento de atletas
* Utilizar parâmetros de rota e query strings
* Trabalhar com arquivos estáticos (CSS)

---

## 4. Problema Abordado

Em ambientes escolares ou esportivos, muitas vezes não há um sistema digital simples para registrar e consultar informações de atletas. Isso pode gerar desorganização, perda de dados e dificuldade no acesso às informações.

---

## 5. Justificativa

A criação deste sistema busca resolver esse problema de forma prática, oferecendo uma aplicação simples, funcional e acessível. Além disso, o desenvolvimento do projeto contribui diretamente para o aprendizado dos conceitos fundamentais de desenvolvimento web com Flask.

---

## 6. Tecnologias Utilizadas

* Python: linguagem principal utilizada no desenvolvimento
* Flask: framework web utilizado para criação da aplicação
* HTML: estrutura das páginas
* CSS: estilização da interface

---

## 7. Estrutura do Projeto

```id="rj1s0m"
projeto/
│
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── cadastro.html
│   ├── atletas.html
│   ├── form_atleta.html
│
├── static/
│   └── style.css
```

Descrição:

* app.py: arquivo principal com a lógica da aplicação e definição das rotas
* templates: arquivos HTML que compõem as páginas do sistema
* static: arquivos estáticos, como CSS

---

## 8. Funcionalidades do Sistema

### 8.1 Autenticação de Usuários

O sistema permite que usuários realizem cadastro e login. Após o login, é criada uma sessão que permite o acesso às funcionalidades internas da aplicação.

Também foi implementada a funcionalidade de logout, que encerra a sessão do usuário.

---

### 8.2 Gerenciamento de Atletas (CRUD)

A aplicação possui uma entidade principal chamada "Atleta", que contém os seguintes dados:

* Nome
* Idade
* Esporte

Operações disponíveis:

* Criar: cadastro de novos atletas
* Ler: listagem de atletas cadastrados
* Atualizar: edição de dados de um atleta
* Deletar: remoção de atletas

---

### 8.3 Filtro de Busca

Foi implementado um sistema de busca utilizando query string, permitindo filtrar atletas pelo nome diretamente pela URL.

Exemplo:

```
/atletas?busca=nome
```

---

### 8.4 Rotas Parametrizadas

O sistema utiliza parâmetros de rota para identificar atletas específicos durante operações como edição e exclusão.

Exemplo:

```
/edit/1
```

---

### 8.5 Templates e Layout

Foi utilizado um template base (base.html) para padronizar a estrutura visual das páginas, evitando repetição de código e facilitando a manutenção.

---

### 8.6 Arquivos Estáticos

A aplicação utiliza um arquivo CSS externo para estilização, garantindo separação entre estrutura e aparência.

---

## 9. Rotas da Aplicação

| Rota           | Método   | Descrição               |
| -------------- | -------- | ----------------------- |
| `/`            | GET      | Página inicial          |
| `/cadastro`    | GET/POST | Cadastro de usuário     |
| `/login`       | GET/POST | Autenticação do usuário |
| `/logout`      | GET      | Encerrar sessão         |
| `/atletas`     | GET      | Listagem de atletas     |
| `/add`         | GET/POST | Cadastro de atleta      |
| `/edit/<id>`   | GET/POST | Edição de atleta        |
| `/delete/<id>` | GET      | Remoção de atleta       |

---

## 10. Como Executar o Projeto

1. Clonar o repositório:

```id="pzn7nx"
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acessar a pasta do projeto:

```id="xy9tnt"
cd seu-repositorio
```

3. Instalar as dependências:

```id="yo4qsr"
pip install flask
```

4. Executar a aplicação:

```id="o0te8n"
python app.py
```

5. Acessar no navegador:

```id="s4z1q9"
http://127.0.0.1:5000/
```

---

## 11. Requisitos Atendidos

* Criação de rotas
* Redirecionamento entre páginas
* Uso de templates
* Uso de arquivos estáticos
* Manipulação de formulários
* Uso dos métodos GET e POST
* Utilização de parâmetros de rota
* Implementação de query strings
* Sistema de autenticação
* CRUD completo

---

## 12. Integrantes

* Marcos Gustavo
* Heloisa Pereira
* Jullyane Sandra
* Maria Luiza 

---

## 13. Considerações Finais

O desenvolvimento deste projeto permitiu aplicar na prática diversos conceitos importantes do desenvolvimento web com Flask. Foi possível compreender melhor a estrutura de uma aplicação web, a organização de rotas, o uso de templates e a interação com formulários.

Além disso, o projeto reforça a importância de soluções simples para problemas reais, demonstrando como a tecnologia pode ser utilizada para melhorar a organização e o acesso à informação.

---
