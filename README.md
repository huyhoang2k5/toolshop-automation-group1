# Toolshop Automation Testing — Group HAH

[![CI](https://github.com/huyhoang2k5/toolshop-automation-group1/actions/workflows/ci.yml/badge.svg)](https://github.com/huyhoang2k5/toolshop-automation-group1/actions/workflows/ci.yml)

## Giới thiệu dự án

Đây là repository thực hiện đồ án nhóm môn **Automation Testing**, tập trung xây dựng và phát triển hệ thống kiểm thử tự động cho ứng dụng Toolshop.

Dự án sử dụng **Python, pytest, Playwright** và **Page Object Model (POM)** để tổ chức mã nguồn, thực hiện kiểm thử giao diện, API và tích hợp quy trình kiểm thử tự động trên GitHub.

Các nội dung được triển khai theo từng buổi học, kế thừa và mở rộng từ những chức năng đã xây dựng trước đó.

## Tiến độ thực hiện

| Buổi | Nội dung | Kết quả |
|---|---|---|
| Buổi 1 — 04/11 | Xây dựng framework và Smoke Testing | Hoàn thành Sprint 1 |
| Buổi 2 — 11/11 | API Testing, Parametrize, Network Mocking và UI Regression | 22 tests passed tại máy |
| Buổi 3 — 18/11 | BDD, Gherkin và GitHub Actions CI | 24 tests passed tại máy, CI xanh trên 3 trình duyệt |
| Buổi 4 | Nội dung tiếp theo | Chờ cập nhật |

## Buổi 1 — Xây dựng nền tảng kiểm thử

Trong buổi đầu tiên, nhóm tập trung thiết lập môi trường và xây dựng cấu trúc dự án kiểm thử tự động theo mô hình Page Object Model.

Các nội dung chính gồm:
- Thiết lập Python, pytest và Playwright.
- Tổ chức Page Object để quản lý locator và thao tác trên giao diện.
- Cấu hình fixtures, markers và các thông số môi trường.
- Xây dựng 4 bài kiểm thử Smoke Test cho các chức năng cơ bản của Toolshop.
- Làm quen với quy trình quản lý mã nguồn, tạo nhánh và Pull Request trên GitHub.

**Kết quả:** Hoàn thành Sprint 1, xây dựng bộ khung kiểm thử và merge Pull Request #1.

[**Xem mã nguồn Buổi 1**](https://github.com/huyhoang2k5/toolshop-automation-group1/tree/d991bfb) · [**Pull Request #1**](https://github.com/huyhoang2k5/toolshop-automation-group1/pull/1)

## Buổi 2 — Kiểm thử API và mở rộng kiểm thử giao diện

Tiếp nối nền tảng đã xây dựng, nhóm mở rộng phạm vi kiểm thử để đánh giá cả giao diện và hoạt động của các API.

Các nội dung chính gồm:
- Kiểm thử API bằng Playwright APIRequestContext.
- Kiểm tra phản hồi HTTP, dữ liệu JSON, trường hợp lỗi và xác thực bằng token.
- Áp dụng tham số hóa dữ liệu kiểm thử với pytest.
- Sử dụng Network Mocking để kiểm tra giao diện khi phản hồi mạng thay đổi.
- Bổ sung các bài kiểm thử hồi quy giao diện.
- Tái sử dụng fixtures và Page Object để giảm mã nguồn trùng lặp.

**Kết quả:** Hoàn thành bộ kiểm thử Sprint 2 với **22/22 trường hợp passed tại máy**; Pull Request #2 đã merge.

[**Xem mã nguồn Buổi 2**](https://github.com/huyhoang2k5/toolshop-automation-group1/tree/106eb05) · [**Pull Request #2**](https://github.com/huyhoang2k5/toolshop-automation-group1/pull/2)

## Buổi 3 — BDD và tích hợp kiểm thử liên tục

Ở buổi thứ ba, nhóm triển khai phương pháp kiểm thử hướng hành vi (BDD) và thiết lập quy trình tự động chạy kiểm thử trên GitHub Actions.

Các nội dung chính gồm:
- Viết kịch bản kiểm thử bằng Gherkin.
- Sử dụng Feature, Scenario Outline và Examples để mô tả luồng nghiệp vụ.
- Kết nối các bước BDD với Page Object thông qua pytest-bdd.
- Thiết lập môi trường Toolshop phục vụ kiểm thử CI.
- Cấu hình GitHub Actions chạy trên Chromium, Firefox và WebKit.
- Tạo báo cáo kiểm thử HTML và cấu hình thu thập Playwright trace.
- Bổ sung badge trạng thái CI vào README.

**Kết quả:** **24/24 trường hợp passed tại máy**. Workflow GitHub Actions đã chạy thành công trên cả ba trình duyệt. Pull Request #3 đang trong quy trình review và merge.

[**Xem mã nguồn Buổi 3**](https://github.com/huyhoang2k5/toolshop-automation-group1/tree/1a47593) · [**Pull Request #3**](https://github.com/huyhoang2k5/toolshop-automation-group1/pull/3)

## Buổi 4 — Nội dung tiếp theo

Phần này sẽ được cập nhật sau khi nhóm thực hiện buổi học tiếp theo, bao gồm nội dung triển khai, các chức năng kiểm thử được bổ sung và kết quả nghiệm thu.

## Công nghệ sử dụng

| Công nghệ | Vai trò |
|---|---|
| Python | Ngôn ngữ lập trình kiểm thử |
| pytest | Framework tổ chức và chạy test |
| Playwright | Tự động hóa trình duyệt và kiểm thử API |
| pytest-bdd | Triển khai kiểm thử hướng hành vi |
| Page Object Model | Tổ chức và tái sử dụng thao tác giao diện |
| Git và GitHub | Quản lý phiên bản, Pull Request và review |
| GitHub Actions | Tự động chạy bộ kiểm thử trên CI |
| Docker | Khởi chạy môi trường Toolshop trong CI |

## Cấu trúc dự án

```text
toolshop-automation-group1/
├── .github/workflows/     # GitHub Actions CI
├── pages/                 # Page Object Model
├── tests/
│   ├── api/               # API Testing
│   ├── bdd/               # BDD Testing
│   ├── data/              # Dữ liệu kiểm thử
│   └── ui/                # UI Testing
├── toolshop/              # Cấu hình Toolshop cho CI
├── conftest.py            # Fixtures dùng chung
├── pytest.ini             # Cấu hình pytest
├── requirements.txt       # Thư viện Python
└── README.md              # Tài liệu dự án
```

## Cài đặt và chạy kiểm thử

Yêu cầu Python 3.12 và môi trường Toolshop đang hoạt động.

### Cài đặt trên Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
```

### Chạy toàn bộ bài kiểm thử

```powershell
python -m pytest tests/ -v
```

### Chạy riêng Smoke Test

```powershell
python -m pytest -m smoke -v
```

### Chạy riêng BDD Test

```powershell
python -m pytest tests/bdd -v
```

Các URL và thông tin cấu hình môi trường được quản lý qua fixtures và biến môi trường. Không đưa token, file `.env` hoặc dữ liệu nhạy cảm lên GitHub.

## Quy trình làm việc nhóm

Nhóm sử dụng GitHub để quản lý mã nguồn theo từng giai đoạn. Các thay đổi được phát triển trên nhánh riêng, sau đó tạo Pull Request để kiểm tra, review và tích hợp vào nhánh `main`.

Dự án hướng đến việc duy trì mã nguồn dễ mở rộng, tái sử dụng Page Object, giảm sự phụ thuộc vào dữ liệu cố định và tăng tính ổn định của bộ kiểm thử.

---

**Repository:** [toolshop-automation-group1](https://github.com/huyhoang2k5/toolshop-automation-group1)

**Môn học:** Automation Testing

**Nhóm thực hiện:** Group HAH
