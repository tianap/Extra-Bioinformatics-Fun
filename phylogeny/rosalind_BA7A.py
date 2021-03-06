"""
Rosalind Problem BA7A: Compute Distances Between Leaves

In this chapter, we define the length of a path in a tree as the sum of the lengths of its edges (rather than the number of edges on the
path). As a result, the evolutionary distance between two present-day species corresponding to leaves i and j in a tree T is equal to 
the length of the unique path connecting i and j, denoted d_(i,j)(T).

Distance Between Leaves Problem

Compute the distances between leaves in a weighted tree.

Given: An integer n followed by the adjacency list of a weighted tree with n leaves.

Return: A space-separated n x n (di, j), where di, j is the length of the path between leaves i and j.

Sample Dataset
4
0->4:11
1->4:2
2->5:6
3->5:7
4->0:11
4->1:2
4->5:4
5->4:4
5->3:7
5->2:6

Sample Output
0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0

"""