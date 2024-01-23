# importing necessary library
import os


# authentication security related variable
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"

# confluent cloud kafka api related variable
API_KEY = os.getenv('API_KEY',None)
API_SECRET_KEY = os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER',None)


# schema related variable
ENDPOINT_SCHEMA_URL  = os.getenv('ENDPOINT_SCHEMA_URL',None)
SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET',None)

# kafka cluster configruation
def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    
    return sasl_conf


# schema configruation
def schema_config():

    schema_config = {'url':ENDPOINT_SCHEMA_URL,
    
                    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"
                    }

    return schema_config



if __name__ == '__main__':
    print(sasl_conf())
    print(schema_config())

