import time
from bs4 import BeautifulSoup
import requests
import random
import re


class Quran:
    chapters = {
        1: "Al-Fatihah (the Opening)",
        2: "Al-Baqarah (the Cow)",
        3: "Aali Imran (the Family of Imran)",
        4: "An-Nisa’ (the Women)",
        5: "Al-Ma’idah (the Table)",
        6: "Al-An’am (the Cattle)",
        7: "Al-A’raf (the Heights)",
        8: "Al-Anfal (the Spoils of War)",
        9: "At-Taubah (the Repentance)",
        10: "Yunus (Yunus)",
        11: "Hud (Hud)",
        12: "Yusuf (Yusuf)",
        13: "Ar-Ra’d (the Thunder)",
        14: "Ibrahim (Ibrahim)",
        15: "Al-Hijr (the Rocky Tract)",
        16: "An-Nahl (the Bees)",
        17: "Al-Isra’ (the Night Journey)",
        18: "Al-Kahf (the Cave)",
        19: "Maryam (Maryam)",
        20: "Ta-Ha (Ta-Ha)",
        21: "Al-Anbiya’ (the Prophets)",
        22: "Al-Haj (the Pilgrimage)",
        23: "Al-Mu’minun (the Believers)",
        24: "An-Nur (the Light)",
        25: "Al-Furqan (the Criterion)",
        26: "Ash-Shu’ara’ (the Poets)",
        27: "An-Naml (the Ants)",
        28: "Al-Qasas (the Stories)",
        29: "Al-Ankabut (the Spider)",
        30: "Ar-Rum (the Romans)",
        31: "Luqman (Luqman)",
        32: "As-Sajdah (the Prostration)",
        33: "Al-Ahzab (the Combined Forces)",
        34: "Saba’ (the Sabeans)",
        35: "Al-Fatir (the Originator)",
        36: "Ya-Sin (Ya-Sin)",
        37: "As-Saffah (Those Ranges in Ranks)",
        38: "Sad (Sad)",
        39: "Az-Zumar (the Groups)",
        40: "Ghafar (the Forgiver)",
        41: "Fusilat (Distinguished)",
        42: "Ash-Shura (the Consultation)",
        43: "Az-Zukhruf (the Gold)",
        44: "Ad-Dukhan (the Smoke)",
        45: "Al-Jathiyah (the Kneeling)",
        46: "Al-Ahqaf (the Valley)",
        47: "Muhammad (Muhammad)",
        48: "Al-Fat’h (the Victory)",
        49: "Al-Hujurat (the Dwellings)",
        50: "Qaf (Qaf)",
        51: "Adz-Dzariyah (the Scatterers)",
        52: "At-Tur (the Mount)",
        53: "An-Najm (the Star)",
        54: "Al-Qamar (the Moon)",
        55: "Ar-Rahman (the Most Gracious)",
        56: "Al-Waqi’ah (the Event)",
        57: "Al-Hadid (the Iron)",
        58: "Al-Mujadilah (the Reasoning)",
        59: "Al-Hashr (the Gathering)",
        60: "Al-Mumtahanah (the Tested)",
        61: "As-Saf (the Row)",
        62: "Al-Jum’ah (Friday)",
        63: "Al-Munafiqun (the Hypocrites)",
        64: "At-Taghabun (the Loss & Gain)",
        65: "At-Talaq (the Divorce)",
        66: "At-Tahrim (the Prohibition)",
        67: "Al-Mulk – (the Kingdom)",
        68: "Al-Qalam (the Pen)",
        69: "Al-Haqqah (the Inevitable)",
        70: "Al-Ma’arij (the Elevated Passages)",
        71: "Nuh (Nuh)",
        72: "Al-Jinn (the Jinn)",
        73: "Al-Muzammil (the Wrapped)",
        74: "Al-Mudaththir (the Cloaked)",
        75: "Al-Qiyamah (the Resurrection)",
        76: "Al-Insan (the Human)",
        77: "Al-Mursalat (Those Sent Forth)",
        78: "An-Naba’ (the Great News)",
        79: "An-Nazi’at (Those Who Pull Out)",
        80: "‘Abasa (He Frowned)",
        81: "At-Takwir (the Overthrowing)",
        82: "Al-Infitar (the Cleaving)",
        83: "Al-Mutaffifin (Those Who Deal in Fraud)",
        84: "Al-Inshiqaq (the Splitting Asunder)",
        85: "Al-Buruj (the Stars)",
        86: "At-Tariq (the Nightcomer)",
        87: "Al-A’la (the Most High)",
        88: "Al-Ghashiyah (the Overwhelming)",
        89: "Al-Fajr (the Dawn)",
        90: "Al-Balad (the City)",
        91: "Ash-Shams (the Sun)",
        92: "Al-Layl (the Night)",
        93: "Adh-Dhuha (the Forenoon)",
        94: "Al-Inshirah (the Opening Forth)",
        95: "At-Tin (the Fig)",
        96: "Al-‘Alaq (the Clot)",
        97: "Al-Qadar (the Night of Decree)",
        98: "Al-Bayinah (the Proof)",
        99: "Az-Zalzalah (the Earthquake)",
        100: "Al-‘Adiyah (the Runners)",
        101: "Al-Qari’ah (the Striking Hour)",
        102: "At-Takathur (the Piling Up)",
        103: "Al-‘Asr (the Time)",
        104: "Al-Humazah (the Slanderer)",
        105: "Al-Fil (the Elephant)",
        106: "Quraish (Quraish)",
        107: "Al-Ma’un (the Assistance)",
        108: "Al-Kauthar (the River of Abundance)",
        109: "Al-Kafirun (the Disbelievers)",
        110: "An-Nasr (the Help)",
        111: "Al-Masad (the Palm Fiber)",
        112: "Al-Ikhlas (the Sincerity)",
        113: "Al-Falaq (the Daybreak)",
        114: "An-Nas (Mankind)"}
    verses = {
        1: 7,
        2: 286,
        3: 200,
        4: 176,
        5: 120,
        6: 165,
        7: 206,
        8: 75,
        9: 129,
        10: 109,
        11: 123,
        12: 111,
        13: 43,
        14: 52,
        15: 99,
        16: 128,
        17: 111,
        18: 110,
        19: 98,
        20: 135,
        21: 112,
        22: 78,
        23: 118,
        24: 64,
        25: 77,
        26: 227,
        27: 93,
        28: 88,
        29: 69,
        30: 60,
        31: 34,
        32: 30,
        33: 73,
        34: 54,
        35: 45,
        36: 83,
        37: 182,
        38: 88,
        39: 75,
        40: 85,
        41: 54,
        42: 53,
        43: 89,
        44: 59,
        45: 37,
        46: 35,
        47: 38,
        48: 29,
        49: 18,
        50: 45,
        51: 60,
        52: 49,
        53: 62,
        54: 55,
        55: 78,
        56: 96,
        57: 29,
        58: 22,
        59: 24,
        60: 13,
        61: 14,
        62: 11,
        63: 11,
        64: 18,
        65: 12,
        66: 12,
        67: 30,
        68: 52,
        69: 52,
        70: 44,
        71: 28,
        72: 28,
        73: 20,
        74: 56,
        75: 40,
        76: 31,
        77: 50,
        78: 40,
        79: 46,
        80: 42,
        81: 29,
        82: 19,
        83: 36,
        84: 25,
        85: 22,
        86: 17,
        87: 19,
        88: 26,
        89: 30,
        90: 20,
        91: 15,
        92: 21,
        93: 11,
        94: 8,
        95: 8,
        96: 19,
        97: 5,
        98: 8,
        99: 8,
        100: 11,
        101: 11,
        102: 8,
        103: 3,
        104: 9,
        105: 5,
        106: 4,
        107: 7,
        108: 3,
        109: 6,
        110: 3,
        111: 5,
        112: 4,
        113: 5,
        114: 6}

    def __init__(self, chapter_no=None, verse_no=None):
        self.chapter_no = chapter_no
        self.verse_no = verse_no

    def parse_verse(self, chapter, verse):
        html_text = requests.get(
            f'https://quran.com/{chapter}/{verse}').text
        site = BeautifulSoup(html_text, 'lxml')
        verse_div = site.find_all(
            'div', class_='verse__translations english')[1]
        verse_par = verse_div.find(
            'p', class_='text text--grey text--medium text--regular translation').text
        return verse_par.strip()

    def check_num(self):
        str_ptrn = re.compile(r"""[a-zA-Z_`~!@#$%^&*;:'"?/\.,+=/*]""")
        match_ptrn = str_ptrn.search(str(self.chapter_no))
        if match_ptrn:
            return 'invalid chapter no'
        else:
            v_ptrn = str_ptrn.search(str(self.verse_no))
            if v_ptrn:
                return 'invalid verse no'
            else:
                if 1 <= int(self.chapter_no) <= 114:
                    return None
                else:
                    return 'Invalid chapter no'

    def get_verse(self):
        if self.check_num() == None:
            int(self.chapter_no)
            if type(self.verse_no) != int and self.verse_no.find('-') != -1:
                min, max = self.verse_no.split('-')
                verse = ''
                for x in range(int(min), int(max)+1):
                    verse += self.parse_verse(self.chapter_no, x) + '\n'
                message = f"""Chapter Name: {self.chapters[int(self.chapter_no)]}
Chapter No. {self.chapter_no}
Verse Number. {self.verse_no}

***{verse}***"""
                return message
            else:
                verse = self.parse_verse(self.chapter_no, int(self.verse_no))
                message = f"""Chapter Name: {self.chapters[int(self.chapter_no)]}
Chapter No. {self.chapter_no}
Verse Number. {self.verse_no}

***{verse}***"""
                return message
        else:
            return self.check_num()

    @staticmethod
    def random_verse():
        chapter_no = random.randrange(1, 115)
        verse_no = random.randrange(1, Quran.verses[chapter_no]+1)
        return Quran(chapter_no, verse_no).get_verse()
