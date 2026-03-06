<h1 align="center">Floyd–Warshall Algorithm</h1>

## Overview

The **Floyd–Warshall Algorithm** is a **dynamic programming algorithm** used to find the **shortest paths between all pairs of vertices** in a **weighted graph**.

Unlike algorithms that compute the shortest path from a single source (like Dijkstra or Bellman–Ford), Floyd–Warshall computes the **shortest distance between every pair of vertices**.

It is known for:

* ✅ Computing **all-pairs shortest paths**
* ✅ Handling **negative edge weights**
* ❌ Being slower for very large graphs

---

## 📌 Key Concepts

### Weighted Graph

A graph where each edge has a **numerical cost (weight)**.

### All-Pairs Shortest Path

Finding the **shortest path between every pair of vertices** in the graph.

### Distance Matrix

Floyd–Warshall uses a **matrix** to store distances between vertices.

Example matrix:

```
     A   B   C
A    0   5   ∞
B    5   0   3
C    ∞   3   0
```

Here:

* **0** = distance to itself
* **∞** = no direct edge

---

## ⚙️ How Floyd–Warshall Works

The algorithm repeatedly updates the shortest path using an **intermediate vertex**.

For every pair of vertices **(i, j)**:

```
distance[i][j] = min(
    distance[i][j],
    distance[i][k] + distance[k][j]
)
```

Where:

* **i** = start vertex
* **j** = destination vertex
* **k** = intermediate vertex

The algorithm checks whether going through **k** gives a shorter path.

---

## 🧩 Example Graph

```
      (3)
  A ------- B
  |         |
 (8)       (2)
  |         |
  C ------- D
      (1)
```

### Edge Weights

| Edge  | Weight |
| ----- | ------ |
| A → B | 3      |
| A → C | 8      |
| B → D | 2      |
| C → D | 1      |

---

## 🧪 Initial Distance Matrix

```
      A    B    C    D
A     0    3    8    ∞
B     ∞    0    ∞    2
C     ∞    ∞    0    1
D     ∞    ∞    ∞    0
```

---

## 🔄 Iteration Example

Suppose we check vertex **B** as an intermediate node.

If:

```
A → B → D
```

Distance becomes:

```
3 + 2 = 5
```

Update matrix:

```
A → D = 5
```

Updated matrix:

```
      A    B    C    D
A     0    3    8    5
B     ∞    0    ∞    2
C     ∞    ∞    0    1
D     ∞    ∞    ∞    0
```

The algorithm continues until **all vertices are tested as intermediates**.

---

## ⏱️ Time & Space Complexity

| Operation        | Complexity |
| ---------------- | ---------- |
| Time Complexity  | O(V³)      |
| Space Complexity | O(V²)      |

Where:

* **V = number of vertices**

---

## 🧠 Python Implementation

```python
def floyd_warshall(graph):

    V = len(graph)

    dist = [row[:] for row in graph]

    for k in range(V):
        for i in range(V):
            for j in range(V):

                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    return dist


INF = float('inf')

graph = [
    [0,   3,   8, INF],
    [INF, 0, INF, 2],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

result = floyd_warshall(graph)

for row in result:
    print(row)
```

### Output

```
[0, 3, 8, 5]
[inf, 0, inf, 2]
[inf, inf, 0, 1]
[inf, inf, inf, 0]
```

---

## 👍 Advantages

* Finds **shortest paths between all vertex pairs**
* Handles **negative edge weights**
* Simple matrix-based implementation
* Works well for **dense graphs**

---

## 👎 Disadvantages

* **High time complexity O(V³)**
* Not efficient for **large sparse graphs**
* Uses **O(V²) memory**

---

## 📊 Floyd–Warshall vs Other Algorithms

| Algorithm      | Purpose                             | Time Complexity |
| -------------- | ----------------------------------- | --------------- |
| Dijkstra       | Single-source shortest path         | O(E log V)      |
| Bellman–Ford   | Single-source with negative weights | O(VE)           |
| Floyd–Warshall | All-pairs shortest paths            | O(V³)           |

---

## 📌 Applications

Floyd–Warshall is used in:

* Network routing analysis
* Shortest paths in **transport systems**
* **Graph theory research**
* **Transitive closure** of graphs
* Dynamic programming problems

---

## 🏁 Summary

The **Floyd–Warshall Algorithm** is a powerful method for computing the **shortest paths between all pairs of vertices** in a graph. Although it has a higher time complexity, its simple matrix-based approach makes it useful for smaller graphs and dense networks.

