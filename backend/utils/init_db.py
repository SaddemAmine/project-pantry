from database import engine, Base
from models import *

def main():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main()
