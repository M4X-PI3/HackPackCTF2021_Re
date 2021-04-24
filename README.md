# HackPackCTF2021_Re
Write-up reverse hackpack CTF 2021
CTF competitive site: https://ctf2021.hackpack.club

REVERSE

I> Function Pointer Fun (50)
* Bước đầu tiên mình thường làm trong việc reverse một file là scan metadata của file này.
* https://www.metadata2go.com
![image](https://user-images.githubusercontent.com/83124718/115960665-ef84a300-a53c-11eb-9ced-083eb80789e2.png)

* Sau đó bỏ vào PE tương thích để reverse.
![image](https://user-images.githubusercontent.com/83124718/115960752-602bbf80-a53d-11eb-9ac0-026d957a3491.png)
* Đọc qua có thể thấy, đây là chương trình nhập password với 4 ký tự, và hàm pickFunction chính là point để kiểm tra password nhập vào.
* Theo dấu hàm pickFunction
![image](https://user-images.githubusercontent.com/83124718/115960933-58204f80-a53e-11eb-9883-297cf83d90c8.png)
* Kiểm tra lần lượt từng fucntion return thì nhận thấy funcTwo sẽ trả về flag sau khi nhập đúng password
* Password nhập vào là seed 4 ký tự, để hàm pickFunction trả về funcTwo, ta cần nhập password để response trả về giá trị là 73(dec)
* Mình viết 1 chương trình python đơn giản để giải password này(FPF_solver.py)
* password: 0I@I
* submit password là ra flag
* flag{c1RcU1t5_R_fUn!2!}

II> GaussBot
* Tương tự, trước tiên ta kiểm tra metadata file GaussBot và bỏ vào IDA tương thích
![image](https://user-images.githubusercontent.com/83124718/115961780-17c2d080-a542-11eb-99ea-0c444b81494d.png)
* Trong chương trình này, các dữ liệu đều liên quan tính toán với 'code', nên follow code và kiểm tra thêm trong này có gì.
![image](https://user-images.githubusercontent.com/83124718/115961845-6d977880-a542-11eb-98d5-6800729dd87d.png)
* Chương trình có thực hiện những lênh push data vào stack. các dữ liệu này rất có thể là flag, mình kiểm tra và giải mã sạng ascii thì thấy được flag.
* Hoặc sau khi thực hiện các lệnh push và in, sau đó có 1 subprocess có thể process này sẽ so sánh các data đã push vào trong stack
![image](https://user-images.githubusercontent.com/83124718/115963804-2bbf0000-a54b-11eb-8ebd-e6fdc2994b51.png)
* Khi decompile subprocess này bạn sẽ thấy được flag được ghi lại.
![image](https://user-images.githubusercontent.com/83124718/115963841-67f26080-a54b-11eb-963f-4b065640d5f1.png)
* flag{pr0gram-inside-4-pr0gram}

III> BF means best friend, right?
* BF nghĩa là best friend?
* Google thì thấy ngay BF là BrainF**k,
* Để kiểm tra những giá trị của đoạn mã này lưu trong memory, mình sử dụng phần mềm VBBrainFNET.exe
![image](https://user-images.githubusercontent.com/83124718/115963956-244c2680-a54c-11eb-879e-73930fce2c66.png)
flag{brain-blast}

IV> Exhell 
* exhell.xlsx một file excel, mở lên xem thử bên trong có gì,
* trong file này có 2 sheet Buget và sUpErSeCrEt.
* Trong sheet Buget mình kiểm tra ở đây chỉ đơn thuần là những box lưu text thông thường, nhưng ở cell nope(H9) bên dưới cell flag{...}, một hàm gọi về sheet sUpErSeCrEt kiểm tra bool tại cell K1 sUpErSeCrEt
![image](https://user-images.githubusercontent.com/83124718/115964428-b0f7e400-a54e-11eb-9bde-7a7ddcd6dad9.png)
* Qua sheet sUpErSeCrEt mình để ý thấy các giá trị lần được được tính toán tuần tự bằng OR AND và NOT lần lượt tự A>B>C>D>E>F mục tiêu sẽ là làm ô K1 trả về giá trị True
* Column A là giá trị binary truy suất từ cell flag ở sheet Buget như vậy khi K1 trả về True thì các giá trị ở column A sẽ là flag cần tìm.
* Để giải quyết vấn đề này, mình kiểm tra các ô tính toán sai bao gồm cả cell A6 và A7 (vì flag bắt đầu bằng 'flag{')
* Copy sheet này thành Sheet3 và đổi các giá trị column A thành static
![image](https://user-images.githubusercontent.com/83124718/115964393-89088080-a54e-11eb-9096-a9d0e63c9bb0.png)
* Mình viết một đoạn code python để giải (exhell_solver.py) các giá trị từ A6 -> A41
flag{0h_g33z_th4t5_a_l0t_sp3nt_0n_L3Cr0ix}
