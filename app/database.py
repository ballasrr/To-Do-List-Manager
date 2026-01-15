from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Настройка БД (по умолчанию sqlite в локальном файле)
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# Для sqlite требуется аргумент connect_args
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Простая зависимость для FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Утилита для инициализации базы (создаёт таблицы, определённые в моделях)
def init_db():
    try:
        from app.models.models import Base
        Base.metadata.create_all(bind=engine)
    except Exception:
        pass
