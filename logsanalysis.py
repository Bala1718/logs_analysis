#!/usr/bin/env python3
import psycopg2
import time


def connect():
    return psycopg2.connect("dbname=news")


query1 = """
SELECT articles.title, COUNT(*) As num
FROM ARTICLES
Join log
ON log.path LIKE concat('/article/%',articles.slug)
GROUP BY articles.title
ORDER BY num DESC
LIMIT 3
"""

query2 = """
SELECT authors.name, COUNT(*) AS num
FROM Authors
JOIN articles
ON authors.id = articles.author
JOIN log
ON log.path like concat('/article/%', articles.slug)
GROUP BY authors.name
ORDER BY num DESC
LIMIT 3
"""

query3 = 
"SELECT to_char(date,'Mon DD,YYYY')as date,err_prc from err_perc where err_prc>1.0"


def get_popular_articles():
    db = connect()
    c = db.cursor()
    c.execute(query1)
    results = run_query(query1)
    print('\n Top Views')
    count = 1
    for i in results:
        number = '(' + str(count) + ') "'
        title = i[0]
        views = '" with ' + str(i[1]) + " views"
        print(number + title + views)
    count += 1
    
    def get_popular_authors():
        db=connect() 
        c=db.cursor()
        c.execute(query2)    
        results = run_query(query2)
        print('\n Popular author views')
        count = 1
        for i in results:
            print('(' + str(count) + ') ' + i[0] + ' with ' + str(i[1]) + " views")
            count += 1
            
            
def get_days_with_errors():
    db = connect()
    c = db.cursor()
    c.execute(query3)
    results = run_query(query3)

    # Resutls
    print('DAYS WITH MORE THAN 1% ERRORS:')
    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print(date + " -- " + errors)


if __name__ == "__main__":
    print('Results-\n')
get_popular_articles()
get_popular_authors()
get_days_with_errors()









        



	   

