from sqlalchemy import Column, String, create_engine, Integer, FLOAT, DATETIME,DATE,TIMESTAMP,Text,func
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Inventory(Base):
    __tablename__ = 'idc_asset_inventory'
    serial_no = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Integer, default=1)
    idc = Column(Integer)
    cabinet = Column(String(20))
    addresses = Column(Integer)
    host_name = Column(String(100))
    model = Column(String(50))
    asset_code = Column(String(20))
    asset_sn = Column(String(20))
    ip_business_code = Column(String(50))
    ip_admin = Column(String(50))
    department = Column(String(20))
    interfac_person = Column(String(10))
    project = Column(String(50))
    project_contract = Column(String(20))
    project_acceptance_time = Column(DATE)
    state = Column(Integer)
    off_shelf_evaluation = Column(Integer)
    cpu_config = Column(String(50))
    memory_config = Column(String(50))
    disk_config = Column(String(50))
    cpu_use_rate = Column(Integer)
    memory_use_rate = Column(Integer)
    disk_use_rate = Column(Integer)
    remark = Column(String(50))
    create_time = Column(DATETIME, default=func.now())
    update_time = Column(TIMESTAMP,default=func.now(), onupdate=func.now())
    is_delete = Column(Integer, default=0)

class Inventory_Ip(Base):
    __tablename__ = 'idc_asset_inventory_ip'
    serial_no = Column(Integer, primary_key=True, autoincrement=True)
    ip_business_code = Column(String(50))
    ip_value = Column(String(50))
    create_time = Column(DATETIME,default=func.now())
    update_time = Column(TIMESTAMP, default=func.now(),onupdate=func.now())
    is_delete = Column(Integer,default=0)

# class User(UserMixin,Base):
#     __tablename__ = 'idc_asset_inventory_user'
#     dgdh = Column(Integer, primary_key=True)
#     username = Column(String(50),unique=True)
#     password = Column(Text)
#     email = Column(String(255))
#     createtime = Column(DATETIME)

# class Role(Base):
#     __tablename__ = 'role'
#     roleid = Column(Integer, primary_key=True)
#     rolename = Column(String(32))
#
# class Role_user(Base):
#     __tablename__ = 'user_role'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer)
#     role_id = Column(Integer)

class User(UserMixin,Base):
    __tablename__ = 'idc_asset_inventory_user'
    dgdh = Column(Integer, primary_key=True,unique=True)
    name = Column(String(50))
    password = Column(Text)
    # idc_asset_inventory_user_action_view = relationship('Action',backref='user')


class ActionView(Base):
    __tablename__ ='idc_asset_inventory_user_action_view'
    dgdh = Column(Integer,primary_key=True)
    name = Column(String(50))
    department = Column(String(50))
    action_id = Column(Integer,primary_key=True)

class DepartmentView(Base):
    __tablename__='idc_asset_inventory_department_view'
    department_id = Column(Integer,primary_key=True)
    department = Column(String(50))

class InventoryView(Base):
    __tablename__ = 'idc_asset_inventory_view'
    serial_no = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(Integer, default=1)
    idc_name = Column(Integer)
    cabinet = Column(String(20))
    cabinet_addresses = Column(Integer)
    host_name = Column(String(100))
    model = Column(String(50))
    asset_code = Column(String(20))
    asset_sn = Column(String(20))
    ip_business_code = Column(String(50))
    ip_value = Column(String(50))
    ip_admin = Column(String(50))
    department = Column(String(20))
    interfac_person = Column(String(10))
    project = Column(String(50))
    project_contract = Column(String(20))
    project_acceptance_time = Column(DATE)
    state = Column(Integer)
    off_shelf_evaluation = Column(Integer)
    cpu_config = Column(String(50))
    memory_config = Column(String(50))
    disk_config = Column(String(50))
    cpu_use_rate = Column(Integer)
    memory_use_rate = Column(Integer)
    disk_use_rate = Column(Integer)
    remark = Column(String(50))
    # create_time = Column(DATETIME, default=func.now())
    update_time = Column(TIMESTAMP,default=func.now(), onupdate=func.now())
    is_delete = Column(Integer, default=0)