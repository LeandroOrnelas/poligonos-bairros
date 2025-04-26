
# 📝 Visualização Geoespacial de Uberlândia

---

Este diretório contém notebooks que constroem **mapas interativos** sobre diferentes aspectos da cidade de Uberlândia, utilizando dados geográficos e bibliotecas de visualização espacial.

Atualmente disponíveis:

- 🏥 **Mapa das Unidades de Saúde Públicas**: exibe a distribuição de hospitais, UBSs, UAIs e outras unidades de saúde, baseado em fontes oficiais.
- 🚌 **Mapa dos Terminais Urbanos**: exibe a localização dos principais terminais de ônibus da cidade, para análise de infraestrutura de transporte público.

Os mapas são construídos com foco em análise visual, agrupamento inteligente de pontos e possibilidade de controle de camadas.

---

## 📍 1. Criação do mapa base

Cada mapa é inicializado usando `folium.Map`, com centro em Uberlândia (`location=[-18.914, -48.275]`) e zoom configurado para melhor visualização.

```python
mapa = folium.Map(location=[-18.914, -48.275], zoom_start=12)
```

**Documentação relacionada:**
- 📚 <a href="https://python-visualization.github.io/folium/latest/user_guide/map.html" target="_blank">folium.Map</a>

---

## 📝 2. Adição de título

Cada mapa recebe um título em HTML posicionado no topo, utilizando `Element` do Folium.

```python
titulo_html = "<h1 align='center' style='font-size:26px'><b>Título do Mapa</b></h1>"
mapa.get_root().html.add_child(Element(titulo_html))
```

---

## 📍🗺️ 3. Plotagem das Zonas Territoriais (Bairros)

As áreas dos bairros são desenhadas como polígonos com base em dados GeoJSON, utilizando `folium.GeoJson`.

```python
folium.GeoJson(
    gdf_bairros,
    style_function=...,
    tooltip=folium.GeoJsonTooltip(...)
).add_to(mapa)
```

- As camadas territoriais são configuradas para não aparecer no menu de camadas (`control=False`).

**Documentação relacionada:**
- 📚 [folium-geojson](https://python-visualization.github.io/folium/latest/user_guide/geojson/geojson.html)

---

## 🏷️ 4. Agrupamento e Marcação de Pontos de Interesse

Cada tipo de ponto de interesse (estabelecimentos de saúde, terminais urbanos, etc) é agrupado em `FeatureGroup` para facilitar o controle de visualização.

- Ícones personalizados são atribuídos a cada marcador.
- Informações adicionais são exibidas via tooltip ao passar o mouse.

**Documentação relacionada:**
- 📚 [folium-feature-group](https://python-visualization.github.io/folium/latest/user_guide/plugins/featuregroup_subgroup.html)
- 📚 [folium-marker](https://python-visualization.github.io/folium/latest/getting_started.html)
- 📚 [folium-customicon](https://python-visualization.github.io/folium/latest/user_guide/ui_elements/icons.html)
- 📚 [folium-tooltip](https://python-visualization.github.io/folium/latest/user_guide/geojson/geojson_popup_and_tooltip.html)

---

## ☑ 5. Controle de Camadas (LayerControl)

O `LayerControl` é adicionado para permitir que o usuário ative ou desative a visualização dos diferentes grupos de camadas.

```python
folium.LayerControl(collapsed=False, position='topright').add_to(mapa)
```

**Documentação relacionada:**
- 📚 [folium-layer-control](https://python-visualization.github.io/folium/latest/user_guide/ui_elements/layer_control.html)

---

## 🗃️ 6. Exportação dos Mapas

Os mapas gerados são exportados em formato `.html`, permitindo visualização independente do ambiente Jupyter.

```python
mapa.save("../MapsHTML/nome_mapa.html")
```

---

# 📖 Conceitos Importantes Utilizados

| Conceito             | Explicação                                                                 |
|:---------------------|:--------------------------------------------------------------------------|
| `folium.Map()`        | Cria o mapa base com localização e zoom inicial                           |
| `Element`             | Permite adicionar HTML personalizado no mapa                             |
| `GeoJson`             | Desenha áreas poligonais no mapa a partir de dados GeoJSON                |
| `FeatureGroup`        | Agrupa marcadores para controle de visibilidade                          |
| `Marker`              | Representa um ponto de interesse no mapa                                 |
| `CustomIcon`          | Usa imagem personalizada como ícone dos marcadores                       |
| `LayerControl`        | Permite controle interativo das camadas de dados                         |
| `Tooltip`             | Exibe informações ao passar o mouse sobre o marcador                     |
| `MarkerCluster`       | Agrupa automaticamente marcadores próximos para melhorar a visualização |
| `save()`              | Exporta o mapa gerado para arquivo `.html`                               |

---

# ✨ Observações Finais

- O fundo OpenStreetMap foi configurado para permanecer sempre ativo.
- A camada de bairros (zonas territoriais) é fixa e não pode ser desativada.
- O projeto pode ser expandido para novas categorias de pontos de interesse ou diferentes classificações territoriais.

---

# 📬 Contato

<p align="left">
  <a href="mailto:leandro.nanndo@gmail.com" title="Gmail">
    <img src="https://img.shields.io/badge/-Gmail-FF0000?style=flat-square&labelColor=FF0000&logo=gmail&logoColor=white" alt="Gmail"/>
  </a>
  <a href="https://www.linkedin.com/in/leandroornelas/" title="LinkedIn">
    <img src="https://img.shields.io/badge/-Linkedin-0e76a8?style=flat-square&logo=Linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="https://api.whatsapp.com/send?phone=5534991949009" title="WhatsApp">
    <img src="https://img.shields.io/badge/-WhatsApp-25d366?style=flat-square&labelColor=25d366&logo=whatsapp&logoColor=white" alt="WhatsApp"/>
  </a>
</p>

---
