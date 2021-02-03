<h1>Skema belajar membuat kolaborasi project dalam sebuah repositori</h1>

1. Membuat Repositori baru dan memasukan file yang akan dikelola bersama

2. Menambahkan collaborator
    *   Buka settings pada repository
    *   Pilih menu manage access
    *   klik invite collaborator
    *   ketik nama jogjaembedded dan add

3. Pull request
    *   Masuk ke akun yang kita gunakan sebagai collaborator
    *   Lakukan forking dan kemudian clone
    *   buat branch baru agar tidak mengganggu data asli
    *   buka akun github, compare & pull
    *   Tambahkan pesan pull request

4. Merge pull request
    *   buka akun utama yang membuat repo
    *   periksa pull request
    *   tambahkan pesan diskusi agar yang memberikan request tahu
    *   jika pull request diterima, klik confirm merge

5. Bug Tracking
    *   Bug merupakan masalah/kerusakan dalam program yang perlu diperbaiki
    *   Features merupakan layanan atau ide untuk diimplementasikan
        *   fitur labels akan menghighlight tiap issues atau masalah dengan warna
            tersendiri
        *   Milestones dapat digunakan untuk menandai waktu dari sekumpulan masalah
            yang berguna untuk mengidentifikasi masalah apa yang harus dikerjakan
            untuk rilis fitur selanjutnya
        *   Search, fitur autocomplete untuk mencari issues ataupun milestones
        *   Assigment, dapat digunakan untuk menunjukkan kepada PIC atau orang yang
            bertanggung jawab atas suatu pekerjaan/issues untuk diselesaikan.
        *   Auto-close, ketika commit messages berisi kata fixed/fixes, close/closes/closed
            diikuti #[issue number], maka secara otomatis akan dianggap selesai
        *   Mentions, menggunakan #[issue-number] dalam messages akan dijadikan hyperlink
            untuk mempermudah menyampaikan issues terkait dalam percakapan
    *   To Do List ceklis item yang telah selesai

6. Analytics/insight
    *   Graph, menyediakan fitur analisis sbb:
        *   Contributors, mengetahui siapa contributor dan berapa banyak kode yang ditambah
            ataupun dihapus
        *   Commit Activity, mengetahui waktu commit dalam satu tahun (dalam satuan pekan)
        *   Code Frequwncy, mencatat banyaknya kode yg di commit selama life cycle sebuah 
            project
        *   Punchard, mengetahui waktu rata-rata dalam satuan hari commit dilakukan 
    *   Network, menyediakan fitur
        *   data kontributor
        *   commit yang dilakukan
        *   waktu commit
        *   branch yang dibuat, dst

7.  Project Management
    *   [Trello](https://trello.com/)
    *   [Pivotal Tracker](http://www.pivotaltracker.com/)

8.  Continoues Integration, digunakan untuk otomasi build dan test error saat integrasi 
    sebuah project agar dapat diselesaikan dengan cepat
    *   [Travis CI](https://www.travis-ci.com/)
    *   [Jenkins](http://jenkins-ci.org/)

9. Code Review, dapat digunakan untuk mengetahui
    *   inline command atau pertanyaan didalam baris kode
    *   Mengcompare branch dalam repo menggunakan tag [menggunakan URL pattern], dapat 
        diatur untuk mengabaikan whitespace/spasi [tambahkan ?w=1] pada URL pattern
    *   menambahkan .diff (seperti halnya git diff) untuk mendapatkan informasi dalam kode
    *   menambahkan .patch untuk membandingkan isi URL pattern dan diubah dalam bentuk  
        email sehingga lebih mudah dibaca
    *   Line Linking, dapat dibuat dengan klik pada line number akan menambahakn #line pada
        akhir URL dan merubah line menjadi kuning. dapat digunakan #start-end untuk membuat
        line linking dalam range tertentu

10. Documenting Method
    *   Formal Documentation menggunakan Github Wiki
    *   Informal Documantation menggunakan [Github Hubot](https://github.com/github/hubot)
    *   Mention, shorcut, Emoji