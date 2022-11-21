from aiogram.dispatcher.filters.state import State, StatesGroup

class StatesGroup(StatesGroup):
    stateInMainMenu = State()
    stateInBookingMenu = State()
    stateInReviewsMenu = State()
    stateInBarAndKitchengMenu = State()
    steteInOpenMenu = State()
