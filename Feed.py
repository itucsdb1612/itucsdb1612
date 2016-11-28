class Feed:
    def __init__(self, id, date, userId, bookId, typeId):
        self.id = id
        self.date=date
        self.userId = userId
        self.bookId = bookId
        self.typeId = typeId

def insert_feed(cursor,feed):
    statement = """INSERT INTO FEEDS (DATE,USERID,BOOKID,TYPEID) VALUES (
                %s, %s, %s, %s
                )"""
    cursor.execute(statement,(feed.date,feed.userId,feed.bookId,feed.typeId));
def get_all_feeds(cursor):
    statement = """SELECT FEEDS.DATE, SITEUSER.USERNAME, BOOKS.TITLE, FEEDTYPES.TYPE FROM FEEDS, SITEUSER, BOOKS, FEEDTYPES
                    WHERE (FEEDS.USERID=SITEUSER.USERID) AND (FEEDS.BOOKID=BOOKS.BOOKID) AND (FEEDS.TYPEID=FEEDTYPES.ID) """
    cursor.execute(statement);
