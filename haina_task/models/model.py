import datetime as dt
import json
import sqlite3
from pathlib import Path

import appdirs

from haina_task.models.task import Task


class Model:
    def __init__(self) -> None:
        user_data_path = Path(appdirs.user_data_dir("haina-task", "nikohonu"))
        user_data_path.mkdir(exist_ok=True, parents=True)
        database_path = user_data_path / "database.db"
        self.connect = sqlite3.connect(
            database_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
        )
        self.create_tables()

    def create_tables(self) -> None:
        with self.connect:
            self.connect.execute(
                """
                CREATE TABLE IF NOT EXISTS "project" (
                    "id"	      INTEGER,
                    "name"	      TEXT NOT NULL,
                    "description" TEXT,
                    PRIMARY KEY("id" AUTOINCREMENT)
                );"""
            )
            self.connect.execute(
                """
                CREATE TABLE IF NOT EXISTS "task" (
                    "id"	          INTEGER,
                    "name"	          TEXT NOT NULL,
                    "chain"	          TEXT,
                    "description"	  TEXT,
                    "schedule"	      timestamp,
                    "deadline"	      timestamp,
                    "recurrence"      TEXT,
                    "project_id"	  INTEGER,
                    FOREIGN KEY("project_id") REFERENCES "project"("id"),
                    PRIMARY KEY("id" AUTOINCREMENT)
                );"""
            )

    def __del__(self) -> None:
        self.connect.close()

    def create_or_get_project(self, name: str | None) -> int | None:
        if not name:
            return None
        cursor = self.connect.cursor()
        cursor.execute("SELECT id FROM project WHERE name = ?", (name,))
        existing_row = cursor.fetchone()
        if not existing_row:
            cursor.execute("INSERT INTO project(name) VALUES (?)", (name,))
            self.connect.commit()
            return cursor.lastrowid
        return int(existing_row[0])

    def add_task(self, task: Task) -> int | None:
        cursor = self.connect.cursor()
        cursor.execute(
            """
            INSERT INTO 
                task(name, chain, description, schedule, deadline, recurrence, project_id)
                VALUES(?, ?, ?, ?, ?, ?, ?)""",
            task.as_tuple(self.create_or_get_project),
        )
        self.connect.commit()
        return cursor.lastrowid
