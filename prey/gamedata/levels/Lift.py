{
    "description": """
Вы вошли в кабину лифта и нажали на кнопку вниз. 
Лифт издал легкий гудок, предупреждающий о начале движения и плавно поехал на нижний этаж. 
Спустившись, вы вышли в небольшой коридор, который разветвляется на два рукава - один вел в сторону капитанской рубки, 
а второй на инженерную палубу. В конце коридора над капитанской рубкой мигал красный фонарик, который должен был предупреждать о разгерметизации помещения. 
Но подумав, вы решили, что система вполне могла дать сбой, и тогда сигнал горел без причины. 
    """,
    "description_visited": """
Вы стоите в коридоре, из которого можно перейти либо в капитанскую рубку, либо отправиться за приключениями
на инженерную палубу.
""",
    "transitions": [
        {
            "level": "Hall",
            "message": "Вернуться в холл"
        },
        {
            "level": "CaptainCabin",
            "message": "Пройти в капитанскую рубку"
        }
    ],
    "actions": [
        {
            "id": "EngineeringDeck",
            "message": "Отправиться на инженерную палубу",
            "once": True
        }
    ]
}