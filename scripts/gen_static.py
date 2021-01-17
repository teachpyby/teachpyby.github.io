import chevron, os, argparse

def gen_lessons(directory, template):
    """
    Генерирует в папке html страницы для презентаций. Для того чтобы знать что
    генерировать, мы используем файл toc.txt. Который говорит какая тема у какой
    презентации. Это нужно для того чтобы менять <title>.

    directory - папка, для которой генерируем страницы
    template  - шаблон для html страницы
    """
    toc = os.path.join(directory, 'toc.txt')
    generated = []
    print(f':: {directory}  ', end='', flush=True)

    if not os.path.exists(toc):
        print('')
        return generated

    for line in open(toc, 'r'):
        slides, title = line.rstrip().split(' ', 1)
        lesson = chevron.render(template, {'title': title, 'slides': slides})
        dst_file = os.path.basename(slides).replace('.md', '.html')
        dst_path = os.path.join(directory, dst_file)

        with open(dst_path, 'w') as out:
            out.write(lesson)
        print('.', end='', flush=True)
        generated.append((dst_path, title))

    print('')
    return generated

parser = argparse.ArgumentParser()
parser.add_argument('--lesson_template', type=str,
                    help='path to lesson template')
parser.add_argument('--dir', type=str,  action='append',
                    help='path to target directory')


args = parser.parse_args()
template = None

with open(args.lesson_template, 'r') as reader:
    template = reader.read()

print('Gen dirs')
for d in args.dir:
    gen_lessons(d, template)