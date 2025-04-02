# Algorithm to chop the genome using the 4 gametes test
Code to use the chopping algorithm described in Kerdoncuff et al. 2020 'Testing for population decline using maximal linkage disequilibrium blocks' (https://doi.org/10.1016/j.tpb.2020.03.004) (python for now, C coming soon)

There are two main functions, one to find the pairs of incompatible sites and one to locate (at best) the recombination points. If you want more details it's described in section 4.1.2. The chopping algorithm of the manuscript.

One function to find the incompatible pairs 'incompatibilities(variants, haplotypes, window_size)', the input is a vector (variants) with the position of the mutations, a matrice (haplotypes) with the genotypes of the individuals for each variant in (variants) (0 or 1), a window length (window_size), the output is a matrice of pairs of incompatible positions.

A second function 'selection_segment_rm(incompatibi)', which correspond to the algorithm, takes the matrice of incompatible pairs (incompatilibi) as an input and create a vector of recombination locations:  Class recombiS[] with an inferior limit and a superior limit, and a median (updated at the end). (In French, limit is ‘borne’)

