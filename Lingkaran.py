import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar lingkaran dengan radius tertentu
def draw_circle(a, b, r):
    # Membuat sudut theta dari 0 hingga 2π untuk melacak seluruh lingkaran
    theta = np.linspace(0, 2 * np.pi, 100)
    
    # Menghitung koordinat x dan y pada keliling lingkaran
    x = a + r * np.cos(theta)  # Koordinat x berdasarkan pusat a dan radius r
    y = b + r * np.sin(theta)  # Koordinat y berdasarkan pusat b dan radius r

    # Menampilkan lingkaran dengan koordinat x dan y yang dihitung
    plt.plot(x, y, label=f"Circle with radius {r}")
    plt.grid(True)  # Menampilkan grid untuk membantu visualisasi
    plt.axis('equal')  # Memastikan sumbu x dan y berskala sama

    # Menambahkan garis radius dari pusat lingkaran ke salah satu titik pada keliling
    x_radius = [a, a + r]  # Membuat garis horizontal dari pusat ke keliling
    y_radius = [b, b]  # Menyimpan posisi y untuk garis radius
    plt.plot(x_radius, y_radius, 'g--')  # Menampilkan garis radius dengan warna hijau putus-putus

    # Menambahkan anotasi pada radius lingkaran
    plt.annotate(f"Radius = {r}", xy=(a + r / 2, b), xytext=(a + r / 2, b + 0.1),
                 ha='center', color='green')

    plt.legend()  # Menampilkan label lingkaran
    plt.show()  # Memunculkan grafik lingkaran

# Menentukan titik pusat lingkaran (a, b) dan panjang radius r
draw_circle(5, 10, 6)
