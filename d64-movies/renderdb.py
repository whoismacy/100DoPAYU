from sqlalchemy import Integer, create_engine, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class MovieDb(Base):
    __tablename__ = "movies_favourite"
    movie_id = Column("id", Integer, primary_key=True)
    movie_title = Column("movie_title", String, nullable=False, )
    movie_year = Column("movie_year", Integer, nullable=False)
    movie_plot = Column("movie_plot", String, nullable=False)
    movie_poster_link = Column("movie_poster_link", String, nullable=True, unique=True)
    movie_rating = Column("rt_rating", String, nullable=False)

    def __init__(self, title, year, plot, poster_link, rt_rating):
        super().__init__()
        self.movie_title = title.title()
        self.movie_year = year
        self.movie_plot = plot
        self.movie_poster_link = poster_link
        self.movie_rating = rt_rating

# Creating engine
engine = create_engine("sqlite:///movie-database.db", echo=True)
Base.metadata.create_all(bind=engine)

# Creating the Session
Session = sessionmaker(bind=engine)
session = Session()

def film_in_db(cinema):
    return session.query(MovieDb).filter(MovieDb.movie_title == cinema.title()).first() is not None

def add_to_db(movie_list):
    new_films = []
    for film in movie_list:
        if not film_in_db(film.get('title')):
            cine = MovieDb(film.get('title'), film.get('year'), film.get('plot'), film.get('poster_link'), film.get('rt_rating'))
            new_films.append(cine)
    if new_films:
        session.bulk_save_objects(new_films)
        session.commit()

def add_movie(film):
    if not film_in_db(film):
        cine = MovieDb(film.get('title'), film.get('year'), film.get('plot'), film.get('poster_link'),film.get('rt_rating'))
        session.add(cine)
        session.commit()

def drop_movie(movie):
    query_response = session.query(MovieDb).filter_by(movie_title = movie).first()
    if query_response:
        session.delete(query_response)
        session.commit()
        return True
    return False

def get_all():
    return [{"id":frame.movie_id, "title":frame.movie_title, "year":frame.movie_year, "plot":frame.movie_plot, "poster_link":frame.movie_poster_link, "rating":frame.movie_rating} for frame in session.query(MovieDb).all()]

def all_movie_titles():
    return [frame.movie_title for frame in session.query(MovieDb).all()]

def edit_movie(name, rating):
    query_request = session.query(MovieDb).filter_by(movie_title = name).first()
    if query_request:
        query_request.movie_rating = rating
        session.commit()
        return True
    return False

print(all_movie_titles())
# add_to_db([{'title': 'There Will Be Blood', 'year': 2007, 'plot': 'The intersecting life stories of Daniel Plainview and Eli Sunday in early twentieth century California is presented. Miner turn oilman Daniel Plainview is a driven man who will do whatever it takes to achieve his goals. He works hard but he also takes advantage of those around him at their expense if need be. His business partner is his son H.W., who in reality he "acquired" when H.W.\'s biological single father, who worked on one of Daniel\'s rigs, got killed in a workplace accident. Daniel is deeply protective of H.W. if only for what H.W. brings to the partnership. Eli Sunday is one in a pair of twins, whose family farm Daniel purchases for the major oil deposit located on it. Eli, the local preacher and a self-proclaimed faith healer, wants the money from the sale of the property to finance his own church. The lives of the two competitive men often clash as Daniel pumps oil off the property and tries to acquire all the surrounding land at bargain prices to be able to build a pipeline to the coast, and as Eli tries to build his own religious empire.', 'poster_link': 'https://m.media-amazon.com/images/M/MV5BMjAxODQ4MDU5NV5BMl5BanBnXkFtZTcwMDU4MjU1MQ@@._V1_SX300.jpg', 'rt_rating': '91%'},
#            {'title': '12 Years a Slave', 'year': 2013, 'plot': "Based on an incredible true story of one man's fight for survival and freedom. In the pre-Civil War United States, Solomon Northup, a free black man from upstate New York, is abducted and sold into slavery. Facing cruelty personified by a malevolent slave owner, as well as unexpected kindnesses, Solomon struggles not only to stay alive, but to retain his dignity. In the twelfth year of his unforgettable odyssey, Solomon's chance meeting with a Canadian abolitionist will forever alter his life.", 'poster_link': 'https://m.media-amazon.com/images/M/MV5BMjExMTEzODkyN15BMl5BanBnXkFtZTcwNTU4NTc4OQ@@._V1_SX300.jpg', 'rt_rating': '95%'},
#            {'title': 'Inglourious Basterds', 'year': 2009, 'plot': 'In German-occupied France, young Jewish refugee Shosanna Dreyfus witnesses the slaughter of her family by Colonel Hans Landa. Narrowly escaping with her life, she plots her revenge several years later when German war hero Fredrick Zoller takes a rapid interest in her and arranges an illustrious movie premiere at the theater she now runs. With the promise of every major Nazi officer in attendance, the event catches the attention of the "Basterds", a group of Jewish-American guerrilla soldiers led by the ruthless Lt. Aldo Raine. As the relentless executioners advance and the conspiring young girl\'s plans are set in motion, their paths will cross for a fateful evening that will shake the very annals of history.', 'poster_link': 'https://m.media-amazon.com/images/M/MV5BODZhMWJlNjYtNDExNC00MTIzLTllM2ItOGQ2NGVjNDQ3MzkzXkEyXkFqcGc@._V1_SX300.jpg', 'rt_rating': '89%'},
#            {'title': 'In the Mood for Love', 'year': 2000, 'plot': 'Set in Hong Kong, 1962, Chow Mo-Wan is a newspaper editor who moves into a new building with his wife. At the same time, Su Li-zhen, a beautiful secretary and her executive husband also move in to the crowded building. With their spouses often away, Chow and Li-zhen spend most of their time together as friends. They have everything in common from noodle shops to martial arts. Soon, they are shocked to discover that their spouses are having an affair. Hurt and angry, they find comfort in their growing friendship even as they resolve not to be like their unfaithful mates.', 'poster_link': 'https://m.media-amazon.com/images/M/MV5BN2Q4NjllMDgtOTk2Zi00YzM1LWJmOTMtNmRiZDgyZGJmMjQzXkEyXkFqcGc@._V1_SX300.jpg', 'rt_rating': '92%'},
#            {'title': 'La haine', 'year': 1995, 'plot': 'The film follows three young men and their time spent in the French suburban "ghetto," over a span of twenty-four hours. Vinz, a Jew, Saïd, an Arab, and Hubert, a black boxer, have grown up in these French suburbs where high levels of diversity coupled with the racist and oppressive police force have raised tensions to a critical breaking point. During the riots that took place a night before, a police officer lost his handgun in the ensuing madness, only to leave it for Vinz to find. Now, with a newfound means to gain the respect he deserves, Vinz vows to kill a cop if his friend Abdel dies in the hospital, due the beating he received while in police custody.', 'poster_link': 'https://m.media-amazon.com/images/M/MV5BMThlMDA3NDYtZGM2Zi00NmJhLThlYWItZjViZTkzZWU1ZWRiXkEyXkFqcGc@._V1_SX300.jpg', 'rt_rating': '96%'},
#            {'title': 'Sound of Metal', 'year': 2019, 'plot': "Keeping at bay his inner demons by devoting himself to art, metal drummer, Ruben, has been living for the moment for the past four years. Then, while on tour with his lead-singer/girlfriend, Lou, Ruben realises that his hearing is rapidly deteriorating. As this sudden hearing loss turns his world upside down, and numbing fear paired with angry denial take over, Ruben reluctantly accepts to join a small deaf community overseen by Joe, a compassionate Vietnam War veteran. Now, Ruben needs to find some solid ground, understand that being deaf is not a handicap and that deafness isn't something to fix. But, is Ruben willing to accept his new life and learn how to be deaf?", 'poster_link': 'https://m.media-amazon.com/images/M/MV5BMWE5ZmYwNDEtYTYwMS00MTc0LTk2ZWItZTM1MjQ1ZDYzZGUzXkEyXkFqcGc@._V1_SX300.jpg', 'rt_rating': '97%'},
#            {'title': 'No Country for Old Men', 'year': 2007, 'plot': 'In rural Texas, welder and hunter Llewelyn Moss (Josh Brolin) discovers the remains of several drug runners who have all killed each other in an exchange gone violently wrong. Rather than report the discovery to the police, Moss decides to simply take the two million dollars present for himself. This puts the psychopathic killer, Anton Chigurh (Javier Bardem), on his trail as he dispassionately murders nearly every rival, bystander and even employer in his pursuit of his quarry and the money. As Moss desperately attempts to keep one step ahead, the blood from this hunt begins to flow behind him with relentlessly growing intensity as Chigurh closes in. Meanwhile, the laconic Sheriff Ed Tom Bell (Tommy Lee Jones) blithely oversees the investigation even as he struggles to face the sheer enormity of the crimes he is attempting to thwart.', 'poster_link': 'https://m.media-amazon.com/images/M/MV5BMjA5Njk3MjM4OV5BMl5BanBnXkFtZTcwMTc5MTE1MQ@@._V1_SX300.jpg', 'rt_rating': '93%'},
#            {'title': 'Birdman', 'year': 2014, 'plot': 'A portrait of Robert, a troubled but poetic soul struggling with his purgatorial existence in a hackney scrapyard.', 'poster_link': 'N/A', 'rt_rating': '91%'},
#            {'title': 'Parasite', 'year': 2019, 'plot': 'The Kims - mother and father Chung-sook and Ki-taek, and their young adult offspring, son Ki-woo and daughter Ki-jung - are a poor family living in a shabby and cramped half basement apartment in a busy lower working class commercial district of Seoul. Without even knowing it, they, especially Mr. and Mrs. Kim, literally smell of poverty. Often as a collective, they perpetrate minor scams to get by, and even when they have jobs, they do the minimum work required. Ki-woo is the one who has dreams of getting out of poverty by one day going to university. Despite not having that university education, Ki-woo is chosen by his university student friend Min, who is leaving to go to school, to take over his tutoring job to Park Da-hye, who Min plans to date once he returns to Seoul and she herself is in university. The Parks are a wealthy family who for four years have lived in their modernistic house designed by and the former residence of famed architect Namgoong. While Mr. and Mrs. Park are all about status, Mrs. Park has a flighty, simpleminded mentality and temperament, which Min tells Ki-woo to feel comfortable in lying to her about his education to get the job. In getting the job, Ki-woo further learns that Mrs. Park is looking for an art therapist for the Parks\' adolescent son, Da-song, Ki-woo quickly recommending his professional art therapist friend "Jessica", really Ki-jung who he knows can pull off the scam in being the easiest liar of the four Kims. In Ki-woo also falling for Da-hye, he begins to envision himself in that house, and thus the Kims as a collective start a plan for all the Kims, like Ki-jung using assumed names, to replace existing servants in the Parks\' employ in orchestrating reasons for them to be fired. The most difficult to get rid of may be Moon-gwang, the Parks\' housekeeper who literally came with the house - she Namgoong\'s housekeeper when he lived there - and thus knows all the little nooks and crannies of it better than the Parks themselves. The question then becomes how far the Kims can take this scam in their quest to become their version of the Parks.', 'poster_link': 'https://m.media-amazon.com/images/M/MV5BYjk1Y2U4MjQtY2ZiNS00OWQyLWI3MmYtZWUwNmRjYWRiNWNhXkEyXkFqcGc@._V1_SX300.jpg', 'rt_rating': '99%'},
#            {'title': 'Memories of Murder', 'year': 2003, 'plot': 'In 1986, in the province of Gyunggi, in South Korea, a second young and beautiful woman is found dead, raped and tied and gagged with her underwear. Detective Park Doo-Man and Detective Cho Yong-koo, two brutal and stupid local detectives without any technique, investigate the murder using brutality and torturing the suspects, without any practical result. The Detective Seo Tae-Yoon from Seoul comes to the country to help the investigations and is convinced that a serial-killer is killing the women. When a third woman is found dead in the same "modus-operandi", the detectives find leads of the assassin.', 'poster_link': 'https://m.media-amazon.com/images/M/MV5BYmRjOWE5NmMtYTdkYS00ODFlLWJiMTMtYzE2NDZlZjlkZDQ0XkEyXkFqcGc@._V1_SX300.jpg', 'rt_rating': 'N/A'},
#            {'title': 'Incendies', 'year': 2010, 'plot': "A mother's last wishes send twins Jeanne and Simon on a journey to the Middle East in search of their tangled roots. Adapted from Wajdi Mouawad's acclaimed play, Incendies tells the powerful and moving tale of two young adults' voyage to the core of deep-rooted hatred, never-ending wars and enduring love.", 'poster_link': 'https://m.media-amazon.com/images/M/MV5BYWFmMjdmNjctNzhhOC00ZmMzLTkwOGItMmVmZDU4MjE2MTYwXkEyXkFqcGc@._V1_SX300.jpg', 'rt_rating': '91%'}]
# )