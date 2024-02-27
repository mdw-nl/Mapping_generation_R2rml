import yaml


class Config_mapping:
    def __init__(self, path_file):
        with open(path_file, 'r') as f:
            self.config_data = yaml.safe_load(f)
        self.subject_list = self.config_data['subject_section']
        self.predicate_list = self.config_data['predicate_section']
        self.uri_list = self.config_data["uri_section"]


class Config_r2rml:
    def __init__(self, path_file):
        with open(path_file, 'r') as f:
            self.config_data = yaml.safe_load(f)

        self.data_source_info = self.config_data["data source"]
        self.r2rml_map_loc = self.config_data["mapping"]
        self.data_source_type = self.data_source_info[0]["type_data"]

        self.mapping_loca = self.r2rml_map_loc[0]["path"]
        self.data_source_path_uri = self.data_source_info[0]["path_data"] if self.data_source_type == "csv" else \
            self.data_source_info[0]["db_uri"]

        if self.data_source_type != "csv" and self.data_source_type != "DB":
            raise Exception("Format not supported. Please specify csv or DB")
        elif self.data_source_type != "csv" and self.data_source_type == "DB" and self.data_source_uri is None:
            raise Exception("Error db address missing")
        elif self.data_source_type == "csv" and self.data_source_path_uri is None and self.data_source_type != "DB":
            raise Exception("Error csv path missing")
