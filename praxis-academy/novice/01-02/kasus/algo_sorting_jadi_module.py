def simple_sort(nums):
    return sorted(nums)

def simple_sort_reverse(nums):
    return sorted(nums, reverse=True)

def bubblesort(array): 
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array)-1):
            # mencari item yg tidak urut pertama kali
            if array[i] > array[i+1]:
                #semua item dalam array dibandingkan dengan item yang berdekatan
                array[i], array[i+1] = array[i+1], array[i]
                #lakukan swap lagi
                swapped = True

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i-1
        next_element = array[i]
        # setiap item array dibandingkan dengan nilai terdekat setelahnya
        # mencari yg tidak urut, yg urut dibiarkan, yg tidak urut di swap posisi
        while(array[j] > next_element) and (j >= 0):
            array[j+1] = array[j]
            j = j-1
        array[j+1] = next_element

def selection_sort(sample):
    # i menunjukkan berapa kali nilai disusun
    for i in range(len(sample)):
        # sumsikan bahwa angka pertama yg tidak urut juga yg terkecil
        low_val_index = i
        # buat loop untuk iterasi elemen yg tidak urut
        for j in range(i+1, len(sample)):
            if sample[j] < sample[low_val_index]:
                low_val_index = j
        # menukar nilai terendah elemen tak urut dengan elemen pertama nilai tak urut
        sample[i], sample[low_val_index] = sample[low_val_index], sample[i]

def counting_sort(arr):
    size = len(arr) # size dijadikan sebagai panjangnya array
    output = [0] * size # siapkan penampung array dengan nilai awal nol

    # inisialisasi hitung array
    count = [0] * (size+1) # wadah array

    #masukkan setiap element ke hitung array 
    for i in range(0, size):
        count[arr[i]] += 1

    #masukkan nilai kumulatif        
    for i in range(1,len(count)):
        count[i] += count[i-1]

    #temukan index dari setiap elemen dari array asli  dalam count array
    # letakkan elemen ke output array        
    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    #copy nilai yang disimpan ke array asli        
    for i in range(0, size):
        arr[i] = output[i]

__version__ = '0.1'