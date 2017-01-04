import pickle

#define class
class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'

summer = Bird()

picklestring = pickle.dumps(summer)

print(picklestring)

print('--------------------')

fn = 'a.pkl'
with open(fn, 'w') as f:
    picklestring = pickle.dump(summer, f)

print('----------------------')


with open(fn, 'r') as f:
    summer = pickle.load(f)


