from SPARQLWrapper import SPARQLWrapper, JSON

sparql_endpoint_url = "http://localhost:7200/rest/repositories/sdm_lab_2"

sparql = SPARQLWrapper(sparql_endpoint_url)

sparql.setQuery("""
    SELECT ?subject ?predicate ?object
    WHERE {
        ?subject ?predicate ?object.
    }
    LIMIT 10
""")

sparql.setReturnFormat(JSON)

results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(f"{result['subject']['value']} {result['predicate']['value']} {result['object']['value']}")
