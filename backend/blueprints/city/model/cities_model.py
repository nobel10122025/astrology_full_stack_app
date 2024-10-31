from mongoengine import StringField, IntField, Document, FloatField

class Cities(Document):
    id = IntField(required = True)
    city = StringField(required = True)
    city_ascii = StringField(required = True)
    lat = FloatField(required= True)
    lng = FloatField(required= True)
    country = StringField(required = True)
    iso2 = StringField(required = True)
    iso3 = StringField(required = True)
    _id=  StringField(required = True)