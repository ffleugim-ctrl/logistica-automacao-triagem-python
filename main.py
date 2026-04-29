# Lista de 20 produtos simulando uma carga de Devoluções (DV) em Cajamar
produtos_carga = [
    {"id": "ML001", "nome": "iPhone 15", "valor": 5000, "estado": "danificado", "embalagem": "rasgada"},
    {"id": "ML002", "nome": "Fone de Ouvido", "valor": 150, "estado": "novo", "embalagem": "intacta"},
    {"id": "ML003", "nome": "MacBook Air", "valor": 8000, "estado": "defeito", "embalagem": "intacta"},
    {"id": "ML004", "nome": "Teclado Mecânico", "valor": 300, "estado": "novo", "embalagem": "amassada"},
    {"id": "ML005", "nome": "Monitor 24'", "valor": 900, "estado": "danificado", "embalagem": "violada"},
    {"id": "ML006", "nome": "Cabo USB-C", "valor": 50, "estado": "novo", "embalagem": "intacta"},
    {"id": "ML007", "nome": "Smartwatch", "valor": 1200, "estado": "novo", "embalagem": "amassada"},
    {"id": "ML008", "nome": "Mouse Gamer", "valor": 250, "estado": "novo", "embalagem": "intacta"},
    {"id": "ML009", "nome": "Cadeira Office", "valor": 800, "estado": "danificado", "embalagem": "rasgada"},
    {"id": "ML010", "nome": "Tablet Pro", "valor": 3500, "estado": "novo", "embalagem": "intacta"},
    {"id": "ML011", "nome": "Carregador 20W", "valor": 120, "estado": "defeito", "embalagem": "intacta"},
    {"id": "ML012", "nome": "Ring Light", "valor": 100, "estado": "usado", "embalagem": "violada"},
    {"id": "ML013", "nome": "Placa de Vídeo", "valor": 4500, "estado": "danificado", "embalagem": "rasgada"},
    {"id": "ML014", "nome": "SSD 1TB", "valor": 400, "estado": "novo", "embalagem": "intacta"},
    {"id": "ML015", "nome": "Webcam 4K", "valor": 600, "estado": "novo", "embalagem": "amassada"},
    {"id": "ML016", "nome": "Microfone Cond.", "valor": 550, "estado": "novo", "embalagem": "intacta"},
    {"id": "ML017", "nome": "Projetor HD", "valor": 2000, "estado": "defeito", "embalagem": "intacta"},
    {"id": "ML018", "nome": "Suporte Monitor", "valor": 150, "estado": "novo", "embalagem": "intacta"},
    {"id": "ML019", "nome": "Caixa de Som", "valor": 300, "estado": "novo", "embalagem": "amassada"},
    {"id": "ML020", "nome": "Console Portátil", "valor": 2500, "estado": "danificado", "embalagem": "violada"}
]

print(f"{'ID':<7} | {'PRODUTO':<18} | {'VALOR':<8} | {'DESTINO FINAL'}")
print("-" * 60)

# Processando a carga e enviando alertas
for item in produtos_carga:
    # Lógica de Destino
    if item["estado"] == "novo" and item["embalagem"] == "intacta":
        destino = "✅ REESTOQUE"
    elif item["estado"] == "novo" and item["embalagem"] == "amassada":
        destino = "🛠️ REWORK"
    elif item["estado"] == "danificado" or item["estado"] == "defeito":
        destino = "🚛 SELLER"
    else:
        destino = "🗑️ OUTLET"

    # Exibe o resultado na tela
    print(f"{item['id']:<7} | {item['nome']:<18} | R$ {item['valor']:<6} | {destino}")

    # LÓGICA DE ALERTA: Se for caro (acima de R$ 2000) e estiver danificado/defeito
    if item["valor"] >= 2000 and (item["estado"] == "danificado" or item["estado"] == "defeito"):
        print(f"   ⚠️  [ALERTA ENVIADO]: E-mail de alta prioridade enviado ao Supervisor sobre o {item['nome']}!")
