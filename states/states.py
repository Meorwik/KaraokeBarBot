from aiogram.dispatcher.filters.state import State, StatesGroup

class StatesGroup(StatesGroup):
    stateInMainMenu = State()
    stateInBookingMenu = State()
    stateInEatingMenu = State()
    stateInReviewsMenu = State()
    