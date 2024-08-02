import sqlite3
import pandas as pd
import networkx as nx
from bokeh.io import show, output_file
from bokeh.plotting import figure, from_networkx
from bokeh.models import Range1d, MultiLine, Circle, NodesAndLinkedEdges
from bokeh.palettes import Spectral4

conn = sqlite3.connect('keywords.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
pre_modules = [row[0] for row in cursor.fetchall()]

modules = []
modules_keywords = {}
for module in pre_modules:
    cursor.execute(f"SELECT keywords FROM {module};")
    keywords = [row[0] for row in cursor.fetchall()]
    if keywords != []:
        modules.append(module)
        modules_keywords[module] = keywords

df = pd.DataFrame(0, index=modules, columns=modules)
G = nx.Graph()

for module1 in modules:
    G.add_node(module1)
    for module2 in modules:
        if module1 != module2:
            common_keywords = set(modules_keywords[module1]).intersection(modules_keywords[module2])
            df.at[module1, module2] = len(common_keywords)
            if len(common_keywords) > 0:
                G.add_edge(module1, module2, weight=len(common_keywords))

print("Nodes of G:\n", G.nodes(), "\nTotal: ", len(G.nodes()))

weights = {node: sum(data['weight'] for _, _, data in G.edges(node, data=True)) for node in G.nodes()}
max_weight = max(weights.values())

min_radius = 0.02
max_radius = 0.1
radius_scale = {node: min_radius + (max_radius - min_radius) * (weight / max_weight) for node, weight in weights.items()}

HOVER_TOOLTIPS = [("Module", "@index"), ("Weight", "@weight")]

title = "Network Graph of Module Similarities"
plot = figure(tooltips = HOVER_TOOLTIPS,
              tools="pan,wheel_zoom,save,reset", active_scroll='wheel_zoom',
            x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1), title=title)

graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0), k=2)

graph_renderer.node_renderer.glyph = Circle(fill_color=Spectral4[0])
graph_renderer.node_renderer.selection_glyph = Circle(fill_color=Spectral4[2])
graph_renderer.node_renderer.hover_glyph = Circle(fill_color=Spectral4[1])

graph_renderer.node_renderer.data_source.data['radius'] = [radius_scale[node] for node in G.nodes()]
graph_renderer.node_renderer.data_source.data['weight'] = [weights[node] for node in G.nodes()]
graph_renderer.node_renderer.glyph.radius = 'radius'
graph_renderer.node_renderer.selection_glyph.radius = 'radius'
graph_renderer.node_renderer.hover_glyph.radius = 'radius'

graph_renderer.edge_renderer.glyph = MultiLine(line_color="#CCCCCC", line_alpha=0.8, line_width=1)
graph_renderer.edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[2], line_width=2)
graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[1], line_width=2)

graph_renderer.selection_policy = NodesAndLinkedEdges()
graph_renderer.inspection_policy = NodesAndLinkedEdges()

plot.renderers.append(graph_renderer)

output_file("modules_network.html")
show(plot)

conn.close()