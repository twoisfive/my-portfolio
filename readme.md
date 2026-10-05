Pertanyaan Reflektif Tugas 5:

1. Debouncing merupakan suatu teknik dimana berbagai operasi programming yang terjadi dalam rentang waktu sangat dekat digabungkan menjadi satu batch agar operasinya hanya dilaksanakan beberapa kali. Hal ini digunakan dalam searching karena seseorang sudah mengetahui query yg ia ingin tulis sehingga operasi berulang tidak melambatkan proses tersebut
2. Await digunakan agar javascript dapat berjalan secara asinkronus. Await menyimpan suatu promise dimana kode lain dapat berjalan saat proses await berjalan di background lalu ketika operasi tersebut, promise akan callback terhadap fungsi dan melanjutkan kode pada await. Jika tidak menggunakan await, kode tersebut tidak akan dapat mengolah response yang dikirim balik oleh server.
3. XSS atau Cross-site scripting merupakan suatu teknik untuk melalui policy yang mengharuskan suatu request dilaksanakan dari origin yang sama sehingga mengeksekusi kode dari pihak yang melakukan XSS seperti jika kodenya berasal dari source code sendiri. Django lebih baik dalam menangani XSS karena kode django melaksanakan auto-escaping yang mengubah berbagai tag menjadi kode aman untuk diproses dibandingkan AJAX yang lebih rentan terhadap XSS karena tidak memiliki proteksi otomatis apapun.

Penggunaan AI TI 5:
Dalam pengerjaan tugas ini, ChatGPT dan Deepseek digunakan untuk memahami tugas, konsep-konsep dalam pertanyaan reflektif, serta membantu menulis beberapa bagian kode

Penggunaan AI TI 4:
Dalam pengerjaan tugas ini, ChatGPT digunakan untuk memahami tugas, konsep autorisasi dan autentikasi, serta membantu menulis beberapa bagian kode

Pertanyaan Reflektif Tugas 3:

1. Kita menggunakan ModelForm pada proyek ini karena ModelForm mengkaitkan suatu form terhadap suatu model sehingga dapat juga memvalidasi jika data sesuai dengan keperluan model. {% csrf\_token %} diperlukan untuk menjaga agar situs lain tidak bisa menggunakan form untuk melakukan POST request tanpa persetujuan user.
2. JSON lebih disukai dalam web development modern karena banyak API yang dipakai oleh browser dibuat sekitar penggunaan JSON karena kemudahannya untuk di-parse dibandingkan XML
3. Dalam fungsi view yang mengambil data dan mengembalikkan nya sebagai JSON perlu diserialisasi karena model disimpan sebagai python object sehingga perlu dikonversi agar compatible dengan JSON ketika mengembalikkan Http Response nya

Penggunaan AI Tugas 3:
Saya menggunakan AI deepseek \& Claude untuk membantu dalam pembelajaran pemahaman konsep dan membantu dalam penulisan kode seperti pada penulisan dasar template dan me-refactor CSS.

Deskripsi proyek:
Membuat page baru yang menunjukkan proyek-proyek telah dikerjakan dengan membuat model Projects, template projects.html, dan menambahkan routing di URL serta fungsi render nya di views.py.

Model projects berisi detail-detail proyek seperti role saat pembuatan, tech stack yang digunakan, serta link jika ada

Penggunaan AI:
Dalam pengerjaan tugas saya menggunakan AI ChatGPT dan Claude untuk memahami model MVT, membantu dalam penulisan kode, serta pengecekan jika kode dapat dilengkapkan atau dirapihkan
