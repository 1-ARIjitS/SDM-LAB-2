from rdflib import Graph, URIRef, BNode, Literal
from rdflib import Namespace
import pandas as pd
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
    dg.write_png("./GRAPH/ontology_with_instances.png")
    display(Image(png))

# research= URIRef("http://www.example.edu/research/") 
research = Namespace("http://www.example.edu/research/")

# Create a new Graph
g = Graph()

# Adding triples

# adding paper node
g.add((research.paper, RDF.type, RDFS.Class))
# Instance- adding papers
df_node_papers= pd.read_csv("DATA/papers.csv", delimiter=",")
for index, row in df_node_papers.iterrows():
    paper_id = URIRef(research + f"paper_{row["paperId"]}")
    title = Literal(row["title"])
    abstract = Literal(row["abstract"])
    pages = Literal(row["pages"])
    doi = Literal(row["DOI"])
    link = URIRef(row["link"])
    date = Literal(row["date"])

    # Add triples to the graph
    g.add((paper_id, RDF.type, research.paper))
    g.add((paper_id, research.title, title))
    g.add((paper_id, research.abstract, abstract))
    g.add((paper_id, research.pages, pages))
    g.add((paper_id, research.DOI, doi))
    g.add((paper_id, research.link, link))
    g.add((paper_id, research.date, date))

# adding author node
g.add((research.author, RDF.type, RDFS.Class))
# Instance- adding authors
df_node_authors= pd.read_csv("DATA/authors.csv", delimiter=",")
for index, row in df_node_authors.iterrows():
    author_id = URIRef(research + f"author_{row["authorId"]}")
    name = Literal(row["name"])
    email = Literal(row["email"])

    # Add triples to the graph
    g.add((author_id, RDF.type, research.author))
    g.add((author_id, research.name, name))
    g.add((author_id, research.email, email))

# adding writes node
g.add((research.writes, RDF.type, RDFS.Class))

# adding edge between author and writes
g.add((research.write_role, RDFS.domain, research.author))
g.add((research.write_role, RDFS.range, research.writes))
g.add((research.write_role, RDF.type, RDF.Property))

# adding edge between writes and paper
g.add((research.write, RDFS.domain, research.writes))
g.add((research.write, RDFS.range, research.paper))
g.add((research.write, RDF.type, RDF.Property))

# adding author writes paper node
df_node_author_writes_paper= pd.read_csv("DATA/author_writes.csv", delimiter=",")
for index, row in df_node_author_writes_paper.iterrows():
    author_writes_paper_id= URIRef(research + f"awp_{index}")
    author_id = URIRef(research + f"author_{row["start_id"]}")
    paper_id = URIRef(research + f"paper_{row["end_id"]}")
    corresponding_author = Literal(row["corresponding_author"])

    # Add triples to the graph
    g.add((author_writes_paper_id, RDF.type, research.writes))
    g.add((author_id, research.write_role, author_writes_paper_id))
    g.add((author_writes_paper_id, research.write, paper_id))
    g.add((author_writes_paper_id, research.corresponding_author, corresponding_author))

# adding conferences node
g.add((research.conferences, RDF.type, RDFS.Class))
# Instance- adding conferences
df_node_conferences= pd.read_csv("DATA/conferecnes.csv", delimiter=",")
for index, row in df_node_conferences.iterrows():
    conference_id = URIRef(research + f"conference_{row["publicationId"]}")
    name = Literal(row["name"])
    year = Literal(row["year"])
    venue = Literal(row["venue"])
    issn = Literal(row["issn"])
    url = Literal(row["url"])
    edition = Literal(row["edition"])
    chair = Literal(row["conferenceChair"])

    # Add triples to the graph
    g.add((conference_id, RDF.type, research.conferences))
    g.add((conference_id, research.name, name))
    g.add((conference_id, research.year, year))
    g.add((conference_id, research.venue, venue))
    g.add((conference_id, research.issn, issn))
    g.add((conference_id, research.url, url))
    g.add((conference_id, research.edition, edition))
    g.add((conference_id, research.conferenceChair, chair))

# adding workshops node
g.add((research.workshops, RDF.type, RDFS.Class))
# Instance- adding workshops
df_node_workshops= pd.read_csv("DATA/workshops.csv", delimiter=",")
for index, row in df_node_workshops.iterrows():
    workshop_id = URIRef(research + f"workshop_{row["publicationId"]}")
    name = Literal(row["name"])
    year = Literal(row["year"])
    venue = Literal(row["venue"])
    issn = Literal(row["issn"])
    url = Literal(row["url"])
    edition = Literal(row["edition"])
    chair = Literal(row["workshopChair"])

    # Add triples to the graph
    g.add((workshop_id, RDF.type, research.workshops))
    g.add((workshop_id, research.name, name))
    g.add((workshop_id, research.year, year))
    g.add((workshop_id, research.venue, venue))
    g.add((workshop_id, research.issn, issn))
    g.add((workshop_id, research.url, url))
    g.add((workshop_id, research.edition, edition))
    g.add((workshop_id, research.workshopChair, chair))

# adding journals node
g.add((research.journals, RDF.type, RDFS.Class))
# Instance- adding journals
df_node_journals= pd.read_csv("DATA/journal.csv", delimiter=",")
for index, row in df_node_journals.iterrows():
    journal_id = URIRef(research + row["publicationId"])
    publication_type = Literal(row["publicationType"])
    name = Literal(row["name"])
    venue = Literal(row["venue"])
    year = Literal(row["year"])
    issn = Literal(row["issn"])
    url = Literal(row["url"])
    volume = Literal(row["volume"])
    editor = Literal(row["JournalEditor"])

    # Add triples to the graph
    g.add((journal_id, RDF.type, research.journals))
    g.add((journal_id, research.publicationType, publication_type))
    g.add((journal_id, research.name, name))
    g.add((journal_id, research.venue, venue))
    g.add((journal_id, research.year, year))
    g.add((journal_id, research.issn, issn))
    g.add((journal_id, research.url, url))
    g.add((journal_id, research.volume, volume))
    g.add((journal_id, research.journalEditor, editor))

# adding keywords node
g.add((research.keywords, RDF.type, RDFS.Class))
# Instance- adding keywords
df_node_keywords= pd.read_csv("DATA/keywords.csv", delimiter=",")
for index, row in df_node_keywords.iterrows():
    keyword_id = URIRef(research + f"keyword_{row["ID"]}")
    name = Literal(row["name"])
    domain = Literal(row["domain"])

    # Add triples to the graph
    g.add((keyword_id, RDF.type, research.keywords))
    g.add((keyword_id, research.name, name))
    g.add((keyword_id, research.domain, domain))

# adding proceedings node
g.add((research.proceedings, RDF.type, RDFS.Class))
# Instance- adding proceedings
df_node_proceedings= pd.read_csv("DATA/proceedings.csv", delimiter=",")
for index, row in df_node_proceedings.iterrows():
    proceeding_id = URIRef(research + f"proceeding_{row["ID"]}")
    name = Literal(row["name"])
    city = Literal(row["city"])

    # Add triples to the graph
    g.add((proceeding_id, RDF.type, research.proceedings))
    g.add((proceeding_id, research.name, name))
    g.add((proceeding_id, research.city, city))

# adding reviewer derived node
g.add((research.reviewer, RDFS.subClassOf, research.author))
g.add((research.reviewer, RDF.type, RDFS.Class))

# adding reviews edge
g.add((research.reviews, RDFS.domain, research.reviewer))
g.add((research.reviews, RDFS.range, research.paper))
g.add((research.reviews, RDF.type, RDF.Property))

# Instance- adding reviewers node and reviews edge
df_node_reviewers= pd.read_csv("DATA/reviews_with_decisions.csv", delimiter=",")
for index, row in df_node_reviewers.iterrows():
    reviewer_id = URIRef(research + f"reviewer_{row["reviewerId"]}")
    paper_id = URIRef(research + f"paper_{row["paperId"]}")

    # Add triples to the graph
    g.add((reviewer_id, RDF.type, research.reviewer))
    g.add((reviewer_id, research.reviews, paper_id))

# adding cited_paper derived node 
g.add((research.cited_paper, RDFS.subClassOf, research.paper))
g.add((research.cited_paper, RDF.type, RDFS.Class))

# adding cites edge
g.add((research.cites, RDFS.domain, research.cited_paper))
g.add((research.cites, RDFS.range, research.paper))
g.add((research.cites, RDF.type, RDF.Property))

# Instance- adding cited_paper node and cites edge
df_node_cited_papers= pd.read_csv("DATA/paper_cite_paper.csv", delimiter=",")
for index, row in df_node_reviewers.iterrows():
    paper_id = URIRef(research + f"paper_{row["paper_id"]}")
    cited_paper_id = URIRef(research + f"paper_{row["cited_paper_id"]}")

    # Add triples to the graph
    g.add((cited_paper_id, RDF.type, research.cited_paper))
    g.add((cited_paper_id, research.cites, paper_id))

# adding presented_in edge for conferences 
g.add((research.presented_in, RDFS.domain, research.paper))
g.add((research.presented_in, RDFS.range, research.conferences))
g.add((research.presented_in, RDF.type, RDF.Property))

# Instance- adding paper_presented_in_condferences edge
df_edge_paper_presented_in_conference= pd.read_csv("DATA/paper_presented_in_condference.csv", delimiter=",")
for index, row in df_edge_paper_presented_in_conference.iterrows():
    paper_id = URIRef(research + f"paper_{row["START_ID"]}")
    conference_id = URIRef(research + f"conference_{row["END_ID"]}")

    # Add triples to the graph
    g.add((paper_id, research.presented_in, conference_id))

# adding presented_in edge for workshops 
g.add((research.presented_in_work, RDFS.domain, research.paper))
g.add((research.presented_in_work, RDFS.range, research.workshops))
g.add((research.presented_in_work, RDF.type, RDF.Property))

# Instance- adding paper_presented_in_workshops edge
df_edge_paper_presented_in_workshop= pd.read_csv("DATA/paper_presented_in_workshop.csv", delimiter=",")
for index, row in df_edge_paper_presented_in_workshop.iterrows():
    paper_id = URIRef(research + f"paper_{row["START_ID"]}")
    workshop_id = URIRef(research + f"workshop_{row["END_ID"]}")

    # Add triples to the graph
    g.add((paper_id, research.presented_in_work, workshop_id))

# adding published_in edge for journals 
g.add((research.published_in, RDFS.domain, research.paper))
g.add((research.published_in, RDFS.range, research.journals))
g.add((research.published_in, RDF.type, RDF.Property))

# Instance- adding paper_published_in_journals edge
df_edge_paper_published_in_journal= pd.read_csv("DATA/paper_published_in_journal.csv", delimiter=",")
for index, row in df_edge_paper_published_in_journal.iterrows():
    paper_id = URIRef(research + f"paper_{row["START_ID"]}")
    journal_id = URIRef(research + f"conference_{row["END_ID"]}")

    # Add triples to the graph
    g.add((paper_id, research.published_in, journal_id))

# adding has edge for papers 
g.add((research.has, RDFS.domain, research.paper))
g.add((research.has, RDFS.range, research.keywords))
g.add((research.has, RDF.type, RDF.Property))

# Instance- adding paper_has_keywords edge
df_edge_paper_has_keywords= pd.read_csv("DATA/paper_keyword.csv", delimiter=",")
for index, row in df_edge_paper_has_keywords.iterrows():
    paper_id = URIRef(research + f"paper_{row["START_ID"]}")
    keyword_id = URIRef(research + f"keyword_{row["END_ID"]}")

    # Add triples to the graph
    g.add((paper_id, research.has, keyword_id))

# adding is_partof edge for conferences 
g.add((research.is_partof, RDFS.domain, research.conferences))
g.add((research.is_partof, RDFS.range, research.proceedings))
g.add((research.is_partof, RDF.type, RDF.Property))

# Instance- adding confernce_is_part_of_proceedings edge
df_edge_conference_is_part_of_proceedings= pd.read_csv("DATA/conference_part_of_proceedings.csv", delimiter=",")
for index, row in df_edge_conference_is_part_of_proceedings.iterrows():
    conference_id = URIRef(research + f"conference_{row["START_ID"]}")
    proceeding_id = URIRef(research + f"proceeding_{row["END_ID"]}")

    # Add triples to the graph
    g.add((conference_id, research.is_partof, proceeding_id))

# adding is_partof edge for workshops
g.add((research.work_is_partof, RDFS.domain, research.workshops))
g.add((research.work_is_partof, RDFS.range, research.proceedings))
g.add((research.work_is_partof, RDF.type, RDF.Property))

# Instance- adding workshop_is_part_of_proceedings edge
df_edge_workshop_is_part_of_proceedings= pd.read_csv("DATA/paper_keyword.csv", delimiter=",")
for index, row in df_edge_workshop_is_part_of_proceedings.iterrows():
    workshop_id = URIRef(research + f"workshop_{row["START_ID"]}")
    proceeding_id = URIRef(research + f"proceeding_{row["END_ID"]}")

    # Add triples to the graph
    g.add((workshop_id, research.work_is_partof, proceeding_id))

# Serialize the graph to a file
# print(g.serialize())
print(g.serialize("./TBOX_DATA/tbox_and_abox.rdf", format="xml"))

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