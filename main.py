import Ru_Venera as Ru_V
import random


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

    elif i == 2:
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
    elif i == 4:
        m2 = input(Ru_V.event_4).lower()
        if m2 == "да":
            print(Ru_V.event_401)
            return humans, eat, drink, research, sanitary
        if m2 == "нет":
            print(Ru_V.event_402)
            research -= research * 0.07
            return humans, eat, drink, research, sanitary
    elif i == 5:
        print(Ru_V.event_5)
        research += research * 0.15
        return humans, eat, drink, research, sanitary
    elif i == 6:
        m3 = input(Ru_V.event_6).lower()
        if m3 == "да":
            print(Ru_V.event_601)
            research += research * 0.1
            return humans, eat, drink, research, sanitary
        if m3 == "нет":
            print(Ru_V.event_602)
            sanitary -= sanitary * 0.7
            return humans, eat, drink, research, sanitary
    elif i == 7:
        m4 = input(Ru_V.event_7).lower()
        if m4 == "да":
            print(Ru_V.event_701)
            return humans, eat, drink, research, sanitary
        if m4 == "нет":
            print(Ru_V.event_702)
            humans = 0
            return humans, eat, drink, research, sanitary
    elif i == 8:
        print(Ru_V.event_8)
        drink += drink * 0.2
        return humans, eat, drink, research, sanitary
    elif i == 9:
        print(Ru_V.event_9)
        humans -= 6
        research -= research * 0.1
        return humans, eat, drink, research, sanitary
    elif i == 10:
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

    if c == 1:
        eat += eat*0.05
        drink -= drink * 0.001 * humans
        sanitary -= sanitary * 0.005 * humans
        research += research * 0.5 * humans * 0.1

    elif c == 2:
        drink += drink * 0.05
        eat -= eat * 0.001 * humans
        sanitary -= sanitary * 0.005 * humans
        research += research * 0.5 * humans * 0.1

    elif c == 3:
        sanitary += sanitary * 0.5
        eat -= eat * 0.001 * humans
        drink -= drink * 0.001 * humans
        research += research * 0.5 * humans * 0.1

    elif c == 4:
        research += research * humans * 0.1
        eat -= eat * 0.001 * humans
        drink -= drink * 0.001 * humans
        sanitary -= sanitary * 0.005 * humans
    else:
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
    
