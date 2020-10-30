from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Comando para importar dados sobre atletas e jogos de arquivos CSV ' \
           'para povoar as tabelas do banco.'

    def handle(self, *args, **options):

        self.import_data_from_csv_file()

    def import_data_from_csv_file(self):

        self.stdout.write(self.style.SUCCESS('Todos os dados foram importados com sucesso!'))