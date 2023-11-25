import networkx as nx
import matplotlib.pyplot as plt

from torch_geometric.utils import to_networkx
from torch_geometric.datasets import QM9

def visualize_graph(G, color, title="Molecule Visualization"):
    plt.figure(figsize=(7, 7))
    plt.xticks([])
    plt.yticks([])
    plt.title(title)
    nx.draw_networkx(G, pos=nx.spring_layout(G, seed=42), with_labels=True,
                     node_color=color, cmap="Set2")
    plt.show()

# load data
dataset = QM9(root="./data/5A")

# pick molecule (i.e. 0 is )
molecule = dataset[72081]

# get atomic numbers of atoms in molecule
unique_identifiers = molecule.x[:, 0]

# visualise molecule
G = to_networkx(molecule, to_undirected=True)
visualize_graph(G, color=unique_identifiers, title=f'{molecule.smiles}')