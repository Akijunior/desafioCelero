import ast
import csv
import os

from django.core.management.base import BaseCommand

from django.conf import settings

import numpy as np
import pandas as pd

from apps.athlete.models import Athlete, Game, Sport, Medal, Event


class Command(BaseCommand):
    help = 'Comando para importar dados sobre atletas e jogos de arquivos CSV ' \
           'para povoar as tabelas do banco.'

    def handle(self, *args, **options):
        self.import_data_from_csv_file()

    def import_data_from_csv_file(self):
        loc = os.path.join(settings.CSV_ROOT, "athlete_events.csv")

        df_athletes = pd.read_csv(loc, nrows=20)
        df_athletes = df_athletes.fillna(0)

        print(df_athletes['Name'].nunique())
        print(df_athletes['Games'].nunique())
        print(df_athletes['Sport'].nunique())
        print(df_athletes['Event'].nunique())

        print("\n")


        for index, row in df_athletes.iterrows():
            athlete, created = Athlete.objects.get_or_create(athlete_id=int(row['ID']),
                                                             defaults={'name': row['Name'], 'sex': row['Sex'],
                                                                       'age': row['Age'], 'height': row['Height'],
                                                                       'weight': row['Weight'],
                                                                       'team': row['Team'], 'noc': row['NOC']})
            game, created = Game.objects.get_or_create(game_name=row['Games'],
                                                       defaults={'year': row['Year'],
                                                                 'season': row['Season'],
                                                                 'city': row['City'],
                                                                 })
            sport, created = Sport.objects.get_or_create(sport=row['Sport'])
            event, created = Event.objects.get_or_create(event=row['Event'],
                                                         defaults={'sport': sport})
            medal = Medal.objects.create(athlete=athlete,
                                         event=event,
                                         medal=row['Medal']
                                         )

        print(Athlete.objects.count())
        print(Game.objects.count())
        print(Sport.objects.count())
        print(Event.objects.count())
        print(Medal.objects.count())

        self.stdout.write(self.style.SUCCESS('Todos os dados foram importados com sucesso!'))
