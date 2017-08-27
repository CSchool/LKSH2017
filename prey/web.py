import pickle

from flask import Flask, send_from_directory, redirect, request

from encryption import AESCipher, enc_key
from game import Game, GameResult

app = Flask(__name__)


@app.route("/game/<path:path>")
def send_static(path):
    return send_from_directory('resources', path)


@app.route("/")
def index():
    return redirect("/game/index.html")


@app.route("/server", methods=['POST'])
def serve():
    sess = request.values.get('sess')
    if not (type(sess) is str):
        return "Invalid parameter: sess", 400
    ach = request.values.get('achievments');
    if not (type(ach) is str):
        return "Invalid parameter: achievments", 400
    cipher = AESCipher(enc_key)
    new = False
    if ach == "":
        achievments = set()
    else:
        decr = cipher.decrypt(ach)
        if not decr:
            return "Invalid parameter: achievments", 400
        achievments = pickle.loads(decr)
    if sess == "":
        session = {
            "current_location": "",
            "previous_location": "",
            "visited_locations": set(),  # index
            "completed_actions": set(),  # index
            "items": set(),
            'current_events': {},
            'current_action': {},
            "log": "",
            "log_here": True,
            "started": False,
            "facts": set(),
            "flamethrower_count": 0,
            "ending": 0,
            "result": GameResult.CONTINUE
        }
        new = True
    else:
        decr = cipher.decrypt(sess)
        if not decr:
            return "Invalid parameter: sess", 400
        session = pickle.loads(decr)
    session['log'] = ''
    game = Game(True)
    game.achievments = achievments
    game.started = session['started']
    for key in session:
        setattr(game, key, session[key])

    inp = request.values.get('input')
    if not (type(inp) is str):
        return "Invalid parameter: input", 400
    if inp == "unload":
        return "", 200
    inp = inp.strip()
    if inp == "" and session['started']:
        return "> ", 200
    try:
        width = int(request.values.get('width'))
    except:
        width = 100
    game._drawer.set_term_width(width)
    if new:
        game.draw_logo()
        game.write_intro()
        game._drawer.log += "\n\nНажмите ENTER для продолжения..."
    elif game.started:
        if game.get_result() == GameResult.CONTINUE:
            game.apply_user_event(inp)
        elif game.get_result() == GameResult.NEED_INPUT:
            game.apply_user_input(inp)
        if game.get_result() == GameResult.WIN:
            game.logging("")
            game.logging("Поздравляем, Вы прошли игру и выжили!")
            game.logging("")
            game.logging("Концовка {} из {}".format(game.ending, game.total_endings))
            game.logging("")
            game._drawer.log = "\\cmd::quit" + game._drawer.log
            do_award = ("Ending_%d" % game.ending) not in game.achievments
            game.achievments.add("Ending_%d" % game.ending)
            if do_award:
                game.award_achievments("Ending_%d" % game.ending)
        elif game.get_result() == GameResult.LOSE:
            game.logging("")
            game.logging("К сожалению, Вы проиграли!")
            game.logging("")
            game.logging("Концовка {} из {}".format(game.ending, game.total_endings))
            game.logging("")
            game._drawer.log = "\\cmd::quit" + game._drawer.log
            do_award = ("Ending_%d" % game.ending) not in game.achievments
            game.achievments.add("Ending_%d" % game.ending)
            if do_award:
                game.award_achievments("Ending_%d" % game.ending)
        else:
            game.award_achievments()
            game._drawer.log += "> "
        game.award_achievments()
    else:
        game.start_game()
        game._drawer.log += "> "
        game.started = True
        session['started'] = True
    log = game._drawer.log
    for key in session:
        if hasattr(game, key):
            session[key] = getattr(game, key)
    del session['log']
    ret = cipher.encrypt(pickle.dumps(session))
    ach = cipher.encrypt(pickle.dumps(game.achievments))
    return ret + "~~SEPARATOR~~" + ach + "~~SEPARATOR~~" + log


if __name__ == "__main__":
    app.run()
