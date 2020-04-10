SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# Instead of the word `function`, in Python, you use `def`
def approximate_size(size, a_kilobyte_is_1024_bytes=True):

    '''Convert a file size to human-readable form.

    (this is a doc string)

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000
    Returns: string
    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000 #this is like a ternary

    # if a_kilobyte_is_1024_bytes:
    #     multiple = 1024
    # else:
    #     multiple = 1000

    for suffix in SUFFIXES[multiple]:
        size /= multiple    # size = size/multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)  
                                    # .format lets you put a variable in your string return value
                        # .1f means 1 number after decimal; f = floating point
                        # you can put text between the curly brackets in your return string
    raise ValueError('number too large')

if __name__ == '__main__':    
    # ^checks to see if this is the file specified in the terminal to run
    print(approximate_size(16384, False))
    print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=False))
    print(approximate_size(16384))
                            # ^you must pass in as many arguments you have unless you specified a default value (which we did)