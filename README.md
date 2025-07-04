# 🏦 Sistema Bancário Interativo em Python

Este projeto é uma simulação de um sistema bancário simples, feito em Python, com suporte para múltiplos usuários e conta-corrente vinculada automaticamente no momento do cadastro.

## 💡 Funcionalidades

- Cadastro de usuários com CPF, nome, data de nascimento e endereço
- Geração automática de conta-corrente vinculada ao usuário
- Login por CPF
- Depósitos (após login)
- Saques com regras:
  - Até 3 saques por dia
  - Limite de R$500 por saque
  - Sem permitir saques acima do saldo
- Extrato bancário
- Interface via terminal interativo

## 📋 Menu de opções

[c] Cadastrar usuário
[l] Login
[s] Saque
[d] Depósito
[e] Extrato
[q] Sair


## 🧱 Estrutura do código

- **usuarios**: lista de dicionários com dados cadastrais
- **contas**: lista de contas vinculadas aos usuários
- **saldo, extrato, limite de saque**: gerenciados globalmente (versão simples)
- **Funções principais**:
  - `criar_usuario()`
  - `login()`
  - `saque(valor)`
  - `deposito(valor)`
  - `ver_extrato()`

## 🚀 Como usar

1. Execute o script em um terminal com Python 3:
   ```bash
   python sistema_banco.py
📌 Observações
Este é um projeto didático e serve como base para aplicar conceitos de:

Estruturas de dados (listas, dicionários)

Funções e escopo

Entrada/saída no terminal

Validações e lógica de negócio simples
