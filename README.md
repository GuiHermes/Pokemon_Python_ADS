## Sobre

Um jogo de batalha Pokémon feito em Python, com suporte a **2 jogadores ou 1 jogador vs IA**, com sons, imagens no terminal e Pokédex interativa.

## Funcionalidades

* Escolha de Pokémon para **2 jogadores** ou contra a **IA**.
* Cada Pokémon possui:

  * Vida, ataque, chance de crítico, tipos e fraquezas.
  * Dois ataques diferentes com dano específico.
  * Som ao atacar e música de fundo durante a batalha.
  * Imagem exibida no terminal.
* **Pokédex interativa** para consultar informações dos Pokémons.
* Console pode ser limpo diretamente do menu.

## Tecnologias

* Python 3
* `pygame` – para sons e música de fundo
* `colorama` – para cores no terminal
* `term-image` – para exibir imagens no terminal
* `requests` e `tempfile` – para baixar e tocar áudio temporário

## Como jogar

1. Execute o arquivo Python:

```bash
python pokemon_main.py
```

2. Escolha uma opção no menu:

   * Iniciar jogo 2 jogadores
   * Iniciar jogo 1 jogador (vs IA)
   * Ver Pokédex
   * Limpar console
   * Sair

3. Durante a batalha:

   * Escolha entre os ataques disponíveis ou desista.
   * A batalha termina quando a vida de um Pokémon chega a zero.

## Observações

* O jogo exibe imagens no terminal usando `term-image`, mas a aparência pode variar dependendo do terminal.
* Mais Pokémons podem ser adicionados à lista facilmente, sem alterar a lógica da Pokédex.

## Integrantes

* Guilherme - https://github.com/GuiHermes
* Matheus - https://github.com/Matheus-Rod03
* Gustavo - https://github.com/gurezende7
* Hian - https://github.com/hian128
