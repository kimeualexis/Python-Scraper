from bs4 import BeautifulSoup
import requests
import csv


def scrape_site(url):
	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')

	csv_file = open('data.csv', 'w')
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['headline', 'summary', 'video_link'])

	for article in soup.find_all('article'):
		headline = article.a.text
		print(headline)

		summary = article.find('div', class_='entry-content').p.text
		print(summary)

		vid_src = article.find('iframe', class_='youtube-player')['src']
		vid_id = vid_src.split('/')[4]
		vid_id = vid_id.split('?')[0]

		yt_link = f'https://youtube.com/watch?v={vid_id}'
		print(yt_link)

		csv_writer.writerow([headline, summary, yt_link])
	csv_file.close()


scrape_site('')
