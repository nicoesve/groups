import permutation


class PermutationGroup:
    """Represents a permutation group

    Attributes
    -----
    n: int
        The size of the index set for the group
    e: Permutation
        The identity of the group

    Methods
    ----
    c(perm_1, perm_2)
        Concatenates two permutations
    """

    def __init__(self, n):
        """
        Parameters
        ----
        n: int
            The size of the index set for the group
        """
        self.n = n
        self.e = permutation.Permutation(list(range(1, n + 1)))

    def c(self, perm_1, perm_2):
        """Concatenates two permutations

        Parameters
        -----
        perm_1: Permutation
        perm_2: Permutation

        Returns
        -----
        Permutation
        """
        return permutation.Permutation(
            [perm_2.execute(perm_1.execute(k)) for k in range(1, self.n + 1)]
        )

    def inv(self, perm):
        """Computes the inverse of a permutation

        Parameters
        ------
        perm: Permutation

        Returns
        -----
        Permutation
        """
        return permutation.Permutation(
            [perm.index(k) + 1 for k in range(1, self.n + 1)]
        )

    def pow(self, perm, exponent):
        """Computes a power of a permutation

        Parameters
        ----
        perm: Permutation
        exponent: int

        Returns
        ----
        Permutation
        """
        current = self.e
        if exponent > 0:
            for i in range(exponent):
                current = self.c(current, perm)
        elif exponent < 0:
            for i in range(exponent):
                current = self.c(current, self.inv(perm))
        return current
