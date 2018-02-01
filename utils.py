"""Utilities for the GRE Quantitative Practice Project"""

def isInt(val, greaterThan=None, lessThan=None):
    """
    Returns a boolean variable for if val is a valid integer. This test
    is subject to upper and lower bounds that are optional. The function
    throws a ``ValueError`` if it cannot parse numbers from any of the
    arguements.

    :param val:
    :param greaterThan:
    :param lessThan:
    :return: boolean
    """

    try:
        val = float(val)
        greaterThan = float(greaterThan)
        lessThan = float(lessThan)
    except ValueError:
        raise ValueError

    if val == int(val):

        val = int(val)

        if ( (greaterThan is None or val > greaterThan) and
             (lessThan    is None or val < lessThan) ):
            return True

    else:
        return False

def isPositivInt(val, lessThan=None):
    return isInt(val, greaterThan=0, lessThan=lessThan)

