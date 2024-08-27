from sqlalchemy import create_engine
from sqlalchemy.sql import text


engine = create_engine("postgresql+psycopg2://myuser:mypassword@localhost:5432/mydb")


def app():
    # Connect to engine
    with engine.connect() as conn:
        # query statement
        stmt = text("select * from pg_database")
        # execute and print
        print(conn.execute(stmt).fetchall())


if __name__ == "__main__":
    app()
