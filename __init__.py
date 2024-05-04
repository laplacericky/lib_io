import numpy as np

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


def npvector2str(x, precision=3, specifier = 'g', sep = '\t', width = '', summarize_zero = True):
    if np.any(x) or not summarize_zero:
        return sep.join([f'{x[i]:{width}.{precision}{specifier}}' for i in range(x.shape[0])])
    else:
        return f'0 ({x.shape[0]:d},)'

def npmatrix2str(x, precision=3, specifier = 'g', sep = '\t', width = '', summarize_zero = True):
    if np.any(x) or not summarize_zero:
        return '\n'.join([ npvector2str(x[i], precision=precision, specifier = specifier, sep = sep, width = width, summarize_zero = False) for i in range(x.shape[0]) ])
    else:
        return f'0 ({x.shape[0]:d},{x.shape[1]:d})'

def np3dtensor2str(x, precision=3, specifier = 'g', sep = '\t', width = '', br = '------', summarize_zero = True):
    if np.any(x) or not summarize_zero:
        return f'\n{br}\n'.join([ npmatrix2str(x[i], precision=precision, specifier = specifier, sep = sep, width = width, summarize_zero = summarize_zero) for i in range(x.shape[0])])
    else:
        return f'0 ({x.shape[0]:d},{x.shape[1]:d},{x.shape[2]:d})'
