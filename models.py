import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Sequence
from sqlalchemy.types import DateTime
from sqlalchemy.dialects.postgresql import UUID, JSON
from manage import db


# ---------------------------------------------------------------------------------
# Database Models
# ---------------------------------------------------------------------------------
# This file contains the models for all database tables which includes data types
# primary keys, and foreign key relationships.
#
# Created with SQLAlchemy Abstraction
#


class Accounts(db.Model):
    __tablename__ = 'accounts'
    id = Column(Integer, Sequence('account_id_seq'), primary_key=True, unique=True, nullable=False)
    account_id = Column(UUID(as_uuid=True), unique=True, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True, comment="true, false")

    def __init__(self, account_id, is_active):
        self.account_id = account_id
        self.is_active = is_active

    def __repr__(self):
        return "<Account(id='%s', account_id='%s', is_active='%s')>" % (
            self.id,
            self.account_id,
            self.is_active
        )


class Users(db.Model):
    __tablename__ = "users"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, unique=True, nullable=False)
    user_types_id = Column(Integer, ForeignKey('user_types.id'), nullable=False, comment="admin, student")
    first_name = Column(String(255))
    last_name = Column(String(255))
    date_of_birth = Column(DateTime())
    gender = Column(Integer)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(255))
    password = Column(String(255), nullable=False)
    address = Column(String(255))
    address2 = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    postal_code = Column(String(255))
    photo = Column(String(255))
    is_email_verified = Column(Boolean, nullable=False, default=False, comment="true, false")
    email_hash_token = Column(String(255))
    created = Column(DateTime(), nullable=False, default=datetime.datetime.now())
    modified = Column(DateTime(), nullable=False, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __init__(self, user_types_id, first_name, last_name, date_of_birth, gender, email, phone_number, password,
                 address, address2, city, state, postal_code, photo, is_email_verified, email_hash_token, created,
                 modified):
        self.user_types_id = user_types_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.address = address
        self.address2 = address2
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.photo = photo
        self.is_email_verified = is_email_verified
        self.email_hash_token = email_hash_token
        self.created = created
        self.modified = modified

    def __repr__(self):
        return "<User(id='%s', user_types_id='%s', first_name='%s', last_name='%s', date_of_birth='%s'" \
               ", gender='%s', email='%s', phone_number='%s', password='%s', address='%s', address2='%s'" \
               ", city='%s', state='%s', postal_code='%s', photo='%s', is_email_verified='%s'" \
               ", email_hash_token='%s', created='%s', modified='%s')>" % (
                   self.id,
                   self.user_types_id,
                   self.first_name,
                   self.last_name,
                   self.date_of_birth,
                   self.gender,
                   self.email,
                   self.phone_number,
                   self.password,
                   self.address,
                   self.address2,
                   self.city,
                   self.state,
                   self.postal_code,
                   self.photo,
                   self.is_email_verified,
                   self.email_hash_token,
                   self.created,
                   self.modified
               )


class BanGorillaEmails(db.Model):
    __tablename__ = "ban_gorilla_emails"
    id = Column(Integer, Sequence('ban_gorilla_email_id_seq'), primary_key=True, unique=True, nullable=False)
    domain = Column(String(255), nullable=False)
    created = Column(DateTime(), nullable=False, default=datetime.datetime.now())
    modified = Column(DateTime(), nullable=False, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __init__(self, domain, created, modified):
        self.domain = domain
        self.created = created
        self.modified = modified

    def __repr__(self):
        return "<Ban Gorilla Email(id='%s', domain='%s', created='%s', modified='%s')>" % (
            self.id,
            self.domain,
            self.created,
            self.modified
        )


class Configurations(db.Model):
    __tablename__ = "configurations"
    id = Column(Integer, Sequence('configuration_id_seq'), primary_key=True, unique=True, nullable=False)
    name = Column(String(255))
    value = Column(String(255), nullable=False)
    created = Column(DateTime(), nullable=False, default=datetime.datetime.now())
    modified = Column(DateTime(), nullable=False, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __init__(self, name, value, created, modified):
        self.name = name
        self.value = value
        self.created = created
        self.modified = modified

    def __repr__(self):
        return "<Configuration(id='%s', name='%s', value='%s', created='%s', modified='%s')>" % (
            self.id,
            self.name,
            self.value,
            self.created,
            self.modified
        )


class UserTypes(db.Model):
    __tablename__ = "user_types"
    id = Column(Integer, Sequence('user_type_id_seq'), primary_key=True, unique=True, nullable=False)
    name = Column(String(255))
    created = Column(DateTime(), nullable=False, default=datetime.datetime.now())
    modified = Column(DateTime(), nullable=False, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __init__(self, name, created, modified):
        self.name = name
        self.created = created
        self.modified = modified

    def __repr__(self):
        return "<User Type(id='%s', name='%s', created='%s', modified='%s')>" % (
            self.id,
            self.name,
            self.created,
            self.modified
        )


class Memberships(db.Model):
    __tablename__ = "memberships"
    id = Column(Integer, Sequence('membership_id_seq'), primary_key=True, unique=True, nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    accounts_id = Column(UUID(as_uuid=True), ForeignKey('accounts.account_id'), nullable=False)
    created = Column(DateTime(), nullable=False, default=datetime.datetime.now())
    modified = Column(DateTime(), nullable=False, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __init__(self, users_id, accounts_id, created, modified):
        self.users_id = users_id
        self.accounts_id = accounts_id
        self.created = created
        self.modified = modified

    def __repr__(self):
        return "<Membership(id='%s', users_id='%s', accounts_id='%s', created='%s', modified='%s')>" % (
            self.id,
            self.users_id,
            self.accounts_id,
            self.created,
            self.modified
        )


class ResetPasswordTokens(db.Model):
    __tablename__ = "reset_password_tokens"
    id = Column(Integer, Sequence('reset_token_password_id_seq'), primary_key=True, unique=True, nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    token = Column(String(255), nullable=False)
    status = Column(String(255), nullable=False, default='new', comment='new, used')
    created = Column(DateTime(), nullable=False, default=datetime.datetime.now())
    modified = Column(DateTime(), nullable=False, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __init__(self, users_id, token, status, created, modified):
        self.users_id = users_id
        self.token = token
        self.status = status
        self.created = created
        self.modified = modified

    def __repr__(self):
        return "<Reset Password Token(id='%s', users_id='%s',token='%s',status='%s', created='%s', modified='%s')>" % (
            self.id,
            self.users_id,
            self.token,
            self.status,
            self.created,
            self.modified
        )


class OldPasswords(db.Model):
    __tablename__ = "old_passwords"
    id = Column(Integer, Sequence('old_password_id_seq'), primary_key=True, unique=True, nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    password = Column(String(255), nullable=False)
    created = Column(DateTime(), nullable=False, default=datetime.datetime.now())
    modified = Column(DateTime(), nullable=False, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __init__(self, users_id, password, created, modified):
        self.users_id = users_id
        self.password = password
        self.created = created
        self.modified = modified

    def __repr__(self):
        return "<Old Password(id='%s', users_id='%s',password='%s', created='%s', modified='%s')>" % (
            self.id,
            self.users_id,
            self.password,
            self.created,
            self.modified
        )
