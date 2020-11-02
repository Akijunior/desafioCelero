import pandas as pd

from apps.athlete.models import Athlete, Sport, Game, Event, Medal


def import_csv(csv_file, num_lines=None):
    df_athletes = pd.read_csv(csv_file, nrows=num_lines) if num_lines else pd.read_csv(csv_file)
    df_athletes = df_athletes.fillna(0)

    try:

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

            medal = Medal.objects.get_or_create(
                athlete=athlete,
                event=event,
                game=game,
                defaults={'medal': row['Medal']}
            )

    except FileNotFoundError:
        print("O nome do arquivo não foi encontrado no diretório csv_data."
              "Favor, verifique e tente novamente.")

    except KeyError:
        print("As colunas do arquivo CSV recebido não conferem com as que são esperadas:\n "
              "'ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC', 'Games', 'Year',"
              " 'Season', 'City', 'Sport', 'Event', 'Medal'.\n"
              "Favor, verifique e após isso tente novamente.")