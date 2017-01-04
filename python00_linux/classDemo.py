class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self, dx, dy):
        position = [0, 0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position

summer = Bird()

print summer.way_of_reproduction
print 'after move:', summer.move(5, 8)

print '**************************************'

class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True

class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False

summer = Chicken()
print summer.have_feather
print summer.move(5, 8)

print '**************__init__()****************'
class happyBird(Bird):
    def __init__(self, more_words):
        print 'We are happy birds.', more_words

summer = happyBird('Happy, Happy!')

