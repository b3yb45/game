import Ru_Venera as Ru_V
from random import choice
from turtle import *


def daily(population, hunger, thirst, sanitary, research):
    hunger -= population
    thirst -= population
    sanitary -= population
    research += 0.5 * population

    print(Ru_V.daily)
    action = int(input('1 - выращивание еды, 2 - добыча воды, '
                       '3 - провести санобработку, 4 - провести исследование. '))

    if action == 1:
        hunger += 4 * population

    elif action == 2:
        thirst += 4 * population

    elif action == 3:
        sanitary += 4 * population

    else:
        research += 0.5 * population

    if hunger and thirst >= 70 and sanitary >= 55:
        population += 2

    elif hunger or thirst <= 50:
        population -= 1
        research -= research * 0.15

    elif sanitary <= 30:
        hunger -= hunger * 0.05
        thirst -= thirst * 0.05
        population -= 1

    return population, hunger, thirst, sanitary, research


def resource_check(hunger, thirst, sanitary, research):
    hunger = max(hunger, 0)
    hunger = min(hunger, 100)

    thirst = max(thirst, 0)
    thirst = min(thirst, 100)

    sanitary = max(sanitary, 0)
    sanitary = min(sanitary, 100)

    research = max(research, 0)

    return hunger, thirst, sanitary, research


def mars_event(i, population, hunger, thirst, sanitary, research):
    if i == 0:
        print('К счастью или сожалению, сегодня ничего интересного не произошло.')

        return population, hunger, thirst, sanitary, research

    elif i == 1:
        print('На поверхности защитного купола образовалась трещина, радиоактивный фон повышается.\n'
              "1 - отправить инженеров для ремонта и рискнуть их жизнями.\n"
              "2 - срочно заблокировать отсек вместе с людьми в нём.")

        var_1 = int(input())
        if var_1 == 1:
            print('Пробоина была успешно закрыта, однако несколько инженеров погибли из-за острой лучевой болезни.')
            population -= 2

        else:
            print('Отсек был заблокирован, все люди внутри погибли.')
            population -= 4

        return population, hunger, thirst, sanitary, research

    elif i == 2:
        print('Ваши исследователи обнаружили некое существо, сильно напоминающее лицехвата из "Чужого."\n'
              '1 - принести существо на базу.\n'
              '2 - оставить от греха подальше.')

        var_2 = int(input())
        if var_2 == 1:
            print('Кто бы мог подумать! Паразит начал бросаться на людей, отсек заблокировали вместе с людьми.')
            population -= 4

        else:
            print("Вы оставили существо там, где нашли и мирно ушли на базу. Ничего не произошло.")

        return population, hunger, thirst, sanitary, research

    elif i == 3:
        print('Исследователи обнаружили новый вид бактерий около небольшой пещеры.\n'
              '1 - взять небольшой образец и вернуться на базу.\n'
              '2 - заглянуть в пещеру в надежде собрать больше образцов.')

        var_3 = int(input())
        if var_3 == 1:
            print('Изучив новый вид бактерий вы немного продвинулись в исследовании. Жаль, что образец был невелик.')
            research += research * 0.05

        else:
            print('Этот вид бактерий оказался крайне полезным для вашего исследования. Вы значительно продвинулись.')
            research += research * 0.15

        return population, hunger, thirst, sanitary, research

    elif i == 4:
        print('От вентиляции исходит неприятный запах.\n'
              '1 - искать источник запаха.\n'
              '2 - не обращать внимние')

        var_4 = int(input())
        if var_4 == 1:
            print('Засорился фильтр, как это могли не заметить?')
            sanitary += sanitary * 0.1

        else:
            print('Судя по всему, то, от чего исходил запах, попало в один из источников воды.')
            sanitary -= sanitary * 0.05
            thirst -= thirst * 0.1

        return population, hunger, thirst, sanitary, research

    elif i == 5:
        print('Кажется, что жители базы заскучали.\n'
              '1 - потрататить немного еды и устроить вечеринку.\n'
              '2 - подарить им губозакатывательный аппарат.')

        var_5 = int(input())
        if var_5 == 1:
            print('После вечеринки астрологи объявили неделю шаловливых гормонов. На базе теперь больше жителей.')
            population += population * 0.1
            hunger -= hunger * 0.05
            sanitary -= sanitary * 0.02

        else:
            print('Жители продолжают скучать, зато еда расходуется благоразумно.')
            hunger += hunger * 0.02
            sanitary += sanitary * 0.02

        return population, hunger, thirst, sanitary, research

    elif i == 6:

        print('Исследователи обнаружили новое растения, для изучения его питательных свойств им нужен доброволец.\n'
              '1 - предоставить добровольца.\n'
              '2 - отказать.')

        var_6 = int(input())
        if var_6 == 1:
            print('Растение оказалось съедобным и довольно питательным, можно включить его в рацион')
            hunger += hunger * 0.1

        else:
            print('Говорят, что любопытной Варваре на базаре нос оторвали, но может таки стоило рискнуть?')

        return population, hunger, thirst, sanitary, research

    elif i == 7:
        print('К базе подбежал неизвестный пушистый зверёк, кажется он зовёт нас куда-то.\n'
              '1 - Отправить группу вслед.\n'
              '2 - Проигнорировать.')

        var_7 = int(input())
        if var_7 == 1:
            print('Мама зверёнка попала в яму, вы помогли ей выбраться. Они привели вас к своему.\n'
                  'Вы - настоящий исследователь, так что отдали приказ собрать марсианский навоз. Урожая стало больше.')
            hunger += hunger * 0.1

        else:
            print('У автора возникли вопросики к вашей человечности...')

        return population, hunger, thirst, sanitary, research

    elif i == 8:
        print('Появилась возможность запросить ресурсы у Земли.\n'
              '1 - запросить продовольствие.\n'
              '2 - запросить питьевую воду.\n'
              '3 - запросить робот - пылесос.\n'
              "4 - запросить исследовательское оборудование.")

        var_8 = int(input())
        if var_8 == 1:
            print('Продовольствие было доставлено на базу.')
            hunger += hunger * 0.1

        elif var_8 == 2:
            print('Запасы питьевой воды были доставлены на базу.')
            thirst += thirst * 0.1

        elif var_8 == 3:
            print('Несколько роботов - пылесосов были доставлены на базу.')
            sanitary += sanitary * 0.1

        else:
            print('Новое оборудование было доставлено на базу.')
            research += research * 0.1

        return population, hunger, thirst, sanitary, research

    elif i == 9:
        print('К вам подошёл один из учёных и сообщил, что для ускорение исследования нужно 5 подопытных людей.\n'
              '1 - согласиться.\n'
              '2 - отказать.')

        var_9 = int(input())
        if var_9 == 1:
            print('Вы пожертвовали 5 человек на благо науки. исследование продвинулось.')
            population -= 5
            research += research * 0.15

        else:
            print('Вы отказали учёному.')

        return population, hunger, thirst, sanitary, research


def moon_event(i, population, hunger, thirst, sanitary, research):
    if i == 0:
        print('К счастью или сожалению, сегодня ничего интересного не произошло.')

        return population, hunger, thirst, sanitary, research

    elif i == 1:
        print('На поверхности защитного купола образовалась трещина, радиоактивный фон повышается.\n'
              "1 - отправить инженеров для ремонта и рискнуть их жизнями.\n"
              "2 - срочно заблокировать отсек вместе с людьми в нём.")

        var_1 = int(input())
        if var_1 == 1:
            print('Пробоина была успешно закрыта, однако несколько инженеров погибли из-за острой лучевой болезни.')
            population -= 2

        else:
            print('Отсек был заблокирован, все люди внутри погибли.')
            population -= 4

        return population, hunger, thirst, sanitary, research

    elif i == 2:
        print('Ваши исследователи обнаружили некое существо, сильно напоминающее лицехвата из "Чужого."\n'
              '1 - принести существо на базу.\n'
              '2 - оставить от греха подальше.')

        var_2 = int(input())
        if var_2 == 1:
            print('Кто бы мог подумать! Паразит начал бросаться на людей, отсек заблокировали вместе с людьми.')
            population -= 4

        else:
            print("Вы оставили существо там, где нашли и мирно ушли на базу. Ничего не произошло.")

        return population, hunger, thirst, sanitary, research

    elif i == 3:
        print('Исследователи обнаружили новый вид бактерий около небольшой пещеры.\n'
              '1 - взять небольшой образец и вернуться на базу.\n'
              '2 - заглянуть в пещеру в надежде собрать больше образцов.')

        var_3 = int(input())
        if var_3 == 1:
            print('Изучив новый вид бактерий вы немного продвинулись в исследовании. Жаль, что образец был невелик.')
            research += research * 0.05

        else:
            print('Этот вид бактерий оказался крайне полезным для вашего исследования. Вы значительно продвинулись.')
            research += research * 0.15

        return population, hunger, thirst, sanitary, research

    elif i == 4:
        print('От вентиляции исходит неприятный запах.\n'
              '1 - искать источник запаха.\n'
              '2 - не обращать внимние')

        var_4 = int(input())
        if var_4 == 1:
            print('Засорился фильтр, как это могли не заметить?')
            sanitary += sanitary * 0.1

        else:
            print('Судя по всему, то, от чего исходил запах, попало в один из источников воды.')
            sanitary -= sanitary * 0.05
            thirst -= thirst * 0.1

        return population, hunger, thirst, sanitary, research

    elif i == 5:
        print('Вы обнаружили богатое месторождение гелия.\n'
              '1 - потратить часть запасов на исследование.\n'
              '2 - игнорировать.')

        var_5 = int(input())
        if var_5 == 1:
            print('Вам удалось добыть большое количество образцов для дальнейшего исследования и эксплуатации.')
            hunger -= hunger * 0.1
            thirst -= thirst * 0.1
            sanitary -= sanitary * 0.1
            research += 0.15

        else:
            print('Ничего не произошло.')

        return population, hunger, thirst, sanitary, research

    elif i == 6:
        print('Ученые предсказывают скорое усиление солнечного ветра.\n'
              '1 - потратить часть запасов на защитные меры.\n'
              '2 - игнорировать.')

        var_6 = int(input())
        if var_6 == 1:
            print('Благодаря предпринятым мерам никто не пострадал.')
            hunger -= hunger * 0.1
            thirst -= thirst * 0.1
            sanitary -= sanitary * 0.1

        else:
            print('Последствия ужасны. Часть персонала погибла, оборудование вышло из строя,'
                  ' еда и вода портятся из-за перебоев электричества.')
            population -= 5
            thirst -= thirst * 0.5
            sanitary -= sanitary * 0.3
            hunger -= hunger * 0.5
            research -= research * 0.2

        return population, hunger, thirst, sanitary, research

    elif i == 7:
        print('Вы улавливаете странный сигнал.\n'
              '1 - Исследовать.\n'
              '2 - Проигнорировать.')

        var_7 = int(input())
        if var_7 == 1:
            print('Отследив сигнал группа ученых спускается в пещеру. Там они обнаруживают старый луноход, '
                  'связь с котороым была потеряна. '
                  'За время своей автоматической работы он собрал большое количество образцов и данных. '
                  'Также, вы приводите его в рабочее состояние.')

            hunger -= hunger * 0.1
            thirst -= thirst * 0.1
            research += research * 0.15

        else:
            print('По какой-то причине ученые стали находить меньше образцов неподалеку от базы.')
            research -= research * 0.05

        return population, hunger, thirst, sanitary, research

    elif i == 8:
        print('Появилась возможность запросить ресурсы у Земли.\n'
              '1 - запросить продовольствие.\n'
              '2 - запросить питьевую воду.\n'
              '3 - запросить робот - пылесос.\n'
              "4 - запросить исследовательское оборудование.")

        var_8 = int(input())
        if var_8 == 1:
            print('Продовольствие было доставлено на базу.')
            hunger += hunger * 0.1

        elif var_8 == 2:
            print('Запасы питьевой воды были доставлены на базу.')
            thirst += thirst * 0.1

        elif var_8 == 3:
            print('Несколько роботов - пылесосов были доставлены на базу.')
            sanitary += sanitary * 0.1

        else:
            print('Новое оборудование было доставлено на базу.')
            research += research * 0.1

        return population, hunger, thirst, sanitary, research

    elif i == 9:
        print('К вам подошёл один из учёных и сообщил, что для ускорения исследования нужно 5 подопытных людей.\n'
              '1 - согласиться.\n'
              '2 - отказать.')

        var_9 = int(input())
        if var_9 == 1:
            print('Вы пожертвовали 5 человек на благо науки. исследование продвинулось.')
            population -= 5
            research += research * 0.15

        else:
            print('Вы отказали учёному.')

        return population, hunger, thirst, sanitary, research


def game_over():
    shape('turtle')
    bgcolor('black')
    pencolor('red')
    pensize(5)
    pu()
    goto(-240, 150)
    pd()
    fd(90)
    pu()
    goto(-240, 150)
    pd()
    rt(90)
    fd(150)
    lt(90)
    fd(100)
    lt(90)
    fd(80)
    lt(90)
    fd(60)
    pu()

    goto(-110, 150)
    pd()
    lt(90)
    fd(150)
    pu()
    goto(-110, 150)
    pd()
    lt(90)
    fd(100)
    rt(90)
    fd(60)
    rt(90)
    fd(100)
    pu()
    rt(180)
    fd(100)
    pd()
    rt(90)
    fd(90)
    pu()

    goto(20, 150)
    pd()
    fd(150)
    pu()
    goto(20, 150)
    pd()
    lt(35)
    fd(100)
    lt(115)
    fd(100)
    rt(150)
    fd(150)
    pu()

    goto(150, 155)
    pd()
    lt(90)
    fd(90)
    pu()
    goto(150, 155)
    pd()
    rt(90)
    fd(75)
    lt(90)
    fd(80)
    lt(180)
    fd(80)
    lt(90)
    fd(75)
    lt(90)
    fd(100)
    pu()

    pensize(4)

    goto(-220, -40)
    pd()
    rt(90)
    fd(120)
    lt(90)
    fd(60)
    lt(90)
    fd(120)
    lt(90)
    fd(60)
    pu()

    goto(-90, -40)
    pd()
    lt(105)
    fd(125)
    lt(150)
    fd(125)
    pu()

    goto(40, -40)
    pd()
    rt(75)
    fd(75)
    pu()
    goto(40, -40)
    pd()
    rt(90)
    fd(50)
    lt(90)
    fd(65)
    lt(180)
    fd(65)
    lt(90)
    fd(65)
    lt(90)
    fd(80)
    pu()

    goto(180, -40)
    pd()
    fd(50)
    rt(90)
    fd(50)
    rt(90)
    fd(50)
    pu()
    goto(180, -40)
    pd()
    lt(90)
    fd(120)
    lt(180)
    fd(70)
    rt(140)
    fd(80)
    done()


def sobitie(i, humans, eat, drink, sanitary, research):
    if i == 0:
        print(Ru_V.event_0)

        return humans, eat, drink, sanitary, research

    elif i == 1:
        print(Ru_V.event_1)

        research += research * 0.05
        eat += eat * 0.03
        drink += drink * 0.03

        return humans, eat, drink, sanitary, research

    elif i == 2:
        print(Ru_V.event_2)

        eat -= eat * 0.15
        drink -= drink * 0.20
        research -= research * 0.08
        sanitary -= sanitary * 0.1

        return humans, eat, drink, sanitary, research

    elif i == 3:
        m1 = input(Ru_V.event_3).lower()
        if m1 == "да":
            print(Ru_V.event_301)
            research += research * 0.25
            humans -= 2

            return humans, eat, drink, sanitary, research

        if m1 == "нет":
            return humans, eat, drink, sanitary, research

    elif i == 4:
        m2 = input(Ru_V.event_4).lower()

        if m2 == "да":
            print(Ru_V.event_401)
            return humans, eat, drink, sanitary, research

        if m2 == "нет":
            print(Ru_V.event_402)
            research -= research * 0.07

            return humans, eat, drink, sanitary, research

    elif i == 5:
        print(Ru_V.event_5)
        research += research * 0.15

        return humans, eat, drink, sanitary, research

    elif i == 6:
        m3 = input(Ru_V.event_6).lower()

        if m3 == "да":
            print(Ru_V.event_601)
            research += research * 0.15

            return humans, eat, drink, sanitary, research

        if m3 == "нет":
            print(Ru_V.event_602)
            sanitary -= sanitary * 0.25

            return humans, eat, drink, sanitary, research

    elif i == 7:
        m4 = input(Ru_V.event_7).lower()
        if m4 == "да":
            print(Ru_V.event_701)
            return humans, eat, drink, sanitary, research

        if m4 == "нет":
            print(Ru_V.event_702)
            humans = 0

            return humans, eat, drink, sanitary, research

    elif i == 8:
        print(Ru_V.event_8)
        drink += drink * 0.2

        return humans, eat, drink, sanitary, research

    elif i == 9:
        print(Ru_V.event_9)
        humans -= 3
        research -= research * 0.1

        return humans, eat, drink, sanitary, research

    elif i == 10:
        m5 = input(Ru_V.event_10).lower()
        if m5 == "да":
            print(Ru_V.event_101)
            research -= research * 0.3

            return humans, eat, drink, sanitary, research

        if m5 == "нет":
            print(Ru_V.event_101)
            return humans, eat, drink, sanitary, research


day = 0

moon_flag = True
mars_flag = True
venus_flag = True

moon_population = 10
mars_population = 10
venus_population = 10

moon_hunger = 70
mars_hunger = 70
venus_hunger = 70

moon_thirst = 70
mars_thirst = 70
venus_thirst = 70

moon_sanitary = 70
mars_sanitary = 70
venus_sanitary = 70

moon_research = 1
mars_research = 1
venus_research = 1

moon_var = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
mars_var = moon_var
venus_var = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(Ru_V.greeting)
print('')

venus = input('Имена исследователей Венеры: ')
print(venus+','+' добро пожаловать на исследовательскую станцию Венеры!')

mars = input('Имена исследователей Марса: ')
print(mars+','+' добро пожаловать на исследовательскую станцию Марса!')

moon = input('Имена исследователей Луны: ')
print(moon+','+' добро пожаловать на исследовательскую станцию Луны!')

while moon_flag or mars_flag or venus_flag:
    if not moon_flag and not mars_flag and not venus_flag:
        print('Все игроки проиграли. Игра окончена.')
        game_over()
        break

    day += 1
    print(Ru_V.unit_day, day)
    print('')

    # Ход Луны
    if (moon_population > 0 or moon_research < 100) and moon_flag:
        print(f'{moon}, Ваш ход!')
        print(f'Игрок {moon}, на лунной базе на данный момент:')
        print(round(moon_population), Ru_V.unit_humans)
        print(round(moon_hunger), Ru_V.unit_eat)
        print(round(moon_thirst), Ru_V.unit_drink)
        print(round(moon_sanitary), Ru_V.unit_sanitary)
        print(round(moon_research), Ru_V.unit_research)
        print('')

        moon_population, moon_hunger, moon_thirst, moon_sanitary, moon_research = \
            daily(moon_population, moon_hunger, moon_thirst, moon_sanitary, moon_research)

        if len(moon_var) >= 1:
            moon_c = choice(moon_var)
            moon_var.remove(moon_c)
            moon_population, moon_hunger, moon_thirst, moon_sanitary, moon_research = \
                moon_event(moon_c, moon_population, moon_hunger, moon_thirst, moon_sanitary, moon_research)

        else:
            moon_var = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            moon_c = choice(moon_var)
            moon_var.remove(moon_c)
            moon_population, moon_hunger, moon_thirst, moon_sanitary, moon_research = \
                moon_event(moon_c, moon_population, moon_hunger, moon_thirst, moon_sanitary, moon_research)

        moon_hunger, moon_thirst, moon_sanitary, moon_research = \
            resource_check(moon_hunger, moon_thirst, moon_sanitary, moon_research)

        print('')

    elif moon_population <= 0:
        moon_flag = False
        print(f'{moon}, ', Ru_V.game_over)
        print('')

    elif moon_research >= 100:
        moon_flag = False
        print(f'{moon}, ', Ru_V.victory)
        print('')

    # Ход Венеры
    if (venus_population > 0 or venus_research < 100) and venus_flag:
        print(f'{venus}, Ваш ход!')
        print(f'Игрок {venus}, на базе Венеры на данный момент:')
        print(round(venus_population), Ru_V.unit_humans)
        print(round(venus_hunger), Ru_V.unit_eat)
        print(round(venus_thirst), Ru_V.unit_drink)
        print(round(venus_sanitary), Ru_V.unit_sanitary)
        print(round(venus_research), Ru_V.unit_research)
        print('')

        venus_population, venus_hunger, venus_thirst, venus_sanitary, venus_research = \
            daily(venus_population, venus_hunger, venus_thirst, venus_sanitary, venus_research)

        if len(venus_var) >= 1:
            venus_c = choice(venus_var)
            venus_var.remove(venus_c)
            venus_population, venus_hunger, venus_thirst, venus_sanitary, venus_research = \
                sobitie(venus_c, venus_population, venus_hunger, venus_thirst, venus_sanitary, venus_research)

        else:
            venus_var = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            venus_c = choice(venus_var)
            venus_var.remove(venus_c)
            venus_population, venus_hunger, venus_thirst, venus_sanitary, venus_research = \
                sobitie(venus_c, venus_population, venus_hunger, venus_thirst, venus_sanitary, venus_research)

        venus_hunger, venus_thirst, venus_sanitary, venus_research = \
            resource_check(venus_hunger, venus_thirst, venus_sanitary, venus_research)

        print('')

    elif venus_population <= 0:
        venus_flag = False
        print(f'{venus}, ', Ru_V.game_over)
        print('')

    elif venus_research >= 100:
        venus_flag = False
        print(f'{venus}, ', Ru_V.victory)
        print('')

    # Ход Марса
    if (mars_population > 0 or mars_research < 100) and mars_flag:
        print(f'{mars}, Ваш ход!')
        print(f'Игрок {mars}, на марсианской базе на данный момент:')
        print(round(mars_population), Ru_V.unit_humans)
        print(round(mars_hunger), Ru_V.unit_eat)
        print(round(mars_thirst), Ru_V.unit_drink)
        print(round(mars_sanitary), Ru_V.unit_sanitary)
        print(round(mars_research), Ru_V.unit_research)
        print('')

        mars_population, mars_hunger, mars_thirst, mars_sanitary, mars_research = \
            daily(mars_population, mars_hunger, mars_thirst, mars_sanitary, mars_research)

        if len(mars_var) >= 1:
            mars_c = choice(mars_var)
            mars_var.remove(mars_c)
            mars_population, mars_hunger, mars_thirst, mars_sanitary, mars_research = \
                mars_event(mars_c, mars_population, mars_hunger, mars_thirst, mars_sanitary, mars_research)

        else:
            mars_var = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            mars_c = choice(mars_var)
            mars_var.remove(mars_c)
            mars_population, mars_hunger, mars_thirst, mars_sanitary, mars_research = \
                mars_event(mars_c, mars_population, mars_hunger, mars_thirst, mars_sanitary, mars_research)

        mars_hunger, mars_thirst, mars_sanitary, mars_research = \
            resource_check(mars_hunger, mars_thirst, mars_sanitary, mars_research)

        print('')

    elif mars_population <= 0:
        mars_flag = False
        print(f'{mars}, ', Ru_V.game_over)
        print('')

    elif mars_research >= 100:
        mars_flag = False
        print(f'{mars}, ', Ru_V.victory)
        print('')
