def noraml_numbering(input_list):
    return sorted(range(len(input_list)), key=input_list.__getitem__)

def rankdata(a):
    n = len(a)
    n_vec=noraml_numbering(a)
    r_vec=[a[rank] for rank in n_vec]
    sum_ranks = 0
    duplicate_count = 0
    zero_array = [0]*n
    for i in range(n):
        sum_ranks += i
        duplicate_count += 1
        if i==n-1 or r_vec[i] != r_vec[i+1]:
            averagerank = sum_ranks / float(duplicate_count) + 1
            for j in range(i-duplicate_count+1,i+1):
                zero_array[n_vec[j]] = averagerank
            sum_ranks = 0
            duplicate_count = 0
    return zero_array
# a=[['XAX100', -1.0, 1.0], ['XAX1000', 1.0, 1.0], ['XAX1010', 1.0, 1.0], ['XAX1004', -2.0, 2.0], ['XAX1011', -2.0, 2.0], ['XAX1020', 3.0, 3.0], ['XAX1006', 4.0, 4.0], ['XAX1009', -4.0, 4.0], ['XAX1019', -4.0, 4.0], ['XAX1021', 4.0, 4.0], ['XAX1017', 6.0, 6.0], ['XAX1018', 6.0, 6.0], ['XAX1003', -7.0, 7.0], ['XAX1008', 7.0, 7.0], ['XAX101', 7.0, 7.0], ['XAX1013', 7.0, 7.0], ['XAX102', 7.0, 7.0], ['XAX1', -9.0, 9.0], ['XAX1022', 9.0, 9.0], ['XAX1005', 13.0, 13.0], ['XAX1007', 16.0, 16.0], ['XAX1002', 17.0, 17.0], ['XAX1015', -17.0, 17.0], ['XAX1001', 20.0, 20.0], ['XAX1012', -20.0, 20.0], ['XAX1014', 20.0, 20.0], ['XAX1023', 24.0, 24.0], ['XAX10', 31.0, 31.0]]
# ranking_data=[]
# for i in a:
#     ranking_data.append(i[2])
# ranks=rankdata(ranking_data)
#
# data_ranks=list(zip(a,ranks))
# print(data_ranks)
# #[(['XAX1016', 0.0, 0.0], 1.0), (['XAX100', -1.0, 1.0], 3.0), (['XAX1000', 1.0, 1.0], 3.0), (['XAX1010', 1.0, 1.0], 3.0), (['XAX1004', -2.0, 2.0], 5.5), (['XAX1011', -2.0, 2.0], 5.5), (['XAX1020', 3.0, 3.0], 7.0), (['XAX1006', 4.0, 4.0], 9.5), (['XAX1009', -4.0, 4.0], 9.5), (['XAX1019', -4.0, 4.0], 9.5), (['XAX1021', 4.0, 4.0], 9.5), (['XAX1017', 6.0, 6.0], 12.5), (['XAX1018', 6.0, 6.0], 12.5), (['XAX1003', -7.0, 7.0], 16.0), (['XAX1008', 7.0, 7.0], 16.0), (['XAX101', 7.0, 7.0], 16.0), (['XAX1013', 7.0, 7.0], 16.0), (['XAX102', 7.0, 7.0], 16.0), (['XAX1', -9.0, 9.0], 19.5), (['XAX1022', 9.0, 9.0], 19.5), (['XAX1005', 13.0, 13.0], 21.0), (['XAX1007', 16.0, 16.0], 22.0), (['XAX1002', 17.0, 17.0], 23.5), (['XAX1015', -17.0, 17.0], 23.5), (['XAX1001', 20.0, 20.0], 26.0), (['XAX1012', -20.0, 20.0], 26.0), (['XAX1014', 20.0, 20.0], 26.0), (['XAX1023', 24.0, 24.0], 28.0), (['XAX10', 31.0, 31.0], 29.0)]
