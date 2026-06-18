структура проекта
VelosipedDrive/
│
├── main.py
│
├── database/
│   ├── db.py
│   ├── create_db.py
│   └── bicycle.db
│
├── models/
│   ├── user.py
│   ├── product.py
│   ├── order.py
│   └── pickup_point.py
│
├── windows/
│   ├── login_window.py
│   ├── guest_window.py
│   ├── manager_window.py
│   ├── admin_window.py
│   ├── product_window.py
│   ├── order_window.py
│   └── edit_product_window.py
│
├── services/
│   ├── auth_service.py
│   ├── product_service.py
│   └── order_service.py
│
├── imports/
│   ├── import_users.py
│   ├── import_products.py
│   ├── import_orders.py
│   └── import_pickup_points.py
│
├── resources/
│   ├── icon.ico
│   ├── logo.png
│   └── style.qss
│
├── excel/
│   ├── user_import.xlsx
│   ├── Tovar.xlsx
│   ├── Заказ_import.xlsx
│   └── Пункты выдачи_import.xlsx
│
└── requirements.txt
