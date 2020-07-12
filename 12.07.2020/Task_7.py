import json
from statistics import mean

with open('file_7', 'r', encoding='UTF-8') as f:
    content = f.readlines()

revenue = {firm.split()[0]: int(firm.split()[-2]) - int(firm.split()[-1]) for firm in content}
average = {'average_profit': mean(i for i in list(revenue.values()) if i > 0)}

with open('file_7.json', 'w', encoding='UTF-8') as f:
    json.dump([revenue, average], f)
