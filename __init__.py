
def prompt_options_str(options):
    return '\n'.join([ f"{i}: {x} :{i}" for i,x in enumerate(options)]) + '\n'

def prompt_options(options):
    i = int(input(prompt_options_str(options)))
    print(f'Entered: {options[i]}')
    return i, options[i]


def limited_lines(lines, start, end, step, more_info = False):
    if len(lines) == 0:
        return '(EMPTY)'
    sl = lines[start: end: step]
    output = '\n'.join(sl) + '\n'

    if len(sl) < len(lines):
        output += f'--More--'
        if more_info:
            output += f'({len(sl):d}/{len(lines):d})'
    else:
        output += '(END)'
    return output


def npvector2str(x, precision=3, specifier = 'g', sep = '\t', width = ''):
    return sep.join([f'{x[i]:{width}.{precision}{specifier}}' for i in range(x.shape[0])])

def npmatrix2str(x, precision=3, specifier = 'g', sep = '\t', width = ''):
    return '\n'.join([ npvector2str(x[i], precision=precision, specifier = specifier, sep = sep, width = width) for i in range(x.shape[0]) ])
