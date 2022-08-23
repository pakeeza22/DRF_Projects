from rest_framework import serializers
from .models import Student

# Validators
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("name should be start with 'r'!")


# with serializer.Serializer
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, validators=[start_with_r])
    age = serializers.IntegerField(allow_null=True)
    city = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # Field level validation
    def validate_age(self, age):
        if age >= 100:
            raise serializers.ValidationError("Incorrect age value!")
        return age

    # Object level validation
    def validate(self, data):
        nm = data.get('name')
        age = data.get('age')
        if nm =="" or nm == "/":
            raise serializers.ValidationError("Please input the name!")
        return data


# with serializer.ModelSerializer
class StudentModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, validators=[start_with_r])
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ['name', 'age']
        # extra_kwargs = {'name':{'read_only':True}}

    # Field level validation
    def validate_age(self, age):
        if age >= 100:
            raise serializers.ValidationError("Incorrect age value!")
        return age

    # Object level validation
    def validate(self, data):
        nm = data.get('name')
        age = data.get('age')
        if nm =="" or nm == "/":
            raise serializers.ValidationError("Please input the name!")
        return data