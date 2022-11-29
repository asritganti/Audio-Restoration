# function to calculate the median of given list of numbers
def median_fltr(data):
    #docstring
    '''
    Takes input array of real numbers, Sorts the array and returns the median of the data
    Args:
        Data(int): Array of Real Numbers

    Returns: 
        sort_data(num_mid):  A single real number 
    '''
    sort_data = sorted(data)

    len_sort = len(sort_data)

    num_mid = (len_sort - 1)//2

    return(sort_data[num_mid])
