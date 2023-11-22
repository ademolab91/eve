from langchain.chat_models import ChatOpenAI
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

_model = ChatOpenAI()

# Connect to demo db
db = SQLDatabase.from_uri(f"sqlite:///demo.sqlite3")

# if you update this, you MUST also update ../pyproject.toml
# with the new `tool.langserve.export_attr`
chain = SQLDatabaseChain.from_llm(_model, db)
