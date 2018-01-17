from flask import Flask
from models import db, Orders
from os import getenv
from format_phone import format_phone_number
import time
import psycopg2
from sqlalchemy.exc import OperationalError

app = Flask(__name__)

POSTGRES = {
    'user': getenv('DB_USER'),
    'pw': getenv('DB_PASSWORD'),
    'db': getenv('DB_NAME'),
    'host': getenv('DB_HOST'),
    'port': getenv('DB_PORT'),
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


if __name__ == "__main__":
    last_order_id = 0
    timeout = 2
    while True:
        with app.app_context():
            try:
                orders = Orders.query.all()[last_order_id:]
                if len(orders) != 0:
                    for order in orders:
                        number = order.contact_phone
                        new_number = format_phone_number(number)
                        print(number, new_number)
                        order.formatted_phone = new_number
                    db.session.commit()
                    last_order_id = orders[-1].id
            except (psycopg2.OperationalError, OperationalError) as e:
                pass
            finally:
                time.sleep(timeout)
