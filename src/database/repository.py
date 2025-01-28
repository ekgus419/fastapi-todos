from typing import List

from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from database.orm import ToDo


def get_todos(session: Session) -> List[ToDo]:
    return list(session.scalars(select(ToDo)))


def get_todo_by_todo_id(session: Session, todo_id: int) -> ToDo | None:
    return session.scalar(select(ToDo).where(ToDo.id == todo_id))

def create_todo(session: Session, todo: ToDo) -> ToDo:
    session.add(instance=todo) # 인스턴스 먼저 생성
    session.commit() # 데이터베이스에 저장
    session.refresh(instance=todo) # 리프레쉬후 반영된 todo를 다시 읽어온다
    return todo

def update_todo(session: Session, todo: ToDo) -> ToDo:
    session.add(instance=todo) # 인스턴스 먼저 생성
    session.commit() # 데이터베이스에 저장
    session.refresh(instance=todo) # 리프레쉬후 반영된 todo를 다시 읽어온다
    return todo

def delete_todo(session: Session, todo_id: int) -> None:
    session.execute(delete(ToDo).where(ToDo.id == todo_id))
    session.commit()