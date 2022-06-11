from django.db import models

# Create your models here.



class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)


# ~ member1 = Members(firstname='Tobias', lastname='Refsnes')
# ~ member2 = Members(firstname='Linus', lastname='Refsnes')
# ~ member3 = Members(firstname='Lene', lastname='Refsnes')
# ~ member4 = Members(firstname='Stale', lastname='Refsnes')
# ~ members_list = [member1, member2, member3, member4]
# ~ for x in members_list:
	# ~ x.save()
