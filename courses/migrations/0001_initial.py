drom django.db import migrations, models
class Migrations(migrations.Migration):
	initial = True
	dependencies = [
	]
	operations = [
	]
	operations = [
	    migrations.CreateModel(
	    	name='Course',
	    	fields=[
	    	    ('id', models.AutoField(auto_created=True,primary_key=True)),
	    	    ('image', models.ImageField(upload_to'images/')),
,	    	    ('summary', models.CharField(max_length=200)),
	    	],
	    ),
	]
	models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)