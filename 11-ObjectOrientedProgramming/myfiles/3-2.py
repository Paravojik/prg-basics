class MusicPiece():
    def __init__(self,performer,title,album,year):
        self.performer=performer
        self.title=title
        self.album=album
        self.year=year


    def __str__(self):
        return f"{'Performer:':<15} {self.performer}\n{'Title:':<15} {self.title}\n{'Album:':<15} {self.album}\n{'Year:':<15} {self.year}\n"
    


song1=MusicPiece('Ed Sheeran',"Hearts Don't Break Around Here","Divide",2007)
print(song1)