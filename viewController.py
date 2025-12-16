import pandas as pd
from IPython.display import display
import readController
import pdfController
# 📊 Passo 5: Visualizando o Resultado
# Vamos transformar o JSON (texto) em uma Tabela interativa.
pdfController.criar_pdf_falso("teoria_das_cordas.pdf", "A Teoria das Cordas propõe que os blocos fundamentais do universo não são pontos, mas sim minúsculos filamentos de energia vibrantes operando em múltiplas dimensões.")
pdfController.criar_pdf_falso("reverse_mapping.pdf", "Reverse Mapping (Mapeamento Reverso) é o processo de inverter a direção de uma busca de dados: em vez de usar uma chave para encontrar um valor (o padrão), você usa o valor para descobrir a qual chave ele pertence.")
pdfController.criar_pdf_falso("crud.pdf", "CRUD é um acrônimo para as quatro operações básicas que podem ser realizadas em qualquer sistema de armazenamento de dados persistente (como um banco de dados): Create (Criar),")

meus_dados = readController.analisar_pasta()
df = pd.DataFrame(meus_dados)

# Reordenando as colunas para ficar mais bonito
df = df[["Tema", "Nivel", "Resumo", "Orientação", "nome_original"]]

print("\n--- 🎓 SEU PLANO DE ESTUDOS AUTOMÁTICO ---")
display(df)

