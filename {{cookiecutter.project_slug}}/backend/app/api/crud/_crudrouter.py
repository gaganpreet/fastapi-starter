import json
from typing import Any, Callable, List, Optional

from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.params import Query
from fastapi_crudrouter.core.sqlalchemy import SQLAlchemyCRUDRouter
from sqlalchemy import func, select
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import asc, desc
from starlette.responses import Response


class ReactAdminCompatibleCRUDRouter(SQLAlchemyCRUDRouter):
    def _get_all(self, *args: Any, **kwargs: Any) -> Callable:
        def route(
            response: Response,
            sort_: Optional[str] = Query(None, alias="sort"),
            range_: Optional[str] = Query(None, alias="range"),
            db: Session = Depends(self.db_func),
        ) -> List:
            skip, limit = 0, 10
            if range_:
                start, end = json.loads(range_)
                skip, limit = start, (end - start + 1)

            order_by = desc(self.db_model.id)
            if sort_:
                sort_column, sort_order = json.loads(sort_)
                if sort_order.lower() == "asc":
                    direction = asc
                elif sort_order.lower() == "desc":
                    direction = desc
                else:
                    raise HTTPException(400, f"Invalid sort direction {sort_order}")
                order_by = direction(self.db_model.__table__.c[sort_column])

            total = db.scalar(select(func.count(self.db_model.id)))
            response.headers["Content-Range"] = str(total)
            db_models = (
                db.execute(
                    select(self.db_model).offset(skip).limit(limit).order_by(order_by)
                )
                .scalars()
                .all()
            )
            return db_models

        return route
