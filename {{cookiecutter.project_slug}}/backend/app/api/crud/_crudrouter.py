from typing import Any, Callable, List

from fastapi.param_functions import Depends
from fastapi_crudrouter.core._types import PAGINATION
from fastapi_crudrouter.core.sqlalchemy import SQLAlchemyCRUDRouter
from sqlalchemy import func, select
from sqlalchemy.orm.session import Session
from starlette.responses import Response


class ReactAdminCompatibleCRUDRouter(SQLAlchemyCRUDRouter):
    def _get_all(self, *args: Any, **kwargs: Any) -> Callable:
        def route(
            response: Response,
            db: Session = Depends(self.db_func),
            pagination: PAGINATION = self.pagination,
        ) -> List:
            skip, limit = pagination.get("skip"), pagination.get("limit")

            total = db.scalar(select(func.count(self.db_model.id)))
            response.headers["Content-Range"] = str(total)
            db_models = (
                db.execute(select(self.db_model).offset(skip).limit(limit))
                .scalars()
                .all()
            )
            return db_models

        return route
