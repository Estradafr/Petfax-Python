
from flask import Flask
from flask_migrate import Migrate

def create_app():
    # factory
    app = Flask('App')
    
    # db config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:IEblack30!@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             

    from . import models 
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # index route
    @app.route('/')
    def index():
        return 'Hello this is PetFax'

    # register pet blueprint
    from . import pet, fact
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)
    
    
    return app
