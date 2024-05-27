from SPARQLWrapper import SPARQLWrapper, JSON, POST

def run_sparql_query(endpoint_url, query):
    """
    Execute a SPARQL query against a SPARQL endpoint and return the results.
    Args:
    - endpoint_url: URL of the SPARQL endpoint.
    - query: A string containing the SPARQL query.
    """
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    sparql.setMethod(POST) 
    try:
        results = sparql.query().convert()
        if results["results"]["bindings"]:
            for result in results["results"]["bindings"]:
                for var in result:
                    print(f"{var}: {result[var]['value']}")
            print() 
        else:
            print("No results found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    endpoint = "http://10-192-112-22client.eduroam.upc.edu:7200/repositories/sdm_lab_02"
    
    # Query 1
    query1 = """
        PREFIX research: <http://www.example.edu/research/>

        SELECT ?author ?author_name
        WHERE {
            ?author a research:author ;
                    research:author_name ?author_name .
        }
    """
    print("Results of Query 1:")
    run_sparql_query(endpoint, query1)

    # Query 2
    query2 = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX research: <http://www.example.edu/research/>

        SELECT ?property
        WHERE {
            ?property rdf:type rdf:Property ;
                    rdfs:domain research:author .
        }

    """
    print("Results of Query 2:")
    run_sparql_query(endpoint, query2)

    # Query 3
    query3 = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX research: <http://www.example.edu/research/>

        SELECT ?property
        WHERE {
        {
            ?property rdf:type rdf:Property ;
                    rdfs:domain research:conferences .
        }
        UNION
        {
            ?property rdf:type rdf:Property ;
                    rdfs:domain research:journals .
        }
        }
    """
    print("Results of Query 3:")
    run_sparql_query(endpoint, query3)

    # Query 4
    query4 = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX research: <http://www.example.edu/research/>

        SELECT distinct ?author_name ?paper_title 
        WHERE {
        ?author rdf:type research:author ;
                research:author_name ?author_name ;
                research:writes ?paper .
        ?paper rdf:type research:paper ;
                research:paper_title ?paper_title ;
                research:presented_in ?conferences .
        ?conference rdf:type research:conferences ;
                    research:conference_name ?conference_name .
        }
        order by ?author_name
    """
    print("Results of Query 4:")
    run_sparql_query(endpoint, query4)

if __name__ == "__main__":
    main()
