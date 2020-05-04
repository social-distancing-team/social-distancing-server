from fireo.models import Model
from fireo.fields import TextField

# Create your models here.
class User(Model):
    username = TextField()

    class Meta:
        collection_name = 'users'

    def __str__(self):
        return self.username
