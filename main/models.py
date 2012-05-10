import string
import random
from datetime import datetime
from django.db import models

class Post(models.Model):
    ID_LENGTH = 5
    TITLE_LENGTH = 128

    id = models.CharField(max_length=ID_LENGTH, editable=False, primary_key=True)
    title = models.CharField(max_length=TITLE_LENGTH)
    text = models.TextField(blank=False)
    new = models.BooleanField(default=True)
    date_time = models.DateTimeField()

    def save(self, *args, **kw):
        if (not self.id):
            #generate a unique id
            alph_list = list(string.ascii_letters)
            not_unique = True
            while (not_unique):
                self.id = ''.join(random.sample(alph_list, self.ID_LENGTH))
                if len(Post.objects.filter(id=self.id)) == 0:
                    not_unique = False

            # set the time
            self.date_time = datetime.now()
        return models.Model.save(self, *args, **kw)

    def __unicode__(self):
        return "%s - %s" % (self.title, self.id)

