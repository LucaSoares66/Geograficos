import geopandas as gpd
import folium
import streamlit as st
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import streamlit as st
from streamlit.components.v1 import html
from PIL import Image

# Leitura dos arquivos
rio = gpd.read_file("rio.gpkg")
zonas = gpd.read_file("zonas_rj.zip")

# Criação dos mapas
# Mapa 1 - Arquivo rio.gpkg
m1 = folium.Map(location=[-22.9, -43.2], zoom_start=10)
folium.GeoJson(rio).add_to(m1)

# Mapa 2 - Arquivo zonas_rj.shp
m2 = folium.Map(location=[-22.9, -43.2], zoom_start=10)
folium.GeoJson(zonas).add_to(m2)

# Salvar como HTML temporário
m1.save('mapa_rio.html')
m2.save('mapa_zonas.html')

# App Streamlit


# Carregar logo (formato PNG) - certifique-se que o arquivo está na mesma pasta
logo = Image.open("logo iesb.png")

# Exibir logo no topo centralizado
st.image(logo, width=150)

st.markdown("""
<h2 style='text-align: center;'>Projeto de Visualização Geográfica com Python</h2>
<h4 style='text-align: center;'>Luca Adriano Melo Mendonça Soares</h4>
<h5 style='text-align: center;'>Instituição: IESB - Campus Sul</h5>
<hr>
""", unsafe_allow_html=True)



st.title("Visualização de Mapas do RJ")
col1, col2 = st.columns(2)

st.markdown("""Os setores censitários são divididos pelo IBGE, com base em alguns critérios, sendo os principais: Número de domicílios, Tipo de área (Urbana/Rural), e seus limites geográficos que podem se dar por meio de rios, muros, morros ou estradas.
O IBGE disponibiliza um arquivo shapefile com os os formatos das regiões estabelecidos por coordenadas que juntas compõem um polígono para cada região.
""")

st.markdown("""À partir dos dados do TSE-RJ, extraí os pontos de localidade de cada Zona Eleitoral, com auxílio das bibliotecas GeoPandas. Já com a biblioteca GeoVoronoi, foram criados os polígonos estimados à partir desses pontos, foram mapeados e moldados de acordo com a proximidade de cada Zona Eleitoral. 
O TSE de nenhum estado disponibiliza um shapefile, muitas vezes jornais ou institutos de pesquisa contratam especialistas para estimar essas áreas, assim conseguindo uma visualização mais clara para estudos ou para levar ao público.

""")

with col1:
    st.subheader("Mapa divisão de Setores Censitários - Cidade do Rio de Janeiro")
    st.components.v1.html(open('mapa_rio.html', 'r').read(), height=450)
    st.caption("Fonte: IBGE.")


with col2:
    st.subheader("Mapa estimado de divisão das Zonas Eleitorais - Cidade do Rio de Janeiro")
    st.components.v1.html(open('mapa_zonas.html', 'r').read(), height=450)
    st.caption("Fonte: IBGE.")





# Configuração da página
st.set_page_config(layout='wide')
st.title("Visualização dos Vencedores por Zona Eleitoral - Rio de Janeiro")

# Caminhos dos arquivos HTML (assumindo que estão na mesma pasta do script)
arquivo_2002 = "mapa_vencedores_zona_1_2002.html"
arquivo_2018 = "mapa_vencedores_zona_1_2018.html"

# Colunas lado a lado
col1, col2 = st.columns(2)

with col1:
    st.subheader("Resultado das Eleições 2002")
    with open(arquivo_2002, 'r', encoding='utf-8') as f:
        html(f.read(), height=450)
    st.caption("Fontes: IBGE/TSE.")
    

with col2:
    st.subheader("Resultado das Eleições 2018")
    with open(arquivo_2018, 'r', encoding='utf-8') as f:
        html(f.read(), height=450)
    st.caption("Fontes: IBGE/TSE.")


