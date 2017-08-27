# -*- coding: utf-8 -*-
import string
from enum import Enum
from textwrap import fill

from copy import deepcopy

from gamedata import game_data
from term import get_terminal_size
import subprocess

try:
    h = subprocess.check_output(['git', 'describe']).decode().strip()
    VERSION = "Prey {}".format(h)
except:
    VERSION = "Prey"


class GameResult(Enum):
    CONTINUE = 0
    LOSE = 1
    WIN = 2
    ERROR = 3
    NEED_INPUT = 4


class Game:
    total_endings = 17
    total_achievments = 7

    def __init__(self, log_needed=False):
        self.result = GameResult.CONTINUE
        self.current_location = ""
        self.previous_location = ""
        self.visited_locations = set()  # index
        self.completed_actions = set()  # index
        self.items = set()
        self.current_events = {}
        self.current_action = {}
        self.facts = set()
        self.flamethrower_count = 0
        self.ending = 0
        self.log = None
        self.achievments = set()
        self._drawer = self.Drawer()

        if log_needed:
            self.log = ""
            self._drawer = self.Drawer("")

    def __repr__(self):
        items = ("%s = %r" % (k, v) for k, v in self.__dict__.items())
        return "<%s: {%s}>" % (self.__class__.__name__, ', '.join(items))

    def award_achievments(self, ach=None):
        import gamedata.checkers as checkers
        if self.flamethrower_count >= 2:
            self.facts.add('double_flamethrower')
        else:
            self.facts.discard('double_flamethrower')
        show_total = False
        for achievment in game_data['achievments']:
            if achievment in self.achievments and achievment != ach:
                continue
            if 'checker' in game_data['achievments'][achievment]:
                checker_function = getattr(checkers, game_data['achievments'][achievment]['checker'])
            else:
                checker_function = lambda x, y, z: achievment in z
            if checker_function(self.items, self.facts, self.achievments):
                self.achievments.add(achievment)
                if game_data['achievments'][achievment]['show']:
                    show_total = True
                    msg = " ДОСТИЖЕНИЕ ПОЛУЧЕНО "
                    pad = (self._drawer.get_term_width() - len(msg)) // 2
                    self.logging((pad * "-") + msg + (pad * "-"))
                    self.logging("")
                    self.logging(game_data['achievments'][achievment]['description'])
                    self.logging("")
                    self.logging("-" * self._drawer.get_term_width())
                    self.logging("")
        if show_total:
            self.logging("(получено {} достижений из {})".format(len(self.get_achievments()), Game.total_achievments))
            self.logging("")


    def get_achievments(self):
        res = []
        for achievment in self.achievments:
            if achievment not in game_data['achievments']:
                continue
            if game_data['achievments'][achievment].get('show'):
                res.append(game_data['achievments'][achievment])
        return res

    class Drawer:
        def __init__(self, log=None):
            self.term_width = -1
            self.log = log

        def set_term_width(self, width):
            self.term_width = width

        def get_term_width(self):
            if self.term_width > 0:
                return self.term_width
            return get_terminal_size()[0]

        def draw_ascii_image(self, image):
            mw = max(map(len, image.split('\n')))
            pad = (self.get_term_width() - mw) // 2
            for line in image.split('\n'):
                s = " " * pad + line
                if type(self.log) is str:
                    self.log += s + "\n"
                else:
                    print(s)

        def write_logo(self):
            logo = """


PPPPPPPPPPPPPPPPP                                                                  
P::::::::::::::::P                                                                 
P::::::PPPPPP:::::P                                                                
PP:::::P     P:::::P                                                               
  P::::P     P:::::Prrrrr   rrrrrrrrr       eeeeeeeeeeee  yyyyyyy           yyyyyyy
  P::::P     P:::::Pr::::rrr:::::::::r    ee::::::::::::ee y:::::y         y:::::y 
  P::::PPPPPP:::::P r:::::::::::::::::r  e::::::eeeee:::::eey:::::y       y:::::y  
  P:::::::::::::PP  rr::::::rrrrr::::::re::::::e     e:::::e y:::::y     y:::::y   
  P::::PPPPPPPPP     r:::::r     r:::::re:::::::eeeee::::::e  y:::::y   y:::::y    
  P::::P             r:::::r     rrrrrrre:::::::::::::::::e    y:::::y y:::::y     
  P::::P             r:::::r            e::::::eeeeeeeeeee      y:::::y:::::y      
  P::::P             r:::::r            e:::::::e                y:::::::::y       
PP::::::PP           r:::::r            e::::::::e                y:::::::y        
P::::::::P           r:::::r             e::::::::eeeeeeee         y:::::y         
P::::::::P           r:::::r              ee:::::::::::::e        y:::::y          
PPPPPPPPPP           rrrrrrr                eeeeeeeeeeeeee       y:::::y           
                                                                y:::::y            
                                                               y:::::y             
                                                              y:::::y              
                                                             y:::::y               
                                                            yyyyyyy                


        """

            self.draw_ascii_image(logo)


        def draw_map(self):
            map = r"""
                           _____
             ___          |     |
            |   |         |     |
            | A |xxx_ _xxx|  B  |
            |___|    |    |_____|                               A - Жизнеобеспечение
        _ _ _ _ _    |                                          B - Электростанция
       |         |   |     |\                                   С - Грузовой отсек
       |    O    |   |_ _ _| \                                  D - Жилой отсек
       |_ _ _ _ _|  _ _ _ _|  \                                 I - Коридор
      _ _ _    |   |       | F \                                Y - Кухня
     |     |    \_/        |____\                               V - Пост охраны
     |  L  |\   | |        _ _ _ _ _ _ _                        S - Спортзал
     |_ _ _| \  |Q|       |             |                       R - Дендрарий
              \_|_|_      | |\  |\  |\  |       ___             H - Холл
      _       |     |     | |_\ |_\ |_\ |     /  S  \           L - Хранилище данных
    /_K_\     |  H  |-----|      D      |-xxx|_______|          F - Инженерная палуба
      |       |_ _ _|     | |\  |\  |\  |                       O - Капитанская рубка
(G)-xx|   xxx--|     \    | |_\ |_\ |_\ |                       G - Отдел нейромодов
      |  _|  _ _ _    \   |_ _ _ _ _ _ _|                       Q - Лифт
      | |   (     )    |    _                                   K - Лаборатория
      | |  /|  Y  |    |_ _| \                                  xxx - проход заблокирован
     _|_| / (_ _ _)    |   |  \
    |_I_|<        _    |   |   \
          \      | |   |   | V  |
          _\_    |R|xxx|   |   /
        /     \  |_|       |  /
       |   C   |           |_/
        \_ _ _/

            """

            self.draw_ascii_image(map)

    # get game result
    def get_result(self):
        return self.result

    # get ending
    def get_ending(self):
        return self.ending

    # start game
    def start_game(self):
        self.change_level("Laboratory")

    # draw logo
    def draw_logo(self):
        self._drawer.write_logo()
        self.logging("Вы играете в " + VERSION)
        self.logging("")
        self.logging("")

    # show map to player
    def show_map(self):

        mapping = {
            "Laboratory": 'K',
            'Hall': 'H',
            'Corridor': 'I',
            'DataStore': 'L',
            'Lift': 'Q',
            'LivingRooms': 'D',
            'SecurityPost': 'V',
            'CaptainCabin': 'O',
            'CargoBay': 'C',
            'Kitchen': 'Y',
        }

        self._drawer.draw_map()
        self.logging("Вы находитесь в локации ({})".format(mapping[self.current_location]))

    # show inventory
    def show_inventory(self):
        count = 1

        if not len(self.items):
            self.logging("Инвентарь пуст!")
        else:
            for item in self.items:
                inventory_text = game_data['items'][item]['title']
                if item == "Flamethrower":
                    inventory_text += ". Количество зарядов: ({})".format(self.flamethrower_count)
                self.logging("{}) {}".format(str(count), inventory_text))
                count += 1

    def show_stats(self):
        self.logging("Открытые концовки:")
        endings = ""
        for ending in range(1, Game.total_endings + 1):
            if ("Ending_%d" % ending) in self.achievments:
                endings += "o"
            else:
                endings += "."
        self.logging(endings)
        self.logging("")
        self.logging("Открыто {} из {} достижений".format(len(self.get_achievments()), Game.total_achievments))
        self.logging("")

    # intro message
    def write_intro(self):
        self.logging("""
Десять лет назад человечество столкнулось с  враждебной разумной расой, названной впоследствии тифонами.
Пришельцы обладали коллективным разумом, могли с легкостью изменять форму своего тела, но не испытывали
никаких чувств, привычных человеку, что делало их очень непредсказуемым и безжалостным врагом. Тифоны
атаковали Землю неожиданно, люди оказались совершенно не готовы. В течение пяти лет длилась самая кровавая
и жестокая война в истории человечества, но все же люди смогли выжить и даже отогнать захватчиков далеко в
космос. Пленные тифоны были помещены под стражу на орбитальной станции Талос 1, где группы ученых пытались
найти способ контролировать пришельцев или перенять их способности к метаморфозу. Вы — один из ученых,
работающих на станции. За 4 года упорной работы ваша группа продвинулась далеко вперед и вы были почти
на пороге нового открытия — нейромодификатора, который мог позволить человеку, вколовшему его, изменять
свое тело по желанию в совершенно любой предмет. Но кое-что пошло не так...
""")

    # logging function
    def logging(self, message):
        for msg in message.split('\n\n'):
            if type(self._drawer.log) is str:
                self._drawer.log += fill(msg, self._drawer.get_term_width()) + "\n"
            else:
                print(fill(msg, self._drawer.get_term_width()))

    # check action conditions (can user do it?)
    def check_action_conditions(self, action):
        # check once existing
        once_checking = True if not action.get('once') else action['id'] not in self.completed_actions
        # check facts (include)
        facts_checking_include = True if not action.get('facts') else all(
            fact in self.facts for fact in action['facts'])
        # check facts (exclude)
        facts_checking_exclude = True if not action.get('exclude_facts') else all(
            fact not in self.facts for fact in action['exclude_facts'])
        # items check
        items_checking = True if not action.get('items') else all(
            item in self.items for item in action['items'])

        # flamethrower count
        flamethrower_count = True
        if action.get('items') and action['items'][0] == "Flamethrower" and self.flamethrower_count <= 0:
            flamethrower_count = False

        return once_checking and facts_checking_include and \
               facts_checking_exclude and items_checking and flamethrower_count

    # check transition conditions
    def check_transition_conditions(self, transition):
        # check facts
        facts_checking_include = True if not transition.get('facts') else all(
            fact in self.facts for fact in transition['facts'])

        return facts_checking_include

    # create user events on this level
    def define_user_events(self, transitions=None, actions=None, suppress_inventory=False, suppress_map=False, suppress_stats=False):
        if actions is None:
            actions = []

        if transitions is None:
            transitions = []

        letters = string.ascii_lowercase
        letter_index = 0
        events = {}

        for transition in transitions:
            # if we had facts on transitions - we can check it here
            if self.check_transition_conditions(transition):
                while letter_index in ['i', 'm', 's']:
                    letter_index += 1

                events[letters[letter_index]] = {
                    'type': 'transition',
                    'data': transition
                }

                letter_index += 1

        for action in actions:
            if self.check_action_conditions(action):
                while letter_index in ['i', 'm', 's']:
                    letter_index += 1

                events[letters[letter_index]] = {
                    'type': 'action',
                    'data': action
                }

                letter_index += 1

        # inventory and map
        if not suppress_inventory:
            # dirty hack
            if not( self.current_location == 'Kitchen' and 'has_fight_kitchen' not in self.facts):
                events['i'] = {
                    'type': 'action',
                    'data': "show_inventory"
                }

        if not suppress_map:
            if 'can_view_map' in self.facts:
                events['m'] = {
                    'type': 'action',
                    'data': "show_map"
                }

        if not suppress_stats:
            if self.achievments:
                events['s'] = {
                    'type': 'action',
                    'data': 'show_stats'
                }

        return events

    # print user events message
    def print_user_events(self, events):
        self.logging("")
        self.logging("Ваши действия:")

        for key in sorted(events.keys()):
            event_data = events[key]['data']
            msg = event_data['message'] if 'message' in event_data else ''

            # dirty hack to implement messages for 'Turn back', 'Inventory', 'Map'
            if events[key]['type'] == 'transition' and event_data['level'] == self.previous_location \
                    and self.current_location != self.previous_location:
                msg = "Вернуться назад ({})".format(msg)

            if events[key]['type'] == 'action':
                if event_data == 'show_inventory':
                    msg = "Посмотреть инвентарь"
                elif event_data == 'show_map':
                    msg = "Посмотреть карту"
                elif event_data == 'show_stats':
                    msg = "Посмотреть статистику"

            self.logging("{}) {}".format(key, msg))

        # new line
        self.logging("")

    # make user's action
    def apply_action(self, action):
        if 'conditions' in action:
            if 'check_item' in action['conditions']:
                contain_all = True
                for item in action['conditions']['check_item']['items']:
                    if item not in self.items:
                        contain_all = False
                        break

                action = action['conditions']['check_item']['if_exists'] if contain_all else \
                    action['conditions']['check_item']['if_not_exists']
            elif 'checker' in action['conditions']:
                import gamedata.checkers as checkers

                checker_function = getattr(checkers, action['conditions']['checker'])
                action = action['conditions'].get('if_true') if checker_function(self.items, self.facts) \
                    else action['conditions'].get('if_false')

        description = action['description']
        self.logging(description)

        if 'actions' in action:
            if type(action["actions"]) == list:
                for chunk in action["actions"]:
                    if type(chunk) == tuple:
                        if chunk[0] == 'give_unique_item' and chunk[1]:
                            self.items.add(chunk[1])
                            if chunk[1] == "Flamethrower":
                                self.flamethrower_count = 1
                        elif chunk[0] == 'add_fact':
                            if type(chunk[1]) == list:
                                for fact in chunk[1]:
                                    self.facts.add(fact)
                            else:
                                self.facts.add(chunk[1])
                    elif type(chunk) is dict:
                        if chunk.get('decrease_flamethrower'):
                            self.flamethrower_count -= 1
                        elif chunk.get('increase_flamethrower'):
                            self.flamethrower_count += 1
            else:
                if action["actions"].get('show_map'):
                    self.show_map()
                if action["actions"].get('show_inventory'):
                    self.show_inventory()
                if action["actions"].get('show_stats'):
                    self.show_stats()
                if action["actions"].get('death'):
                    self.ending = action['actions'].get('ending')
                    self.result = GameResult.LOSE
                    return
                if action["actions"].get('win'):
                    self.ending = action['actions'].get('ending')
                    self.result = GameResult.WIN
                    return
                if action["actions"].get('decrease_flamethrower'):
                    self.flamethrower_count -= 1
                if action["actions"].get('increase_flamethrower'):
                    self.flamethrower_count += 1

        # action_chain - it is a scene, where we can't escape to locations until scene's ending

        events = []

        if 'events_chain' in action:
            events = self.define_user_events(actions=action['events'], suppress_inventory=True, suppress_map=True, suppress_stats=True)
        else:
            events = self.define_user_events(transitions=action['transitions'], suppress_inventory=True,
                                             suppress_map=True, suppress_stats=True) \
                if 'transitions' in action else self.current_events

        if not len(events):
            self.logging("!!! Something is wrong - events list for player is empty !!!")

        self.current_events = events
        self.print_user_events(events)

        self.result = GameResult.CONTINUE

    # take proper level description
    def apply_level_description(self, level_index, data):
        if level_index not in self.visited_locations:
            return data['description']
        else:
            return data['description_visited'] if 'description_visited' in data else data['description']

    # change level (state and text)
    def change_level(self, level_index):
        status = GameResult.CONTINUE

        # check existing of level
        if level_index not in game_data["levels"]:
            self.logging("Incorrect number of level!\n")
            self.result = GameResult.CONTINUE  # GameResult.ERROR
            return

        # update level history
        if self.current_location != level_index:
            self.previous_location = self.current_location
            self.current_location = level_index

        # check if some item is needed on start
        level = game_data["levels"][level_index]

        description = ""
        transitions = deepcopy(level['transitions']) if 'transitions' in level else []
        actions = deepcopy(level['actions']) if 'actions' in level else []

        # check conditions on level
        if 'conditions' in level:
            import gamedata.checkers as checkers
            for condition in level['conditions']:
                # we can apply only one condition (if there 2 of them)

                condition_data = {}

                if 'checker' in condition:
                    checker_function = getattr(checkers, condition['checker'])
                    condition_data = condition.get('if_true') if checker_function(self.items, self.facts) \
                        else condition.get('if_false')
                elif 'check_previous_location' in condition:
                    previous_location = condition['check_previous_location']
                    condition_data = condition.get('if_true') if self.previous_location == previous_location \
                        else condition.get('if_false')

                if condition_data:
                    description = self.apply_level_description(level_index, condition_data)

                    if 'actions' in condition_data:
                        for action in condition_data['actions']:
                            if action not in actions:
                                actions.append(action)

                    if 'transitions' in condition_data:
                        for transition in condition_data['transitions']:
                            if transition not in transitions:
                                transitions.append(transition)

        else:
            description = self.apply_level_description(level_index, level)

        self.logging(description)

        # need to print events only if game is running
        events = self.define_user_events(transitions=transitions, actions=actions)
        self.current_events = events
        self.print_user_events(events)

        # need to push location as visited
        self.visited_locations.add(level_index)

    def apply_user_input(self, user_input):
        action = self.current_action
        import gamedata.checkers as checkers

        checker_function = getattr(checkers, action['checker'])
        condition_data = action.get('if_true') if checker_function(user_input) else action.get('if_false')

        if condition_data:
            self.current_action = {}
            self.apply_user_event(choice=None, action={'type': 'action', 'data': condition_data})

    # apply user's event
    def apply_user_event(self, choice, action=None):
        if choice not in self.current_events and not action:
            self.logging("!!! Варианта ответа ({}) не существует в текущем варианте событий !!!".format(choice))
            self.result = GameResult.CONTINUE  # GameResult.ERROR
            return

        event = self.current_events[choice] if choice else action

        if event['type'] == 'transition':
            self.change_level(event['data']['level'])
        elif event['type'] == 'action':
            action = None

            if 'id' in event['data']:
                self.completed_actions.add(event['data']['id'])

                if event['data']['id'] not in game_data['actions']:
                    self.logging(
                        "!!! События ({}) (id={}) не существует в игровых данных !!!".format(choice,
                                                                                             event['data']['id']))
                    self.result = GameResult.CONTINUE  # GameResult.ERROR
                    return

                action = game_data['actions'][event['data']['id']]
            else:
                # check is it a map/inventory/stats call
                if event['data'] == 'show_inventory':
                    action = game_data['actions']['Inventory']
                elif event['data'] == 'show_map':
                    action = game_data['actions']['Map']
                elif event['data'] == 'show_stats':
                    action = game_data['actions']['Stats']
                else:
                    self.logging("Something wrong with action applying - no id and it is not an inventory/map/stats call! "
                                 "Data: {}".format(event))

                    self.result = GameResult.CONTINUE  # GameResult.ERROR
                    return

            # need to check if we need input from user (code, for example)
            if 'conditions' in action:
                self.current_action = action['conditions']
                if 'need_user_input' in action['conditions']:
                    self.logging(action['description'])
                    self.result = GameResult.NEED_INPUT
                    return

            self.apply_action(action)
