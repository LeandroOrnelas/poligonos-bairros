# 🗺️ Mapeamento de Bairros de Uberlândia (MG) com Python e GeoPandas

Este projeto faz parte de um estudo prático com **Python**, envolvendo manipulação de dados geográficos e visualização de mapas.

O foco principal é a **criação manual de polígonos** representando os bairros de Uberlândia (MG), com classificação por **zona territorial** (Leste, Oeste, Norte, Sul ou Central), e sua **plotagem sobre mapas base** usando o `contextily`.

---

## 🎯 Objetivos

- Praticar a manipulação de dados espaciais em Python com **GeoPandas** e **Shapely**.
- Criar manualmente os contornos dos bairros via coordenadas geográficas (WKT).
- Classificar os bairros por zona territorial.
- Visualizar os dados em um mapa com **tiles do OpenStreetMap**.

---

## 🧰 Tecnologias e Bibliotecas Utilizadas

- **Python 3**
- [GeoPandas](https://geopandas.org/)
- [Shapely](https://shapely.readthedocs.io/)
- [Contextily](https://contextily.readthedocs.io/)
- [Matplotlib](https://matplotlib.org/)

---

## 🌍 Sobre a Reprojeção

As coordenadas foram definidas manualmente em latitude/longitude (EPSG:4326 - WGS84). Para que os polígonos se alinhem corretamente com mapas base (como OpenStreetMap), é necessário reprojetar os dados para o sistema EPSG:3857 (Web Mercator).

ℹ️ A conversão correta é feita com:

```python
gdf.set_crs(epsg=4326, inplace=True)  # Define o CRS original
gdf = gdf.to_crs(epsg=3857)           # Converte para Web Mercator
``` 
---
## 📫 Contato
[![Linkedin: Leandro Ornelas](https://img.shields.io/badge/-Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white&link={https://www.linkedin.com/in/leandroornelas/}/)]({[Link](https://www.linkedin.com/in/leandroornelas/)})
