class Track:
    defTrack1 = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1, 1, 1, 1, 1, 1, 1, 1, 1,-1],
                 [-1, 1, 0, 0, 0, 0, 0, 0, 1,-1],
                 [-1, 1, 0, 0, 0, 0, 0, 0, 1,-1],
                 [-1, 1, 0, 0, 0, 0, 0, 0, 1,-1],
                 [-1, 1, 0, 0, 0, 0, 0, 0, 1,-1],
                 [-1, 1, 0, 1, 1, 1, 1, 0, 1,-1],
                 [-1, 1, 0, 1,-1,-1, 1, 0, 1,-1],
                 [-1, 1, 1, 1,-1,-1, 1, 1, 1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

    track = None

    def copyTrack(self, track):
        return [row[:] for row in track]

    def __init__(self):
        self.track = self.copyTrack(self.defTrack1)

    def __str__(self):

        sizeX = len(self.track[0])
        sizeY = len(self.track)

        string = ""
        for iy in xrange(0,sizeY):
            string += " ".join(str(x).zfill(2) for x in self.track[iy])
            string += "\n"

        return string
