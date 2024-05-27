from rdflib import Graph, URIRef, BNode, Literal
from rdflib.term import Node
from rdflib import Namespace
import pandas as pd
import io
import os
import pydotplus
from IPython.display import display, Image
from rdflib.tools.rdf2dot import rdf2dot
from rdflib.tools.rdf2dot import rdf2dot
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD

# Load the ABox and TBox RDF graphs into rdflib Graph objects
abox_graph = Graph()
abox_graph.parse("./ABOX_DATA/abox_final_test.rdf", format="xml")  # Load ABox RDF graph

tbox_graph = Graph()
tbox_graph.parse("./TBOX_DATA/tbox_final_test.rdf", format="xml")  # Load TBox RDF graph

# Link ABox nodes to TBox classes using rdf:type
print("processing the classes...")
for abox_node in abox_graph.subjects(RDF.type, None):
    for tbox_class in tbox_graph.objects(abox_node, RDF.type):
        abox_graph.add((abox_node, RDF.type, tbox_class))

# Link ABox edges to TBox properties
print("processing the properties...")
for subject, predicate, object_ in abox_graph:
    if predicate is not None:  # Check if the predicate is not None
        if isinstance(predicate, Node):  # Ensure the predicate is an rdflib term
            abox_graph.add((subject, predicate, object_))

# Serialize the RDF graph containing both ABox and TBox triples
combined_graph = abox_graph + tbox_graph
linked_directory= "./LINKED_GRAPH"
if not os.path.exists(linked_directory):
    os.makedirs(linked_directory)
    
combined_graph.serialize(os.path.join(linked_directory, "linked_graph.rdf"), format="xml")  # Serialize as RDF/XML

# Import the serialized RDF graph into GraphDB
# Use GraphDB's interface or API to import the serialized RDF graph into your repository