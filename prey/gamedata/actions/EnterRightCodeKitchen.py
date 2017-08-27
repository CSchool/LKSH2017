{
    "description": """Вы ввели правильный код! Теперь можно войти в холодильник. Или не стоит? Зачем Вам сейчас еда?""",
    "events_chain": True,
    "events": [
        {
            "id": "PassThroughRefrigeratorKitchen",
            "message": "Войти в холодильник",
            "once": True
        },
        {
            "id": "StopAtRefrigeratorKitchen",
            "message": "Остаться у порога",
            "once": True
        }
    ]
}