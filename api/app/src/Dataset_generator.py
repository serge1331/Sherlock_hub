from .Data_collectors import __all__ 
import pandas as pd
import importlib



_collectors = __all__

class DatasetGenerator:
    def __init__(self, keyword, langue='fr'):
        self.keyword = keyword
        self.langue = langue
        self.df = pd.DataFrame()
        self.collectors = _collectors

    def generator(self):
        for i in self.collectors:
            data_source_plugin = importlib.import_module(i , 'src.Data_collectors')
            collected_data =  data_source_plugin.collect(self.keyword)
            self.df = pd.concat([self.df , pd.DataFrame(collected_data)])
        return self.df
    