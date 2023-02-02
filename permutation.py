class Permutation:
    """
    A class that represents a permutation

    Attributes
    ------
    code: list
        the long representation of the permutation

    Methods
    ------
    execute(k)
        performs the permutation on the index k
    """

    def __init__(self, code):
        """
        Parameters
        -------
        code: list
            the long representation of the permutation
        """
        self.code = code

    def execute(self, k):
        """Performs the permutation on an index

        Parameters
        ------
        k: int
            The index on which to apply the permutation

        Returns
        -----
        int
            the image of the index under the permutation
        """
        return self.code[k - 1]
