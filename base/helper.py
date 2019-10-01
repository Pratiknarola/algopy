def zero_pad(value, rtype = str):

    if type(value) is not str:
        raise TypeError("Only supports string (str), not {}".format(str(type(value))))

    if len(value) % 4:
        return rtype(('0'*(4 - (len(value) % 4)) + value))
    else:
        return rtype(value)


def to_string(num_list, sep = ' '):

    if type(num_list) is not list:
        raise TypeError("Only supports list, not {}".format(str(type(num_list))))

    return sep.join(num_list)






