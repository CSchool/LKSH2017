{
    "title": "Грузовой отсек",
    "description": """
Вы отворили дверь в грузовой отсек и настороженно заглянули внутрь. 
Перед вами предстало просторное помещение с ячейками для хранения на стенах, несколькими отсеками со спасательными капсулами и круглый шлюз, 
через который обычно переправляли приходящие на станцию грузы. Кнопка работоспособности горела только над одной из дверей. 
Не заметив ничего предвещающего опасность, вы зашли внутрь и направились к капсуле. 
Проходя мимо единственной открытой ячейки, вы заметили странное свечение. Вы не обратили на это внимания и пошли дальше. 
Вы дошли до активной капсулы, и уже хотели приложить руку на панель открытия, как позади что-то упало. Вы резко обернулись и замерли от страха. 
На вас шло непонятное существо с длинными лапами с тремя когтистыми пальцами на каждой, квадратной головой с маленькими блестящими глазками и тонким кривоватым телом. 
Оно уже начинало раскрывать свою огромную пасть с длинными острыми зубами, похожими на лезвия ножа.
""",
    "actions": [
        {
            "id": "FlamethrowerUsingCargoBay",
            "items": ["Flamethrower"],
            "message": "Применить огнемет по назначению",
            "once": True
        },
        {
            "id": "SurrenderRunCargoBay",
            "message": "Попробовать добежать до спасательной капсулы",
            "once": True
        },
        {
            "id": "SurrenderMoveBackCargoBay",
            "message": "Медленно пятиться назад",
            "once": True
        }
    ]
}