import yaml


print(yaml.load(open("demo.yaml"), Loader=yaml.FullLoader))
