#!/usr/bin/python3

from telegram import InlineKeyboardButton

not_interface = False
default_time = 0.0
roots = [560950095]
limit = 2000000000
seconds_limits_album = 40000
max_songs = 4000
telegram_file_api_limit = 1500000000
telegram_audio_api_limit = 50000000
db_file = "dwsongs.db"
loc_dir = "Songs/"
ini_file = "settings.ini"
photo = "example.png"
bot_name = "PieRatedBot"
api_chart = "https://api.deezer.com/chart"
api_artist = "https://api.deezer.com/artist/%s"
api_type1 = "https://api.deezer.com/search/{}/?q={}"
api_type2 = "https://api.deezer.com/search/?q={}:\"{}\""
song_default_image = "https://e-cdns-images.dzcdn.net/images/cover/1800x1800-000000-80-0-0.jpg"
services_supported = ["spotify", "deezer"]
comandss = ["start", "settings", "info", "shazam", "help"]
settingss = ["quality", "tongue"]
qualities = ["FLAC", "MP3_320", "MP3_256", "MP3_128"]
send_image_track_query = "Track: %s \nArtist: %s \nAlbum: %s \nDate: %s"
send_image_album_query = "Album: %s \nArtist: %s \nDate: %s \nTracks amount: %d"
send_image_artist_query = "Artist: %s \nAlbum numbers: %d \nFans on Deezer: %d"
tags_query = "Album: %s\nDate: %s\nLabel: %s\nGenre: %s"
info_msg = "Version: %s\nName: @%s\nCreator: %s\nChannel: %s\nUsers: %d\nTotal downloads: %d"
send_image_playlist_query = "Creation: %s \nUser: %s \nTracks amount: %d"
insert_query = "INSERT INTO DWSONGS (id, query, quality) values ('%s', '%s', '%s')"
where_query = "SELECT query FROM DWSONGS WHERE id = '{}' and quality = '{}'"
user_exist = "SELECT chat_id FROM CHAT_ID where chat_id = '%d'"
share_message = "tg://msg?text=Start @%s for download all the songs which you want ;)" % bot_name
start_message = "Welcome to @%s \nPress '/' to get commands list" % bot_name
not_supported_links = "The bot doesn't support this link %s :("

help_message = (
	"/start: Start the bot" +
	"\n\n/settings: Manage settings" +
	"\n\n/shazam: Identify a song by a voice or audio message (You can do without calling this command, just send the media)" +
	"\n\n/help: Show this message" +
	"\n\n" +
	"Just send a spotify or deezer link to download, or type what you are looking for"
)

end_keyboard = [
	[
		InlineKeyboardButton(
			"SHARE",
			url = share_message
		)
	]
]

qualities_keyboard = [
	[
		InlineKeyboardButton(
			qualities[a],
			callback_data = qualities[a]
		),
		InlineKeyboardButton(
			qualities[a + 1],
			callback_data = qualities[a + 1]
		)
	] for a in range(
		0, len(qualities), 2
	)
]

first_time_keyboard = [
	[
		InlineKeyboardButton(
			"Pie Rated Bot",
			url = "t.me/%s?start" % bot_name
		)
	]
]

queries = {
	"top": {
		"query": "%s/top?limit=30",
		"text": "TOP 30"
	},

	"albums": {
		"query": "%s/albums",
		"text": "ALBUMS"
	},

	"radio": {
		"query": "%s/radio",
		"text": "RADIO"
	},

	"related": {
		"query": "%s/related",
		"text": "RELATED"
	},

	"download": {
		"text": "Download"
	},

	"info": {
		"text": "Info"
	},

	"back": {
		"text": "BACK"
	},

	"s_art": {
		"query": "art: %s",
		"text": "Search by artist"
	},

	"s_alb": {
		"query": "alb: %s",
		"text": "Search by album"
	},

	"s_pla": {
		"query": "pla: %s",
		"text": "Search playlist"
	},

	"s_lbl": {
		"query": "lbl: %s",
		"text": "Search label"
	},

	"s_trk": {
		"query": "trk: %s",
		"text": "Search track"
	},

	"s_": {
		"query": "%s",
		"text": "Global search"
	}
}
