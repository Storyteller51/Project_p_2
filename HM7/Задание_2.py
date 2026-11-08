def business_card(name, surname, **kwargs):
    print(f"{name} {surname}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

business_card(
    "Иван",
    "Иванов",
    age=30,
    city="Минск",
    company="Google",
    email="ivan@gmail.com"
)