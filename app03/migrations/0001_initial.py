# Generated by Django 2.2.7 on 2019-11-28 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='authordetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ahobby', models.CharField(default='dog', max_length=32, null=True)),
                ('alocation', models.CharField(default='Canada', max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='authorinfo',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('aname', models.CharField(max_length=32)),
                ('aage', models.IntegerField(default=20, null=True)),
                ('aphone', models.CharField(max_length=32, null=True)),
                ('adetails', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app03.authordetails')),
            ],
        ),
        migrations.CreateModel(
            name='publishinfo',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='bookinfo',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('bname', models.CharField(max_length=32)),
                ('bprice', models.DecimalField(decimal_places=2, default=16.99, max_digits=6)),
                ('binventory', models.IntegerField(default=100)),
                ('bsalesvolume', models.IntegerField(default=0)),
                ('book_pubish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app03.publishinfo')),
            ],
        ),
        migrations.CreateModel(
            name='authors_books',
            fields=[
                ('abid', models.AutoField(primary_key=True, serialize=False)),
                ('authorsid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app03.authorinfo')),
                ('booksid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app03.bookinfo')),
            ],
            options={
                'unique_together': {('authorsid', 'booksid')},
            },
        ),
        migrations.AddField(
            model_name='authorinfo',
            name='boos',
            field=models.ManyToManyField(through='app03.authors_books', to='app03.bookinfo'),
        ),
    ]
