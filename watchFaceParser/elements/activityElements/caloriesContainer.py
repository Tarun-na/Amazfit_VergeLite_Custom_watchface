from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.analogDialFaceElements.clockHand import ClockHand 

class CaloriesContainer:
    definitions = {
        1: { 'Name': 'Circle', 'Type': CircleScale},
        3: { 'Name': 'ClockHand', 'Type': ClockHand},
    }
