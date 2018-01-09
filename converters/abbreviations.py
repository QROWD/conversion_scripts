from rdflib.graph import Graph
from rdflib.namespace import RDFS
from rdflib.term import Literal

from converters import Converter
from utils.rdf import get_resource
from utils.rdfserialization import get_rdf_serialization_by_file_suffix
from utils.vocabularies import dbpediaontology as dbo


class AbbreviationsConverter(Converter):
    def __init__(self, file_path):
        self.file_path = file_path
        self.lang = 'en'

    def set_lang(self, lang):
        self.lang = lang

    def to_rdf(self):
        g = Graph()

        with open(self.file_path) as in_file:
            for line in in_file:
                if line.strip():
                    full, abbrv = line.split('|')

                    full_uri = get_resource(full)
                    abbrv_uri = get_resource(abbrv)
                    g.add((full_uri, dbo.abbreviation, abbrv_uri))
                    g.add((
                        full_uri,
                        RDFS.label,
                        Literal(full.strip(), lang=self.lang)))
                    g.add((
                        abbrv_uri,
                        RDFS.label,
                        Literal(abbrv.strip(), lang=self.lang)))

        return g

    def to_rdf_file(self, out_file_path):
        ser_format = get_rdf_serialization_by_file_suffix(out_file_path)

        rdf = self.to_rdf()

        rdf.serialize(out_file_path, ser_format)
