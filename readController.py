import time
import json
import os
from google import genai
from google.genai import types # Importante para configurações de tipo
import dotenv

# 1. Carregar a API Key
dotenv.load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") 

client = genai.Client(api_key=api_key)

def analisar_pasta():
    pasta = "meus_downloads"
    # Garante que a pasta existe para evitar erro
    if not os.path.exists(pasta):
        print(f"A pasta '{pasta}' não foi encontrada.")
        return []

    arquivos = [f for f in os.listdir(pasta) if f.endswith('.pdf')]
    relatorio_final = []

    print(f"🚀 Iniciando análise de {len(arquivos)} documentos...\n")

    for arquivo in arquivos:
        caminho = os.path.join(pasta, arquivo)
        print(f"📄 Lendo: {arquivo}...", end="", flush=True)

        try:
            # A. Upload usando o CLIENT (Syntax correta da nova lib)
            # Lê o arquivo em modo binário para upload
            with open(caminho, "rb") as f:
                arquivo_nuvem = client.files.upload(file=f, config={'display_name': arquivo, 'mime_type': 'application/pdf'})

            # B. Espera processar
            while arquivo_nuvem.state.name == "PROCESSING":
                time.sleep(1)
                arquivo_nuvem = client.files.get(name=arquivo_nuvem.name)

            if arquivo_nuvem.state.name == "FAILED":
                print(" Falha no processamento do arquivo. ❌")
                continue

            # C. O PEDIDO (PROMPT)
            prompt = """
            Você é um assistente escolar. Analise este PDF e retorne um JSON com:
            1. "Tema": O assunto falado no documento.
            2. "Resumo": Uma frase resumindo o conteúdo.
            3. "Nivel": Fácil, Médio ou Difícil.
            4. "Orientação": Uma orientação de estudo para se aprender sobre o tema.
            """

            # D. Gera a resposta (DENTRO DO LOOP)
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=[arquivo_nuvem, prompt],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )

            # E. Guarda os dados
            dados = json.loads(response.text)
            dados["nome_original"] = arquivo
            relatorio_final.append(dados)

            print(" Feito! ✅")

            # F. Limpeza (importante na nova lib)
            client.files.delete(name=arquivo_nuvem.name)

        except Exception as e:
            print(f"\n❌ Erro ao processar {arquivo}: {e}")

    return relatorio_final

# Executa
if __name__ == "__main__":
    meus_dados = analisar_pasta()
    print(json.dumps(meus_dados, indent=4, ensure_ascii=False))