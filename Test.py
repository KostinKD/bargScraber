
from bs4 import BeautifulSoup



html = "<div style='min-height: 140px' class='formserv'><span class='servgrp'>Вид парной:</span> <a href='/пар/финская-парная/' rel='nofollow'>финская парная</a>, <a href='/пар/русская-баня/' rel='nofollow'>русская баня</a><br /><span class='servgrp'>Кухня:</span></div>"
soup = BeautifulSoup(html, 'html.parser')
kitchen = soup.find('span', class_='servgrp', string='Кухня:')
print(kitchen)
text_before_kitchen = kitchen.previousSibling.previousSibling
print(text_before_kitchen) # Выводим на экран