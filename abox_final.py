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
    dg.write_png("./GRAPH/ontology_with_instances.png")
    display(Image(png))

# research= URIRef("http://www.example.edu/research/") 
research = Namespace("http://www.example.edu/research/")

# Create a new Graph
g = Graph()

# Adding instances 

# adding paper node
df_node_papers= pd.read_csv("DATA/CSV_FILES/papers.csv", delimiter=",")
print("processing paper node...")
for index, row in df_node_papers.iterrows():
    paper_id = URIRef(research + f"paper_{row['paperId']}")
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
df_node_authors= pd.read_csv("DATA/CSV_FILES/authors.csv", delimiter=",")
print("processing author node...")
for index, row in df_node_authors.iterrows():
    author_id = URIRef(research + f"author_{row['authorId']}")
    name = Literal(row["name"])
    email = Literal(row["email"])

    # Add triples to the graph
    g.add((author_id, RDF.type, research.author))
    g.add((author_id, research.name, name))
    g.add((author_id, research.email, email))

# adding author writes paper property
df_node_author_writes_paper= pd.read_csv("DATA/CSV_FILES/author_writes.csv", delimiter=",")
print("processing author writes paper and corresponding author edge...")
for index, row in df_node_author_writes_paper.iterrows():
    # author_writes_paper_id= URIRef(research + f"awp_{index}")
    author_id = URIRef(research + f"author_{row['start_id']}")
    paper_id = URIRef(research + f"paper_{row['end_id']}")
    corresponding_author = str(row["corresponding_author"])

    g.add((author_id, research.writes, paper_id))
    # only adding those edges that where corresponding_author is true
    if corresponding_author.lower() == 'true':
        g.add((author_id, research.corresponding_author, paper_id))

# adding conferences node
df_node_conferences= pd.read_csv("DATA/CSV_FILES/conferences.csv", delimiter=",")
print("processing conferences node...")
for index, row in df_node_conferences.iterrows():
    conference_id = URIRef(research + f"conference_{row['publicationId']}")
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
df_node_workshops= pd.read_csv("DATA/CSV_FILES/workshops.csv", delimiter=",")
print("processing workshops node...")
for index, row in df_node_workshops.iterrows():
    workshop_id = URIRef(research + f"workshop_{row['publicationId']}")
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
df_node_journals= pd.read_csv("DATA/CSV_FILES/journal.csv", delimiter=",")
print("processing journals node...")
for index, row in df_node_journals.iterrows():
    journal_id = URIRef(research + row['publicationId'])
    publication_type = Literal(row['publicationType'])
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
df_node_keywords= pd.read_csv("DATA/CSV_FILES/keywords.csv", delimiter=",")
print("processing keywords node...")
for index, row in df_node_keywords.iterrows():
    keyword_id = URIRef(research + f"keyword_{row['ID']}")
    name = Literal(row["name"])
    domain = Literal(row["domain"])

    # Add triples to the graph
    g.add((keyword_id, RDF.type, research.keywords))
    g.add((keyword_id, research.name, name))
    g.add((keyword_id, research.domain, domain))

# adding proceedings node
df_node_proceedings= pd.read_csv("DATA/CSV_FILES/proceedings.csv", delimiter=",")
print("processing proceedings node...")
for index, row in df_node_proceedings.iterrows():
    proceeding_id = URIRef(research + f"proceeding_{row['ID']}")
    name = Literal(row["name"])
    city = Literal(row["city"])

    # Add triples to the graph
    g.add((proceeding_id, RDF.type, research.proceedings))
    g.add((proceeding_id, research.name, name))
    g.add((proceeding_id, research.city, city))

# adding reviews edge
df_node_reviewers= pd.read_csv("DATA/CSV_FILES/reviews_with_decisions.csv", delimiter=",")
print("processing reviewer reviews paper edge...")
for index, row in df_node_reviewers.iterrows():
    reviewer_id = URIRef(research + f"reviewer_{row['reviewerId']}")
    paper_id = URIRef(research + f"paper_{row['paperId']}")

    # Add triples to the graph
    g.add((reviewer_id, RDF.type, research.reviewer))
    g.add((reviewer_id, research.reviews, paper_id))

# adding cites edge
df_node_cited_papers= pd.read_csv("DATA/CSV_FILES/paper_cite_paper.csv", delimiter=",")
print("processing paper cites paper edge...")
for index, row in df_node_cited_papers.iterrows():
    paper_id = URIRef(research + f"paper_{row['paper_id']}")
    cited_paper_id = URIRef(research + f"paper_{row['cited_paper_id']}")

    # Add triples to the graph
    g.add((paper_id, research.cites, cited_paper_id))

# adding paper_presented_in_condferences edge
df_edge_paper_presented_in_conference= pd.read_csv("DATA/CSV_FILES/paper_presented_in_conference.csv", delimiter=",")
print("processing paper presented in conference edge...")
for index, row in df_edge_paper_presented_in_conference.iterrows():
    paper_id = URIRef(research + f"paper_{row['START_ID']}")
    conference_id = URIRef(research + f"conference_{row['END_ID']}")

    # Add triples to the graph
    g.add((paper_id, research.presented_in, conference_id))

# adding paper_presented_in_workshops edge
df_edge_paper_presented_in_workshop= pd.read_csv("DATA/CSV_FILES/paper_presented_in_workshop.csv", delimiter=",")
print("processing paper presented in workshop edge...")
for index, row in df_edge_paper_presented_in_workshop.iterrows():
    paper_id = URIRef(research + f"paper_{row['START_ID']}")
    workshop_id = URIRef(research + f"workshop_{row['END_ID']}")

    # Add triples to the graph
    g.add((paper_id, research.presented_in_work, workshop_id))

# adding paper_published_in_journals edge
df_edge_paper_published_in_journal= pd.read_csv("DATA/CSV_FILES/paper_published_in_journal.csv", delimiter=",")
print("processing paper published in journal edge...")
for index, row in df_edge_paper_published_in_journal.iterrows():
    paper_id = URIRef(research + f"paper_{row['START_ID']}")
    journal_id = URIRef(research + f"conference_{row['END_ID']}")

    # Add triples to the graph
    g.add((paper_id, research.published_in, journal_id))

# adding has edge
df_edge_paper_has_keywords= pd.read_csv("DATA/CSV_FILES/paper_keyword.csv", delimiter=",")
print("processing paper has keywords edge...")
for index, row in df_edge_paper_has_keywords.iterrows():
    paper_id = URIRef(research + f"paper_{row['START_ID']}")
    keyword_id = URIRef(research + f"keyword_{row['END_ID']}")

    # Add triples to the graph
    g.add((paper_id, research.has, keyword_id))

# adding confernce_is_part_of_proceedings edge
df_edge_conference_is_part_of_proceedings= pd.read_csv("DATA/CSV_FILES/conference_part_of_proceedings.csv", delimiter=",")
print("processing conference is part of proceedings edge...")
for index, row in df_edge_conference_is_part_of_proceedings.iterrows():
    conference_id = URIRef(research + f"conference_{row['START_ID']}")
    proceeding_id = URIRef(research + f"proceeding_{row['END_ID']}")

    # Add triples to the graph
    g.add((conference_id, research.is_partof, proceeding_id))

# Instance- adding workshop_is_part_of_proceedings edge
df_edge_workshop_is_part_of_proceedings= pd.read_csv("DATA/CSV_FILES/paper_keyword.csv", delimiter=",")
print("processing workshop is part of proceedings edge...")
for index, row in df_edge_workshop_is_part_of_proceedings.iterrows():
    workshop_id = URIRef(research + f"workshop_{row['START_ID']}")
    proceeding_id = URIRef(research + f"proceeding_{row['END_ID']}")

    # Add triples to the graph
    g.add((workshop_id, research.work_is_partof, proceeding_id))

directory = './ABOX_DATA/'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the file path
os_path = os.path.join(directory, "abox_final.rdf")

print(g.serialize(os.path.join(directory, "abox_final.rdf"), format="xml"))

# visualize graph
# visualize(g)