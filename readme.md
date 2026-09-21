Pertanyaan Reflektif Tugas 3:

1. Kita menggunakan ModelForm pada proyek ini karena ModelForm mengkaitkan suatu form terhadap suatu model sehingga dapat juga memvalidasi jika data sesuai dengan keperluan model. {% csrf_token %} diperlukan untuk menjaga agar situs lain tidak bisa menggunakan form untuk melakukan POST request tanpa persetujuan user.
2. JSON lebih disukai dalam web development modern karena banyak API yang dipakai oleh browser dibuat sekitar penggunaan JSON karena kemudahannya untuk di-parse dibandingkan XML
3. Dalam fungsi view yang mengambil data dan mengembalikkan nya sebagai JSON perlu diserialisasi karena model disimpan sebagai python object sehingga perlu dikonversi agar compatible dengan JSON ketika mengembalikkan Http Response nya

Penggunaan AI Tugas 3:
Saya menggunakan AI deepseek & Claude untuk membantu dalam pembelajaran pemahaman konsep dan membantu dalam penulisan kode seperti pada penulisan dasar template dan me-refactor CSS.

Deskripsi proyek:
Membuat page baru yang menunjukkan proyek-proyek telah dikerjakan dengan membuat model Projects, template projects.html, dan menambahkan routing di URL serta fungsi render nya di views.py.

Model projects berisi detail-detail proyek seperti role saat pembuatan, tech stack yang digunakan, serta link jika ada

Penggunaan AI:
Dalam pengerjaan tugas saya menggunakan AI ChatGPT dan Claude untuk memahami model MVT, membantu dalam penulisan kode, serta pengecekan jika kode dapat dilengkapkan atau dirapihkan
