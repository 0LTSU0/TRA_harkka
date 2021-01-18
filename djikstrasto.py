INF = float("inf")


class WEN:      #Weighted edge node
    def __init__(self,nodde,weigght=0):
        self.node = nodde
        self.weight = weigght

class WG:       #Weighted graph
    def __init__(self,everticies):
        self.evertices = everticies
        self.adjencylist = {}
        self.vertices = []
        self.distance = {}
        self.p = {}

        for x in range(1,everticies+1): #listojen "alustukset"
            self.adjencylist[x] = []
            self.vertices.append(x)
            self.distance[x] = INF
            self.p[x] = None

def dijkstra(data):                             #tavallaan tämän dijkstratoteutuksen main funktio, hoitaa muiden kutsumiset ja addaa edget yms.
    citiesnroads = data.readline().split()
    cities = int(citiesnroads[0])			    #montako kaupunkia
    roads = int(citiesnroads[1])				#montako tietä
    print('')
    print("Löytyi {} kaupunkia ja {} tietä".format(cities, roads))						
    print('')
    graph = WG(cities)				            #graafi
    print('Suoritetaan algoritmia...')
    print('')
    for i in range(roads):						#lisätään edget 
        rivi = data.readline().split()
        solmu1 = int(rivi[0])
        solmu2 = int(rivi[1])
        paino = int(rivi[2])
        graph.adjencylist[solmu1].append(WEN(solmu2,paino))
        graph.adjencylist[solmu2].append(WEN(solmu1,paino))
    
    dest = int(data.readline())
    djikstraalgo(graph,1)
    print("Matalimman kohdan sisältämä polku reitillä 1 -> {}:".format(dest))
    route = []
    heights = []                        #korkeuksien erot, jota ei itseasiassa käytetä mihinkään (lisää tästä selostuksessa)
    
    maxi = path(graph,dest,route,heights)      #tehdään route (ja heights) listat
    print(route)
    #print(heights)
    #maxi = highest(heights,len(route)-1)
    print('')
    print("Korkein kohta tällä reitillä on",maxi)
    

def djikstraalgo(gr,start):             #varsinaisen dijkstra algoreitmin suoritus
    for i in gr.vertices:
        gr.distance[i] = INF
        gr.p[i] = 0
    gr.distance[start]=0
    
    queue = [i for i in gr.vertices]
    #print(queue)
    while len(queue) > 0:
        minv = INF
        u = 0
        for v in queue:
            if gr.distance[v] < minv:
                minv = gr.distance[v]
                u = v
        queue.remove(u)

        for e in gr.adjencylist[u]:                         
            v = e.node                                      
            if gr.distance[v] > max(gr.distance[u],e.weight):   #pääasiallinen ero perusmuotoon tässä: ei etsitä lyhintä polkua vaan sitä, missä pienin maksimi paino
                gr.distance[v] = max(gr.distance[u],e.weight)   #tämä kohta oli ongelmallinen, mutta ratkaisu löytyi: https://cseweb.ucsd.edu/classes/sp00/cse202/graphs1.pdf
                gr.p[v] = u


def path(gr,u,route,heights):               #Lista kaupungeista, jotka reitille tulee sekä epämääräinen lista painoista. Käytännössä siitä näkee aina, missä kohtaa maksimipaino on muuttunut
    if gr.p[u] != 0:
        path(gr,gr.p[u],route,heights)
    #print(u,gr.distance[u])
    route.append(u)
    heights.append(gr.distance[u])
    return gr.distance[u]

def noroute():                              #Jos djikstraalgo aiheuttaa erroria (eli reittiä ei voida muodostaa), tullaan tänne
	print("Reitin muodostus ei onnistu!")
	print("Onko kaupunkien välillä varmasti yhtenäinen polku?")