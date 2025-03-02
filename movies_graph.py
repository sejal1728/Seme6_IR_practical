import xml.dom.minidom
import networkx as nx
import matplotlib.pyplot as plt

# Function to parse the XML file and extract movie relationships
def parse_xml(filename):
    """Parses the XML file and extracts movie titles."""
    movies_graph = nx.Graph()

    # Load and parse the XML file
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement

    # Get all movies in the collection
    movies = collection.getElementsByTagName("movie")

    movie_titles = []  # Store movie titles for edges
    genre_map = {}  # Store genre relationships

    for movie in movies:
        if movie.hasAttribute("title"):
            title = movie.getAttribute("title")
            movie_titles.append(title)
            movies_graph.add_node(title)  # Add movie as a node

            # Get genre (type) of the movie
            type_element = movie.getElementsByTagName('type')[0]
            genres = type_element.childNodes[0].data.split(", ")  # Split multiple genres
            
            # Create genre relationships
            for genre in genres:
                if genre not in genre_map:
                    genre_map[genre] = []
                genre_map[genre].append(title)

    # Connect movies of the same genre
    for genre, titles in genre_map.items():
        for i in range(len(titles)):
            for j in range(i + 1, len(titles)):
                movies_graph.add_edge(titles[i], titles[j])  # Add edges

    return movies_graph

# Function to compute topic-specific PageRank
def compute_pagerank(graph, topic_movies, alpha=0.85):
    """Computes topic-sensitive PageRank with a bias towards topic-related movies."""
    bias = {node: (1 / len(topic_movies) if node in topic_movies else 0) for node in graph}
    return nx.pagerank(graph, alpha=alpha, personalization=bias)

# Function to visualize the movie graph
def visualize_graph(graph):
    """Draws and displays the graph."""
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph)  # Layout for better visualization
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=8)
    plt.title("Movie Genre Web Graph")
    plt.show()

# Main Execution
if __name__ == "__main__":
    # Step 1: Parse the XML file and build the graph
    movie_graph = parse_xml("movies.xml")

    # Step 2: Define topic-specific movies (e.g., Anime genre)
    topic_movies = ["One Piece: Stampede", "Your Name"]

    # Step 3: Compute topic-specific PageRank
    page_ranks = compute_pagerank(movie_graph, topic_movies)

    # Step 4: Display PageRank scores
    print("\nTopic-Specific PageRank Scores:")
    for movie, score in sorted(page_ranks.items(), key=lambda x: x[1], reverse=True):
        print(f"{movie}: {score:.4f}")

    # Step 5: Visualize the Movie Web Graph
    visualize_graph(movie_graph)
