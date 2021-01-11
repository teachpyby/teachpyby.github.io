import sys, io, os, argparse, csv

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
        score_list = [int(x) if x else 0 for x in row[1:]]
        score[name] = score_list

  return (tasks, score)

def gen_table(tasks, rating):
  out = io.StringIO()

  print("<thead>", file = out)
  print("  <tr>", file = out)
  print("  <th></th>", file = out)
  block = None
  count = 0
  for t in tasks:
    b, _ = t.split(".")
    if block != b:
      if block != None:
        print(f'  <th colspan="{count}">{block}</th>', file = out)
      block = b
      count = 1
    else:
      count += 1
  print(f'  <th colspan="{count}">{block}</th>', file = out)
  print("  </tr>", file = out)

  print("  <tr>", file = out)
  print("  <td></td>", file = out)
  for t in tasks:
    block, id = t.split('.')
    print("  <td>", id, "</td>", file = out)
  print("  <td></td>", file = out) # total
  print("</tr>", file = out)
  print("</thead>", file = out)


  print("<tbody>", file = out)
  for k, v in sorted(rating.items(), key = lambda item: -sum(item[1])):
    print("<tr>", file=out)
    print("  <th>", k, "</th>", file = out)

    score = v + [0] * (len(tasks) - len(v))
    for s in score:
      print("  <td>", s, "</td>", file = out)
    print(  "<td><b>", sum(v), "</b></td>", file = out)
    print("</tr>", file=out)
  print("</tbody>", file = out)

  return out.getvalue()

def gen_rating(template, tasks, score):
  return template.replace('{{table}}', gen_table(tasks, score))

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