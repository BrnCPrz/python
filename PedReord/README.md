# Reordering a pedigree by *Kahn's* algorithm
 This script is an adaptation of the reord/renum function in __PedWorks.py__ ([more](https://github.com/BrnCPrz/PedWorks)) program. It has the objective of presenting a new method to reorder a pedigree using a network theory framework. 
 
 The Kahn's algorithm (Kahn, 1962) for network topological sorting performs a linear ordering of its vertices such that for every edge [x,y] connecting vertices x and y, x will come before y in the final ordering. When applied to genealogical structured data (or simply pedigrees!), edge connections [x,y] may be interpreted as the parent-child relationship, where the parent is represented by x and progeny by y. This brings the perception that when applying the algorithm, x (parents) will always come before their progeny (y) in the final ordering.
 
#### Required imports:
 * NetworkX - [GitHub](https://networkx.github.io/)
 * Numpy - [Website](http://www.numpy.org/)
 * Collections - [docs](https://docs.python.org/2/library/collections.html)
 * Pandas - [Website](http://pandas.pydata.org/)

#### References:
Kahn, Arthur B. (1962), "Topological sorting of large networks", Communications of the ACM 5 (11): 558–562, doi:10.1145/368996.369025
