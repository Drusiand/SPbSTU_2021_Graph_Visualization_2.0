# Graph visualization

This is a simple student project designed for visualization deep-first search (DFS) and breadth-first search (BFS) algorithms (currently using matploib). Output data is stored in gif-files with corresponding names.


## Installation

To make the program work properly, you will have install third-party dependedencies via typing  
```  
code pip install -r requirements.txt  
```  
in terminal.


## Results

### Visualization of BFS algorithm:
![alt-текст](https://github.com/Drusiand/SPbSTU_2021_Graph_Visualization_2.0/blob/master/test/data/gif_test/bfs.gif)

### Visualization of dFS algorithm:
![alt-текст](https://github.com/Drusiand/SPbSTU_2021_Graph_Visualization_2.0/blob/master/test/data/gif_test/dfs.gif)


## Usage exmples
### graph_letters.txt
```
A: B,C
B: D,E
C: F,G
E: H
F: I
H: J

```
Note:  
- 1st node (in that case node with value "A") will be the begining for DFS and BFS algorithms;  


### Building a graph
```python
from python.graph import Graph
graph_letters = Graph.build_graph_from_file("graph_letters.txt")
```

### Drawing graph
```python
from python.graph import Graph
# ...
# building graph...
# ...
graph.draw()
```

### Building gif-files
```python
from python.custom_graph import custom_graph
# ...
# building graph...
# ...
opts = {"bfs.gif": bfs(graph, graph.get_start()),
        "dfs.gif": dfs(graph, graph.get_start())}
graph.build_gif(opts)
```
