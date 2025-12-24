def isolation_score(route_gdf):
    if route_gdf.empty:
        return 0.5
    avg_segment_length = route_gdf['length'].mean()
    return min(avg_segment_length / 200, 1.0)
# for later -- higher is worse is more isolated