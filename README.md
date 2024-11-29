# K-Nearest-Neighbor-Graph

# Goal

K-nearest neighbor graph (K-NNG) is an important method for many web-related applications, such as similarity search.

I refer to the paper [Efficient K-Nearest Neighbor Graph Construction for
Generic Similarity Measures](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=103ac7f316bf8cdad3133b4ce2bbd28d091e7974) to construct a K-NNG for k-nearest neighbors search tasks (example : Retrieval augmented Generation ).

This paper presents a method called "NN-Descent" that offers several benefits:

- General: The method works with any arbitrary similarity metric between two objects.
- Scalable: The method only considers local information between two objects, making it ideal for large datasets.
- Fast and Accurate: The method achieves high performance speeds.
- Easy to Implement: The method has a straightforward implementation.

# Idea

The method's core principle is "a neighbor's neighbor is also likely to be a neighbor." This insight allows us to improve the K-NN approximation for each point by exploring its neighbors' neighbors. This is supported by the following mathematical term:

$Pr({u ∈ B^{'}
[v]}) ≥ 1−
(1 − K/|B_{r/2}(v)|^{2})^{ |B_{r/2}(v)| }
≈ K/|Br/2(v)|.$

- $B^{'}
  [v] :$ The dataset represents the neighbors of neighbors of Point $v$.

The method assumes that when K is large enough, u will fall within the 1/2 radius of $v$. Using this principle, we can improve the KNNG performance through iterative neighbor updates.

**Reference : [NN-Descent构建K近邻图——论文超详细注解](https://blog.csdn.net/whenever5225/article/details/105598694)**

# Method ( Algorithm : NNDescentFull )

1. Obtain a dataset of neighbors for point $v$: $B[v]$.
2. For each v:
   - Get $old[v]$, which contains all items flagged as False in $B[v]$.
   - Get $new[v]$, which contains $ρK$ items flagged as True in $B[v]$ through sampling, then mark these items as False.
3. Create $old'$ and $new'$ by reversing $old$ and $new$, then set c = 0.
4. For each v:
   - Create a new $old[v]$ by combining $old[v]$ with $Sample(old'[v], ρK)$.
   - Create a new $new[v]$ by combining $new[v]$ with $Sample(new'[v], ρK)$.
   - Compare pairs where $u1, u2 ∈ new[v], u1 < u2$ or $u1 ∈ new[v], u2 ∈ old[v]$, evaluate the distance between $u1$ and $u2$, then update $B[u1]$ and $B[u2]$.
   - Update c based on the number of updates.
5. Return to step 2 if $c > δNK$.

# Default Parameters

- $K = 20, ρ = 1.0 , ρ = 0.001$

# Visualization

K - Nearest Neighbors Graph      

![KNNG.png](C:\Users\User\OneDrive\文件\GitHub\K-Nearest-Neighbor-Graph\KNNG.png)