import time

# Daftar Kasus A dan B
a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]   # Kasus A (Descending)
b = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]   # Kasus B (Partially Sorted)

# 1. Implementasi Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 2. Implementasi Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Memilih pivot sebagai elemen tengah
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Fungsi untuk mengukur waktu eksekusi
def measure_time_sorting(sort_function, data):
    start_time = time.time()
    result = sort_function(data.copy())
    end_time = time.time()
    return end_time - start_time, result

# Testing dan Pengukuran Waktu

# Bubble Sort - Kasus A
bubble_time_a, bubble_sorted_a = measure_time_sorting(bubble_sort, a)
# Bubble Sort - Kasus B
bubble_time_b, bubble_sorted_b = measure_time_sorting(bubble_sort, b)

# Quick Sort - Kasus A
quick_time_a, quick_sorted_a = measure_time_sorting(quick_sort, a)
# Quick Sort - Kasus B
quick_time_b, quick_sorted_b = measure_time_sorting(quick_sort, b)

# Hasil Output
print("=== Bubble Sort ===")
print(f"Kasus A (Descending):\nWaktu = {bubble_time_a:.6f} detik, Hasil = {bubble_sorted_a}")
print(f"Kasus B (Partially Sorted):\nWaktu = {bubble_time_b:.6f} detik, Hasil = {bubble_sorted_b}")

print("\n=== Quick Sort ===")
print(f"Kasus A (Descending):\nWaktu = {quick_time_a:.6f} detik, Hasil = {quick_sorted_a}")
print(f"Kasus B (Partially Sorted):\nWaktu = {quick_time_b:.6f} detik, Hasil = {quick_sorted_b}")
# Kasus A
# 1. Quick Sort lebih efisien dibandingkan Bubble Sort pada data terurut secara descending, terutama jika pivot dipilih dengan strategi yang baik.
# 2. Bubble Sort tidak efisien karena harus melakukan pertukaran elemen berulang kali hingga mencapai urutan yang benar.
# Kasus B
# 1. Quick Sort jauh lebih efisien daripada Bubble Sort pada list yang hampir terurut, karena menggunakan pendekatan divide-and-conquer yang lebih optimal.
# 2. Bubble Sort tetap melakukan banyak perbandingan dan pertukaran meskipun sebagian besar data sudah terurut, sehingga tidak seefisien Quick Sort.
# Kesimpulan mneyeluruh
# Untuk Kasus A (Descending Order), Quick Sort lebih baik daripada Bubble Sort, terutama jika pemilihan pivot dilakukan dengan benar.
# Untuk Kasus B (Partially Sorted), Quick Sort sangat unggul dibandingkan Bubble Sort, karena menggunakan pendekatan divide-and-conquer yang optimal bahkan pada data yang sebagian terurut.