from collections import defaultdict
import re
import sys
import os

try:
    file = sys.argv[1]
except:
    file = [file for file in os.listdir('input') if file.endswith('.txt')][0]
    file = './input/' + file

outfile = './output/top_cost_drug.txt'
scrib = defaultdict(set) # dict tracking unique prescribers
costsum = defaultdict(float) # dict tracking total drug cost
bad = set()

# col positions of each column
last = 1 # col position of prescriber_last_name
first = 2 # col position of prescriber_first_name
drug = 3
cost = 4


# update the dicts tracking unique prescribers and total drug cost
def update_dicts(line):
    # input must be a list of strs of length 5
    scrib[line[drug]].add((line[first], line[last]))
    costsum[line[drug]] += float(line[cost])

with open(file, 'rt') as f:
    for i, line in enumerate(f):
        line = line.strip().split(',')
        # check that there are 5 elements
        if len(line) == 5:
            # skip header
            if i == 0: 
                continue
            update_dicts(line)
        else: 
            # handle splitting rows with commas inside of cells
            line = re.split(r'"(.*?)"|,', ','.join(line))
            line = [elem for elem in line if elem not in [None,'']]
            if len(line) == 5:
                update_dicts(line)
                if ',' in line[drug]:
                    # track drug names with commas for re quoting
                    bad.add(line[drug])
            else:
                sys.stderr.write(f'Failed to parse and proccess row {i} of file\n')

# unique prescriber count
scrib = {key: len(set) for key, set in scrib.items()}

## Write aggregations to csv

# write a line with drug quoted or not
def write_line(drug, no_quote = True):
    try:
        if no_quote:
            f.write(f'{drug},{scrib[drug]},{costsum[drug]}\n') 
        else:
            f.write(f'"{drug}",{scrib[drug]},{costsum[drug]}\n') 
    except:
        sys.stderr.write(f'Failed to write output row for {drug}\n')  


with open(outfile, 'wt') as f:
    # write header
    f.write('drug_name,num_prescriber,total_cost\n')
    for drug in scrib.keys():
        if drug not in bad:
            write_line(drug)
        else:
            write_line(drug, no_quote = False)       

print('Script Ran Completely')