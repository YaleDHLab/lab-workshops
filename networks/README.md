# Getting Started with Networks

In this workshop, we will cover:
- What networks are,
- Why you might use them, and
- How you can generate them using Gephi and NetworkX.

## What are networks?

Let's start with an example and some terminology. At their simplest, networks can be defined as things connected to other things.

If you've ever played Six Degrees of Kevin Bacon, you already have some experience with networks. The premise of the game is that you can connect any actor in Hollywood to Kevin Bacon in six moves or less. For example, Sally Field starred in *Forrest Gump* with Tom Hanks, and Tom Hanks starred in Apollo 13 with Kevin Bacon. The game is based on the concept of "six degrees of separation," the idea that any two people in the world are six or fewer acquaintances apart.

<p align="center"><img src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/bacon-network.jpg"></p>

In the case of Six Degrees of Kevin Bacon, people are connected to other people based on the films in which they appeared. In network (or "graph") terminology, the people would be called **nodes** and the films would be called **edges**.

<p align="center"><img width="700" height="350" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/basic-network.png"></p>

Depending on what field you're coming from, nodes might also be referred to as **vertices** or **actors**, while edges might be called **links** or **ties**. For this workshop, we'll stick with nodes and edges.

### Edges
#### Directed & Undirected
Networks can have a directionality associated with them, which would be visually indicated by the edge. 

In the case of a **directed network**, edges are typically represented as arrows. Popular examples of directed networks include epistolary networks (where there are writers and recipients) and Twitter networks (where you follow someone and they might or might not follow you back). The direction matters.   


<p align="center"><img width="700" height="350" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/directed-network.png"></p>

**Undirected networks** are typically represented as a line (straight or curved—people have strong opinions on which to use!). These are networks in which there isn't a meaningful direction. For example, a Facebook network wouldn't have a direction because if you're friends with someone on Facebook, they're automatically friends with you, too.

<p align="center"><img width="700" height="350" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/basic-network.png"></p>

If you're unsure what kind of network you have, start out by treating it as a directed network when compiling your edge list, because it's much more time intensive to switch from undirected to directed midway through a project than it is to switch from directed to undirected. It's considered bad practice to have a network that is mixed, with undirected and directed connections in one graph, as it's harder to decipher what's happening in the graph.

#### Weight
Edges can also have a weight to them, which is generally represented by changing the thickness of the line. An edge with a weight of 10 would be thicker than an edge with a weight of 1. You can use edge weight to indicate a stronger connection. For example, in a graph of a novel, we might connect characters to one another if they exchange lines. Characters that exchange lines frequently with one another would have a higher weight.

<p align="center"><img width="700" height="350" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/weighted-network.png"></p>

#### *Hamlet* Network
Let's take a quick look at why properties like direction and weight matter. In this network of *Hamlet*, characters are connected to other characters if they exchanged dialogue. While this graph presents some insights into the plot's structure and the characters' centrality to the plot's unfolding, it also misses features that might be important, depending on what questions you're hoping to ask of the graph (as Moretti acknowledges). For instance, since there's no direction, we lose the significance of the ghost only responding to Hamlet. Without an edge weight, we can't tell that Hamlet and Claudius exchange far more lines with one another than do Horatio and Claudius. Whether these details matter depends on what you're trying to see with the network.

<p align="center"><img width="600" height="500" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/hamlet-network.png"><a href='https://litlab.stanford.edu/LiteraryLabPamphlet2.pdf' target='_blank'></br>"Network Theory, Plot Analysis"</a></p>

### Nodes
Nodes, frequently represented as circles, can be anything—not just people. Nodes can be places, concepts, words, etc. Networks with nodes all of the same type (for example, all authors) are called unipartite graphs. Networks with two node types (authors and publishers) are bipartite.

<p align="center"><img width="700" height="350" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/bipartite-network.png"></p>

It's important to know which kind of network you have, because that will affect what kind of statistics you can run on it. To convert a bipartite graph into a unipartite graph, you can **project** the network. For example, in a network where authors are connected to publishers, you can project the network by turning publishers into edges, leading to a graph where authors are connected to other authors if they have a publisher in common. 

<p align="center"><img width="700" height="350" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/projected-network.png"></p>

## How can we "read" a network?
To think about how we interpret a network, let's imagine we want to create a graph that shows how students in a class are connected by shared research interests. As a proxy, we could link students to one another if they have favorite classes in common. The resulting graph might look something like: 
<p align="center"><img width="800" height="350" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/class-network-edge-labels.png"></br>Network of Favorite Classes</p>

Turning the edge labels off, let's look at subregions of the network and their shape. Star and kite shapes represent **cliques**, subnetworks where everyone is connected to everyone else. Cliques are very resilient networks because if you remove one entity, the others are all still connected. At the opposite end of the spectrum, lines are vulnerable to target attack, because we could prevent communication between different nodes by taking out the node in the middle of the line. Circle subnetworks are somewhere in the middle; removing one node doesn't prevent communication from reaching other nodes, but it could increase the time it takes for a message to make its way to the whole group.

One type of node to look out for is a "broker." A broker is a node that connects otherwise disparate parts of the graph. 
<p align="center"><img width="800" height="350" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/class-network.png"></br>Network of Favorite Classes</p>

For deeper insights, we change the color and size of nodes according to different properties or statistical measures. 

### Degree
A node's **degree** is determined by the number of connections it has. A higher degree means the node is more highly connected.

### Modularity
**Modularity** is a measure that tries to detect subcommunities within the larger network.
<p align="center"><img width="800" height="350" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/class-network-degree.png"></br>Nodes Sized by Degree and Colored by Modularity Score</p>

### Betweenness Centrality
**Betweenness Centrality** measures how often a node is on the shortest path to any other node in the network. 
<p align="center"><img width="800" height="350" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/class-network-betweenness-centrality.png"></br>Nodes Sized by Betweenness Centrality and Colored by Modularity Score</p>

### Cautions
Be careful of reading into the overall layout of nodes on the network. Human perception innately wants to interpret close objects as being more connected than distant objects, but in networks, layout of oftentimes arbitrary. Just because I move Lauren closer to Amy, doesn't change their relationship. They're still 5 hops away from one another (you can calculate this by counting the edges between them).
<p align="center"><img width="900" height="450" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/class-network-layout.png"></br>Class Network with Altered Layout</p>

In general, when interpreting a network, you want to focus on the connections you do see rather than on missing connections. Nodes that are completely separate from the graph are called **isolates**. The reason you may not want to focus too heavily on isolates is that they could be separated because of insufficient data. Or, they could be separated because of how you defined the edges.

**The way you define edges will fundamentally determine the resulting network.** As an example, let's redefine our edges for the class network. Instead of connecting students because they have the exact favorite classes in common, let's connect them because they have the same type of favorite classes in common (in other words, it doesn't matter if it's the same literature class, just that it's a literature class). Now our network is more densely connected. There are no longer isolates, and Isabelle stands out as a broker, connecting the students who favor history in the orange group with those who favor literature in the blue group.

<p align="center"><img width="700" height="450" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/class-network-disciplines.png"></br>Network of Favorite Classes by Discipline</p>

## Why might we use networks?
Networks are good for seeing underlying structures in your data — key players, weak spots, patterns. We can use networks to test and nuance our assumptions. For a few use cases:

- <a href='http://www.datasketch.es/october/code/nadieh/' target='_blank'>Royal Constellations</a> by Nadieh Bremer

- <a href='http://republicofletters.stanford.edu/casestudies/franklin.html' target='_blank'>Visualizing Benjamin Franklin's Correspondence Network</a> in Mapping the Republic of Letters

- Gendered Critique of Marvel Movies (circa 2017) Network

<p align="center"><img width="700" height="350" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/marvel-network-whole.png"></br>Whole Network</p>

<p align="center"><img width="700" height="350" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/marvel-network-male.png"></br>Male Character Network</p>

<p align="center"><img width="700" height="350" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/marvel-network-female.png"></br>Female Character Network</p>

## How do we prepare our data?
Networks take (or create) two kinds of lists:
- the node list stores information about individual entities,
- the edge list stores information about the relationship between entities.

Below is a snippet of the node and edge list that we used to create the Marvel movies network. Each character was given a unique ID (which prevents confusion if characters share the same name), and that unique ID was used to create the edges.

<p align="center"><img width="700" height="450" src="https://github.com/YaleDHLab/lab-workshops/blob/master/networks/images/data-node-edge-lists.png"></br>Marvel Movies Node and Edge List</p>
