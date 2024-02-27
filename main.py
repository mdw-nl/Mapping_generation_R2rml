from TripleFromTable.mapping_generation import Triple_process
from TripleFromTable.r2rml_process import r2rml_conversion


if __name__ == "__main__":
    a = Triple_process("./config_file/config_r2rml.yml")
    a.start_flow()
    b = r2rml_conversion("./config_file/config_r2rml_data.yml")
    b.create_namespace(a.uri_l)
    b.materialize()
    b.save_kg()


