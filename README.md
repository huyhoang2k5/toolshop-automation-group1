# Toolshop Automation Testing — Sprint 1

## Giới thiệu

Dự án kiểm thử tự động website Toolshop, sử dụng **Python, pytest, Playwright và Page Object Model (POM)**.

Repository được sử dụng để thực hiện đồ án nhóm môn Automation Testing qua các buổi học.

## Buổi 1 — Sprint 1 (04/11/2026)

### Mục tiêu
- Tìm hiểu và áp dụng mô hình Page Object Model.
- Xây dựng bộ khung kiểm thử tự động.
- Viết các bài kiểm thử Smoke Test cho những chức năng cơ bản của Toolshop.
- Thực hành quy trình làm việc nhóm với Git, GitHub và Pull Request.

### Nội dung thực hiện
1. Thiết lập các file cấu hình `conftest.py`, `pytest.ini`, `requirements.txt`, `.gitignore` và `.env.example`.
2. Tổ chức thư mục `pages/` chứa các Page Object.
3. Xây dựng 4 bài kiểm thử Smoke Test:
   - Tìm kiếm sản phẩm.
   - Thêm sản phẩm vào giỏ hàng.
   - Kiểm tra đăng nhập với thông tin không hợp lệ.
   - Kiểm tra form liên hệ khi để trống thông tin.
4. Quản lý mã nguồn trên nhánh `feature/sprint1` và tạo Pull Request #1.

### Cách chạy kiểm thử

```bash
python -m pytest -m smoke -v
```

### Kết quả
- Đã xây dựng bộ khung kiểm thử tự động.
- Đã triển khai 4 Smoke Tests sử dụng Page Object Model.
- Đã hoàn thành Sprint 1 và merge Pull Request #1 vào nhánh `main`.

### Mã nguồn và Pull Request
- [Xem mã nguồn Sprint 1](https://github.com/huyhoang2k5/toolshop-automation-group1/tree/d991bfb)
- [Xem Pull Request #1](https://github.com/huyhoang2k5/toolshop-automation-group1/pull/1)

---

**Các buổi tiếp theo:** Sprint 2 mở rộng kiểm thử API, Network Mocking và UI Regression; Sprint 2B bổ sung BDD và GitHub Actions CI.
