import requests
import re
import urllib.request
import sys

objeto = ""
captcha = ""
imagem = ""

url = "https://rastreamento.correios.com.br/app/index.php#"

url_request_api = f"https://rastreamento.correios.com.br/app/resultado.php?objeto={object}&captcha={captcha}&mqs=S"

session = requests.session()

headers = {
  'Accept':
  'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed- exchange;v=b3;q=0.9',
  'Accept-Encoding':
  'gzip, deflate, br',
  'Fache-Control':
  'max-age=0',
  'Sec-Fetch-Fest':
  'document',
  'User-Agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

fazer_get = session.get(url, headers=headers)

html = fazer_get.text

regex_imagem = re.search(
  r'<img\s*id="captcha_image"\s*src="..([^>]*)"\s*alt="CAPTCHA\s*Image">',
  html, re.S)

imagem = regex_imagem.group(1)

url_base_imagem = f"https://rastreamento.correios.com.br{imagem}"

# 1 passo: baixar imagem
# 2 passo abrir
# 3 converter para texto
try:
  urllib.request.urlretrieve(url_base_imagem, "captcha.png")
  print("Imagem salva! =)")
except:
  erro = sys.exc_info()
  print("Ocorreu um erro:", erro)