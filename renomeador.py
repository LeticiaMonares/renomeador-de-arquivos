import os

# Caminho da sua pasta com os arquivos (ajuste se necessário)
pasta_alvo = r'C:\Users\PRIO-023\Documents\Arquivos para renomear'
prefixo = 'arquivo'  # Pode mudar para 'mapa', 'documento', etc

def renomear_em_massa(pasta, prefixo):
    # Lista arquivos (ignorando pastas)
    arquivos = os.listdir(pasta)
    arquivos = [f for f in arquivos if os.path.isfile(os.path.join(pasta, f))]

    # DEBUG: mostrar os arquivos encontrados
    print(f'\n📁 {len(arquivos)} arquivos encontrados em: {pasta}')
    print("Arquivos encontrados:")
    for a in arquivos:
        print(" -", a)
    print()

    # Renomeia
    for i, nome_antigo in enumerate(arquivos, start=1):
        extensao = os.path.splitext(nome_antigo)[1]
        novo_nome = f"{prefixo}_{i:03d}{extensao}"
        origem = os.path.join(pasta, nome_antigo)
        destino = os.path.join(pasta, novo_nome)

        os.rename(origem, destino)
        print(f"✅ {nome_antigo} → {novo_nome}")

    print("\n✨ Renomeação finalizada com sucesso!")

if __name__ == "__main__":
    renomear_em_massa(pasta_alvo, prefixo)
