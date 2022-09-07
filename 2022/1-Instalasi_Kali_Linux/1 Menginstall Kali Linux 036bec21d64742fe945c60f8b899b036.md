# 1. Menginstall Kali Linux

Hari ini kita akan menginstall zona eksperimen kita yaitu Kali Linux dalam virtual machine menggunakan VirtualBox

Sepertinya kita akan membutuhkan ~10GB free space di storage kalian jadi tolong dipersiapkan yaa…

Guide ini bukan guide yang definitif, melainkan guide secara general yang bisa dijadikan referensi bagi kalian. 

Silakan dan sangat direkomendasikan untuk bereksprimen agar kalian lebih kenal dengan Linux. Selalu baca dan dimengerti apa yang disampaikan di layar, karena jika tidak berhati-hati maka akan terjadi sesuatu yang tidak diinginkan.

# Download VirtualBox

Pertama, kita mendownload virtualbox yang dapat kalian akses di [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads) 

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled.png)

download sesuai dengan platform kalian yaa…

Jika sudah download, diinstall seperti biasa.

# Download Kali Linux

Kedua, kita mendownload Kali Linux di [https://www.kali.org/get-kali/](https://www.kali.org/get-kali/)

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%201.png)

Pilih **bare metal**, kemudian download yang installer

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%202.png)

# Instalasi Kali Linux

## Meng-setup virtual machine baru

Sesudah itu kita membuka VirtualBox nya, dan pilih **new/baru** pada menu diatas aplikasi

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%203.png)

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%204.png)

Set nama dan folder mesin sesuai dengan pilihan kalian, dan **tipe diganti ke Linux dengan versi Debian** (karena Kali basisnya adalah Debian)**.** Jika sudah, klik next/lanjut

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%205.png)

Untuk ukuran RAM, boleh 1GB. Kalau punya banyak RAM, 2GB juga boleh. Kemudian klik lanjut/next.

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%206.png)

Pilih **buat hard disk virtual sekarang**. 

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%207.png)

Pilih **VDI (VirtualBox Disk Image),** kemudian klik next/lanjut

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%208.png)

Pilih **alokasi secara dinamik**, kemudian klik next/lanjut

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%209.png)

Silakan ganti lokasi VDI jika diinginkan, dan set ukuran ke 8GB atau lebih.

Klik buat dan tunggu hingga selesai

## Meng-boot installer Kali

### Memasukkan .iso yang sudah diunduh

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2010.png)

Klik kanan pada VM yang tadi sudah dibuat dan pilih **pengaturan/settings.**

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2011.png)

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2012.png)

Pergi ke **Penyimpanan,** kemudian **pilih ikon CD, klik Pilih sebuah berkas disk/select a file.**

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2013.png)

Pilih file .iso Kali yang sudah kalian download, dan klik open.

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2014.png)

Klik **OK** untuk menyimpan settingan.

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2015.png)

Pilih **Mulai.**

### Instalasi Kali Linux

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2016.png)

Pilih Graphical Install dengan keyboard, tekan ENTER di keyboard.

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2017.png)

Pilih bahasa, dan klik continue/lanjut.

Untuk menu selajutnya (localization), pilih other → Asia → Indonesia. Kemudian di continue terus sampai keluar loading.

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2018.png)

Klik continue.

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2019.png)

Domain name dikosongkan tidak apa. Klik continue.

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2020.png)

Masukkan nama lengkap kalian. Klik continue

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2021.png)

Masukkan username kalian. Klik continue

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2022.png)

Buat password yang aman (jangan contoh gambar ini yaa :D ). Klik continue

Mungkin kalian masih menemukan beberapa settingan lain seperti time zone, silakan diisi sendiri.

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2023.png)

Pilih **Guided-use entire disk**. Klik continue

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2024.png)

Pilih virtual hard disk yang tadi sudah kita buat. Klik continue.

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2025.png)

Cek lagi pilihan disk, **jangan sampai salah karena data disana akan terhapus!**

Pilih **All files in one partition**, klik continue.

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2026.png)

Cek lagi, baca baca lagi, kalau sudah benar pilih **finish partitioning,** dan kllik continue

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2027.png)

Pilih **yes** jika sudah siap dan klik continue

Instalasi akan mulai berjalan, silakan tunggu sampai selesai

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2028.png)

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2029.png)

[OPSIONAL] 

Pilih desktop environment dan koleksi tools yang kalian inginkan, disini kami memakai default Kali

Klik continue dan tunggu instalasi hingga selesai

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2030.png)

Menginstall bootloader, tolong baca warning pada gambar. Jika sudah siap, pilih yes dan klik continue.

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2031.png)

Pilih virtual harddisk yang tadi kita sudah buat.

![Untitled](1%20Menginstall%20Kali%20Linux%20036bec21d64742fe945c60f8b899b036/Untitled%2032.png)

Finish the installation, reboot

============================================================

Jika kaliamberhasil menemui layar login, selamat! instalasi sudah berjalan dengan sukses…

Bagi yang belum bisa boleh banget tanya ya… see you next time :D