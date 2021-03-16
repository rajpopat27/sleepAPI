# sleepAPI
Sleep API
This is the solution for the assignment for the aleep APP
THe API is built using Django and the frontend is deployed at [Login](#http://sleepapi.anaws14.ml:8000/sleep/login/)
The API endpoints are 
1: /sleep/login
The endpoint is used to authenticate the users
IF the users are not authenticated they are redirected to the signup page

2: /sleep/signup
It allows the user to signup
If the fields are proper it creates a user entry in the data base
Otherwise it gives an error

3: /sleep/info
It is used to collect the sleep information for a particular user and store it in database
If the user is not authenticated it redirects them to login screen

4: /sleep/error
It is the default error page if any error is to be displayed

5: /sleep/success
It si the success page that userr sees after a successfull entry in the database

The database schema is as follows
1.User table 
Default DJango user table with userID .email and password to authenticate the user
3.SleepCycle Table
class SleepCycleModel(models.Model):

    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE,null=True)
    sleepStruggle = models.IntegerField(null=True)
    sleepTime = models.IntegerField(null=True)
    wakeUpTime = models.IntegerField(null=True)
    sleepHours = models.IntegerField(null=True)
the userID is a foreign key for the authentication user table
the other four fields are 
Sleep Struggle time
Wakeup time
Sleep Time
Sleep Hours
