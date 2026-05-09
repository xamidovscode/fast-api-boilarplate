from typing import Any, List, Type, TypeVar, Optional

from fastapi import HTTPException, status
from pydantic import BaseModel

ModelT = TypeVar("ModelT")
SchemaT = TypeVar("SchemaT", bound=BaseModel)


class QueryMixin:
    success: dict = {"msg": "Muvaffaqiyatli o'chirildi"}

    @classmethod
    def error(cls, text: str, status_code: int = status.HTTP_400_BAD_REQUEST) -> HTTPException:
        return HTTPException(detail=text, status_code=status_code)

    async def get_object_or_404(self, stmt) -> Any:
        result = await self.execute(stmt)
        if obj := result.scalar_one_or_none():
            return obj
        raise self.error("Obyekt topilmadi", status.HTTP_404_NOT_FOUND)

    async def get_object_or_none(self, stmt) -> Any | None:
        result = await self.execute(stmt)
        return result.scalar_one_or_none()

    async def get_all(self, stmt) -> List[Any]:
        result = await self.execute(stmt)
        return result.scalars().all()

    async def save(self, model: Type[ModelT], schema: Optional[SchemaT] = None, **extra) -> ModelT:
        """
        Modelni saqlaydi.

        Faqat extra bilan:
            await self.save(User, username="ali", password="hash")

        Faqat schema bilan:
            await self.save(User, schema=body)

        Schema + extra (extra ustunlik qiladi):
            await self.save(User, schema=body, is_active=True, role="admin")
        """
        data = schema.model_dump() if schema else {}
        data.update(extra)
        obj = model(**data)
        self.add(obj)
        await self.commit()
        await self.refresh(obj)
        return obj

    async def update(
            self,
            obj: ModelT,
            schema: Optional[SchemaT] = None,
            **extra,
    ) -> ModelT:
        data = schema.model_dump(exclude_unset=True) if schema else {}
        data.update(extra)
        for field, value in data.items():
            setattr(obj, field, value)
        await self.commit()
        await self.refresh(obj)
        return obj

    async def remove(self, obj: Any) -> dict:
        await self.delete(obj)
        await self.commit()
        return self.success

    async def save_all(self, objects: List[Any]) -> List[Any]:
        self.add_all(objects)
        await self.commit()
        return objects