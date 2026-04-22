# Peer Review Response

## Thông tin nhóm
- Thành viên 1: Vũ Hồng Sơn
- Thành viên 2: Phạm Văn Chung
## Thành viên 1 góp ý cho thành viên 2
Thành viên 1: Code hoạt động đúng nhưng cần cải thiện phần xử lý lỗi và viết test rõ ràng hơn. Một số test còn dùng assert chưa chặt chẽ và chưa bao phủ các trường hợp như sai key hoặc dữ liệu bị chỉnh sửa.

## Thành viên 2 góp ý cho thành viên 1
Thành viên 2: Phần triển khai logic tốt, tuy nhiên cần bổ sung thêm test cho các trường hợp biên và cải thiện cách đặt tên biến để dễ hiểu hơn. Ngoài ra nên thêm comment để giải thích rõ hơn các bước xử lý.

## Nhóm đã sửa gì sau góp ý
Nhóm đã cải thiện lại các test bằng cách xử lý rõ ràng các trường hợp lỗi (ValueError) thay vì dùng assert đơn giản. Bổ sung thêm test cho các tình huống như sai key và tampered ciphertext. Đồng thời chỉnh sửa lại một số tên biến và thêm comment để code dễ đọc và dễ bảo trì hơn.