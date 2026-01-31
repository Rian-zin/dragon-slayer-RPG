import random
import time

def rolar_dados(minimo, maximo):
        forca = random.randint(minimo, maximo)
        return forca

vida_jogador = 40
vida_dragao = 100

while vida_jogador > 0 and vida_dragao > 0:
    time.sleep(1)
    print('\n' + '='*30)
    print(f'Sua vida: {vida_jogador}/40 | Vida do Dragão: {vida_dragao}')
    print('='*30)

    opcao = int(input('1-Ataque Rápido | 2-Ataque Pesado | 3-Curar: '))

    # --- TURNO DO JOGADOR ---
    if opcao == 1:
        dano = rolar_dados(5, 10)
        vida_dragao -= dano
        print('Você parte para cima do Dragão...')
        time.sleep(3)
        print(f'⚔️  Você deu uma estocada rápida! Dano: {dano}')

    elif opcao == 2:
        dano = rolar_dados(15, 30)
        acerto = rolar_dados(0, 1)
        if acerto == 1:
            vida_dragao -= dano
            print('Você usa toda sua força e parte para cima do Dragão...')
            time.sleep(3)
            print(f'💥 CRÍTICO! Você esmagou o dragão! Dano: {dano}')
        else:
            print('Você se embaralha com o ataque...')
            time.sleep(1)
            print('💨 Você tentou bater forte demais e errou!')

    elif opcao == 3:
        if vida_jogador >= 40:
            print('Uma luz divina cai sobre você...')
            time.sleep(2)
            print('❌ Sua vida já está cheia!')
        else:
            cura = rolar_dados(10, 20)
            vida_jogador += cura
            if vida_jogador > 40:
                vida_jogador = 40
                print('Uma luz divina cai sobre você...')
                time.sleep(1)
            print(f'✨ Luz divina! Você recuperou vida. Atual: {vida_jogador}')
    
    else:
        print('🚫 Opção inválida! Perdeu a vez por bobeira.')

    # --- TURNO DO DRAGÃO ---
    if vida_dragao > 0:
        dano_dragao = rolar_dados(5, 15)
        vida_jogador -= dano_dragao
        print('O Dragão está preparando o ataque...')
        time.sleep(3)
        print(f'🔥 O Dragão cospiu fogo! Você tomou {dano_dragao} de dano.')

print('\n' + '-'*30)
if vida_jogador > 0:
    print('O Dragão cai agonizando...')
    time.sleep(1)
    print('🏆 VITÓRIA! O Dragão virou tapete!')
else:
    print('Você cai enquanto queima...')
    time.sleep(1)
    print('☠️ GAME OVER! Você virou churrasquinho.')