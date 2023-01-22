from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Post, Group, Comment, User


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'posts')
        ref_name = 'ReadOnlyUsers'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')

class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group',)

        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Cat.objects.all(),
        #         fields=('name', 'owner'),
        #         message=('Такая комбинация имени котика и его хозяина уже есть '
        #                  'в нашей базе')
        #     )
        # ]

    # def validate(self, data):
    #     if data['color'] == data['name']:
    #         raise serializers.ValidationError(
    #             'Имя не может совпадать с цветом!')
    #     return data

    # def validate_birth_year(self, value):
    #     year = dt.date.today().year
    #     if not (year - 40 < value <= year):
    #         raise serializers.ValidationError('Проверьте год рождения!')
    #     return value

    # def get_age(self, obj):
    #     return dt.datetime.now().year - obj.birth_year

    # def create(self, validated_data):
    #     if 'achievements' not in self.initial_data:
    #         cat = Cat.objects.create(**validated_data)
    #         return cat
    #     else:
    #         achievements = validated_data.pop('achievements')
    #         cat = Cat.objects.create(**validated_data)
    #         for achievement in achievements:
    #             current_achievement, status = Achievement.objects.get_or_create(
    #                 **achievement)
    #             AchievementCat.objects.create(
    #                 achievement=current_achievement, cat=cat)
    #         return cat
