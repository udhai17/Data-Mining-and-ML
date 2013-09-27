import codecs
from math import sqrt
class Recommender:

    def __init__(self, dats, k=1, metric="pearson", n=5):
    # k -> k in the kth nearest neighbour algorithm
    # n -> no. of recommendations to make.

        self.k = k
        self.n = n
        self.usernametoID = {}
        self.userIDtoname = {}
        self.productIDtoname = {}
        self.metric = metric
        if self.metric == "pearson":
            self.fn = self.pearson
    
        if type(data).__name__ == "dict":
            self.data = data
    
        def ConvertProductIDtoname(self,ID):  #for returning the name if the ID no. is given
            if ID in self.productIDtoname:
                return self.productIDtoname[ID]
            else:
                return ID
            
        def Ratings(self, ID, n):  #for returning n top ratings for user with id = ID
            print("The ratings for" + self.userIDtoname)
            ratings = self.data[ID]
            print (len(ratings))
            ratings = list(ratings.items())
            for(k,v) in ratings:
                ratings = [(self.ConvertProductIDtoname(k),v)]
            
        #Now, we sort the ratings array and return
            ratings.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
            ratings = ratings[:n]
            print("%s \t %i", (ratings[0], ratings[1]))
            
        #Now, we start the loading process from the sample data-base.    
        def LoadData(self, path=''):
            self.data = {}
            
        #Loading the data of the database into the self.data()
            i = 0
            f=codecs.open(path + "BX-Book-Ratings.csv" + 'r' + 'UTF-8')
            for line in f:
                i += 1
                fields = line.split(';')
                user = fields[0].strip('"')
                item = field[1].strip('"')
                rating = int(fields[2].strip().strip('"'))
                
                if user in self.data:
                    userRating = self.data[user]
                else:
                    userRating = {}
                
                userRating[item] = rating
                self.data[user] = userRating
                f.close()
                
                
                
                
                
                
                
                
                
                
