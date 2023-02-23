from IPython.terminal import embed
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

from app.core.config import settings
from app.models.user import User

if __name__ == "__main__":
    engine = create_engine(settings.DATABASE_URL, future=True)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

    terminal = embed.InteractiveShellEmbed()
    terminal.extension_manager.load_extension("autoreload")
    terminal.run_line_magic("autoreload", "2")

    db = SessionLocal(future=True)
    terminal.mainloop()
