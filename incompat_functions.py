##
##  incompat_functions.py
##
##
##  Created by Elise Kerdoncuff on 1/3/25.
##

def incompatibilities(variants, haplotypes, window_size):
    incompatibi=[]
    for i in range(len(variants) - 1):
        for j in range(i + 1, i + window_size):
            if j < len(variants):
                if variants[i] > variants[j]:
                    print(f"muta {i}={variants[i]}  muta {j}={variants[j]}, need to sort positions")
                
                table = [0, 0, 0, 0]  # to count the number of 'gametes' present
                
                for k in range(len(haplotypes[i])):
                    if haplotypes[i][k] == 0:
                        if haplotypes[j][k] == 0:  # 0-0
                            table[0] = 1
                        else:  # 0-1
                            table[1] = 1
                    else:
                        if haplotypes[j][k] == 0:  # 1-0
                            table[2] = 1
                        else:  # 1-1
                            table[3] = 1
                
                test4G = sum(table)
                
                if test4G == 4:  # 4 gametes, incompatible
                    incompatibi.append([variants[i],variants[j]])
    
    return incompatibi


class EventRecombi:
    def __init__(self):
        self.limit_inf = 0.0
        self.limit_sup = 0.0
        self.median = 0.0

def selection_segment_rm(incompatibi):
    recombiS = [EventRecombi()]  # Initialize with the first recombination segment
    compteur_segment = 0
    nb_incompat=len(incompatibi)
        
    # Initialization
    recombiS[compteur_segment].limit_inf = incompatibi[0][0]
    recombiS[compteur_segment].limit_sup = incompatibi[0][1]

    # Comparison
    for compteur in range(1, nb_incompat):
        i_2 = incompatibi[compteur][0]
        j_2 = incompatibi[compteur][1]

        # If segment is in the other
        if recombiS[compteur_segment].limit_inf <= i_2 and recombiS[compteur_segment].limit_sup >= j_2:
            recombiS[compteur_segment].limit_inf = i_2
            recombiS[compteur_segment].limit_sup = j_2
        # If segment is independent
        elif i_2 >= recombiS[compteur_segment].limit_sup:
            compteur_segment += 1
            new_segment = EventRecombi()
            new_segment.limit_inf = i_2
            new_segment.limit_sup = j_2
            recombiS.append(new_segment)

    nb_recombi = compteur_segment
    if nb_incompat != 0:
        nb_recombi += 1  # Count the first segment

    # Go backwards
    for i in range(nb_incompat):
        current_incompat = incompatibi[nb_incompat - 1 - i]
        if current_incompat[1] < recombiS[compteur_segment].limit_inf:
            compteur_segment -= 1
        if (recombiS[compteur_segment].limit_inf < current_incompat[0]< recombiS[compteur_segment].limit_sup):
            recombiS[compteur_segment].limit_inf = current_incompat[0]

    # Final step: compute the median of the segments
    breakpoints_recombi=[]
    for i in range(nb_recombi):
        recombiS[i].median = (recombiS[i].limit_sup + recombiS[i].limit_inf) / 2
        breakpoints_recombi.append(recombiS[i].median)
        

    return breakpoints_recombi
