#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game import Game, GameResult


def get_user_request():
    try:
        res = ""
        while res == "":
            res = input("> ").strip()
        return res
    except:
        exit(5)


if __name__ == '__main__':
    game = Game()

    game.draw_logo()
    game.write_intro()

    print()
    input("Нажмите ENTER для продолжения...")
    print()
    print()

    game.start_game()

    while True:
        status = game.get_result()
        if status == GameResult.CONTINUE:
            user_request = get_user_request()
            if user_request.lower() in ['exit', 'quit']:
                exit(0)
            game.apply_user_event(user_request)
        elif status == GameResult.WIN:
            game.logging("")
            game.logging("Поздравляем, Вы прошли игру и выжили!")
            game.logging("")
            game.logging("Концовка {} из {}".format(game.get_ending(), Game.total_endings))
            game.logging("")
            input("Нажмите ENTER для выхода из игры...")
            exit(0)
        elif status == GameResult.LOSE:
            game.logging("")
            game.logging("К сожалению, Вы проиграли!")
            game.logging("")
            game.logging("Концовка {} из {}".format(game.get_ending(), Game.total_endings))
            game.logging("")
            input("Нажмите ENTER для выхода из игры...")
            exit(0)
        elif status == GameResult.NEED_INPUT:
            user_request = get_user_request()
            game.apply_user_input(user_request)