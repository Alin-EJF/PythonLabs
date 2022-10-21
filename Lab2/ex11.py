#in alphabetical order ?
def sort_by_3rd_char(tuples):
    return sorted(tuples, key=lambda x: x[1][2]) #first lambda appearance btw

print(sort_by_3rd_char([('abc', 'bcd'), ('abc', 'zza'), ('abc', 'aac'), ('abc', 'yyy1')]))