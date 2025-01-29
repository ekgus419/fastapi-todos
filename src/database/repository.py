from typing import List

from fastapi import Depends
from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from database.connection import get_db
from database.orm import ToDo, User


class ToDoRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def get_todos(self) -> List[ToDo]:
        return list(self.session.scalars(select(ToDo)))

    def get_todo_by_todo_id(self, todo_id: int) -> ToDo | None:
        return self.session.scalar(select(ToDo).where(ToDo.id == todo_id))

    def create_todo(self, todo: ToDo) -> ToDo:
        self.session.add(instance=todo) # 인스턴스 먼저 생성
        self.session.commit() # 데이터베이스에 저장
        self.session.refresh(instance=todo) # 리프레쉬후 반영된 todo를 다시 읽어온다
        return todo

    def update_todo(self, todo: ToDo) -> ToDo:
        self.session.add(instance=todo) # 인스턴스 먼저 생성
        self.session.commit() # 데이터베이스에 저장
        self.session.refresh(instance=todo) # 리프레쉬후 반영된 todo를 다시 읽어온다
        return todo

    def delete_todo(self, todo_id: int) -> None:
        self.session.execute(delete(ToDo).where(ToDo.id == todo_id))
        self.session.commit()


class UserRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def get_user_by_username(self, username:str) -> User | None:
        return self.session.scalar(
            select(User).where(User.username == username)
        )

    def save_user(self, user: User) -> User:
        self.session.add(instance=user) # 인스턴스 먼저 생성
        self.session.commit() # 데이터베이스에 저장
        self.session.refresh(instance=user) # 리프레쉬후 반영된 todo를 다시 읽어온다
        return user
