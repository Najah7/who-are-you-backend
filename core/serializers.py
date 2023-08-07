from rest_framework.serializers import ModelSerializer

from core.models import User, SNS, Other

class OtherSerializer(ModelSerializer):
    class Meta:
        model = Other
        fields = "__all__"
        

class SNSSerializer(ModelSerializer):
    others = OtherSerializer(many=True, required=False)
    class Meta:
        model = SNS
        fields = "__all__"
        

class UserSerializer(ModelSerializer):
    sns = SNSSerializer(required=False)
    others = OtherSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ["id", "name", "email", "password", "sns", "others"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
