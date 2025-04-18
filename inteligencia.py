import random
from database import registrar_resposta, pegar_respostas_erradas

def gerar_pergunta():
    erradas = pegar_respostas_erradas()
    if erradas and random.random() < 0.5:
        pergunta = random.choice(erradas)
        n1, n2 = map(int, pergunta.split(" x "))
    else:
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
    return n1, n2

def verificar_resposta(n1, n2, resposta_usuario):
    correta = n1 * n2
    acertou = (resposta_usuario == correta)
    pergunta_str = f"{n1} x {n2}"
    registrar_resposta(pergunta_str, resposta_usuario, int(acertou))
    return acertou, correta
