{
    "description": """
Вы собрались и резко вскинули огнемет, когда чудовище уже было в паре шагов от вас. 
Яркое обжигающее пламя вырвалось наружу, моментально воспламеняя монстра. 
Зверь завыл от боли и забыв про вас, упал на пол, пытаясь сбить пламя. 
В свете огня вы видели, как он меняет форму из одной в другую, принимая порой столь странные из них, 
что вы не могли даже понять, что это.  От невозможности выносить этого зрелища и давящего на слух вопля пришельца, 
вы трясущейся рукой открыли дверь, выскочили наружу и резко захлопнули дверь. 
Вы прислонились к стене и глубоко дышали, пытаясь забыть пережитый вами ужас. 
Перед глазами все еще стояла пасть полная острых ножеподобных зубов. 
Неожиданно вам показалось, что из соседней - последней не проверенной вами комнате, раздался всхлип, 
похожий на человеческий. От увиденного вам очень хотелось убежать туда, где казалось было безопаснее, 
в холл или лабораторию, но пересилив себя вы решили все же проверить комнату, ведь там мог оказаться еще один выживший. 
Вы зашли в нее, здесь в отличие от остальных комнат вещи были разбросаны, письменный стол разломан пополам, 
в воздухе витал странный запах. Из большого платяного шкафа доносились всхлипы.  
В то же время вы услышали какой-то стук в коридоре.
""",
    "actions": {
        "decrease_flamethrower": True
    },
    "events_chain": True,
    "events": [
        {
            "id": "OpenWardrobeLivingRoom",
            "message": "Открыть шкаф, чтобы помочь человеку внутри",
            "once": True
        },
        {
            "id": "HideUnderBedLivingRoom",
            "message": "Залезть от страха под кровать",
            "once": True
        }
    ]
}