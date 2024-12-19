# Toric-Variety-implementation
This repository is an implementation of algebro-geometric object called "Toric Varieties".
Toric Varieties are varieties that have a Zariski dense complex torus as a subset with a torus action that is an extension of the torus action on itself. Such varieties have a nice combinatorial representation in terms of fans sitting in a lattice. If $\sigma$ is a cone in the fan, then the co-ordinate ring associated to the open subset of $\sigma$ in the variety is the semi-group algebra C[\sigma^{\ast} \cup M], where $M$ is the dual lattice. The gluing information of these affine charts is contained in the combinatorial information of the fans. 

In the python file "Coputing_a_2D_affine_toric_variety_from_the_generators.ipynb" of the repository, we compute the coordinate ring of a single cone given the genrators of the cone, and the final output is the co-ordinate ring. 
In the file "Standard cone resolution naive.py", we compute the resolution of an affine 2D toric variety, and output the vectors that will generate the resolved 2D toric variety. Note that it will not be affine any longer. 
The work is still in progress, but feel free to email the author any suggestions on:
tsparthasarathy@ksu.edu

Author: Sai Parthasarathy Telikicherla
Designation: Graduate Student, Mathetmatics, Kansas State University. 
