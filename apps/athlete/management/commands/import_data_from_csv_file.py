import os

from django.core.management.base import BaseCommand

from django.conf import settings

import pandas as pd

from apps.athlete.models import Athlete, Game, Sport, Medal, Event
from utils.methods.import_csv import import_csv


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

            import_csv(loc, num_lines=70)

            self.stdout.write(self.style.SUCCESS('Todos os dados foram importados com sucesso!'))

        except FileNotFoundError:
            print("O nome do arquivo não foi encontrado no diretório csv_data."
                            "Favor, verifique e tente novamente.")


