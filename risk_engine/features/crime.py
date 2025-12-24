def crime_density(route_gdf, crime_gdf, buffer_m = 50):
    if route_gdf.empty or crime_gdf is None:
        return 0.0
    route_buffer = route_gdf.geometry.buffer(buffer_m)
    nearby_crimes = crime_gdf[crime_gdf.intersects(route_buffer.unary_union)]
    density = len(nearby_crimes)/max(route_gdf['length'].sum(), 1)
    return min(density*100, 1.0)
# for later -- higher is worse is more crime