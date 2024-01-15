import xml.etree.ElementTree as ET


def obter_namespace(element: ET.Element) -> str:
    # Verificar se o atributo xmlns está presente na tag
    print(element.attrib)
    if 'xmlns' in element.attrib:
        return element.attrib['xmlns']
    
    # Se não, procurar por atributos com o padrão xmlns:prefix
    for attribute in element.attrib:
        if attribute.startswith('xmlns:'):
            return element.attrib[attribute]
    
    return None


def extrair_coordenadas(placemark, namespace):
    # Encontrar o elemento <Point> dentro de <Placemark>
    point = placemark.find(f'.//{namespace}Point')
    
    # Se houver um elemento <Point>, encontrar as coordenadas
    if point is not None:
        coordinates = point.find(f'.//{namespace}coordinates').text
        # As coordenadas são uma string no formato "longitude,latitude,altitude"
        # Vamos dividi-las e retornar latitude e longitude
        longitude, latitude, _ = map(float, coordinates.split(','))
        return latitude, longitude

    return None


def gerar_link_google_maps(latitude, longitude):
    return f'https://www.google.com/maps?q={latitude},{longitude}'


def processar_kml(arquivo_kml, gerar_txt = False):
    tree = ET.parse(arquivo_kml)
    
    root = tree.getroot()
    # namespace = obter_namespace(root)
    namespace = '{http://www.opengis.net/kml/2.2}'
    doc_tag = root.findall(f'.//{namespace}Document')
    name_tag = ""
    if doc_tag is not None:
        name_tag = doc_tag[0].find(f'{namespace}name')
     
    places = root.findall(f'.//{namespace}Placemark')
    
    if not gerar_txt:
        # Iterar sobre todos os elementos <Placemark>
        print(f"{'*' * 100}")
        for placemark in places:
            nome = placemark.find(f'.//{namespace}name').text
            coordenadas = extrair_coordenadas(placemark, namespace)
            
            if coordenadas:
                latitude, longitude = coordenadas
                link_maps = gerar_link_google_maps(latitude, longitude)
                print(f'KMZ: {name_tag.text}')
                print(f'Nome do local: {nome}')
                print(f'Link do Google Maps: {link_maps}')
                print()
        print(f"{'*' * 100}")
    
    else:
        from datetime import datetime
        import os
        data_formatada = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open( os.path.join( os.getcwd(), name_tag.text[:-4] + "_" + data_formatada + ".txt"), "w" ) as fl:
            for placemark in places:
                nome = placemark.find(f'.//{namespace}name').text
                coordenadas = extrair_coordenadas(placemark, namespace)
                
                if coordenadas:
                    latitude, longitude = coordenadas
                    link_maps = gerar_link_google_maps(latitude, longitude)
                    fl.write(f'[KMZ: {name_tag.text}] LOCAL: {nome} | URL: {link_maps}\n')
