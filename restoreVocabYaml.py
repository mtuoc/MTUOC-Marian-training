import sys
import codecs
import yaml

def read_yaml(file_path,maxlength):
    data = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            try:
                line_data = yaml.safe_load(line)
                if line_data is not None and len(str(list(line_data.keys())[0]))<=maxlength:
                    data.update(line_data)
            except yaml.YAMLError:
                pass  # Ignore lines with errors
    return data

def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        try:
            yaml.dump(data, file, default_flow_style=False)
            print("Data successfully written to", file_path)
        except Exception as e:
            print("Error writing YAML file:", e)

fentrada=sys.argv[1]
fsortida=sys.argv[2]
maxlength=int(sys.argv[3])

data=read_yaml(fentrada,maxlength)

write_yaml(data,fsortida)


