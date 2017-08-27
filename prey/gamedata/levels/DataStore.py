{
    "description": """
Вы протиснулись в хранилище данных, дождавшись, когда двери будут открыты. 
Это была просторная комната с серверами и большим терминалом. 
С потолка свисали перепутанные провода, часть из них была порвана. 
Вы подошли к терминалу, экран которого периодически мигал.
""",
    "description_visited": """
Вообще говоря, Вам повезло, что вы смогли оказаться здесь - карточек доступа к месту, через которое проходят
все данные и которое является практически вторым центром управления станции, помимо капитанского мостика, очень мало.
Однако глупо надеяться, что IT-шники не построили второй кордон защиты от неавторизированных пользователей.
А еще очень мешают провода сверху - может их стоит поправить, чтобы не попасть под удар током?
""",
    "transitions": [
        {
            "level": "Hall",
            "message": "Отправиться в холл"
        }
    ],
    "actions": [
        {
            "id": "PlayerIdentification",
            "message": "Приложить свою руку к сканеру отпечатков",
            "once": True,
        },
        {
            "id": "CargoBayOpening",
            "facts": ['player_identified_datastore'],
            "exclude_facts": ["cargo_bay_opened"],
            "message": "Открыть грузовой отсек",
        },
        {
            "id": "SurrenderDataStore",
            "facts": ['player_identified_datastore'],
            "message": "Поправить провода",
            "once": True,
        }
    ]
}