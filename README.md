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
* Tại đây ta thấy chương trình in ra màn hình một cái gì đó và jump đến một địa chỉ khác trên thanh ghi (loc_414D+4)
* Mình đoàn rằng đây là đoạn code chương trình in ra màn hình một đoạn chữ và xử lý thông tin nhập vào trong phần code ghi trên địa chỉ thanh ghi mà chương trình jmp đến.
* Follow đến địa chỉ thanh ghi này
