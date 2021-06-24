from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import Doctor, Patient, Visit, Tooth, PatientNote
from .functions import create_patient_teeth


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="doctor.name")
    surname = serializers.CharField(source="doctor.surname")
    doctor_id = serializers.ReadOnlyField(source="doctor.id")
    facility_name = serializers.ReadOnlyField(source="doctor.facility.name")

    class Meta:
        model = User
        fields = ('username', 'name', 'surname', 'doctor_id', 'email', 'facility_name')


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.is_active = False
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'id', 'email')


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name', 'surname', 'pwz', 'id', 'second_name', 'telephone')

    def create(self, validated_data):
        request = self.context["request"]
        user_data = request.data["user"]
        if User.objects.filter(username=user_data["login"]).exists():
            raise serializers.ValidationError("Użytkownik o podanym loginie już istnieje")
        user = User.objects.create(username=user_data["login"], email=user_data["email"], is_active=False)
        user.set_password(user_data["password"])
        user.save()

        validated_data["user_id"] = user.id
        validated_data["facility_id"] = request.user.doctor.facility.id

        return super().create(validated_data)


class ToothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tooth
        fields = "__all__"


class PatientNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientNote
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ("facility",)

    def create(self, validated_data):
        patient = Patient.objects.create(**validated_data, facility=self.context['request'].user.doctor.facility)
        create_patient_teeth(patient.id)
        return patient


class VisitSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.IntegerField(write_only=True)
    doctor_id = serializers.IntegerField(write_only=True)
    start_time = serializers.TimeField(format="%H:%M")
    end_time = serializers.TimeField(format="%H:%M")

    class Meta:
        model = Visit
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Nieprawidłowe stare hasło.')
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError("Hasła nie są takie same.")
        password_validation.validate_password(data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user


