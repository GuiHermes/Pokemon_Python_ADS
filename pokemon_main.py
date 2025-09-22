import random
from colorama import init, Fore, Back, Style
from term_image.image import from_url
import pygame
import requests
import tempfile

pygame.init()
pygame.mixer.init()

 # Biblioteca para exibir imagens no terminal
init(autoreset=True)  # Faz com que cada print não "herde" cores do anterior
musica = "https://play.pokemonshowdown.com/audio/hgss-johto-trainer.mp3"




# Lista de Pokémons com todas as informações
listaPokemons = [
    {
        "exibNome": f"{Back.LIGHTGREEN_EX}{Fore.GREEN}Bulbasaur{Style.RESET_ALL}",
        "nome": "Bulbasaur",
        "tipo": ["Planta", "Veneno"],
        "vida": 100,
        "ataque": 49,
        "critico": 30,
        "descricao": "Uma estranha semente foi plantada em suas costas ao nascer.",
        "fraquezas": ["Fogo", "Gelo", "Voador", "Psíquico"],
        "nomeAtaque": "Chicote de Vinha",
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
        "audio": "https://play.pokemonshowdown.com/audio/cries/squirtle.mp3",
        "imagem": "https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/007.png"
    },
    {
        "exibNome": f"{Back.YELLOW}{Fore.BLACK}Pikachu{Style.RESET_ALL}",
        "nome": "Pikachu",
        "tipo": ["Elétrico"],
        "vida": 100,
        "ataque": 55,
        "critico": 40,
        "descricao": "Quando vários desses Pokémon se reúnem, sua eletricidade pode causar tempestades.",
        "fraquezas": ["Terra"],
        "nomeAtaque": "Choque do Trovão",
        "audio": "https://play.pokemonshowdown.com/audio/cries/pikachu.mp3",        "imagem": "https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/025.png"
    },
    {
        "exibNome": f"{Back.MAGENTA}{Fore.WHITE}Jigglypuff{Style.RESET_ALL}",
        "nome": "Jigglypuff",
        "tipo": ["Normal", "Fada"],
        "vida": 115,
        "ataque": 45,
        "critico": 20,
        "descricao": "Usa suas cordas vocais especiais para entoar uma canção de ninar que faz os inimigos dormirem.",
        "fraquezas": ["Aço", "Venenoso"],
        "nomeAtaque": "Canção Adormecedora",
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

# Função para iniciar o jogo
def iniciarJogo():
    print("Jogo inciado\n")
    escolhaJogador1 = jogador1()
    escolhaJogador2 = jogador2(escolhaJogador1)

    # Mostra a escolha de cada jogador
    print(f"{Back.LIGHTBLUE_EX}Jogador 1 escolheu{Style.RESET_ALL} - {escolhaJogador1['exibNome']}")
    print(f"{Back.LIGHTRED_EX}Jogador 2 escolheu{Style.RESET_ALL} - {escolhaJogador2['exibNome']}")

    if escolhaJogador1 and escolhaJogador2:
        iniciarBatalha(escolhaJogador1, escolhaJogador2)  # ✅ Passa os pokémons como parâmetro
    else:
        print("Escolha os pokemons primeiro")


def iniciarJogoIA():
    print("Jogo inciado\n")
    escolhaJogador1 = jogador1()
    escolhaIA = jogadorIA(escolhaJogador1)

    # Mostra a escolha de cada jogador
    print(f"{Back.LIGHTBLUE_EX}Jogador 1 escolheu{Style.RESET_ALL} - {escolhaJogador1['exibNome']}")
    print(f"{Back.LIGHTRED_EX}IA escolheu{Style.RESET_ALL} - {escolhaIA['exibNome']}")

    if escolhaJogador1 and escolhaIA:
        print("Até aqui funcionou")
        iniciarBatalhaIA(escolhaJogador1, escolhaIA)  # ✅ Passa os pokémons como parâmetro
    else:
        print("Escolha os pokemons primeiro")


# Função para mostrar imagem direto no terminal
def mostrarImagemTerminal(url):
    try:
        img = from_url(url, width=50)  # largura em caracteres
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
            exibInfo = int(input())  # Recebe a opção do usuário
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
                print(f"Vida - {Fore.GREEN}{p['vida']}")
                print(f"Ataque {Fore.GREEN}{p['ataque']}{Style.RESET_ALL} - Crítico - {Fore.RED}{p['critico']}")
                print(f"{Fore.WHITE}{p['descricao']}")

                # Mostrar imagem no terminal
                mostrarImagemTerminal(p['imagem'])
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
                return listaPokemons[escolha - 1]  # ✅ Retorna dicionário completo
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


# Função placeholder para iniciar batalha (não implementada)
def calcularDanoP1(pokemon):
    dano = pokemon['ataque']
    chanceCritico = random.randint(1, 100)
    if chanceCritico >= 95:
        dano = dano * 2
        print(f"Dano Critico de {pokemon['nome']} - {dano}")
    return dano


def iniciarBatalha(pokemon1, pokemon2):
    vidaP1 = pokemon1['vida']
    vidaP2 = pokemon2['vida']
    turno = 1
    musicaBatalha(musica)
    while vidaP1 > 0 and vidaP2 > 0:
        print(f"=== Turno  {turno} ===")
        pularTurno = int(input("= Jogador 1 =\n1 - Atacar\n2 - Correr da batalha\n"))
        if pularTurno not in [1, 2]:
            print("Opção inválida.")
            continue
        if pularTurno == 1:
            dano = calcularDanoP1(pokemon1)
            vidaP2 = vidaP2 - dano
            iniciarSons(pokemon1['audio'])
            print(
                f"P1 - {pokemon1['nome']} atacou com {pokemon1['nomeAtaque']} tirou {dano} de vida de {pokemon2['nome']} ")

            if vidaP2 <= 0:
                print(f"{pokemon2['nome']} desmaiou - Jogador 1 Venceu!")
                print(f"A partida durou {turno} turnos.")
                pygame.mixer.music.stop()
                break

        else:
            print("Jogador 1 desistiu da partida, o Jogador 2 venceu!")
            print(f"A partida durou {turno} turnos.")
            pygame.mixer.music.stop()
            break

        pularTurno = int(input("= Jogador 2 =\n1 - Atacar\n2 - Correr da batalha\n"))
        if pularTurno not in [1, 2, 3]:
            print("Opção inválida.")
            continue
        if pularTurno == 1:
            dano = calcularDanoP1(pokemon2)
            vidaP1 = vidaP1 - dano
            iniciarSons(pokemon2['audio'])
            print(
                f"P2 - {pokemon2['nome']} atacou com {pokemon2['nomeAtaque']} e tirou {dano} de vida de {pokemon1['nome']} ")
            if vidaP1 <= 0:
                print(f"{pokemon1['nome']} desmaiou - Jogador 2 Venceu!")
                print(f"A partida durou {turno} turnos.")
                pygame.mixer.music.stop()
                break

        else:
            print("Jogador 2 desistiu da partida, o Jogador 1 venceu!")
            print(f"A partida durou {turno} turnos.")
            pygame.mixer.music.stop()
            break

        print(f"Resumo do turno {turno} - {pokemon1['nome']} está com {Fore.GREEN}{vidaP1} de vida.")
        print(f"Resumo do turno {turno} - {pokemon2['nome']} está com {Fore.GREEN}{vidaP2} de vida.")
        turno += 1


def iniciarBatalhaIA(pokemon1, escolhaIA):
    vidaP1 = pokemon1['vida']
    vidaIA = escolhaIA['vida']
    turno = 1
    musicaBatalha(musica)
    while vidaP1 > 0 and vidaIA > 0:
        print(f"=== Turno  {turno} ===")
        pularTurno = int(input("= Jogador 1 =\n1 - Atacar\n2 - Correr da batalha\n"))
        if pularTurno not in [1, 2]:
            print("Opção inválida.")
            continue
        if pularTurno == 1:
            dano = calcularDanoP1(pokemon1)
            vidaIA = vidaIA - dano
            iniciarSons(pokemon1['audio'])
            print(
                f"P1 - {pokemon1['nome']} atacou com {pokemon1['nomeAtaque']} e tirou {dano} de vida de {escolhaIA['nome']} \n")
            
            if vidaIA <= 0:
                print(f"{escolhaIA['nome']} desmaiou - Jogador 1 Venceu!")
                print(f"A partida durou {turno} turnos.\n")
                pygame.mixer.music.stop()
                break
        else:
            print("Jogador 1 desistiu da partida, o Jogador 2 venceu!")
            print(f"A partida durou {turno} turnos.\n")
            pygame.mixer.music.stop()
            break

        dano = calcularDanoP1(escolhaIA)
        vidaP1 = vidaP1 - dano
        iniciarSons(escolhaIA['audio'])
        print(
            f"IA - {escolhaIA['nome']} atacou atacou com {escolhaIA['nomeAtaque']} e tirou {dano} de vida de {pokemon1['nome']} \n")
        
        if vidaP1 <= 0:
            print(f"{pokemon1['nome']} desmaiou - IA Venceu!")
            print(f"A partida durou {turno} turnos.\n")
            pygame.mixer.music.stop()
            break

        print(f"=== Resumo do turno {turno}===\n{pokemon1['nome']} está com {Fore.GREEN}{vidaP1} de vida.")
        print(f"{turno} - {escolhaIA['nome']} está com {Fore.GREEN}{vidaIA} de vida.")
        turno += 1


def jogadorIA(pokemon1):
    pokemonIA = random.choice(listaPokemons)

    if pokemonIA == pokemon1:
        return jogadorIA(pokemon1)

    return {
        "nome": pokemonIA['nome'],
        "ataque": pokemonIA['ataque'],
        "vida": pokemonIA['vida'],
        "nomeAtaque": pokemonIA['nomeAtaque'],
        "exibNome": pokemonIA['exibNome'],
        "audio": pokemonIA['audio']

    }


# Menu principal
while True:
    print("1 - Iniciar Jogo 2 Jogadores")
    print("2 - Iniciar Jogo 1 Jogador")
    print("3 - Ver Pokédex")
    print("4 - Sair\n")
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
            print("Obrigado por jogar!\n")
            break
        case _:
            print("Opção inválida, escolha novamente.\n")
input("pressione ENTER para sair...")