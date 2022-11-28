#function to calculate the median of given list of numbers
def median_fltr(data):
    sort_data = sorted(data)
    len_sort = len(sort_data)

    num_mid = (len_sort - 1)//2

    return(sort_data[num_mid])