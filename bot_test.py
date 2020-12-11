from bot import Bot
from nose.tools import istest, eq_


@istest
def new_bot_should_have_final_state():
    bot = Bot(1)
    eq_(True, bot.in_final_state())

@istest
def bot_should_be_in_accept_in_action_transition():
    bot = Bot(1)
    bot.change_state('010') #de reposo a en acción
    bot.change_state('001') #de en acción a en reposo
    eq_(True, bot.in_final_state())
    eq_(0, bot.get_state())

@istest
def bot_should_be_in_final_state():
    bot = Bot(1)
    bot.change_state('011') #de reposo a calculando
    bot.change_state('100') #de calculando a en movimiento
    bot.change_state('101') #de en movimiento a interactuando
    bot.change_state('110') #de interactuando a regresando
    bot.change_state('001') #de regresando a en reposo
    eq_(True, bot.in_final_state())
    eq_(0, bot.get_state())

@istest
def bot_sould_not_accept_state():
    bot = Bot(1)
    bot.change_state('010')
    bot.change_state('101')
    eq_(1, bot.get_state())