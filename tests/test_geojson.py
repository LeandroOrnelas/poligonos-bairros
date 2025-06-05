import geopandas as gpd
from pathlib import Path

def test_geojson_load():
    path = Path('data/bairros_uberlandia.geojson')
    gdf = gpd.read_file(path)
    assert not gdf.empty
    assert gdf.crs.to_epsg() == 3857
