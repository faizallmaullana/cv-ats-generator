from app import db
import uuid

class tes(db.Model):
    __tablename__ = 'tes'

    id_employee = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(128))
    
    def get_id(self):
        return str(self.id_employee)
