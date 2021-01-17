import chevron, argparse, csv

def read_rating(file):
  tasks = None
  score = {}
  with open(file, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      if not tasks:
        tasks = row[1:]
      else:
        name = row[0]
        score_list = row[1:]
        score[name] = score_list

  return (tasks, score)

def gen_data(tasks, rating):
  data = {
    'block': [],
    'task': [],
    'student': []
  }

  block = None
  count = 0
  for t in tasks:
    b, _ = t.split(".")
    if block != b:
      if block != None:
        data['block'].append({'task_count': count, 'name': block })
      block = b
      count = 1
    else:
      count += 1

  data['block'].append({'task_count': count, 'name': block })

  data['task'] = [{'id': t.split('.')[-1]} for t in tasks]

  for k, v in sorted(rating.items(), key = lambda item: -sum(map(string_to_int, item[1]))):
    student = {'name': k, 'total': sum(map(string_to_int, v)) }
    score = []
    for s in v:
      style = 'text-muted' if s == 'x' else ''
      bold = s in ['6', '7', '8']
      score.append({'value': s, 'style': style, 'bold': bold})

    student['score'] = score
    data['student'].append(student)

  return data

def string_to_int(v):
  return int(v) if v.isnumeric() else 0

def gen_rating(template, tasks, score):
  return chevron.render(template, gen_data(tasks, score))

parser = argparse.ArgumentParser()
parser.add_argument('--rating', type=str,
                    help='path rating CSV')
parser.add_argument('--template', type=str,
                    help='path to template file')
parser.add_argument('--output', type=str,
                    help='path to target file')


args = parser.parse_args()
template = None

with open(args.template, 'r') as reader:
    template = reader.read()

tasks, score = read_rating(args.rating)

with open(args.output, 'w') as writer:
  writer.write(gen_rating(template, tasks, score))