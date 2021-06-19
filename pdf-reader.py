# pip install pymupdf
import fitz

filename = "Jederson Luz's CV"

with fitz.open(f'{filename}.pdf') as pdf:
  text = ''

  for page in pdf:
    text += page.getText()

with open(f'{filename}.txt', 'w', encoding='utf-8') as file:
  file.write(text)

print(text)