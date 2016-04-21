import os, sys, re
__support__ = ['rails', 'python']
__exts__ = {'rails': 'rb',
            'python': 'py'}
__keywords__ = {'rails':
                    {'method': 'def',
                    'class': 'class',
                    'comment': '#'},
                'python':
                    {'method': 'def',
                    'class': 'class',
                    'comment': '#'}
                }

def error(type = 'Default', **kwargs):
    if type is 'USAGE_IMPR_FORM':
        print('USAGE: {} <language>'.format(__file__))
        print('Supported languages: {}'.format( ' '.join(__support__) ))
    if type is 'UNSUPPORTED_LANGUAGE':
        print('Supported languages: {}'.format( ' '.join(__support__) ))
    if type is 'TRAVERSAL_ERROR':
        print('An unknown error occured traversing the directory')
    sys.exit(0)

def start_gen(language):
    fdir = raw_input('Please input the root directory of the project: ')
    try:
        results = {}
        for root, _, files in os.walk(fdir):
            for file in files:
                if file.endswith(__exts__[language]):
                    fpath = '{}/{}'.format(root, file)
                    results[fpath] = gendoc(fpath, __keywords__[language])
        print(results)
    except Exception as e:
        print('{}: {}'.format(type(e).__name__, e))
        error('TRAVERSAL_ERROR')

# Generates the documentation for methods and classes
def gendoc(path, keys):
    comments = {}
    f_lam = lambda el: el.strip().startswith(keys['comment'])
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            if line.strip().startswith(keys['method']+" "):
                print(line)
                method_name = re.match("{} (\w+)".format(keys['method']), line.strip()).groups()[0]
                comments[method_name] = list(filter_until(f_lam, lines[:lines.index(line)]))
    return comments

def filter_until(condition, objs = []):
    for item in reversed(objs):
        if condition(item):
            yield item.strip()[1:].strip()
        else:
            break

if __name__ == '__main__':
    # DOCGEN
    # Start-up Logic
    if len(sys.argv) != 2:
        error('USAGE_IMPR_FORM')
    language = sys.argv[1]

    if language not in __support__:
        error('UNSUPPORTED_LANGUAGE')

    start_gen(sys.argv[1])
