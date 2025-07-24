class Piece:

    def __init__(self):
        self.attacks = [0 for square in range(64)]

    def getCoord(self, index):
        """
        Convert square index to coordinates.

        {args}
        index (int): index corresp to square

        {returns}
        The square's rank & file coordinates.
        """

        rank = index // 8
        file = index % 8
        return rank, file
    
    def getIndex(self, rank, file):
        """
        Calculate square index from coordinates.

        {args}
        rank (int): row of square
        file (int): column of square

        {returns} index corresponding to square.
        """

        return rank * 8 + file