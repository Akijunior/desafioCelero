from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from .models import Athlete, Game, Sport, Event, Medal

VALIDATE_VALID_EMAIL_REGEX = True
EMAIL_VALIDATE_REGEX = r"[^@]+@[^@]+\.[^@]+"
MIN_PASSWORD_LENGHT = 4


class Custom409(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Já existe um usuário cadastrado com o e-mail em questão."


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = "__all__"


class AthleteDetailSerializer(serializers.ModelSerializer):

    medals = serializers.SerializerMethodField()

    class Meta:
        model = Athlete
        fields = ["id", "athlete_id", "name", "sex", "age", "height",
                  "weight", "team", "noc", "medals"]

    def get_medals(self, obj):
        medals = obj.medal_set.exclude(medal="0")
        return MedalSerializer(medals, many=True).data


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class GameDetailSerializer(serializers.ModelSerializer):

    sports = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ["id", "game_name", "year", "season", "city", "sports"]

    def get_sports(self, obj):
        sports = obj.sports.all()
        return SportSerializer(sports, many=True).data


class MedalSerializer(serializers.ModelSerializer):

    event = serializers.SerializerMethodField()
    game = serializers.SerializerMethodField()


    class Meta:
        model = Medal
        fields = ['medal', 'game', 'event']

    def get_event(self, obj):
        return '%s' % (obj.event.event)

    def get_game(self, obj):
        return '%s' % (obj.game.game_name)



class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"


class SportDetailSerializer(serializers.ModelSerializer):

    events = serializers.SerializerMethodField()

    class Meta:
        model = Sport
        fields = ["id", "sport", "events"]

    def get_events(self, obj):
        events = obj.event_set.all()
        return EventSerializer(events, many=True).data


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label="Senha", max_length=30, style={'input_type': 'password'},
                                     write_only=True, required=False)
    password2 = serializers.CharField(label="Confirmação da senha", max_length=30,
                                      style={'input_type': 'password'},
                                      write_only=True, required=False)
    email = serializers.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def validate(self, data):
        errors = dict()

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserSerializer, self).validate(data)

    def validate_senha(self, senha1, senha2):
        if len(senha1) < MIN_PASSWORD_LENGHT:
            raise serializers.ValidationError(f"A senha deve ter {MIN_PASSWORD_LENGHT} caracteres ou mais")
        if (senha1 != senha2):
            raise serializers.ValidationError("A primeira senha não coincide com a segunda.")
        return senha1

    def validate_email(self, email):
        if User.objects.filter(Q(email=email) | Q(username=email)).exists():
            raise serializers.ValidationError("Já existe um usuário cadastrado com este e-mail")

        return email

    def create(self, validated_data):
        try:
            senha2 = validated_data.pop('password2')
            validated_data['password'] = self.validate_senha(validated_data['password'], senha2)
            validated_data['username'] = validated_data['email']
            auth_usuario = User.objects.create_user(**validated_data)

            auth_usuario.save()

            return User.objects.get(id=auth_usuario.id)

        except IntegrityError as exception:
            raise Custom409(exception)
