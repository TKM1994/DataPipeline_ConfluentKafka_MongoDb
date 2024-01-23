# importing necessary libraries
import pandas as pd
import json

# creating a generic class to use in different scenario
class Generic:
    
    # creating a constructer class and its attribrute dynamically from given dictionary
    def __init__(self, record: dict):
        for k, v in record.items():
            setattr(self, k, v)

    # class method to get schema structure from given file in csv format in sampledata directory
    @classmethod
    def get_schema_to_produce_consume_data(cls, file_path):
        columns = next(pd.read_csv(file_path, chunksize=10)).columns

        schema = dict()

        schema.update(
            {
            "$id": "http://example.com/myURI.schema.json",
            "$schema": "http://json-schema.org/draft-07/schema#",
            "additionalProperties": False,
            "description": "Sample schema to help you get started.",
            "properties": dict(),
            "title": "SampleRecord",
            "type": "object"
            })
        for column in columns:
            schema["properties"].update(
                {
                    f"{column}": {
                                    "description": f"generic {column} ",
                                    "type": "string"
                                }
                }
            )
        
    
        schema = json.dumps(schema)

        return schema

    # this is static method which will return object 
    # by dynamically creating attribute of generic class when dictionary given in input
    @staticmethod
    def dict_to_object(data: dict, ctx):
        return Generic(record=data)

    # this method will will return attribute of class instance in  dictionary format
    def to_dict(self):
        return self.__dict__

   
    # this class method reads a CSV file in chunks of 10 rows
    # creates instances of the Generic class for each row, and yields them one at a time
    @classmethod
    def get_object(cls, file_path):
        chunk_df = pd.read_csv(file_path, chunksize=10)
        n_row = 0
        for df in chunk_df:
            for data in df.values:
                #for each row in chunk_df, object is created by passing a dictionary
                # with key as column name and value as element of row in string
                generic = Generic(dict(zip(df.columns, list(map(str,data)))))
                n_row += 1
                yield generic


    # this class method  automates the setting of schema of topic in confluent kafka cloud by
    # creating a schema.json file from dataset  
    @classmethod
    def export_schema_to_create_confluent_schema(cls, file_path):
        columns = next(pd.read_csv(file_path, chunksize=10)).columns

        schema = dict()
        schema.update({
                    "type": "record",
                    "namespace": "com.mycorp.mynamespace",
                    "name": "sampleRecord",
                    "doc": "Sample schema to help you get started.",
                    })

        fields = []    
        for column in columns:
            fields.append(
                        {
                        "name": f"{column}",
                        "type": "string",
                        "doc": "The string type."  
                        }
            )

        schema.update({"fields":fields})


    
        json.dump(schema,open("schema.json","w"))
        schema = json.dumps(schema)

        return schema
        
        

    def __str__(self):
        return f"{self.__dict__}"

# convert an instance of the Generic class to a dictionary
def instance_to_dict(instance: Generic,ctx):
    return instance.to_dict()
