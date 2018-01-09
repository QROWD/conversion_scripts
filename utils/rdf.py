from urllib.parse import quote

from rdflib.term import URIRef

from utils import constants


def get_resource(local_part_str):
    return URIRef(constants.default_ns + quote(local_part_str.strip(), safe=''))
