from rdflib import Graph, URIRef, BNode, Literal
from rdflib import Namespace
import io
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
    dg.write_png("ontology.png")
    display(Image(png))

# research= URIRef("http://www.example.edu/research/") 
research = Namespace("http://www.example.edu/research/")

# Create a new Graph
g = Graph()

# Adding triples
g.add((research.paper, RDF.type, RDFS.Class))
g.add((research.author, RDF.type, RDFS.Class))
g.add((research.writes, RDF.type, RDFS.Class))
g.add((research.conferences, RDF.type, RDFS.Class))
g.add((research.workshops, RDF.type, RDFS.Class))
g.add((research.journals, RDF.type, RDFS.Class))
g.add((research.keywords, RDF.type, RDFS.Class))
g.add((research.proceedings, RDF.type, RDFS.Class))

g.add((research.reviewer, RDFS.subClassOf, research.author))
g.add((research.reviewer, RDF.type, RDFS.Class))

g.add((research.cited_paper, RDFS.subClassOf, research.paper))
g.add((research.cited_paper, RDF.type, RDFS.Class))

g.add((research.presented_in, RDFS.domain, research.paper))
g.add((research.presented_in, RDFS.range, research.conferences))
g.add((research.presented_in, RDF.type, RDF.Property))

g.add((research.presented_in_work, RDFS.domain, research.paper))
g.add((research.presented_in_work, RDFS.range, research.workshops))
g.add((research.presented_in_work, RDF.type, RDF.Property))

g.add((research.published_in, RDFS.domain, research.paper))
g.add((research.published_in, RDFS.range, research.journals))
g.add((research.published_in, RDF.type, RDF.Property))

g.add((research.has, RDFS.domain, research.paper))
g.add((research.has, RDFS.range, research.keywords))
g.add((research.has, RDF.type, RDF.Property))

g.add((research.write_role, RDFS.domain, research.author))
g.add((research.write_role, RDFS.range, research.writes))
g.add((research.write_role, RDF.type, RDF.Property))

g.add((research.write, RDFS.domain, research.writes))
g.add((research.write, RDFS.range, research.paper))
g.add((research.write, RDF.type, RDF.Property))

g.add((research.reviews, RDFS.domain, research.reviewer))
g.add((research.reviews, RDFS.range, research.paper))
g.add((research.reviews, RDF.type, RDF.Property))

g.add((research.cites, RDFS.domain, research.cited_paper))
g.add((research.cites, RDFS.range, research.paper))
g.add((research.cites, RDF.type, RDF.Property))

g.add((research.is_partof, RDFS.domain, research.conferences))
g.add((research.is_partof, RDFS.range, research.proceedings))
g.add((research.is_partof, RDF.type, RDF.Property))

g.add((research.work_is_partof, RDFS.domain, research.workshops))
g.add((research.work_is_partof, RDFS.range, research.proceedings))
g.add((research.work_is_partof, RDF.type, RDF.Property))

# Serialize the graph to a file
# print(g.serialize())
print(g.serialize("research.rdf", format="xml"))

# visualize graph
visualize(g)

# research:paper rdf:type rdfs:Class .
# research:author rdf:type rdfs:Class .
# research:writes rdf:type rdfs:Class .
# research:conferences rdf:type rdfs:Class .
# research:workshops rdf:type rdfs:Class .
# research:journals rdf:type rdfs:Class .
# research:keywords rdf:type rdfs:Class .
# research:proceedings rdf:type rdfs:Class .

# research:reviewer rdfs:subClassOf research:author ;
# rdf:type rdfs:Class .

# research:cited_paper rdfs:subClassOf research:paper ;
# rdf:type rdfs:Class .

# research:presented_in rdf:domain research:paper ;
# rdf:range research:conferences ;
# rdf:type rdfs:Property .

# research:presented_in_work rdf:domain research:paper ;
# rdf:range research:workshops ;
# rdf:type rdfs:Property .

# research:published_in rdf:domain research:paper ;
# rdf:range research:journals ;
# rdf:type rdfs:Property .

# research:has rdf:domain research:paper ;
# rdf:range research:keywords ;
# rdf:type rdfs:Property .

# research:write_role rdf:domain research:author ;
# rdf:range research:writes ;
# rdf:type rdfs:Property .

# research:write rdf:domain research:writes ;
# rdf:range research:paper ;
# rdf:type rdfs:Property .

# research:reviews rdf:domain research:reviewer ;
# rdf:range research:paper ;
# rdf:type rdfs:Property .

# research:cites rdf:domain research:cited_paper ;
# rdf:range research:paper ;
# rdf:type rdfs:Property .

# research:is_partof rdf:domain research:conferences ;
# rdf:range research:proceedings ;
# rdf:type rdfs:Property .

# research:work_is_partof rdf:domain research:workshops ;
# rdf:range research:proceedings ;
# rdf:type rdfs:Property .