import os

import requests
import openpyxl
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.request
import time
import numpy as np
import cv2
from PIL import Image


# Make a GET request to fetch the raw HTML content


# ursl = [
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81-Time-Park/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B5%D0%B2%D0%B5%D1%80%D0%BD%D1%8B%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8-%D0%B2-%D0%94%D0%BE%D0%BB%D0%B3%D0%BE%D0%BF%D1%80%D1%83%D0%B4%D0%BD%D0%BE%D0%BC/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9A%D0%BB%D1%83%D0%B1-SPACE/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/C%D0%B0%D1%83%D0%BD%D0%B0-%D0%9F%D0%B5%D1%80%D0%B2%D0%BE%D0%BC%D0%B0%D0%B9%D1%81%D0%BA%D0%B0%D1%8F-85/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/SPA-%D1%81%D0%B0%D1%83%D0%BD%D0%B0-%D0%92%D0%BE%D0%B7%D1%80%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/VIP-%D0%91%D0%B0%D0%BD%D1%8F-%D0%BD%D0%B0-%D0%B4%D1%80%D0%BE%D0%B2%D0%B0%D1%85-%D0%BD%D0%B0-%D0%9D%D0%BE%D0%B2%D0%BE%D0%BC-%D0%90%D1%80%D0%B1%D0%B0%D1%82%D0%B5-%D0%9C%D0%98%D0%A0%D0%AA-%D0%91%D0%90%D0%9D%D0%98/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/VIP-club-Premium-GALLERY/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F-%D0%91%D0%B0%D0%BD%D1%8F/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%90%D0%BB%D1%8C%D0%BF%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F-%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BD%D1%8F/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%B8-%D0%BD%D0%B0-%D0%90%D1%81%D1%82%D1%80%D0%B0%D1%85%D0%B0%D0%BD%D1%81%D0%BA%D0%BE%D0%BC-%D0%BF%D0%B5%D1%80%D0%B5%D1%83%D0%BB%D0%BA%D0%B5-%D0%B2-%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B5-%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B5/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%B8-%D1%83-%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D0%B8-%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%BF%D0%BE%D0%BB%D0%B8%D1%82%D0%B5%D0%BD%D0%B0-%D0%91%D0%B0%D0%B1%D1%83%D1%88%D0%BA%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D1%8F-%D0%A1%D0%BE%D0%BA%D0%BE%D0%BB%D0%B8%D0%BD%D0%B0%D1%8F-%D0%B3%D0%BE%D1%80%D0%B0/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%B8-%D0%BD%D0%B0-%D0%B2%D0%BE%D0%B4%D0%B5/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%B8-%D0%BF%D0%BE%D1%81%D1%91%D0%BB%D0%BA%D0%B0-%D0%97%D0%B0%D0%B2%D0%B5%D1%82%D1%8B-%D0%98%D0%BB%D1%8C%D0%B8%D1%87%D0%B0/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%BD%D0%BE-%D0%BE%D0%B7%D0%B4%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81-%D0%BD%D0%B0-%D0%94%D1%83%D0%B1%D0%BD%D0%B8%D0%BD%D1%81%D0%BA%D0%BE%D0%B9/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-%D0%B4%D0%B2%D0%BE%D1%80-%D0%BD%D0%B0-%D0%9B%D0%BE%D0%B1%D0%BD%D0%B5%D0%BD%D1%81%D0%BA%D0%BE%D0%B91/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-%D0%B4%D0%B2%D0%BE%D1%80%D0%B8%D0%BA--%D0%A0%D1%83%D1%87%D0%B5%D1%91%D0%BA/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%94%D0%B5%D0%B2%D1%8F%D1%82%D1%8B%D0%B9-%D0%B2%D0%B0%D0%BB/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81-%D0%90%D0%BD%D0%B0%D0%BD%D0%B0%D1%81/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81-%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BB%D1%83%D0%B1-%D0%9D%D0%B5%D0%BF%D1%82%D1%83%D0%BD/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81-%D0%A0%D0%B5%D0%B7%D0%B8%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D1%8F-%D0%9A%D1%83%D0%BD%D1%86%D0%B5%D0%B2%D0%BE/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A8%D0%B0%D0%BB%D0%B5-%D0%BE%D1%82%D0%B5%D0%BB%D1%8C-%D0%A2%D0%B0%D0%B5%D0%B6%D0%BD%D1%8B%D0%B5-%D0%B4%D0%B0%D1%87%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/-%D0%91%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81-%D0%9B%D0%B5%D0%B3%D0%BA%D0%B8%D0%B9-%D0%BF%D0%B0%D1%80/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D1%8F-%D0%90%D0%BA%D0%B2%D0%B0%D0%BB%D0%B8%D0%BD%D0%B0/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D1%8F--2-%D0%96%D0%B0%D1%80-%D0%9F%D1%82%D0%B8%D1%86%D0%B0/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D1%8F-%D0%BD%D0%B0-%D0%B4%D1%80%D0%BE%D0%B2%D0%B0%D1%85-%D0%B2-%D0%96%D0%B5%D0%BB%D0%B5%D0%B7%D0%BD%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B6%D0%BD%D0%BE%D0%BC/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D1%8F-%D0%BD%D0%B0-%D0%B4%D1%80%D0%BE%D0%B2%D0%B0%D1%85-%D0%B2-%D0%9E%D1%81%D1%82%D0%B0%D1%84%D1%8C%D0%B5%D0%B2%D0%BE/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D1%8F-%D0%BD%D0%B0-%D0%9C%D0%BE%D1%80%D0%BE%D0%B7%D0%B5/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D1%8F-%D0%BD%D0%B0-%D0%A1%D0%BE%D0%B2%D1%85%D0%BE%D0%B7%D0%BD%D0%BE%D0%B9-%D1%83%D0%BB-8-/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D1%8F-%D0%A8%D0%B0%D1%85%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D1%81%D0%BA%D0%B5%D1%82-%D0%91%D0%B0%D1%80/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B5%D0%BB%D1%8B%D0%B5-%D0%A1%D1%82%D0%BE%D0%BB%D0%B1%D1%8B-%D0%B2-%D0%94%D0%BE%D0%BC%D0%BE%D0%B4%D0%B5%D0%B4%D0%BE%D0%B2%D0%BE/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D1%8B%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%92%D0%B8%D0%B4%D0%BD%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F-%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%92%D0%BD%D1%83%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%92%D0%BE%D1%80%D0%BE%D0%BD%D1%86%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8-%D0%B2-%D0%BF%D0%BE%D1%81%D0%B5%D0%BB%D0%BA%D0%B5-%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%BE%D0%BC/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%92%D0%BE%D1%81%D1%82%D1%80%D1%8F%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%92%D1%83%D0%B3%D0%B8-%D0%92%D1%83%D0%B3%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%92%D1%8F%D1%82%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F-%D0%B2-%D0%94%D0%B7%D0%B5%D1%80%D0%B6%D0%B8%D0%BD%D1%81%D0%BA%D0%BE%D0%BC/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F-%D0%B2-%D0%9E%D0%B4%D0%B8%D0%BD%D1%86%D0%BE%D0%B2%D0%BE/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%94%D0%B5%D0%B4%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%94%D0%BE%D0%B7%D0%B0%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%94%D0%BE%D0%BB%D0%B3%D0%BE%D0%BF%D1%80%D1%83%D0%B4%D0%BD%D0%B5%D0%BD%D1%81%D0%BA%D0%B0%D1%8F-%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%96%D1%83%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9A%D0%B0%D0%BB%D0%B8%D1%82%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9A%D0%B0%D0%BF%D0%BE%D1%82%D0%BD%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9A%D0%B5%D0%B4%D1%80%D0%BE%D0%B2%D1%8B%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9A%D0%BE%D1%81%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%BF%D1%80%D0%B5%D1%81%D0%BD%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9A%D1%83%D0%BD%D1%86%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8-/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9B%D0%B5%D1%84%D0%BE%D1%80%D1%82%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9B%D1%83%D0%B3%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9B%D1%8B%D1%82%D0%BA%D0%B0%D1%80%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9B%D1%8C%D0%B2%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9B%D1%8E%D0%B1%D0%BB%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9C%D0%B0%D1%80%D1%8C%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8-%D0%BD%D0%B0-%D1%83%D0%BB%D0%B8%D1%86%D0%B5-%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B5-%D0%9F%D0%BE%D0%BB%D1%8F/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9C%D1%8B%D1%82%D0%B8%D1%89%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9D%D0%B0%D0%B7%D0%B0%D1%80%D1%8C%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9D%D0%B0%D1%85%D0%B0%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9E%D0%B7%D0%B4%D0%BE%D1%80%D0%BE%D0%B2%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE-%D0%B1%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81-%D0%9D%D0%B5%D0%BA%D1%80%D0%B0%D1%81%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%91%D0%B0%D0%BD%D0%B8-%D0%B2-%D0%9D%D0%B5%D0%BA%D1%80%D0%B0%D1%81%D0%BE%D0%B2%D0%BA%D0%B5/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9D%D0%BE%D0%B2%D0%BE%D0%BD%D0%B8%D0%BA%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9E%D0%B1%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F--1-%D0%B2-%D0%9C%D0%B0%D0%BB%D0%B0%D1%85%D0%BE%D0%B2%D0%BA%D0%B5/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9E%D0%B1%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F-%D0%B2-%D0%9B%D1%8B%D1%82%D0%BA%D0%B0%D1%80%D0%B8%D0%BD%D0%BE/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9E%D0%B1%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F-%D0%B2-%D0%9F%D0%BE%D0%B4%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B5-%D0%91%D0%B0%D0%BD%D1%8C%D0%BA%D0%B0/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9E%D0%B1%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F-%D0%BD%D0%B0-%D0%A1%D0%BE%D0%B2%D1%85%D0%BE%D0%B7%D0%BD%D0%BE%D0%B9-%D1%83%D0%BB-55/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9E%D0%B1%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F-%D0%B2-%D0%9F%D0%BE%D0%B4%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B5/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9E%D0%B1%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D1%91%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D1%8F-%D1%81%D0%B0%D1%83%D0%BD%D0%B0-%D0%BD%D0%B0-%D0%9E%D1%87%D0%B0%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B9/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9F%D0%B5%D1%80%D0%BB%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F-%D0%B2-%D0%9C%D1%8B%D1%82%D0%B8%D1%89%D0%B0%D1%85/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9F%D0%BE%D0%B4%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B5-%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9F%D0%BE%D0%BA%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81-%D0%A0%D0%B5%D1%83%D1%82%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8-%D0%B8-%D1%81%D0%B0%D1%83%D0%BD%D1%8B/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A0%D0%B6%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8--%D0%BA%D0%B0%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5-%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%B5%D0%BC/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F-%D0%B2-%D0%94%D1%83%D0%B1%D1%80%D0%BE%D0%B2%D0%B8%D1%86%D0%B0%D1%85/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F-%D0%B2-%D0%9F%D0%BE%D0%B4%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B5/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F-%D0%BD%D0%B0-%D0%B4%D1%80%D0%BE%D0%B2%D0%B0%D1%85-555/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B0%D1%8F-%D0%B1%D0%B0%D0%BD%D1%8F-%D0%BD%D0%B0-%D0%B4%D1%80%D0%BE%D0%B2%D0%B0%D1%85-%D0%B2-%D0%90%D0%BA%D1%81%D0%B8%D0%BD%D1%8C%D0%B8%D0%BD%D0%BE/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8-%D0%B2-%D0%91%D0%B0%D0%BB%D0%B0%D1%88%D0%B8%D1%85%D0%B5/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%91%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81-%D0%A1%D0%B0%D0%BD%D0%B4%D1%83%D0%BD%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%93%D0%9E%D0%90/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%9A%D0%BE%D0%BB%D0%B8%D0%B1%D1%80%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%9D%D0%B0%D0%B4%D0%B5%D0%B6%D0%B4%D0%B0/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%9D%D0%B8%D1%80%D0%B2%D0%B0%D0%BD%D0%B0-%D0%97%D0%B0%D0%BB-%D0%9A%D0%BE%D1%80%D0%B0%D0%B1%D0%BB%D1%8C/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%9D%D0%BE%D0%B2%D1%8B%D0%B9-%D0%BC%D0%B8%D1%80/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%9E%D1%81%D1%82%D1%80%D0%BE%D0%B2/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%9F%D0%B0%D0%BB%D1%8C%D0%BC%D0%B8%D1%80%D0%B0/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%96%D0%B5%D0%BC%D1%87%D1%83%D0%B6%D0%B8%D0%BD%D0%B0-%D0%9D%D0%B8%D0%BB%D0%B0-/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-BonApart/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%9F%D0%BE-%D0%A6%D0%B0%D1%80%D1%81%D0%BA%D0%B8-%D0%9F%D0%B5%D1%80%D0%BE%D0%B2%D0%BE/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%91%D1%83%D1%82%D0%BE%D0%B2%D0%BE/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%B8-%D1%85%D0%B0%D0%BC%D0%BC%D0%B0%D0%BC-%D0%B2-%D0%9C%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D0%B0-%D0%A1%D0%BB%D0%B0%D0%B2%D0%B8%D1%8F-%D0%9E%D1%82%D0%B5%D0%BB%D1%8C/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%BD%D0%B0-%D0%9B%D0%B8%D0%B4%D0%B5%D1%80-%D0%BD%D0%B0-%D0%9F%D0%B5%D1%80%D0%B2%D0%BE%D0%BC%D0%B0%D0%B9%D1%81%D0%BA%D0%BE%D0%B9/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%BD%D0%B0-%D0%91%D0%B0%D0%B9%D0%BA%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%BE%D0%B9/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%BD%D0%B0-%D0%9B%D0%B8%D1%85%D0%BE%D0%B1%D0%BE%D1%80%D0%B0%D1%85/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%BD%D0%B0-%D0%A0%D1%8F%D0%B7%D0%B0%D0%BD%D1%81%D0%BA%D0%BE%D0%BC-%D0%BF%D1%80%D0%BE%D1%81%D0%BF%D0%B5%D0%BA%D1%82%D0%B5/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%BD%D0%B0-%D0%A4%D1%80%D1%83%D0%BD%D0%B7%D0%B5%D0%BD%D1%81%D0%BA%D0%BE%D0%B9/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%BD%D0%B0-%D0%A8%D0%B0%D0%B1%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B5/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%9E%D1%81%D1%82%D0%B0%D0%BD%D0%BA%D0%B8%D0%BD%D0%BE/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%A0%D0%B5%D1%87%D0%BD%D0%BE%D0%B9-%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%A4%D0%B5%D0%BD%D0%B8%D0%BA%D1%81/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%BA%D0%B0%D1%84%D0%B5-%D0%A1%D1%83%D0%BC%D0%B0%D1%85/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%BA%D0%BB%D1%83%D0%B1-%D0%9C%D0%B0%D1%80%D1%80%D0%B0%D0%BA%D0%B5%D1%88/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B5%D0%BB%D0%B5%D0%B7%D0%BD%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%BB%D0%B0%D0%B2%D1%8F%D0%BD%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8-%D0%B2-%D0%A9%D1%91%D0%BB%D0%BA%D0%BE%D0%B2%D0%BE/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%BB%D0%BE%D0%B1%D0%BE%D0%B4%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%BE%D0%B2%D1%85%D0%BE%D0%B7%D0%BD%D1%8B%D0%B9-%D0%B1%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A1%D0%B0%D1%83%D0%BD%D0%B0-%D0%9B%D1%8E%D0%BA%D1%81-%D0%B2-%D0%A7%D0%B5%D1%80%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A2%D1%83%D1%80%D0%B5%D1%86%D0%BA%D0%B8%D0%B9-%D1%85%D0%B0%D0%BC%D0%BC%D0%B0%D0%BC-%D0%B2-%D0%9C%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D0%B0-%D0%98%D1%80%D0%B1%D0%B8%D1%81-%D0%9E%D1%82%D0%B5%D0%BB%D1%8C/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A3%D1%81%D0%B0%D0%B4%D1%8C%D0%B1%D0%B0-%D0%B1%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F-%D0%BD%D0%B0-%D0%92%D0%B8%D1%88%D0%BD%D0%B5%D0%B2%D0%BE%D0%B9/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A3%D1%81%D0%B0%D0%B4%D1%8C%D0%B1%D0%B0-%D0%B1%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F-%D0%BD%D0%B0-%D0%92%D0%BE%D0%B9%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B9/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A3%D1%81%D0%B0%D0%B4%D1%8C%D0%B1%D0%B0-%D0%91%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A3%D1%81%D0%B0%D0%B4%D1%8C%D0%B1%D0%B0-%D0%91%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F-%D0%BD%D0%B0-%D0%9E%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8C%D1%81%D0%BA%D0%BE%D0%BC-%D0%BF%D0%BE%D0%BB%D0%B5/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A3%D1%81%D0%B0%D0%B4%D1%8C%D0%B1%D0%B0-%D0%91%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F-%D0%BD%D0%B0-%D0%9F%D0%B0%D0%BD%D1%84%D0%B8%D0%BB%D0%BE%D0%B2%D0%B0-/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A3%D1%81%D0%B0%D0%B4%D1%8C%D0%B1%D0%B0-%D0%B2-%D0%AE%D1%80%D0%BB%D0%BE%D0%B2%D0%BE/',
# 'https://бани.рф/%D0%B1%D0%B0%D0%BD%D1%8F/%D0%A6%D0%B0%D1%80%D0%B8%D1%86%D1%8B%D0%BD%D1%81%D0%BA%D0%B8%D0%B5-%D0%B1%D0%B0%D0%BD%D0%B8-%D0%B2-%D0%A2%D0%A6-%D0%A6%D0%B0%D1%80%D0%B8%D1%86%D1%8B%D0%BD%D0%BE/'
#         ]

with open('../Moscow/URLs.txt','r', encoding="utf-8") as f:
    lines = f.read().split(',')

ursl = [line.strip() for line in lines]
print(ursl)



with open('../address.txt', 'w') as file:
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    for idx,url in enumerate(ursl):
        # print(ursl)

        page = requests.get(url)
    # Parse the html content
        soup = BeautifulSoup(page.content, "html.parser")

        # addr_list = soup.find_all('div', attrs={'class':'addrsmall3'})
        # addr_list = soup.find('div', id_='addrsmall3').text

        folder_name = soup.find('div', {'id':'contnt'}).find('h1').text
        folder_path = folder_name.replace('"','')
        try:
            os.makedirs(folder_path)
        except Exception as e:
            print(e)
            continue
        file_path = os.path.join(folder_path)
        find_photo = soup.find('div', class_='formphotos')
        find_class = find_photo.find_all('a', {'class': 'big'})


        # nextele = service_a.find_next_siblings("a")
        # for next in nextele:
        #     print(next.text)

        test_all = soup.find('div', class_='formphotos').find('a').a


        Type_Bath = []
        Type_Kitchen = []
        Type_Service = []
        Type_Services = []

        for photo in find_class:
            try:
                href = photo.get('href')
                url = 'https://бани.рф' + href
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                    "Accept-Encoding": "*",
                    "Connection": "keep-alive"}
                response = requests.get(url, headers=headers).content
                # urllib.request.urlretrieve(url, 'img1.jpg')
                file_name = href.split('/')[-1]
                # os.chdir(folder_path)
                with open(os.path.join(folder_path, file_name), 'wb') as f:
                    f.write(response)
                print(photo)

                ############################CROP IMAGE
                os.chdir(folder_path)
                image = Image.open(file_name)
                width, height = image.size
                new_width, new_height = width, height - 72
                left, top, right, bottom = 0, 36, width, height - 36
                image = image.crop((left, top, right, bottom))
                image.save(file_name)
                os.chdir('..')
            except Exception as e:
                print(f'Ошибка {e}')
                continue






            ##########################WATERMARK DELETE
            # img = os.chdir(folder_path)
            # img = cv2.imread(f'{folder_path}/,{file_name}')
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            #
            # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # cnts = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
            #
            # for cnt in cnts:
            #     x, y, w, h = cv2.boundingRect(cnt)
            #     img[y:y + h, x:x + w] = cv2.medianBlur(img[y:y + h, x:x + w], 35)
            #
            # cv2.imwrite('output.jpg', img)





            # worksheet.cell(row=idx + 1, column=9).value = Type_Services
        #     TODO: 1) Обрезать фото 2) Плагин для ватермарки




        # details_list = soup.find('div', class_='detailright1').text

        tabs_list = soup.find('div', class_='zalpads')
        many = False
        if tabs_list:
            many = True
        else:
            pass


        time.sleep(0.7)




