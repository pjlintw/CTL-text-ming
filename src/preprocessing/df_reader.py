import pandas as pd
import os


class DataFrameLoader():
    def __init__(self, data_dir, output=None, select=None):

        input_file = os.path.join(data_dir)

        self.df = pd.read_excel(input_file)

        # if user provide --select
        # then filter
        if select:
            filtered_list = self.columns_name_filter(select, self.df)
            self.df = self.df.filter(items=filtered_list)


        if output:
            self.save(output, self.df)

    def select_parser(self, select):
        return [ i for i in select.split(' ') if i != '']

    def columns_name_filter(self, select, df):
        """Filter unwanted column


        """
        select_col_names_list = self.select_parser(select)
        df_columns_values = df.columns.values
        filtered_list = [column_name
                         for select_item in select_col_names_list for column_name in df_columns_values
                         if select_item in column_name]
        return filtered_list


    def make_dict(self, df):
        """Pandas DataFrame to dictionary

        Example: {'疾病事實': ['中病', '有病', '扶病'] }

        """
        result_dict = dict()
        for column_name in df:
            dict_key = df[column_name].name
            dict_values = df[column_name].dropna().values
            update_dict = {dict_key: dict_values}
            result_dict.update(update_dict)

        return result_dict

    def save(self, output, df):
        """Save to txt

        """
        df_dict = self.make_dict(df)
        with open(output, 'w', encoding='utf-8') as f:
            for dict_key in df_dict:
                for keyword in df_dict[dict_key]:
                    f.write(dict_key + ' ' + keyword.strip() + '\n')