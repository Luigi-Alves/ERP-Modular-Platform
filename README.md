# 🏢 ERP Modular – Sistema de Gestão Empresarial

> Projeto desenvolvido em **dupla**, com foco em **arquitetura corporativa**, **boas práticas** e **aprendizado real de mercado**, utilizando **Python + FastAPI**.

---

## 🎯 Visão Geral

Este projeto consiste no desenvolvimento de um **ERP (Enterprise Resource Planning) modular**, onde cada módulo representa uma área essencial de uma empresa. A aplicação foi pensada para simular **cenários reais do mercado**, priorizando organização, escalabilidade e segurança.

O sistema é estruturado em **módulos independentes**, que se comunicam via API REST utilizando **JSON**.

---

## 👥 Trabalho em Dupla

O projeto é desenvolvido por **dois desenvolvedores**, com divisão clara de responsabilidades, seguindo práticas comuns em times profissionais.

**Responsabilidades gerais:**

* Planejamento conjunto das funcionalidades
* Revisão de código entre a dupla
* Uso de Git Flow (branches + PRs)
* Documentação compartilhada

---

## 🧩 Módulos do Sistema

* 🔐 Autenticação e Usuários
* 📦 Cadastro de Produtos
* 📊 Controle de Estoque
* 🛒 Vendas
* 💰 Financeiro
* 📈 Relatórios

---

## 🏗️ Arquitetura do Projeto

```
Route (API)
   ↓
Service (Regras de Negócio)
   ↓
Repository (Persistência: JSON → SQL futuramente)
```

Essa abordagem permite iniciar o projeto utilizando **JSON em memória** e futuramente migrar para **PostgreSQL**, sem reescrever regras de negócio.

---

## 🚀 Planejamento de Sprints

### 🟢 Sprint 0 – Preparação do Projeto

**Objetivo:** criar a base profissional do sistema

* Criação do repositório GitHub
* Estrutura inicial do projeto FastAPI
* Configuração de ambiente virtual
* Padronização de commits
* Criação do README

📌 Responsabilidade: **Ambos**

---

### 🟢 Sprint 1 – Autenticação & Usuários

**Objetivo:** garantir segurança e controle de acesso

* Login
* Criação de usuários
* Hash de senha
* JWT (access token)
* Perfis (admin / user)

📌 Divisão sugerida:

* Dev A: autenticação
* Dev B: CRUD de usuários

---

### 🟢 Sprint 2 – Produtos (Master Data)

**Objetivo:** criar base de dados do sistema

* Cadastro de produtos
* Validação de dados
* Listagem e atualização
* Estrutura de repositório em JSON

📌 Trabalho colaborativo

---

### 🟢 Sprint 3 – Controle de Estoque

**Objetivo:** aplicar regras de negócio

* Entrada de estoque
* Saída de estoque
* Histórico de movimentações
* Validações (saldo negativo)

📌 Destaque para lógica de negócio

---

### 🟢 Sprint 4 – Vendas

**Objetivo:** integrar módulos

* Criação de vendas
* Associação de produtos
* Cálculo de total
* Baixa automática no estoque

📌 Uso de serviços e transações lógicas

---

### 🟢 Sprint 5 – Financeiro

**Objetivo:** simular fluxo financeiro real

* Contas a receber
* Registro automático de vendas
* Relatórios simples

---

### 🟢 Sprint 6 – Relatórios & Ajustes

**Objetivo:** visão gerencial

* Relatórios por período
* Produtos mais vendidos
* Ajustes finais
* Refatorações

---

## 🛠️ Tecnologias Utilizadas

* Python 3.11+
* FastAPI
* Pydantic
* JWT
* JSON (persistência inicial)
* Git & GitHub

> 🔄 Futuro: PostgreSQL, SQLAlchemy, Alembic, Docker

---

## 📌 Diferenciais do Projeto

* Arquitetura inspirada em sistemas corporativos
* Separação clara de responsabilidades
* Planejamento por sprints
* Projeto em dupla (simulando ambiente profissional)

---

## 🧠 Aprendizados Esperados

* Criação de APIs REST profissionais
* Trabalho em equipe com Git
* Regras de negócio reais
* Pensamento arquitetural
* Evolução gradual de persistência (JSON → SQL)

---

## 📎 Status do Projeto

🚧 Em desenvolvimento

---

## ✍️ Autores

* Desenvolvedor A
* Desenvolvedor B

---

> "Não é apenas um projeto acadêmico, é uma simulação de como sistemas empresariais são pensados e construídos no mundo real."