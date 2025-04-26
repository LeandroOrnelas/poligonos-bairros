


# 📝 Explicação Completa: Mapa de Unidades de Saúde - Uberlândia

---

## 📍 1. Criação do mapa base

O mapa é criado com centro em Uberlândia (`location=[-18.914, -48.275]`) e zoom inicial 12.

```python
mapa = folium.Map(location=[-18.914, -48.275], zoom_start=12)
```

**Documentação relacionada:**
- 📚 [folium.Map](https://python-visualization.github.io/folium/latest/user_guide/quickstart.html#Map)

---

## 📝 2. Adição de título

Um título em HTML é adicionado ao topo do mapa usando `Element`.

```python
titulo_html = "<h1 align='center' style='font-size:26px'><b>Unidades de Saúde - Uberlândia</b></h1>"
mapa.get_root().html.add_child(Element(titulo_html))
```

**Documentação relacionada:**
- 📚 [folium.Element](https://python-visualization.github.io/folium/latest/user_guide/elements.html)

---

## 📍🗺️ 3. Plotagem das Zonas Territoriais (bairros)

As áreas dos bairros são desenhadas como polígonos usando `folium.GeoJson`, com tooltip mostrando nome do bairro e zona territorial.

```python
folium.GeoJson(
    gdf_bairros,
    style_function=...
    tooltip=folium.GeoJsonTooltip(...)
).add_to(mapa)
```

- A camada é adicionada com `control=False`, para não aparecer no menu de camadas.

**Documentação relacionada:**
- 📚 [folium-geojson](https://python-visualization.github.io/folium/latest/user_guide/geojson/geojson.html)

---

## 🏥 4. Agrupamento por Categoria

Cada tipo de unidade (Hospital, UBS, UAI, etc) é agrupada em um `FeatureGroup`.

```python
grupos_categoria = {}
for nome, info in Dic_EstabelecimentoSaude.items():
    # Criação de grupos e marcadores
```

- Um ícone personalizado é escolhido baseado na categoria (`dic_icone_categoria`).
- Se a categoria não tiver ícone específico, usa-se um ícone padrão (`SaudePadrao.png`).
- O `z_index_offset` controla quem fica visualmente acima em sobreposição de ícones.

**Documentação relacionada:**
- 📚 [folium-feature-group](https://python-visualization.github.io/folium/latest/user_guide/folium_features.html#featuregroup)

---

## 💬 5. Adição dos Marcadores

Cada unidade de saúde é adicionada ao seu grupo de categoria.

O marcador inclui:
- Latitude/Longitude
- Tooltip personalizado com Nome, Endereço, Funcionamento e Categoria (exibido ao passar o mouse)
- Ícone específico para o tipo de unidade

**Documentação relacionada:**
- 📚 [folium-marker](https://python-visualization.github.io/folium/latest/user_guide/markers.html)
- 📚 [folium-customicon](https://python-visualization.github.io/folium/latest/user_guide/markers.html#custom-icon)
- 📚 [folium-tooltip](https://python-visualization.github.io/folium/latest/user_guide/markers.html#tooltip)

---

## ☑ 6. Controle de Camadas (LayerControl)

O `LayerControl` é adicionado para permitir que o usuário ative ou desative a visualização dos grupos de categorias.

```python
folium.LayerControl(collapsed=False, position='topright').add_to(mapa)
```

- O menu aparece expandido por padrão (`collapsed=False`).

**Documentação relacionada:**
- 📚 [folium-layer-control](https://python-visualization.github.io/folium/latest/user_guide/ui_elements/layer_control.html)

---

## 🗃️ 7. Exportação do mapa

O mapa é salvo como arquivo HTML para ser acessado fora do Jupyter.

```python
mapa.save("../MapsHTML/mapa_SaudeUberlandia.html")
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
| `z_index_offset`      | Controla a ordem de sobreposição dos ícones no mapa                       |
| `save()`              | Exporta o mapa gerado para arquivo `.html`                               |

---

# ✨ Observações finais

- O fundo OpenStreetMap foi configurado para não ser desativável.
- A camada de bairros também é fixa (não desmarcável).
- O projeto pode ser facilmente expandido para adicionar novas categorias de unidades ou agrupar zonas por cor ou tipo de serviço prestado.

---

---
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