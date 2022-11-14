from newsapi_client import NewsApiClient
import json



news_client = NewsApiClient(api_key="0f374cdc43fc41f78fb481fe3cdcdc9e", session=None)

data = news_client.get_by_headline(q="Star Wars")


d = json.dumps(data)


print(json.loads(d)['status'])



#{'status': 'ok', 'totalResults': 1, 'articles': 
#        [
#            {'source': {'id': 'polygon', 'name': 'Polygon'}, 'author': 'Michael McWhertor', 'title': 'Studio Ghibli’s Star Wars project is a surprise Grogu short on Disney Plus', 'description': 'Star Wars Zen: Grogu and Dust Bunnies from Studio Ghibli and Lucasfilm is streaming on Disney Plus on Nov. 12. The surprise release of the The Mandalorian’s “Baby Yoda” animated short arrives on Disney Plus’ third anniversary.', 'url': 'https://www.polygon.com/star-wars/23453685/studio-ghibli-star-wars-grogu-dust-bunnies-disney-plus-baby-yoda', 'urlToImage': 'https://cdn.vox-cdn.com/thumbor/CvOvwMUy6MgFk-7jBSqUuMXu3r0=/204x0:1722x795/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/22144357/Screen_Shot_2020_12_04_at_7.00.13_AM__2_.png', 'publishedAt': '2022-11-12T00:12:58Z', 'content': 'Lucasfilm and Studio Ghiblis surprise collaboration is now even more surprising because its available to stream Saturday, Nov. 12, on Disney Plus. The new animated short, titled Star Wars Zen: Grogu …
