import os
from reportlab.pdfgen import canvas

os.makedirs("meus_downloads", exist_ok=True)

def criar_pdf_falso(nome_arquivo, texto_conteudo):
    c = canvas.Canvas(f"meus_downloads/{nome_arquivo}")
    c.drawString(100, 750, texto_conteudo)
    c.save()

# Criando 3 arquivos simulados

criar_pdf_falso("teoria_das_cordas.pdf", "A Teoria das Cordas propõe que os blocos fundamentais do universo não são pontos, mas sim minúsculos filamentos de energia vibrantes operando em múltiplas dimensões.")
criar_pdf_falso("reverse_mapping.pdf", "Reverse Mapping (Mapeamento Reverso) é o processo de inverter a direção de uma busca de dados: em vez de usar uma chave para encontrar um valor (o padrão), você usa o valor para descobrir a qual chave ele pertence.")
criar_pdf_falso("crud.pdf", "CRUD é um acrônimo para as quatro operações básicas que podem ser realizadas em qualquer sistema de armazenamento de dados persistente (como um banco de dados): Create (Criar),")

print("📂 Pasta 'meus_downloads' criada com 3 PDFs dentro!")