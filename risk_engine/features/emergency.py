def emergency_access_score(route_gdf):
    if route_gdf.empty:
        return 0.5
    score = 0
    count = 0
    for _, row in route_gdf.iterrows():
        highway = row.get('highway', '')
        if isinstance(highway, list):
            highway = highway[0]
        if highway in ['motorway', 'trunk', 'primary']:
            score += 1.0
        elif highway in ['unclassified', 'tertiary']:
            score += 0.7
        else:
            score += 0.4
        count += 1
    return score / count