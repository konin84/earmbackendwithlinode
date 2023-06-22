from django.db import models

# Create your models here.
import email
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator


phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")


class UserAccountManager(BaseUserManager):
    use_in_migration =True

    def create_user(self , email, password = None):

        if not email or len(email) <= 0:   
            raise  ValueError("Email  is required in this field")
       
        if not password :
            raise ValueError("Password is must! Kindly provide a password")
          
        user = self.model(email=self.normalize_email(email),) 
    
        user.set_password(password)
        user.save(using = self._db)
        return user
      
    def create_superuser(self , email, password):
        user = self.create_user(
            email= self.normalize_email(email), 
              password = password)
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        CLIENT = "CLIENT", 'Client'
        # TENANT = "TENANT", 'Tenant'
        # REALTOR = "REALTOR", 'Realtor',

    class Gender(models.TextChoices):
        MALE = "MALE", 'Male'
        FEMALE = "FEMALE", 'Female'
        OTHER = "OTHER", 'Other'

    class ContactType(models.TextChoices):
        INDIVIDUAL = "INDIVIDUAL", 'Idividual'
        COMPANY = "COMPANY", 'Company'
        
    base_gender = Gender.MALE
    base_role = Role.ADMIN
    base_contact = ContactType.INDIVIDUAL

    role = models.CharField(max_length=15, choices=Role.choices, default=base_role)
    email = models.EmailField(max_length=50, unique=True, verbose_name='email address')
    company_name =models.CharField(max_length=150, blank=True, null=True)
    company_email =models.EmailField(max_length=50, verbose_name ='company email address',  blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # The special permissions here
    is_client = models.BooleanField(default=False)
    #Additional information
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    national = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    # service = models.CharField(max_length=50, blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=20, validators=[phone_validator], unique=True, blank=True, null=True)
    gender = models.CharField(max_length=15, choices=Gender.choices, default=base_gender)
    contactType = models.CharField(max_length=15, choices=ContactType.choices, default=base_contact)
    termsAndConditions = models.BooleanField(default=False)
    # avatar = models.ImageField(null=True, default="avatar.svg", upload_to='images/users')
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
        
  #  defining the manager for the UserAccount model
    objects = UserAccountManager()
      
    def __str__(self):
        return str(self.email)
        # return str(self.email)
      
    def has_perm(self , perm, obj = None):
        return self.is_admin
      
    def has_module_perms(self , app_label):
        return True
  
    def save(self , *args , **kwargs):
        if not self.role or self.role == None : 
            self.role = UserAccount.base_role
        return super().save(*args , **kwargs)
    

class AdministratorManager(models.Manager):
     
     
    def create_user(self , email , password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email  = email.lower()
        user = self.model(
            email = email
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
     
    def get_queryset(self , *args, **kwargs):
         
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(role = UserAccount.Role.ADMIN)
        return queryset	

class Administrator(UserAccount):
    
	class Meta :
		proxy = True
	objects = AdministratorManager()
	
	def save(self , *args , **kwargs):
		self.role = UserAccount.Role.ADMIN
		self.is_admin = True
		self.is_active = True
		self.is_staff = True
        
		return super().save(*args , **kwargs)

class ClientManager(models.Manager):
     
    def create_user(self , email , password = None):
         
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email  = email.lower()
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def get_queryset(self , *args, **kwargs):
    
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(role = UserAccount.Role.CLIENT)
        return queryset	

class Client(UserAccount):
         
    class Meta :
        proxy = True
    objects = ClientManager()
    
    def save(self , *args , **kwargs):
        self.role = UserAccount.Role.CLIENT
        self.is_client = True
        return super().save(*args , **kwargs)

