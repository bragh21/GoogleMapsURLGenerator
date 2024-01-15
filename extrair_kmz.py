import zipfile
import os
import shutil

# Pasta para onde os arquivos KMZ que ja foram extraidos serão movidos após a extração.
DIR_ATUAL = os.getcwd()
KMZ_PROCESSADOS = os.path.join(os.getcwd(), "KMZ Processados")

def listar_arquivos_kmz() -> list:
    arquivos_kmz = []

    # Percorre os arquivos no diretório atual, e armazena o nome de todos com a extensão kmz
    for arquivo in os.listdir(DIR_ATUAL):
        if arquivo.endswith(".kmz"):
            arquivos_kmz.append(arquivo)

    return arquivos_kmz
    
  
def extrair_kmz() -> list:
    # Extrai os arquivos KMZ encontrados
    for kmz in listar_arquivos_kmz():
        pasta_destino = kmz[:-3]
        
        with zipfile.ZipFile(kmz, 'r') as zip_ref:
            zip_ref.extractall(pasta_destino)
        
        # Move o arquivo KMZ que ja foi extraido
        if not os.path.exists(KMZ_PROCESSADOS):
            os.makedirs(KMZ_PROCESSADOS)
        
        kmz_origem = os.path.join(DIR_ATUAL, kmz)
        kmz_destino = os.path.join(KMZ_PROCESSADOS, kmz)
        shutil.move(kmz_origem, kmz_destino)
    
    
def listar_arquivos_kml() -> list:
    arquivos_kml = []
    for pasta_atual, _, arquivos in os.walk(DIR_ATUAL):
        for arquivo in arquivos:
            # Verifica se o arquivo tem a extensão ".kml"
            if arquivo.endswith(".kml"):
                # Adiciona o caminho completo do arquivo à lista
                caminho_completo = os.path.join(pasta_atual, arquivo)
                arquivos_kml.append(caminho_completo)
                
    return arquivos_kml
