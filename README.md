# Redis Study

Repositório criado para estudar Redis com Python e registrar, na prática, os
principais conceitos aprendidos durante o curso.

Além dos exercícios isolados, o projeto possui uma aplicação final que simula
uma camada de cache em um backend: o Redis guarda os dados temporariamente para
leituras rápidas, enquanto um arquivo JSON representa a fonte persistente de
dados.

## O que foi estudado

- Criação de uma conexão com Redis usando `redis-py`.
- Operações básicas de chave-valor (`set`, `get`, `exists` e `delete`).
- Estruturas do tipo hash (`hset`, `hget`, `hgetall` e `hdel`).
- Expiração de chaves e TTL (*Time To Live*) com `expire` e `set(..., ex=...)`.
- Organização do acesso ao Redis usando repositórios e um serviço de aplicação.

## Projeto final: emulação de cache

O projeto final está em [`src`](src) e oferece uma interface de linha de
comando com três operações:

- `add`: grava a chave e o valor no Redis e no arquivo [`src/database/db.json`](src/database/db.json).
- `get`: procura primeiro no Redis. Se a chave não estiver no cache, consulta o JSON.
- `update`: atualiza o valor no Redis e na fonte persistente.

As chaves gravadas pelo repositório Redis expiram após **30 segundos**. Assim,
o comportamento simulado é:

1. Uma escrita atualiza o cache e a fonte persistente.
2. Uma leitura recente é atendida pelo Redis, representando um *cache hit*.
3. Depois da expiração, a leitura consulta o JSON, representando um *cache miss*.

O objetivo é demonstrar a ideia central de um cache backend sem depender de um
banco de dados completo. Em uma aplicação real, o cache poderia ficar na
frente de um banco como PostgreSQL ou MySQL.

## Requisitos

- Python 3.12 ou superior.
- Redis em execução em `localhost:6379`.
- Poetry 2 ou uma instalação equivalente das dependências do projeto.

## Como executar

Clone o repositório e instale as dependências:

```bash
poetry install
```

Inicie o Redis localmente. Com Docker, por exemplo:

```bash
docker run --name redis-course -p 6379:6379 -d redis
```

Execute a aplicação pelo ambiente virtual do Poetry:

```bash
poetry run python src/run.py add name Daniel
poetry run python src/run.py get name
poetry run python src/run.py update name "Daniel Batista"
poetry run python src/run.py get name
```

Também é possível executar sem abrir um shell separado:

```bash
poetry run python src/run.py get name
```

Para conferir os comandos disponíveis:

```bash
poetry run python src/run.py --help
```

O Redis precisa estar disponível antes da execução. Caso contrário, a conexão
com `localhost:6379` falhará.

## Lições

Os exemplos progressivos estão organizados em [`lessons`](lessons):

1. [`1_create_connection`](lessons/1_create_connection): conexão, chaves,
	 hashes e verificação de existência.
2. [`2_methods`](lessons/2_methods): encapsulamento das operações em um
	 repositório.
3. [`3_expiration_ttl`](lessons/3_expiration_ttl): definição de expiração para
	 chaves e hashes.

## Bibliotecas utilizadas

- [`redis`](https://redis.readthedocs.io/): cliente Python oficial para
	comunicação com o Redis.
- `argparse`: biblioteca padrão usada para construir a interface de linha de
	comando.
- `json`, `pathlib`, `dataclasses` e `typing`: bibliotecas padrão utilizadas
	para persistência local, configuração e organização do código.

As dependências do projeto estão declaradas no [`pyproject.toml`](pyproject.toml).

## Estrutura principal

```text
.
+-- lessons/                 # Exercicios sobre os recursos do Redis
+-- src/
|   +-- database/db.json     # Fonte persistente simulada
|   +-- repositories/        # Acesso ao JSON e ao Redis
|   +-- services/            # Regras do fluxo de cache
|   +-- models.py            # Modelos dos comandos
|   +-- utils.py             # Parser e comandos da CLI
|   +-- run.py               # Ponto de entrada do projeto final
+-- pyproject.toml           # Dependencias e configuracao do projeto
+-- poetry.lock              # Versoes bloqueadas das dependencias
```
