# coding=utf-8

from factory.fuzzy import FuzzyInteger, FuzzyText
import factory
import foad.models

class FoadUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = foad.models.FoadUser

    user_id = factory.Sequence(lambda n: n)
    statut = FuzzyInteger(1, 16)
    username = factory.Sequence(lambda n: "123456{}".format(n))
    password = FuzzyText(length=8, chars='abcdefgijklmnopqrstuvwxyz0123456789')
    ied_code = FuzzyText(length=8, chars='abcdefghijklmnopqrstuvwxyz')
    email = factory.LazyAttribute(lambda n: "user{}@example.com".format(n))
    ied_code = FuzzyText(length=8, chars='abcdefghijklmnopqrstuvwxyz')
    nom = factory.Sequence(lambda n: "Guichon{}".format(n))
    prenom = factory.Sequence(lambda n: "Paul{}".format(n))
    official_code = FuzzyText(length=40, chars='abcdefgijklmnopqrstuvwxyz0123456789')
    phoneNumber = FuzzyText(length=10, chars="0123456789")
    perso_email = factory.LazyAttribute(lambda n: "perso{}@example.com".format(n))