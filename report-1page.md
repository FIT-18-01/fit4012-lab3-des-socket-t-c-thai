# Report 1 page - Lab 3

## Thông tin nhóm
- Thành viên 1: Vũ Hồng Sơn
- Thành viên 2: Phạm Văn Chung
## Mục tiêu
 Bài lab nhằm giúp sinh viên hiểu và triển khai cơ chế mã hóa đối xứng sử dụng thuật toán DES ở chế độ CBC. Thông qua việc xây dựng hai thành phần Sender và Receiver, nhóm thực hành quá trình mã hóa, truyền dữ liệu và giải mã an toàn. Ngoài ra, bài lab còn giúp nắm được vai trò của IV (Initialization Vector) trong việc tăng tính bảo mật. Cuối cùng, sinh viên biết cách kiểm thử và đánh giá tính đúng đắn của hệ thống.
## Phân công thực hiện
- Vũ Hồng Sơn: Phụ trách xây dựng chương trình Sender, thực hiện mã hóa dữ liệu và gửi đi.
- Phạm Văn Chung: Phụ trách xây dựng chương trình Receiver, thực hiện giải mã dữ liệu nhận được.
- Cả hai cùng thực hiện kiểm thử, ghi log và xây dựng threat model.
## Cách làm
- Nhóm triển khai hệ thống gồm hai phần:
- Sender nhận dữ liệu đầu vào, mã hóa bằng DES-CBC với khóa bí mật và IV ngẫu nhiên, sau đó gửi dữ liệu.
- Receiver nhận dữ liệu, dùng cùng khóa và IV để giải mã và khôi phục dữ liệu ban đầu.
- Nhóm sử dụng thư viện lập trình để cài đặt DES-CBC.
- Kiểm thử bằng nhiều loại dữ liệu khác nhau để đảm bảo tính chính xác.
## Kết quả
- Chương trình hoạt động đúng yêu cầu:
- Dữ liệu giải mã trùng với dữ liệu ban đầu.
- IV thay đổi giúp tăng bảo mật.
- Hệ thống xử lý tốt nhiều trường hợp dữ liệu.
- Nhóm đã lưu log và có ảnh minh chứng cho các lần chạy thử.

## Kết luận
- Bài lab giúp nhóm hiểu rõ cách hoạt động của DES và chế độ CBC. Việc sử dụng IV làm tăng tính an toàn cho dữ liệu. Nhóm cũng nhận ra tầm quan trọng của kiểm thử và đánh giá bảo mật. Trong thực tế, nên sử dụng các thuật toán mạnh hơn như AES và quản lý khóa chặt chẽ.