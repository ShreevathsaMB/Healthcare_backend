from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Patient, Doctor, PatientDoctorMapping
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            name=validated_data.get('name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name')


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at')


class MappingSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), source='patient', write_only=True
    )
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(), source='doctor', write_only=True
    )

    class Meta:
        model = PatientDoctorMapping
        fields = ('id', 'patient', 'doctor', 'patient_id', 'doctor_id', 'assigned_by', 'assigned_at')
        read_only_fields = ('assigned_by', 'assigned_at')

    def create(self, validated_data):
        request = self.context.get('request')
        mapping = PatientDoctorMapping.objects.create(
            patient=validated_data['patient'],
            doctor=validated_data['doctor'],
            assigned_by=request.user if request else None
        )
        return mapping