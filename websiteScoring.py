from mysql.connector import MySQLConnection, Error
from scoring_dbconfig import read_db_config
from bs4 import BeautifulSoup as BS
import datetime
import os

def calc_score(file):
    content = open("data\\"+ file, "r")
    soup = BS(content, "html.parser")
    score = 0
    score += 3 * len(soup.find_all("div"))
    score += len(soup.find_all("p"))
    score += 3 * len(soup.find_all("h1"))
    score += 2 * len(soup.find_all("h2"))
    score += 5 * len(soup.find_all("html"))
    score += 5 * len(soup.find_all("body"))
    score += 10 * len(soup.find_all("header"))
    score += 10 * len(soup.find_all("footer"))
    score -= len(soup.find_all("font"))
    score -= 2 * len(soup.find_all("center"))
    score -= 2 * len(soup.find_all("big"))
    score -= len(soup.find_all("strike"))
    score -= 2 * len(soup.find_all("tt"))
    score -= 5 * len(soup.find_all("frameset"))
    score -= 5 * len(soup.find_all("frame"))
    content.close()
    return score

def insert_file(file):
    name = str(file)
    score = calc_score(file)
    retrieval = datetime.datetime.now().strftime("%Y-%m-%d")
    query = "INSERT INTO scoring_db(file, score, retrieval)" \
            "VALUES(%s, %s, %s)"
    args = (name, score, retrieval)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def main():
    for file in os.listdir("data"):
        if file.endswith(".html"):
            insert_file(file)
        else:
            continue

if __name__ == "__main__":
    main()
