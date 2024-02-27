from .config.configuration import Config_r2rml
import morph_kgc
import kglab


class r2rml_conversion:
    def __init__(self, config_path):
        self.kg = None
        self.config_g: Config_r2rml = Config_r2rml(config_path)
        self.config_r2rml = f"""
            
            [DataSource1]
            mappings: {self.config_g.mapping_loca}
            file_path: {self.config_g.data_source_path_uri}
         """
        self.namespaces = {
            "ex": "http://example.com/",
            "map": "http://mapping.local/",
            "rr": "http://www.w3.org/ns/r2rml#",
            "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "xsd": "http://www.w3.org/2001/XMLSchema#"
        }

    def materialize(self):
        """
        :return:
        """

        kg = kglab.KnowledgeGraph(
            name="A KG example with students and sports",
            namespaces=self.namespaces,
        )
        kg.materialize(self.config_r2rml)
        self.kg = kg

    def create_namespace(self,list_from_c):
        for el in list_from_c:
            self.namespaces[el["prefix"]] = el["uri"]

    def save_kg(self, output_file="./Output Data/r2rml_output.ttl"):
        """

        :param output_file:
        :return:
        """
        self.kg.save_rdf(output_file)
