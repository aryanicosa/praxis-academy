'''
from algo_sorting_jadi_module import selection_sort
from algo_sorting_jadi_module import bubblesort
from algo_sorting_jadi_module import counting_sort
from algo_sorting_jadi_module import insertion_sort
from algo_sorting_jadi_module import simple_sort
from algo_sorting_jadi_module import simple_sort_reverse
'''
'''
import algo_sorting_jadi_module

print(dir(algo_sorting_jadi_module))
'''
import algo_sorting_jadi_module as algo

array = [4,5,6,7,8,3,2,5,6,7]
algo.selection_sort(array)
print(array)

nums = [2,4,6,7,1,3,4,5]
print(algo.simple_sort_reverse(nums))