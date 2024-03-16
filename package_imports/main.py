import common
import common.validators as validators
import common.models as models
# from common.models import *

validators.is_boolean('true')
validators.is_numeric(10)
validators.is_date('2018-01-01')
validators.is_json('{}')

john_post = models.Post()
john_posts = models.Posts()
john = models.User()

print('\n\n****** self ******')
for k in dict(globals()).keys():
    print(k)
    
print('\n\n ****** common ******')
for k in common.__dict__.keys():
    print(k)
    
print('\n\n ****** models ******')
for k in common.models.__dict__.keys():
    print(k)

