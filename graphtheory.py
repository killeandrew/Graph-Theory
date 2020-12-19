import graphadjacencylist


def main():

    print("----------------")
    print("| codedrome.com |")
    print("| GraphTheory   |")
    print("----------------\n")

    g = create_graph()

    print(g)

    # g = edit_graph(g)

    # print(g)


def create_graph():

    g = graphadjacencylist.GraphAdjacencyList()

    g.add_vertex("Annapolis")
    g.add_vertex("Washington D.C.")
    g.add_vertex("Frederick")
    g.add_vertex("Baltimore")

    g.add_edge("Annapolis", "Washington D.C.", directed = False, weight = 32)
    g.add_edge("Annapolis", "Baltimore", directed = False, weight = 31)
    g.add_edge("Annapolis", "Frederick", directed = False, weight = 75)

    g.add_edge("Washington D.C.", "Baltimore", directed = False, weight = 40)
    g.add_edge("Washington D.C.", "Frederick", directed = False, weight = 50)

    g.add_edge("Frederick", "Baltimore", directed = False, weight = 48)

    return g
    

main() 
