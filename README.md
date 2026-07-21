# Sabor Express

Sistema simples de gerenciamento de restaurantes desenvolvido em Python durante meus estudos de lógica de programação.

O projeto foi criado com o objetivo de praticar conceitos fundamentais da linguagem Python, como funções, listas, dicionários, estruturas de repetição, condicionais e organização de código.

---

## Funcionalidades

* Cadastro de novos restaurantes.
* Listagem de todos os restaurantes cadastrados.
* Alteração do status de um restaurante (Ativado/Desativado).
* Menu interativo no terminal.
* Tratamento básico para entradas inválidas.

---

## Tecnologias utilizadas

* Python 3

---

## Conceitos praticados

* Funções
* Listas
* Dicionários
* Estruturas de decisão (`if`, `elif`, `else`)
* Estruturas de repetição (`for` e `while`)
* Manipulação de dados
* Entrada e saída de dados (`input` e `print`)
* Tratamento de exceções (`try` e `except`)
* Organização e reutilização de código

---

## Estrutura do sistema

### Cadastro de restaurantes

Permite cadastrar um restaurante informando:

* Nome
* Categoria

Todo restaurante é cadastrado inicialmente com o status **Desativado**.

---

### Listagem de restaurantes

Exibe todos os restaurantes cadastrados em formato de tabela, mostrando:

* Nome
* Categoria
* Status (Ativado ou Desativado)

---

### Alteração de status

Permite localizar um restaurante pelo nome e alternar seu status entre:

* Ativado
* Desativado

Caso o restaurante não seja encontrado, o sistema informa ao usuário.

---

### Menu principal

O sistema apresenta um menu com as seguintes opções:

```text
1. Cadastrar restaurante
2. Listar restaurantes
3. Alterar estado do restaurante
4. Sair
```

---

## Estrutura de dados

Os restaurantes são armazenados em uma lista de dicionários.

Exemplo:

```python
restaurantes = [
    {
        "nome": "Mcdonald",
        "categoria": "Lanches",
        "ativo": True
    }
]
```

## Objetivo do projeto

Este projeto faz parte da minha jornada de aprendizado em Python.

O foco foi desenvolver uma aplicação de terminal utilizando boas práticas de organização de código e reforçar os principais conceitos da linguagem por meio de um projeto prático da plataforma Alura.





GitHub: https://github.com/Yasmacx
