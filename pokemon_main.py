import random
from colorama import init, Fore, Back, Style
from term_image.image import from_url
import pygame
import requests
import tempfile
import os
# Teste de commit

init(autoreset=True)
pygame.init()
pygame.mixer.init()
musica = "https://play.pokemonshowdown.com/audio/hgss-johto-trainer.mp3"
# Lista de Pokémons com todas as informações e os dois ataques
listaPokemons = [
    {
        "exibNome": f"{Back.LIGHTGREEN_EX}{Fore.GREEN}Bulbasaur{Style.RESET_ALL}",
        "nome": "Bulbasaur",
        "tipo": ["Planta", "Veneno"],
        "vida": 100,
        "ataque": 25,
        "critico": 30,
        "descricao": "Uma estranha semente foi plantada em suas costas ao nascer.",
        "fraquezas": ["Fogo", "Gelo", "Voador", "Psíquico"],
        "nomeAtaque": "Chicote de Vinha",
        "danoAtaque": 25,
        "nomeAtaque2": "Semente Sanguessuga",
        "danoAtaque2": 35,
        "audio": "https://play.pokemonshowdown.com/audio/cries/bulbasaur.mp3",
        "imagem": "https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/001.png"
    },
    {
        "exibNome": f"{Back.LIGHTRED_EX}{Fore.RED}Charmander{Style.RESET_ALL}",
        "nome": "Charmander",
        "tipo": ["Fogo"],
        "vida": 100,
        "ataque": 52,
        "critico": 30,
        "descricao": "Desde que nasce, uma chama queima na ponta de sua cauda.",
        "fraquezas": ["Água", "Terra", "Pedra"],
        "nomeAtaque": "Presas de Fogo",
        "danoAtaque": 52,
        "nomeAtaque2": "Brasa",
        "danoAtaque2": 40,
        "audio": "https://play.pokemonshowdown.com/audio/cries/charmander.mp3",
        "imagem": "https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/004.png"
    },
    {
        "exibNome": f"{Back.LIGHTBLUE_EX}{Fore.BLUE}Squirtle{Style.RESET_ALL}",
        "nome": "Squirtle",
        "tipo": ["Água"],
        "vida": 100,
        "ataque": 48,
        "critico": 25,
        "descricao": "Quando retrai seu longo pescoço em sua concha, esguicha água com força.",
        "fraquezas": ["Elétrico", "Planta"],
        "nomeAtaque": "Jato d'Água",
        "danoAtaque": 48,
        "nomeAtaque2": "Bolhas",
        "danoAtaque2": 30,
        "audio": "https://play.pokemonshowdown.com/audio/cries/squirtle.mp3",
        "imagem": "https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/007.png"
    },
    {
        "exibNome": f"{Back.YELLOW}{Fore.BLACK}Pikachu{Style.RESET_ALL}",
        "nome": "Pikachu",
        "tipo": ["Elétrico"],
        "vida": 100,
        "ataque": 55,
        "critico": 35,
        "descricao": "Quando vários desses Pokémon se reúnem, sua eletricidade pode causar tempestades.",
        "fraquezas": ["Terra"],
        "nomeAtaque": "Choque do Trovão",
        "danoAtaque": 55,
        "nomeAtaque2": "Investida Trovão",
        "danoAtaque2": 60,
        "audio": "https://play.pokemonshowdown.com/audio/cries/pikachu.mp3",
        "imagem": "https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/025.png"
    },
    {
        "exibNome": f"{Back.MAGENTA}{Fore.WHITE}Jigglypuff{Style.RESET_ALL}",
        "nome": "Jigglypuff",
        "tipo": ["Normal", "Fada"],
        "vida": 115,
        "ataque": 45,
        "critico": 25,
        "descricao": "Usa suas cordas vocais especiais para entoar uma canção de ninar que faz os inimigos dormirem.",
        "fraquezas": ["Aço", "Venenoso"],
        "nomeAtaque": "Canção Adormecedora",
        "danoAtaque": 45,
        "nomeAtaque2": "Tapa",
        "danoAtaque2": 30,
        "audio": "https://play.pokemonshowdown.com/audio/cries/jigglypuff.mp3",
        "imagem": "https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/039.png"
    }
]

def musicaBatalha(url):
    try:
        musicaFundo = requests.get(url)
        tempMusic = tempfile.NamedTemporaryFile(delete=False)
        tempMusic.write(musicaFundo.content)
        tempMusic.close()
        pygame.mixer.init()
        pygame.mixer.music.load(tempMusic.name)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(loops=-1)
    except Exception as e:
        print(f"Erro ao reproduzir musica de fundo {e}")

def iniciarSons(url):
    try:
        som = requests.get(url)
        audioTemporario = tempfile.NamedTemporaryFile (delete=False)
        audioTemporario.write(som.content)    
        audioTemporario.close()
        efeito_sonoro = pygame.mixer.Sound(audioTemporario.name)
        efeito_sonoro.set_volume(0.4)
        efeito_sonoro.play()
    except Exception as e:
        print(f"Erro ao carregar o som: {e}")

# Função para iniciar o jogo (2 jogadores)
def iniciarJogo():
    print("Jogo inciado\n")
    escolhaJogador1 = jogador1()
    escolhaJogador2 = jogador2(escolhaJogador1)

    print(f"{Back.LIGHTBLUE_EX}Jogador 1 escolheu{Style.RESET_ALL} - {escolhaJogador1['exibNome']}")
    print(f"{Back.LIGHTRED_EX}Jogador 2 escolheu{Style.RESET_ALL} - {escolhaJogador2['exibNome']}")

    if escolhaJogador1 and escolhaJogador2:
        iniciarBatalha(escolhaJogador1, escolhaJogador2)
    else:
        print("Erro na escolha dos Pokémons.")


# Função para iniciar o jogo (vs IA)
def iniciarJogoIA():
    print("Jogo inciado\n")
    escolhaJogador1 = jogador1()
    escolhaIA = jogadorIA(escolhaJogador1)

    print(f"{Back.LIGHTBLUE_EX}Jogador 1 escolheu{Style.RESET_ALL} - {escolhaJogador1['exibNome']}")
    print(f"{Back.LIGHTRED_EX}IA escolheu{Style.RESET_ALL} - {escolhaIA['exibNome']}")

    if escolhaJogador1 and escolhaIA:
        iniciarBatalhaIA(escolhaJogador1, escolhaIA)
    else:
        print("Erro na escolha dos Pokémons.")


# Função para mostrar imagem direto no terminal
def mostrarImagemTerminal(url):
    try:
        img = from_url(url, width=50)
        print(img)
    except Exception as e:
        print(f"❌ Erro ao carregar imagem: {e}")


# Função para mostrar a Pokédex
def iniciarPokedex():
    while True:
        print("Digite o numero do pokemon para exibir as informações do mesmo.")
        for i, pokemon in enumerate(listaPokemons):
            print(f"{i + 1} - {pokemon['exibNome']}\n")
        print("0 - Voltar ao menu!")

        try:
            exibInfo = int(input())
        except ValueError:
            print("Digite um número válido!\n")
            continue

        match exibInfo:
            case 0:
                print("Voltando ao menu.")
                break
            case 1 | 2 | 3 | 4 | 5:
                p = listaPokemons[exibInfo - 1]
                iniciarSons(p['audio'])
                print(f"{p['exibNome']}")
                print(f"Tipo - {', '.join(p['tipo'])}")
                print(f"Fraquezas - {', '.join(p['fraquezas'])}")
                print(f"Vida - {Fore.GREEN}{p['vida']}{Style.RESET_ALL}")
                print(f"Ataque {p['nomeAtaque']} - Dano: {Fore.GREEN}{p['danoAtaque']}{Style.RESET_ALL}")
                print(f"Ataque {p['nomeAtaque2']} - Dano: {Fore.GREEN}{p['danoAtaque2']}{Style.RESET_ALL}")
                print(f"Chance de Crítico: {Fore.RED}{p['critico']}%{Style.RESET_ALL}")
                print(f"{Fore.WHITE}{p['descricao']}{Style.RESET_ALL}")
                mostrarImagemTerminal(p['imagem'])
                input("Pressione ENTER para continuar...")

            case _:
                print("Digite uma opção válida!")
        print("\n")


# Função para o jogador 1 escolher Pokémon
def jogador1():
    print("Jogador 1, escolha seu pokemon.")
    for i, pokemon in enumerate(listaPokemons):
        print(f"{i + 1} - {pokemon['exibNome']}\n")
    while True:
        try:
            escolha = int(input("Qual é o seu pokemon: "))
            if 1 <= escolha <= len(listaPokemons):
                return listaPokemons[escolha - 1]
            else:
                print("Pokemon indisponível")
        except ValueError:
            print("Digite um número válido!")


# Função para o jogador 2 escolher Pokémon
def jogador2(escolhaJogador1):
    print("Jogador 2, escolha seu pokemon.")
    while True:
        for i, pokemon in enumerate(listaPokemons):
            if pokemon['nome'] != escolhaJogador1['nome']:
                print(f"{i + 1} - {pokemon['exibNome']}\n")
        try:
            escolha = int(input("Qual é o seu pokemon: "))
            if 1 <= escolha <= len(listaPokemons):
                escolhido = listaPokemons[escolha - 1]
                if escolhido['nome'] == escolhaJogador1['nome']:
                    print("Esse pokemon já foi escolhido, escolha outro\n")
                else:
                    return escolhido
            else:
                print("Pokemon indisponivel")
        except ValueError:
            print("Digite um número válido!")


# Função para calcular o dano
def calcularDano(pokemon, escolhaAtaque):
    dano = 0
    if escolhaAtaque == 1:
        dano = pokemon['danoAtaque']
        nome_ataque_usado = pokemon['nomeAtaque']
    elif escolhaAtaque == 2:
        dano = pokemon['danoAtaque2']
        nome_ataque_usado = pokemon['nomeAtaque2']
    else:  # Caso de opção inválida, retorna 0 dano
        return 0, "Ação Inválida"

# calcula a chance de dar dano critico
    chanceCritico = random.randint(1, 100)
    if chanceCritico <= pokemon['critico']:
        dano *= 1.25
        print(f" Dano Crítico de {pokemon['nome']} com {nome_ataque_usado}! ")
    else:
        print(f"{pokemon['nome']} usou {nome_ataque_usado}!")

    return dano, nome_ataque_usado


# Função de batalha para 2 jogadores
def iniciarBatalha(pokemon1, pokemon2):
    vidaP1 = pokemon1['vida']
    vidaP2 = pokemon2['vida']
    turno = 1
    musicaBatalha(musica)
    while vidaP1 > 0 and vidaP2 > 0:
        print(f"\n=== Turno {turno} ===")
        print(f"Vida de {pokemon1['nome']}: {Fore.GREEN}{vidaP1}{Style.RESET_ALL}")
        print(f"Vida de {pokemon2['nome']}: {Fore.GREEN}{vidaP2}{Style.RESET_ALL}")

        # Ataque do Jogador 1
        print(f"\n= {pokemon1['exibNome']} - Sua vez! =")
        print(f"1 - Usar {pokemon1['nomeAtaque']} (Dano: {pokemon1['danoAtaque']})")
        print(f"2 - Usar {pokemon1['nomeAtaque2']} (Dano: {pokemon1['danoAtaque2']})")
        print("3 - Correr da batalha")

        try:
            escolha_p1 = int(input("Escolha sua ação: "))
        except ValueError:
            print("Opção inválida. Perdeu a vez.")
            escolha_p1 = 0  # Valor inválido para não atacar

        if escolha_p1 == 3:
            print(f"\n{pokemon1['nome']} desistiu. {pokemon2['nome']} venceu!")
            pygame.mixer.music.stop()
            break
        elif escolha_p1 in [1, 2]:
            dano_causado, nome_ataque_usado = calcularDano(pokemon1, escolha_p1)
            vidaP2 -= dano_causado
            iniciarSons(pokemon1['audio'])
            print(f"{pokemon1['nome']} causou {dano_causado} de dano em {pokemon2['nome']}!")
            if vidaP2 <= 0:
                print(f"\n{pokemon2['nome']} desmaiou! {pokemon1['nome']} venceu!")
                print(f"A partida durou {turno} turnos.")
                pygame.mixer.music.stop()
                break
        else:
            print("Opção inválida. Nenhuma ação realizada.")

        # Ataque do Jogador 2 (se a batalha ainda estiver ativa)
        if vidaP1 > 0 and vidaP2 > 0:
            print(f"\n= {pokemon2['exibNome']} - Sua vez! =")
            print(f"1 - Usar {pokemon2['nomeAtaque']} (Dano: {pokemon2['danoAtaque']})")
            print(f"2 - Usar {pokemon2['nomeAtaque2']} (Dano: {pokemon2['danoAtaque2']})")
            print("3 - Correr da batalha")

            try:
                escolha_p2 = int(input("Escolha sua ação: "))
            except ValueError:
                print("Opção inválida. Perdeu a vez.")
                escolha_p2 = 0  # Valor inválido para não atacar

            if escolha_p2 == 3:
                print(f"\n{pokemon2['nome']} desistiu. {pokemon1['nome']} venceu!")
                pygame.mixer.music.stop()
                break
            elif escolha_p2 in [1, 2]:
                dano_causado, nome_ataque_usado = calcularDano(pokemon2, escolha_p2)
                vidaP1 -= dano_causado
                iniciarSons(pokemon2['audio'])
                print(f"{pokemon2['nome']} causou {dano_causado} de dano em {pokemon1['nome']}!")
                if vidaP1 <= 0:
                    print(f"\n{pokemon1['nome']} desmaiou! {pokemon2['nome']} venceu!")
                    print(f"A partida durou {turno} turnos.")
                    pygame.mixer.music.stop()
                    break
            else:
                print("Opção inválida. Nenhuma ação realizada.")

        turno += 1


# Função de batalha contra IA
def iniciarBatalhaIA(pokemon1, pokemonIA):
    vidaP1 = pokemon1['vida']
    vidaIA = pokemonIA['vida']
    turno = 1
    musicaBatalha(musica)
    while vidaP1 > 0 and vidaIA > 0:
        print(f"\n=== Turno {turno} ===")
        print(f"Vida de {pokemon1['nome']}: {Fore.GREEN}{vidaP1}{Style.RESET_ALL}")
        print(f"Vida de {pokemonIA['nome']}: {Fore.GREEN}{vidaIA}{Style.RESET_ALL}")

        # Ataque do Jogador
        print(f"\n= {pokemon1['exibNome']} - Sua vez! =")
        print(f"1 - Usar {pokemon1['nomeAtaque']} (Dano: {pokemon1['danoAtaque']})")
        print(f"2 - Usar {pokemon1['nomeAtaque2']} (Dano: {pokemon1['danoAtaque2']})")
        print("3 - Correr da batalha")

        try:
            escolha_p1 = int(input("Escolha sua ação: "))
        except ValueError:
            print("Opção inválida. Perdeu a vez.")
            escolha_p1 = 0  # Valor inválido para não atacar

        if escolha_p1 == 3:
            print(f"\nVocê desistiu. A IA venceu!")
            pygame.mixer.music.stop()
            break
        elif escolha_p1 in [1, 2]:
            dano_causado, nome_ataque_usado = calcularDano(pokemon1, escolha_p1)
            vidaIA -= dano_causado
            iniciarSons(pokemon1['audio'])
            print(f"{pokemon1['nome']} causou {dano_causado} de dano em {pokemonIA['nome']}!")
            if vidaIA <= 0:
                print(f"\n{pokemonIA['nome']} desmaiou! Você venceu!")
                print(f"A partida durou {turno} turnos.")
                pygame.mixer.music.stop()
                break
        else:
            print("Opção inválida. Nenhuma ação realizada.")

        # Ataque da IA (se a batalha ainda estiver ativa)
        if vidaP1 > 0 and vidaIA > 0:
            print(f"\n= {pokemonIA['exibNome']} - Vez da IA! =")
            # A IA escolhe um ataque aleatório entre 1 e 2
            escolha_ia = random.choice([1, 2])
            dano_causado, nome_ataque_usado = calcularDano(pokemonIA, escolha_ia)
            vidaP1 -= dano_causado
            iniciarSons(pokemonIA['audio'])
            print(
                f"A IA ({pokemonIA['nome']}) atacou com {nome_ataque_usado} e causou {dano_causado} de dano em {pokemon1['nome']}!")
            if vidaP1 <= 0:
                print(f"\n{pokemon1['nome']} desmaiou! A IA venceu!")
                print(f"A partida durou {turno} turnos.")
                pygame.mixer.music.stop()
                break

        turno += 1


# Função para a IA escolher Pokémon
def jogadorIA(pokemon1):
    while True:  # Loop para garantir que a IA não escolha o mesmo pokemon
        pokemonIA = random.choice(listaPokemons)
        if pokemonIA['nome'] != pokemon1['nome']:  # Verifica se é diferente do pokemon do jogador 1
            return pokemonIA

def limparConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Console limpo!\n")
# Menu principal
while True:
    print("\n--- MENU POKÉMON ---")
    print("1 - Iniciar Jogo 2 Jogadores")
    print("2 - Iniciar Jogo 1 Jogador (vs IA)")
    print("3 - Ver Pokédex")
    print("4 - Limpar Console")
    print("5 - Sair\n")
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Digite um número válido!\n")
        continue

    match opcao:
        case 1:
            iniciarJogo()
        case 2:
            iniciarJogoIA()
        case 3:
            iniciarPokedex()
        case 4:
            limparConsole()
        case 5:
            print("Obrigado por jogar!\n")
            break
        case _:
            print("Opção inválida, escolha novamente.\n")


input("Pressione ENTER para sair...")
