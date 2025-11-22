from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import database, Base, engine
from models.tasks import Tasks

app = FastAPI(title="Tasks", docs_url="/")

Base.metadata.create_all(engine)


@app.post("/add_tasks")
def add_tasks(task: str, description: str, status: bool, db: Session = Depends(database)):
    tasks = Tasks(
        task=task,
        description=description,
        status=status,
        created_at=datetime.now()
    )
    db.add(tasks)
    db.commit()
    return {'message': "Topshiriq qo'shildi"}

@app.get("/tasks")
def get_tasks(db: Session = Depends(database)):
    tasks = db.query(Tasks).all()
    return tasks


@app.put("/update_tasks")
def update_tasks(ident: int, task: str, description: str, status: bool, db: Session = Depends(database)):
    tasks = db.query(Tasks).filter(Tasks.id == ident).first()
    if not tasks:
        raise HTTPException(status_code=404, detail="Ma'lumot topilmadi")

    db.query(Tasks).filter(Tasks.id == ident).update({
        Tasks.task: task,
        Tasks.description: description,
        Tasks.status: status,
        Tasks.created_at: datetime.now
    })

    db.commit()
    return {"message": "Ma 'lumot o'zgartirildi"}


@app.delete("/delete_tasks")
def delete_tasks(ident: int, db: Session = Depends(database)):
    check_tasks = db.query(Tasks).filter(Tasks.id == ident).first()
    if not check_tasks:
        raise HTTPException(status_code=404, detail="Topilmadi")

    db.delete(check_tasks)
    db.commit()
    return {"message": "Ma'lumot o'chirildi"}
