from SPARQLWrapper import SPARQLWrapper, POST, DIGEST, POSTDIRECTLY
import configparser

def load_rdf_data(sparql_endpoint, file_path, graph_uri):
    """
    Load RDF data from a file to GraphDB using a SPARQL endpoint.
    
    Args:
    - sparql_endpoint: The URL of the GraphDB SPARQL endpoint for statements.
    - file_path: The full path to the RDF file to be loaded.
    - graph_uri: The URI of the graph where data will be loaded.
    """
    sparql = SPARQLWrapper(sparql_endpoint)
    sparql.setMethod(POST)
    sparql.setHTTPAuth(DIGEST)
    sparql.setRequestMethod(POSTDIRECTLY)
    
    file_uri = f"file://localhost{file_path}"
    query = f"LOAD <{file_uri}> INTO GRAPH <{graph_uri}>"
    sparql.setQuery(query)

    try:
        results = sparql.query()
        print(f"Data loaded successfully from {file_uri} into {graph_uri}")
        print(results.response.read())
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Load configuration
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Retrieve configuration values
    sparql_endpoint = config['GraphDB']['endpoint']
    tbox_file_path = config['TBOX']['file_path']
    tbox_graph_uri = config['TBOX']['graph_uri']
    abox_file_path = config['ABOX']['file_path']
    abox_graph_uri = config['ABOX']['graph_uri']

    # Load TBOX and ABOX
    load_rdf_data(sparql_endpoint, tbox_file_path, tbox_graph_uri)
    load_rdf_data(sparql_endpoint, abox_file_path, abox_graph_uri)

if __name__ == "__main__":
    main()
