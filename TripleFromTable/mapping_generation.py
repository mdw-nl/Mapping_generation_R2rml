from textwrap import dedent
from .config.configuration import Config_mapping


def define_subject_map(iri_class, class_name, column, template="http://example.com/resource/patient/"):
    subject_map = f"""    rr:subjectMap [
            rr:template "{template}{{{column}}}";
            rr:class {iri_class}:{class_name};
        ];
        """
    return subject_map.strip()


def define_predicate_map(iri_predicate, iri_value, column, relation="column", last=False):
    """
    :param last:
    :param column:
    :param iri_predicate:
    :param iri_value:
    :param i:
    :param relation:
    :return:
    """
    predicate_map = f"""    rr:predicateObjectMap [
            rr:predicate {iri_predicate}:{iri_value};
            rr:objectMap [ rr:{relation} "{column}" ];
        ]"""
    if last:
        predicate_map = predicate_map + "."
    else:
        predicate_map = predicate_map + ";"
    return predicate_map.strip()


class Triple_process:

    def __init__(self, config_path):
        self.start = f"""<#TriplesMap1>
    rr:logicalTable [ rr:tableName "ClinicalData" ];"""

        self.config: Config_mapping = Config_mapping(config_path)
        self.starting = None
        self.subject_l = self.config.subject_list
        self.predicate_l = self.config.predicate_list
        self.uri_l = self.config.uri_list

        self.starting_uri = dedent("""\
        @prefix map: <http://mapping.local/>.
        @prefix rr: <http://www.w3.org/ns/r2rml#>.
        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
        @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
        """)

    def starting_point(self):
        """
        TODO:handle database or csv
        :return:
        """
        self.starting = f"""map:patient a rr:TriplesMap;
            rr:logicalTable map:patientQuery;
            """

    def generate_r2rml(self):
        """

        :return:
        """
        r2rml_output = "\n\n".join([self.starting_uri,
                                    self.starting_point(),
                                    define_subject_map("ex", "ClassName"),
                                    define_predicate_map("ex", "predicate", "columnName", 0),
                                    # Add more parts here
                                    ])
        return r2rml_output

    def generate_uri(self):
        """

        :param prefix:
        :param uri:
        :return:
        """
        result = ""
        for ur in self.uri_l:
            temp = dedent(f"""@prefix {ur["prefix"]}:{ur["uri"]}.""")
            result += "\n".join([temp])
        return result

    def check_subject_number(self):
        """
        :return:
        """
        list_f = []
        for sub in self.subject_l:
            list_f.append(sub["id"])
        list_f = list(set(list_f))
        return list_f

    def flow_generation(self):
        """

        :return:
        """
        list_result = []
        list_id = self.check_subject_number()
        #
        for ID in list_id:
            selected_sub = [e for e in self.subject_l if e["id"] == ID]
            #
            for sub in selected_sub:
                temp = "\t" + define_subject_map(template=sub["template"],
                                                 iri_class=sub["iri_class"],
                                                 class_name=sub["class_name"],
                                                 column=sub["column"])
                #
                selected_pred = [e for e in self.predicate_l if e["id_subj"] == ID]
                # for sel in selected_pred:
                for j in range(len(selected_pred)):
                    last = False if j < len(selected_pred) - 1 else True
                    temp = "\n\t".join([temp, define_predicate_map(iri_predicate=selected_pred[j]["iri_predicate"],
                                                                   iri_value=selected_pred[j]["iri_value"],
                                                                   column=selected_pred[j]["column"], last=last)])
                list_result.append(temp)

        return list_result

    def start_flow(self, out_put_dir="./R2rmlMappingFile/"):
        """

        :param out_put_dir:
        :return:
        """

        result = "\n".join([self.starting_uri + self.generate_uri(), self.start])
        ending = self.flow_generation()

        for i in ending:
            result = "\n\n".join([result, i])

        with open(out_put_dir + "mapping.ttl", "w") as file:
            file.write(result)
            file.close()
