from turtle import position
from symbol import yield_arg
from bs4 import BeautifulSoup
import requests
url="https://www.imdb.com/india/top-rated-indian-movies/"
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
def scrap_top_list():
    main_div=soup.find('div', class_ ='lister')
    tbody=main_div.find('tbody',class_ ='lister-list')
    trs=tbody.find_all('tr')
    movie_ranks=[]
    movie_name=[]
    year_of_realease=[]
    movie_urls=[]
    movie_ratings=[]
    for tr in trs:
        position=tr.find('td',class_="titleColumn").get_text().strip()
        rank=""
        for i in position:
            if "," not in i:
                rank=rank+i
            else:
                break
        movie_ranks.append(rank)
        title=tr.find('td',class_="titleColumn").a.get_text()
        movie_name.append(title)
        year=tr.find('td',class_="titleColumn").span.get_text()
        year_of_realease.append(year)
        imdb_rating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        movie_ratings.append(imdb_rating)
        link=tr.find('td',class_="titleColumn").a['href']
        movie_link="https://www.imdb.com"+link
        movie_urls.append(movie_link)
    top_movies=[]
    details={'position':' ','name':' ','year':' ','rating':' ','url':' '}
    for i in range(0,len(movie_ranks)):
        details['position']= (movie_ranks[i])
        details['name']=str(movie_name[i])
        year_of_realease[i]=year_of_realease[i][1:5]
        details['year']=int(year_of_realease[i])
        details['rating']=float(movie_ratings[i])
        details['url']=movie_urls[i]
        top_movies.append(details.copy())
    return(top_movies)
top_list_movies=(scrap_top_list())
def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[] for i in years}
    for i in movies:
        # name=i
        year=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i) 
    return movie_dict
group_by_year(top_list_movies) 
dec_arg=group_by_year(top_list_movies)
def group_by_decade(movies):
    moviedec={}
    list1=[]
    for index in movies:
        mod=index%10
        decade=index-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movies:
            if x<=dec10 and x>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
    return(moviedec)
print(group_by_decade(dec_arg))
