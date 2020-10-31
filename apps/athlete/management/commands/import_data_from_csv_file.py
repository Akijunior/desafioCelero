import os

from django.core.management.base import BaseCommand

from django.conf import settings

import pandas as pd

from apps.athlete.models import Athlete, Game, Sport, Medal, Event


class Command(BaseCommand):
    help = 'Comando para importar dados sobre atletas e jogos de arquivos CSV ' \
           'para povoar as tabelas do banco.' \
           'Para fazer a importação diretamente pelo django, deve-se antes certificar ' \
           'de que o arquivo CSV desejado para importar se encontra dentro da pasta' \
           'csv_data em apps. Feito isso, chama-se o comando passando ao final o nome do ' \
           'arquivo de importação sem a extensão ".csv" ao final e, caso o arquivo atenta ao ' \
           'padrão do athlete_events da Kagle a importação seguirá com êxito.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_name', type=str)

    def handle(self, *args, **options):
        self.import_data_from_csv_file(**options)

    def import_data_from_csv_file(self, *args, **options):

        try:

            loc = os.path.join(settings.CSV_ROOT, options['csv_file_name'] + ".csv")

            df_athletes = pd.read_csv(loc)
            df_athletes = df_athletes.fillna(0)

            for index, row in df_athletes.iterrows():

                athlete, created = Athlete.objects.get_or_create(
                    athlete_id=int(row['ID']),
                    defaults={
                        'name': row['Name'],
                        'sex': row['Sex'],
                        'age': row['Age'],
                        'height': row['Height'],
                        'weight': row['Weight'],
                        'team': row['Team'],
                        'noc': row['NOC']
                    })

                sport, created = Sport.objects.get_or_create(
                    sport=row['Sport'])

                game, created = Game.objects.get_or_create(
                    game_name=row['Games'],
                    defaults={
                        'year': row['Year'],
                        'season': row['Season'],
                        'city': row['City'],
                    })

                game.sports.add(sport)

                event, created = Event.objects.get_or_create(
                    event=row['Event'],
                    defaults={'sport': sport}
                )

                medal = Medal.objects.create(
                    athlete=athlete,
                    event=event,
                    medal=row['Medal']
                )

                self.stdout.write(self.style.SUCCESS('Todos os dados foram importados com sucesso!'))

        except FileNotFoundError:
            print("O nome do arquivo não foi encontrado no diretório csv_data."
                            "Favor, verifique e tente novamente.")


