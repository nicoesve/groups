import permutation
import group

perm_1 = permutation.Permutation((3, 4, 1, 2, 5))

perm_2 = permutation.Permutation([4, 1, 5, 2, 3])

group_5 = group.PermutationGroup(5)

print(group_5.pow(perm_2, 3).code)
