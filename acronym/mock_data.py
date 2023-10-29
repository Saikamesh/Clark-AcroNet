from django.contrib.auth.hashers import make_password
from faker import Faker
from acronym.models import Acronym, Users, Suggestions

fake = Faker()

# Generate mock data for Acronym model
def generate_acronyms(num_acronyms):
    for i in range(num_acronyms):
        acronym_name = fake.word().upper()[:10]
        full_form = fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None)
        description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
        location = fake.city()
        phone_number = fake.random_int(min=1000000000, max=9999999999)
        email = fake.email()
        website = fake.url()
        created_on = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
        acronym = Acronym.objects.create(acronym_name=acronym_name, full_form=full_form, description=description, location=location, phone_number=phone_number, email=email, website=website, created_on=created_on)

# Generate mock data for Users model
def generate_users(num_users):
    for i in range(num_users):
        user_name = fake.user_name()
        password = make_password(fake.password())
        email = fake.email()
        user_type = fake.random_element(elements=('admin', 'user'))
        user = Users.objects.create(user_name=user_name, password=password, email=email, user_type=user_type)


# Generate mock data for Suggestions model
def generate_suggestions(num_suggestions):
    for i in range(num_suggestions):
        acronym_name = fake.word().upper()[:10]
        full_form = fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None)
        description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
        location = fake.city()
        phone_number = fake.random_int(min=1000000000, max=9999999999)
        email = fake.email()
        website = fake.url()
        created_on = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
        suggested_by_name = fake.user_name()
        suggested_by_email = fake.email()
        status = fake.random_element(elements=('approved', 'rejected', 'pending'))
        suggestion = Suggestions.objects.create(acronym_name=acronym_name, full_form=full_form, description=description, location=location, phone_number=phone_number, email=email, website=website, created_on=created_on, suggested_by_name=suggested_by_name, suggested_by_email=suggested_by_email, status=status)