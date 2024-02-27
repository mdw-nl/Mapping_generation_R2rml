import pandas as pd


class data:
    """

    """

    def __init__(self, **args):
        """
        :param args:
        """
        self.data: pd.DataFrame = pd.DataFrame()
        self.source_data = args["source"]
        self.subject = args["primary_subject"]


    def load_data(self):
        """

        :return:
        """
        if self.source_data == "database":
            self.data = pd.DataFrame
        elif self.source_data == "csv":
            pass
        else:
            raise Exception("Wrong")

    def get_columns(self):
        """

        :return:
        """
        columns = self.data.columns.values
        return columns

    def get_data_type_col(self, col):
        """

        :param col:
        :return:
        """
        dtype_c = self.data.dtypes[col]
        return dtype_c

    def get_number_samples(self):
        """

        :return:
        """
        n_sample = len(self.data.index)
        return n_sample


