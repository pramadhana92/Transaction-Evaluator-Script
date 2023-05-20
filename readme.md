# Transcation Evaluator Script

Script ini berfungsi untuk mengolah file csv berupa data transaksi dan menghasilkan evaluasi sebagai berikut:

1. Nilai total penjualan
2. Baris penjualan dengan nilai penjualan tertinggi
3. Nilai jumlah penjualan
4. Daftar produk yang terjual

Adapun kolom yang bersifat *required* pada file csv adalah:
1. produk
2. jumlah

Agar script ini bisa lebih mudah digunakan maka terdapat GUI untuk memudahkan pemilihan file csv dan membaca hasil evaluasi dari script.

## Contoh penggunaan
Script dapat digunakan dengan syntax mudah seperti berikut:
```
python transaction_evaluator.py
```

Sample transaksi juga telah disediakan yaitu *example_transaction.csv*, yang dapat dipilih ketika menjalankan script.

## Deployment

Script ini dibuat menggunakan library bawaan python yaitu csv, tkinter dan os. Sehingga pengguna tidak perlu repot menginstall library tambahan.