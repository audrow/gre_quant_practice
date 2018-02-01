def isInt(val, greaterThan=None, lessThan=None):

    try:
        val = float(val)
    except ValueError:
        raise ValueError

    if val == int(val):

        val = int(val)

        if ( (greaterThan is None or val > float(greaterThan)) and
             (lessThan    is None or val < float(lessThan)) ):
            return True

    else:
        return False

def isPositivInt(val, lessThan=None):
    return isInt(val, greaterThan=0, lessThan=lessThan)

