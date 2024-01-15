from extrair_kmz import extrair_kmz, listar_arquivos_kml
from gerar_url import processar_kml

# Extrai todos os arquivos KMZ presentes na pasta atual, se tiver
extrair_kmz()

# Obtem uma lista completa de todos os arquivos KML no diretório atual, em toda a arvore de subdiretórios
arquivos_kml = listar_arquivos_kml()

for kml in arquivos_kml:
    processar_kml(kml, gerar_txt = True)
    
    
# Comando para empacotar o script
# C:\Users\anderson.bragherolli\AppData\Roaming\Python\Python311\Scripts\pyinstaller.exe --onefile main.py