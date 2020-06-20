import yaml

dict_yaml = {'100€': [1, 2, 3], '200€': 2, '300€': {1: 'a', 2: 'b'}}

with open('file.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(dict_yaml, f_n, default_flow_style=True, allow_unicode=True)
with open('file.yaml', encoding='utf-8') as f_n:
    f_n_content = yaml.load(f_n, Loader=yaml.FullLoader)

print(f_n_content)
