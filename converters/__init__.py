from abc import ABC, abstractmethod


class Converter(ABC):
    @abstractmethod
    def to_rdf(self):
        pass

    @abstractmethod
    def to_rdf_file(self, out_file_path):
        pass
