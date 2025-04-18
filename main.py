from inteligencia import gerar_pergunta, verificar_resposta

print("🤖 Olá! Vamos treinar tabuada! (digite 'sair' para encerrar)")

while True:
    n1, n2 = gerar_pergunta()
    resposta = input(f"Quanto é {n1} x {n2}? ")

    if resposta.lower() == 'sair':
        print("Até mais! 👋")
        break

    if not resposta.isdigit():
        print("Por favor, digite um número.")
        continue

    resposta = int(resposta)
    acertou, correta = verificar_resposta(n1, n2, resposta)

    if acertou:
        print("✅ Isso aí! Resposta correta!")
    else:
        print(f"❌ Ops! A resposta correta era {correta}.")
