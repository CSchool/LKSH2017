{
    "description": "<< Введите в терминале код, который подходит к решению >>",
    "events_chain": True,
    "once": True,
    "conditions": {
        "need_user_input": True,
        "checker": "check_kitchen_code",
        "if_true": {
            "id": "EnterRightCodeKitchen"
        },
        "if_false": {
            "id": "EnterWrongCodeKitchen"
        }
    }
}