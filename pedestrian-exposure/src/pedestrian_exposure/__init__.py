"""Your one-line package description."""

from __future__ import annotations
# import pandas as pd

__version__ = "0.1.0"


# src/pedestrian_exposure_uoa/loader.py
import osmnx as ox


def load_route(origin, destination, place="Auckland, New Zealand"):
    """Fetch the shortest walking route between two addresses.

    Parameters
    ----------
    origin : str
        Starting address, e.g. "Britomart, Auckland".
    destination : str
        Ending address, e.g. "Karangahape Road, Auckland".
    place : str, default "Auckland, New Zealand"
        Place name used to scope the OSMnx graph download.

    Returns
    -------
    geopandas.GeoDataFrame
        Edges of the shortest walking route in EPSG:2193 (NZTM).
    """
    # 1. Download the walking network for the area
    G = ox.graph_from_place(place, network_type="walk")

    # 2. Geocode the two addresses to (lat, lon) tuples
    o_lat, o_lon = ox.geocoder.geocode(origin)
    d_lat, d_lon = ox.geocoder.geocode(destination)

    # 3. Snap each address to the nearest network node
    orig_node = ox.distance.nearest_nodes(G, o_lon, o_lat)
    dest_node = ox.distance.nearest_nodes(G, d_lon, d_lat)

    # 4. Shortest path, then convert the node list to a GeoDataFrame of edges
    nodes = ox.shortest_path(G, orig_node, dest_node, weight="length")
    edges = ox.routing.route_to_gdf(G, nodes)

    # 5. Reproject to NZTM so all spatial maths are in metres
    return edges.to_crs("EPSG:2193")

def function_two(arg1):
    """One-line summary."""
    raise NotImplementedError


def function_three(arg1, arg2):
    """One-line summary."""
    raise NotImplementedError