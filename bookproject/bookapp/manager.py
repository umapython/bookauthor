from django.contrib.auth.base_user import BaseUserManager
class CustomUserManager(BaseUserManager):
    use_in_migrations=True
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email is must")
        email=self.normalize_email(email)
        password=self.model(email=email,**extra_fields)
        user=user.set_password(password)
        user.save()
        return user
    def create_user(self,email,name,contact,password=None):
        return self._create_user(email=email,password=password,name=name,contact=contact)
