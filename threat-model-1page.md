# Threat Model - Lab 3

## Thông tin nhóm
- Thành viên 1: Vũ Hồng Sơn
- Thành viên 2: Phạm Văn Chung

## Assets
- Dữ liệu người dùng (username, password, email, thông tin cá nhân)
- Cơ sở dữ liệu hệ thống
- Server backend và API
- Source code của ứng dụng
- Session / token xác thực
- Hệ thống thanh toán (nếu có)

## Attacker model
- Truy cập ứng dụng qua internet như một người dùng bình thường
- Gửi request tùy ý đến server (bao gồm request độc hại)
- Thử khai thác lỗ hổng như SQL Injection, XSS
- Nghe lén traffic nếu kết nối không bảo mật
- Tấn công brute-force vào tài khoản
- Có thể có kiến thức cơ bản đến trung bình về bảo mật web

## Threats
- SQL Injection
    Kẻ tấn công chèn câu lệnh SQL vào input để truy cập trái phép database
- Cross-Site Scripting (XSS)
    Chèn mã JavaScript độc hại để đánh cắp cookie hoặc session
- Brute-force / Credential Stuffing
    Thử nhiều mật khẩu để chiếm quyền tài khoản
- Man-in-the-Middle (MITM)
    Nghe lén hoặc thay đổi dữ liệu khi truyền nếu không dùng HTTPS

## Mitigations
- Chống SQL Injection
    Sử dụng prepared statements / ORM
    Validate và sanitize input
- Chống XSS
    Escape output
    Sử dụng Content Security Policy (CSP)
- Chống brute-force
    Giới hạn số lần đăng nhập (rate limiting)
    Sử dụng CAPTCHA
    Áp dụng MFA (Multi-Factor Authentication)
- Chống MITM
    Sử dụng HTTPS (TLS)
    HSTS (HTTP Strict Transport Security)

## Residual risks
- Người dùng sử dụng mật khẩu yếu vẫn có thể bị lộ tài khoản
- Lỗ hổng zero-day trong framework hoặc thư viện bên thứ ba
- Lỗi cấu hình server hoặc triển khai sai
