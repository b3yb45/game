import Ru_Venera as Ru_V
import random
from random import choice
from turtle import *

population = 20
hunger = 100
thirst = 100
sanitary = 100
research = 1
day = 0
var = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

mars = input('Имена исследователей Марса: ')
print(mars+','+' добро пожаловать на исследовательскую станцию Марса!')


def event(i, population, hunger, thirst, sanitary, research):
    if i == 0:
        var.remove(0)
        print('К счастью или сожалению, сегодня ничего интересного не произошло.')
        return population, hunger, thirst, sanitary, research
    elif i == 1:
        var.remove(1)
        print('На поверхности защитного купола образовалась трещина, радиоактивный фон повышается.\n'
              "1 - отправить инженеров для ремонта и рискнуть их жизнями.\n"
              "2 - срочно заблокировать отсек вместе с людьми в нём.")
        var_1 = int(input())
        if var_1 == 1:
            print('Пробоина была успешно закрыта, однако несколько инженеров погибли из-за острой лучевой болезни.')
            population -= 5
        else:
            print('Отсек был заблокирован, все люди внутри погибли.')
            population -= 10
        return population, hunger, thirst, sanitary, research
    elif i == 2:
        var.remove(2)
        print('Ваши исследователи обнаружили некое существо, сильно напоминающее лицехвата из "Чужого."\n'
              '1 - принести существо на базу.\n'
              '2 - оставить от греха подальше.')
        var_2 = int(input())
        if var_2 == 1:
            print('Кто бы мог подумать! Паразит начал бросаться на людей, отсек заблокировали вместе с людьми.')
            population -= 10
        else:
            print("Вы оставили существо там, где нашли и мирно ушли на базу. Ничего не произошло.")
        return population, hunger, thirst, sanitary, research
    elif i == 3:
        var.remove(3)
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
        var.remove(4)
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
        var.remove(5)
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
        var.remove(6)
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
        var.remove(7)
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
        var.remove(8)
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
        var.remove(9)
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


while population > 0 or research < 100:
    day += 1
    print('День', day)
    action = int(input('1 - выращивание еды, 2 - добыча воды, \n'
                       '3 - провести санобработку, 4 - провести исследование.'))
    if action == 1:
        hunger += hunger * 0.01 * population
        thirst -= thirst * 0.002 * population
        sanitary -= sanitary * 0.005 * population
        research += research * 0.4
    elif action == 2:
        hunger -= hunger * 0.003 * population
        thirst += thirst * 0.01 * population
        sanitary -= sanitary * 0.004 * population
        research += research * 0.5
    elif action == 3:
        hunger -= hunger * 0.003 * population
        thirst -= thirst * 0.004 * population
        sanitary += sanitary * 0.02 * population
        research += research * 0.05
    else:
        hunger -= hunger * 0.003 * population
        thirst -= thirst * 0.004 * population
        sanitary -= sanitary * 0.003 * population
        research += research

    if len(var) >= 1:
        c = choice(var)
        population, hunger, thirst, sanitary, research = event(c, population, hunger, thirst, sanitary, research)
    else:
        var = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        c = choice(var)
        population, hunger, thirst, sanitary, research = event(c, population, hunger, thirst, sanitary, research)

    if population <= 0:
        print('Вы не справились с миссией.')
        game_over()
        break
    elif research >= 100:
        print('Вы успешно завершили миссию!')
        break
    elif hunger > 100:
        hunger = 100
    elif hunger < 0:
        hunger = 0
    elif thirst > 100:
        thirst = 100
    elif thirst < 0:
        thirst = 0
    elif sanitary > 100:
        sanitary = 100
    elif sanitary < 0:
        sanitary = 0
    elif research < 0:
        research = 0
    elif hunger >= 70 and thirst >= 70 and sanitary >= 55:
        population += 2
        research += research * 0.005
    elif hunger <= 50 or thirst <= 50:
        population -= 5
        research -= research * 0.005
    elif sanitary <= 30:
        hunger -= hunger * 0.05
        thirst -= thirst * 0.05
        population -= 5
    print(round(population), 'людей на базе.')
    print(round(hunger), '- уровень голода.')
    print(round(thirst), '- уровень жажды.')
    print(round(sanitary), '- уровень чистоты.')
    print(round(research), '- прогресс исследования.')


print(Ru_V.greeting)

humans = 10
eat = 100
drink = 100
research = 1
sanitary = 100
day = 0

venus_events = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sobitie(i, humans, eat, drink, research, sanitary):
    if i == 0:
        print(Ru_V.event_0)

        return humans, eat, drink, research, sanitary

    elif i == 1:
        print(Ru_V.event_1)

        research += research * 0.05
        eat += eat * 0.03
        drink += drink * 0.03

        return humans, eat, drink, research, sanitary

    if i == 2:
        print(Ru_V.event_2)

        eat -= eat * 0.15
        drink -= drink * 0.20
        research -= research * 0.08
        sanitary -= sanitary * 0.1

        return humans, eat, drink, research, sanitary

    elif i == 3:
        m1 = input(Ru_V.event_3).lower()
        if m1 == "да":
            print(Ru_V.event_301)
            research += research * 0.25
            humans -= 3
            return humans, eat, drink, research, sanitary
        if m1 == "нет":
            return humans, eat, drink, research, sanitary
    if i == 4:
        m2 = input(Ru_V.event_4).lower()
        if m2 == "да":
            print(Ru_V.event_401)
            return humans, eat, drink, research, sanitary
        if m2 == "нет":
            print(Ru_V.event_402)
            research -= research * 0.07
            return humans, eat, drink, research, sanitary
    if i == 5:
        print(Ru_V.event_5)
        research += research * 0.15
        return humans, eat, drink, research, sanitary
    if i == 6:
        m3 = input(Ru_V.event_6).lower()
        if m3 == "да":
            print(Ru_V.event_601)
            research += research * 0.1
            return humans, eat, drink, research, sanitary
        if m3 == "нет":
            print(Ru_V.event_602)
            sanitary -= sanitary * 0.7
            return humans, eat, drink, research, sanitary
    if i == 7:
        m4 = input(Ru_V.event_7).lower()
        if m4 == "да":
            print(Ru_V.event_701)
            return humans, eat, drink, research, sanitary
        if m4 == "нет":
            print(Ru_V.event_702)
            humans = 0
            return humans, eat, drink, research, sanitary
    if i == 8:
        print(Ru_V.event_8)
        drink += drink * 0.2
        return humans, eat, drink, research, sanitary
    if i == 9:
        print(Ru_V.event_9)
        humans -= 6
        research -= research * 0.1
        return humans, eat, drink, research, sanitary
    if i == 10:
        m5 = input(Ru_V.event_10).lower()
        if m5 == "да":
            print(Ru_V.event_101)
            research -= research * 0.9
            return humans, eat, drink, research, sanitary
        if m5 == "нет":
            print(Ru_V.event_101)
            return humans, eat, drink, research, sanitary


while humans != 0:
    day += 1
    print(Ru_V.unit_day, day)
    c = input(Ru_V.daily).lower()

    if c == "садоводство":
        eat += eat*0.05
        drink -= drink * 0.001 * humans
        sanitary -= sanitary * 0.005 * humans
        research += research * 0.5 * humans * 0.1

    elif c == "добыча воды":
        drink += drink * 0.05
        eat -= eat * 0.001 * humans
        sanitary -= sanitary * 0.005 * humans
        research += research * 0.5 * humans * 0.1

    elif c == "уборка":
        sanitary += sanitary * 0.5
        eat -= eat * 0.001 * humans
        drink -= drink * 0.001 * humans
        research += research * 0.5 * humans * 0.1

    elif c == "изучение":
        research += research * humans * 0.1
        eat -= eat * 0.001 * humans
        drink -= drink * 0.001 * humans
        sanitary -= sanitary * 0.005 * humans

    event_number = random.choice(venus_events)
    humans, eat, drink, research, sanitary = sobitie(event_number, humans, eat, drink, research, sanitary)

    if humans == 0:
        print(Ru_V.game_over)
        break

    if eat > 100:
        eat = 100

    if drink > 100:
        drink = 100

    if sanitary > 100:
        sanitary = 100

    if eat >= 70 and drink >= 70 and sanitary >= 55:
        humans += 1

    if eat <= 30 and drink <= 30:
        research -= research * 0.005

    if sanitary <= 30:
        eat -= eat * 0.005
        drink -= drink * 0.005

    if research >= 100:
        print(Ru_V.victory)
        break

    print(round(humans), Ru_V.unit_humans)
    print(round(eat), Ru_V.unit_eat)
    print(round(drink), Ru_V.unit_drink)
    print(round(research), Ru_V.unit_research)
    print(round(sanitary), Ru_V.unit_sanitary)
    
