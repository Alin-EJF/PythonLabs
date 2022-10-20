def appear_x_times(x, lists):
     appear_x_times_list = []
     appear_in_lists = []

     for list in lists:
         for item in list:
                 appear_in_lists.append(item)

     for item in appear_in_lists:
         if item not in appear_x_times_list and appear_in_lists.count(item) == x:
             appear_x_times_list.append(item)

     return appear_x_times_list

print(appear_x_times(2, [[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]]))