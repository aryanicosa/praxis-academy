<h1>  Langkah-langkah belajar dasar kolaborasi dengan github: </h1>

<h4>**STEP 1. Menggunakan akun utama yang membuat project/repositori**</h4>

1. Melalui terminal buat direktori lokal rhymes dan masuk
  * mkdir rhymes
  * cd rhymes

2. inisialisasi git
  * git init

3. buat readme.txt kosong
  * touch README.txt
  * git add README.txt
  * git commit -m "commit pertama"

4. menambahkan penjelasan pada file README.txt
echo "this is a collection of my fav nursery rhymes." >> README.txt
  * git status
  * git diff
  * git add README.txt
  * git commit -m "Add project overview to README.txt"

5. mendownload/menambahkan beberapa file lain ke dalam repo lokal
link nya error, jadi tambahk file baru secara manual saja

  * git add rhyme-baru.txt
  * git status
  * git commit -m "add rhyme-baru.txt"

#jika semua mau di commit bisa add sekaligus
  * git add .
  * git commit -m "commit semua yang belum di commit"

6. buka history commit
  * git log
  * git log --oneline
  * git log -p

7. tambahkan remote git kemudian push
  * git remote add origin https://github.com/aryanicosa/rhymes.git
  * git branch -M main
  * git push -u origin main

<h4>**STEP 2. Menggunakan akun lain untuk mengkopi/clone atau untuk bekerjasama 
dapat melakukanfork project/repositori dari akun utama**</h4>

1. Pindah ke akun lain
  * buka https://github.com/aryanicosa/rhymes sebagai repo yang akan dikolaborasi
  * lakukan fork

2. buat direktori baru untuk dijadikan penyimpanan clone 
  * mkdir rhymes-2
  * cd rhymes-2
  * git clone https://github.com/jogjaembedded/rhymes
  * cd rhymes

3. Buat branch baru agar tidak merubah branch dari repo yang di fork
  * git checkout -b hickory-dickory

4. tambahkan fille yang disarankan, kemudian push ke branch
  * git add hickory-dickory-dock.txt
  * git commit -m 'Added hickory-dickory-dock.txt.'
  * git push origin hickory-dickory

5. Buka akun github, refresh halaman. maka akan muncul branch baru
buat pull request dengan menambahkan pesan agar pada repo utama yg di fork diketahui
apa yang disarankan

<h4>**STEP 3. Mereview dan menerima/menolak pull request**</h4>

1. Kembali ke akun utama dan repo rhyme. Perhatikan bahwa pada bar pull request
   muncul pemberitahuan
2. Agar tidak terjadi kesalahan, lebih baik ganti nama branch repo lokal terlebih dahulu
masuk ke repo rhymes lokal, kemudian rename origin
  * cd rhymes
  * git remote rename origin arya

3. Tambahkan remote point ke repo duplikat yang di fork oleh jogja
  * git remote add jogja https://github.com/jogjaembedded/rhymes.git
  pastikan kalau sudah benar
  * git remote -v

4. Fetch duplikat yang dikerjakan jogja
  * git fetch jogja

5. tampilkan semua branch yang ada pada repo lokal maupun remote
  * git branch -a

6. checkout ke repo jogja yang sudah di fetch dan review
  * git checkout -b hickory-dickory bob/hickory-dickory
  * git diff main hickory-dickory
  * git log -1 -p

7. jika tidak ada masalah, pindah ke repo main lokal dan gabungkan
  * git checkout main
  * git merge hickory-dickory

8. push repo lokal ke repo utama github (arya)
  * git push

9. hapus branch milik jogja yang sudah du merge
  * git branch -D hickory-dickory

10. Kembali ke github dan amati bahwa tidak ada lagi pull request

<h4>**STEP 4. Membuat banyak perubahan di forked repo**</h4>

1. masuk kembali ke repo lokal yg di clone dari fork yang dilakukan

2. Ganti name origin
  * git remote rename origin jogja

3. Tambahkan remote point ke repo asli, kemudian periksa
  * git remote add arya https://github.com/aryanicosa/rhymes.git
  * git remote -v

4. Update main branch di lokal repo untuk menyamakan dengan repo yang di fork
  * git remote update
  * git checkout main
  * git merge arya/main

5. periksa apakah ada perbedaan
  * git diff arya/main

6. push semua data update di repo lokal ke github jogja
  * git push jogja main

7. buat branch baru
  * git checkout -b jogjas-changes

8. Menambahkan beberapa file
seperti sebelumnya
  * git add ...

9. melakukan perubahan berulang kali seperti membenahi typo, atau menambahkan baris
  * git commit -am "Update README.txt"
melakukan perubahan lagi kemudian commit lagi
  * git commit -am "Update README.txt"
melakukan perubahan lagi kemudian commit lagi
  * git commit -am "Update README.txt"

10. setelah melakukan banyak aktivitas kemudian melihat log
  * git log --oneline

11. Dikarenakan terlalu banyak perubahan sepele, maka dilakukan clean up terhadap
commit yang tidak perlu dengan rebase
  * git rebase -i 567a79b

12. atur urutan yang ingin di rebase, kemudian ubah pick menjadi squash untuk menggabung menjadi 1 commit keatas

  /home/aryanicosa/rhymes-2/rhymes/.git/rebase-merge/git-rebase-todo  Modified  
pick a0a53f4 tambah rhyme-baru-1.txt
pick 509fa06 tambah rhyme-baru-2.txt
pick 648596f Update README.txt
squash 60880f1 Fixed typo in README.txt
squash 4a7a25d Update README.txt
squash add3823 Update README.txt

# Rebase 567a79b..add3823 onto 60880f1 (6 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup <commit> = like "squash", but discard this commit's log message
# x, exec <command> = run command (the rest of the line) using shell

13. setelah rebase dirasa cukup, kemudian dapat melakukan push ke branch baru pada remote jogja
  * git push --set-upstream jogja jogjas-changes

14. buatlah pull request seperti sebelumnya untuk direview dan di acc
