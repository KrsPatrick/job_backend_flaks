from extensions import db


joblist = []

def get_last_id():
    last_job = 1

    if joblist:
        last_job = joblist[-1].id + 1

    return last_job



class Job(db.Model):

    __tablename__ = "Job"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    salary = db.Column(db.Integer)
    is_published = db.Column(db.Boolean(), default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    @property
    def data(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "salary": self.salary
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_published_jobs(cls):
        return cls.query.filter_by(is_published=True).all()

    @classmethod
    def get_one_job(cls, job_id):
        return cls.query.filter_by(id=job_id).first()

