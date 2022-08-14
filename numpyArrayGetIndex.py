import numpy as np
# import time

arr = np.array([10, 15, 12, 14, 13, 40, 45, 15, 16, 17, 19])
target_gt_value = 40


# arr = np.random.randint(60, size=5000000)
# print(arr)
# start_time = time.perf_counter() #starting timer after generated array.

try:
    first_index_above_target_value = np.where(arr > target_gt_value)[0][0]
    indexes_less_target_value = np.where(arr < target_gt_value)[0]
    found_index = indexes_less_target_value[np.where(indexes_less_target_value >
                                                     first_index_above_target_value)[0][0]]

    # print(time.perf_counter() - start_time, "seconds")
    print(f"Found @ index: {found_index} with value: {arr[found_index]}")
except:
    print("Ohhh..")
