from rdflib import Graph, URIRef, BNode, Literal
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

# function to visualize graph
def visualize(g):
    stream = io.StringIO()
    rdf2dot(g, stream, opts = {display})
    dg = pydotplus.graph_from_dot_data(stream.getvalue())
    png = dg.create_png()
    dg.write_png("./GRAPH/ontology.png")
    display(Image(png))

# research= URIRef("http://www.example.edu/research/") 
research = Namespace("http://www.example.edu/research/")

# Create a new Graph
g = Graph()

# Adding triples

# adding paper node
print("adding paper node...")
g.add((research.paper, RDF.type, RDFS.Class))

# adding author nodec
print("adding author node...")
g.add((research.author, RDF.type, RDFS.Class))

# adding the writes edge
print("adding writes edge...")
g.add((research.writes, RDFS.domain, research.author))
g.add((research.writes, RDFS.range, research.paper))
g.add((research.writes, RDF.type, RDF.Property))

# adding corresponding_author edge
print("adding corresponding author edge...")
g.add((research.corresponding_author, RDFS.domain, research.author))
g.add((research.corresponding_author, RDFS.range, research.paper))
g.add((research.corresponding_author, RDF.type, RDF.Property))
g.add((research.corresponding_author, RDFS.subPropertyOf, research.writes))

# adding conferences node
print("adding conferences node...")
g.add((research.conferences, RDF.type, RDFS.Class))

# adding workshops node
print("adding workshops node...")
g.add((research.workshops, RDF.type, RDFS.Class))

# adding journals node
print("adding journals node...")
g.add((research.journals, RDF.type, RDFS.Class))

# adding keywords node
print("adding keywords node...")
g.add((research.keywords, RDF.type, RDFS.Class))

# adding proceedings node
print("adding proceedings node...")
g.add((research.proceedings, RDF.type, RDFS.Class))

# adding reviewer derived node
print("adding reviewer node...")
g.add((research.reviewer, RDFS.subClassOf, research.author))
g.add((research.reviewer, RDF.type, RDFS.Class))

# adding reviews edge
print("adding reviews edge...")
g.add((research.reviews, RDFS.domain, research.reviewer))
g.add((research.reviews, RDFS.range, research.paper))
g.add((research.reviews, RDF.type, RDF.Property))

# adding cites edge
print("adding cites edge...")
g.add((research.cites, RDFS.domain, research.paper))
g.add((research.cites, RDFS.range, research.paper))
g.add((research.cites, RDF.type, RDF.Property))

# adding presented_in edge for conferences 
print("adding presented_in edge...")
g.add((research.presented_in, RDFS.domain, research.paper))
g.add((research.presented_in, RDFS.range, research.conferences))
g.add((research.presented_in, RDF.type, RDF.Property))

# adding presented_in edge for workshops 
print("adding presented_in_work edge...")
g.add((research.presented_in_work, RDFS.domain, research.paper))
g.add((research.presented_in_work, RDFS.range, research.workshops))
g.add((research.presented_in_work, RDF.type, RDF.Property))

# adding published_in edge for journals 
print("adding published_in edge...")
g.add((research.published_in, RDFS.domain, research.paper))
g.add((research.published_in, RDFS.range, research.journals))
g.add((research.published_in, RDF.type, RDF.Property))

# adding has edge for papers 
print("adding has edge...")
g.add((research.has, RDFS.domain, research.paper))
g.add((research.has, RDFS.range, research.keywords))
g.add((research.has, RDF.type, RDF.Property))

# adding is_partof edge for conferences
print("adding is_partof edge...") 
g.add((research.is_partof, RDFS.domain, research.conferences))
g.add((research.is_partof, RDFS.range, research.proceedings))
g.add((research.is_partof, RDF.type, RDF.Property))

# adding is_partof edge for workshops
print("adding work_is_partof edge...")
g.add((research.work_is_partof, RDFS.domain, research.workshops))
g.add((research.work_is_partof, RDFS.range, research.proceedings))
g.add((research.work_is_partof, RDF.type, RDF.Property))

# creating directory
directory = './TBOX_DATA/'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the file path
filepath = os.path.join(directory, "tbox_f.xml")

print(g.serialize(filepath, format="pretty-xml"))

# visualize graph
visualize(g)