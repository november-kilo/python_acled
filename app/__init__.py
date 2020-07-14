from sqlalchemy import create_engine

from app.Constants import Constants

engine = create_engine(f'sqlite:///data/{Constants.DATABASE}', echo=True)
