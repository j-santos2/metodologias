from functools import wraps

from sqlalchemy.exc import IntegrityError

from .import app, db


def commit_after(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret_value = func(*args, **kwargs)
        try:
            db.session.commit()
            app.logger.info('Transaction commited successfully')
            return ret_value
        except IntegrityError as e:
            db.session.rollback()
            app.logger.info('Transaction failed applying rollback')    
            return None
    return wrapper
