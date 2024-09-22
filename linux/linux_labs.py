import json

def handle_table_task(task):
    for row in task['table']:
        new_row = []
        for cell in row:
            if cell.strip() != 'fill':
                print(cell)
            else:
                line = input("")
                cell = line
        print('  '.join(row))
        

with open('linux_data.json') as f:
    data = json.load(f)
    labs = data['labs']
    table_task = labs[2]['tasks'][0]

    handle_table_task(table_task)
