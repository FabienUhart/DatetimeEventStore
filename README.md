DatetimeEventStore

***Temps de réalisation:***
	4h en ayant voulu faire du traitement de fichier en premier lieu, json

***Fonctionnement:***
	● DatetimeEventStore.store_event(at, event)​​ permettant de stocker un évènement en l’associant à un ​ datetime.datetime​​ .
	● DatetimeEventStore.get_events(start, end)​​ permettant de récupérer les évènements associés aux datetimes appartenant à la période spécifié en paramètre.

	Création d'une base de donnée pouvant être supprimée, sqlite3

***choix des technos:***
	Le choix de la base de donnée sqlite3 est que c'est une BDD simple à intégré et qui permet la gestions d'un petit jeu de donnée.
	Il m'etait judicieux de faire une création en amont et de faire une gestion de la connexion.


***Modification future:***
	Changement de la BDD pour du requetage plus rapide
	Possibilité de faire de la gestion de l'évènement, donc suppression de lots

	Exemple pour vider la table entièrement:    
	    def truncate(self):
	        """ truncate the table"""
	        c = self.conn.cursor()
	        sqlite_truncate = '''DELETE FROM EVENTS;'''
	        c.execute(sqlite_truncate)
	        self.conn.commit()
	
	Utilisation de logs dans le package en tant que parametres