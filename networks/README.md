# Getting Started with Networks

In this workshop, we will cover:
- What networks are,
- Why you might use them, and
- How you can generate them using Gephi and NetworkX.

## What are networks?

Let's start with an example and some terminology. At their simplest, networks can be defined as things connected to other things.

If you've ever played Six Degrees of Kevin Bacon, you already have some experience with networks. The premise of the game is that you can connect any actor in Hollywood to Kevin Bacon in six moves or less. For example, Sally Field starred in *Forrest Gump* with Tom Hanks, and Tom Hanks starred in Apollo 13 with Kevin Bacon. The game is based on the concept of "six degrees of separation," the idea that any two people in the world are six or fewer acquaintances apart.

![Six Degrees of Kevin Bacon](https://github.com/YaleDHLab/lab-workshops/blob/networks/networks/images/bacon-network.jpg)

In the case of Six Degrees of Kevin Bacon, people are connected to other people based on the films in which they appeared. In network (or "graph") terminology, the people would be called **nodes** and the films would be called **edges**.

![Basic Network](https://github.com/YaleDHLab/lab-workshops/blob/networks/networks/images/basic-network.png)

Depending on what field you're coming from, nodes might also be referred to as **vertices** or **actors**, while edges might be called **links** or **ties**. For this workshop, we'll stick with nodes and edges.

### Edges
#### Directed & Undirected
Networks can have a directionality associated with them, which would be visually indicated by the edge. 

In the case of a **directed network**, edges are typically represented as arrows. Popular examples of directed networks include epistolary networks (where there are writers and recipients) and Twitter networks (where you follow someone and they might or might not follow you back). The direction matters.   

![Directed Network](https://github.com/YaleDHLab/lab-workshops/blob/networks/networks/images/directed-network.png)

**Undirected networks** are typically represented as a line (straight or curved—people have strong opinions on which to use!). These are networks in which there isn't a meaningful direction. For example, a Facebook network wouldn't have a direction because if you're friends with someone on Facebook, they're automatically friends with you, too.

![Undirected Network](https://github.com/YaleDHLab/lab-workshops/blob/networks/networks/images/basic-network.png)

If you're unsure what kind of network you have, start out by treating it as a directed network when putting your edge list together, because it's much more time intensive to switch from undirected to directed midway through a project.

#### Weight
Edges can also have a weight to them, which is generally represented by changing the thickness of the line. An edge with a weight of 10 would be thicker than an edge with a weight of 1. You can use edge weight to indicate a stronger connection. For example, in a graph of a novel, we might connect characters to one another if they exchange lines. Characters that exchange lines frequently with one another would have a higher weight.

![Weighted Network](https://github.com/YaleDHLab/lab-workshops/blob/networks/networks/images/weighted-network.png)

#### *Hamlet* Network
Let's take a quick look at why properties like direction and weight matter. In this network of *Hamlet*, characters are connected to other characters if they exchanged dialogue. While this graph presents some insights into the plot's structure and the characters' centrality to the plot's unfolding, it also misses features that might be important, depending on what questions you're hoping to ask of the graph (as Moretti acknowledges). For instance, since there's no direction, we lose the significance of the ghost only responding to Hamlet. Without an edge weight, we can't tell that Hamlet and Claudius exchange far more lines with one another than do Horatio and Claudius. Whether these details matter depends on what you're trying to see with the network.

![Hamlet Network](https://github.com/YaleDHLab/lab-workshops/blob/networks/networks/images/hamlet-network.png)

### Nodes
Nodes, frequently represented as circles, can be anything—not just people. Nodes can be places, concepts, words, etc. Networks with nodes all of the same type (for example, all authors) are called unipartite graphs. Networks with two node types (authors and publishers) are bipartite.

![Bipartite Network](https://github.com/YaleDHLab/lab-workshops/blob/networks/networks/images/bipartite-network.png)

It's important to know which kind of network you have, because that will affect what kind of statistics you can run on it. To convert a bipartite graph into a unipartite graph, you can **project** the network. For example, in a network where authors are connected to publishers, you can project the network by turning publishers into edges, leading to a graph where authors are connected to other authors if they have a publisher in common. 

![Projected, Unipartite Network](https://github.com/YaleDHLab/lab-workshops/blob/networks/networks/images/projected-network)
