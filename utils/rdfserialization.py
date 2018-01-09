from os.path import sep

from utils import constants

suffix2serialization = {
    'nt': constants.ntriples,
    'xml': constants.rdfxml,
    'rdf': constants.rdfxml,
    'ttl': constants.turtle
}


def get_rdf_serialization_by_file_suffix(file_path):
    file = file_path.rsplit(sep)[-1]
    suffix = file.rsplit('.')[-1]

    return suffix2serialization.get(suffix, constants.rdfxml)
