from functions import args_params, detect_action


def main():
    '''
    Используйте команду "python3 main.py -h" Для вывода сообщения с описанием работы программы
    '''
    arg_parse = args_params()
    detect_action(arg_parse)


if __name__ == "__main__":
    main()
