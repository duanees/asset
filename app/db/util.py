from sqlalchemy import create_engine, func
from sqlalchemy import alias, and_, func,outerjoin, or_
from sqlalchemy.orm import sessionmaker, aliased
from app.db.models import *
engine=create_engine("mysql+pymysql://root:zbb629@localhost:3306/wasu?charset=utf8", encoding='utf8')

class ConnectionPool():
    def __init__(self):
        self.session = None

    def __enter__(self):
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

# def list_data(**kwargs):
#     page = kwargs.get('page', 1)
#     row_count = kwargs.get('row_count', 15)
#     with ConnectionPool() as session:
#         data = session.query(Inventory).filter(and_(Inventory.is_delete == 0)
#                                       ).order_by(Inventory.serial_no).offset(page).limit(row_count).all()
#         count = session.query(Inventory).filter(Inventory.is_delete == 0).count()
#     return data, count

# def list_data(**kwargs):
#     page = kwargs.get('page', 1)
#     row_count = kwargs.get('row_count', 15)
#     with ConnectionPool() as session:
#         data = session.query(Inventory,DepartmentView.department, func.IF(Inventory.ip_business_code,
#                                                 func.group_concat(func.inet_ntoa(Inventory_Ip.ip_value),
#                                                                                    ), '').label('ip_business')
#                              ).outerjoin(Inventory_Ip, Inventory_Ip.ip_business_code == Inventory.ip_business_code
#                                          ).outerjoin(DepartmentView, DepartmentView.department_id == Inventory.department
#                                                      ).filter(Inventory.is_delete == 0
#                                                               ).group_by(Inventory.serial_no
#                                                                          ).order_by(Inventory.serial_no
#                                                                                      ).offset(page).limit(
#             row_count).all()
#         count = session.query(Inventory).filter(Inventory.is_delete == 0).count()
#     return data, count

def list_data(**kwargs):
    page = kwargs.get('page', 1)
    row_count = kwargs.get('row_count', 15)
    with ConnectionPool() as session:
        data = session.query(InventoryView).group_by(InventoryView.serial_no).offset(page).limit(
            row_count).all()
        count = session.query(InventoryView).filter(InventoryView.is_delete == 0).count()
    return data, count

def get_user(dgdh=None, name=None):
    with ConnectionPool() as session:
        data = session.query(User.dgdh, User.name, User.password, ActionView.dgdh).filter(
            and_(or_(User.name == name, User.dgdh == dgdh))
        ).all()
    return data[0] if data else None

def insert_inventory(**kwargs):
    with ConnectionPool() as session:
        ine = Inventory(**kwargs)
        session.add(ine)
        session.commit()

def insert_inventory_ip(**kwargs):
    with ConnectionPool() as session:
        ip = Inventory_Ip(**kwargs)
        session.add(ip)
        session.commit()

def list_department():
    with ConnectionPool() as session:
        data = session.query(DepartmentView).all()
    return data


def delete_inventory(serial_nos):
    with ConnectionPool() as session:
        inv = session.query(Inventory).filter(Inventory.serial_no.in_(serial_nos)).all()
        session.delete(inv)
        session.commit()

def delete_inventory_ip(serial_nos):
    with ConnectionPool() as session:
        inv_ip = session.query(Inventory_Ip).filter(and_(Inventory.serial_no.in_(serial_nos),
                                                   Inventory.ip_business_code == Inventory_Ip.ip_business_code)).all()
        session.delete(inv_ip)
        session.commit()
def get_inventory(serial_no):
    with ConnectionPool() as session:
        data = session.query().filter().one()
    return data


