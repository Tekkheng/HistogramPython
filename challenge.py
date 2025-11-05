import matplotlib.pyplot as plt
import numpy as np

def create_histogram(data, title='Histogram'):
    print(f"Mulai proses untuk {len(data)} data...")

    jumlah_bins = int(np.sqrt(len(data))) 
    plt.figure(figsize=(10, 6)) 
    counts, bins, patches = plt.hist(data, bins=jumlah_bins, edgecolor='black', alpha=0.75)

    plt.title(title, fontsize=16)
    plt.xlabel('Rentang Nilai', fontsize=12)
    plt.ylabel('Frekuensi (Jumlah)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    rata_rata = np.mean(data)
    plt.axvline(rata_rata, color='red', linestyle='dashed', linewidth=2)
    plt.legend([f'Rata-rata: {rata_rata:.2f}'])
    
    plt.savefig('hasil_histogram.png')
    print(f"Grafik telah disimpan sebagai 'hasil_histogram.png'")
    print("Plot selesai. Menampilkan...")
    plt.show()

if __name__ == "__main__":
    data_nilai = [
        82, 75, 68, 91, 85, 79, 79, 88, 95, 72, 65, 88, 90, 77, 85, 81, 93, 74, 86, 79,
        66, 92, 58, 61, 75, 80, 71, 71, 89, 55, 62, 82, 75, 68, 91, 85, 79, 79, 88, 95,
        72, 65, 88, 90, 77, 85, 81, 93, 74, 86, 79, 66, 92, 58, 61, 75, 80, 71, 71, 89,
        55, 62, 84, 78, 67, 90, 83, 76, 88, 92, 70, 64, 87, 91, 75, 84, 80, 89, 73, 85,
        77, 68, 94, 59, 63, 79, 81, 74, 72, 90, 56, 60, 83, 78, 66, 92, 85, 80, 87, 91
    ]
    create_histogram(data_nilai, title='Histogram Untuk Nilai Ujian Karyawan')

    print("Program selesai.")



# perintah untuk package yang diinstall
# pip install matplotlib