# Contenido de la demo Hotel Goartín (Málaga) (es/ca/en/fr). Hechos de hotelgoartin.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Habitación doble','Doble con terraza','Habitación individual'],'ca':['Habitació doble','Doble amb terrassa','Habitació individual'],'en':['Double room','Double with terrace','Single room'],'fr':['Chambre double','Double avec terrasse','Chambre individuelle']}
RD={
'es':['Con cama de matrimonio o dos camas individuales (twin), climatización frío y calor, escritorio y baño privado.','Cama de matrimonio o dos camas y una terraza privada para disfrutar del aire libre.','Cómoda y funcional, con wifi gratuito, televisión, teléfono directo y baño con secador.'],
'ca':['Amb llit de matrimoni o dos llits individuals (twin), climatització fred i calor, escriptori i bany privat.','Llit de matrimoni o dos llits i una terrassa privada per gaudir de l\'aire lliure.','Còmoda i funcional, amb wifi gratuït, televisió, telèfon directe i bany amb assecador.'],
'en':['With a double bed or two single beds (twin), heating and air conditioning, a desk and a private bathroom.','A double bed or two beds and a private terrace to enjoy the outdoors.','Comfortable and functional, with free wifi, TV, direct-dial phone and a bathroom with hairdryer.'],
'fr':['Avec un lit double ou deux lits simples (twin), climatisation chaud et froid, bureau et salle de bain privée.','Un lit double ou deux lits et une terrasse privée pour profiter du plein air.','Confortable et fonctionnelle, avec wifi gratuit, télévision, téléphone direct et salle de bain avec sèche-cheveux.']}
ART={
'hero':('skyline',8101,['#1f4f6e','#e7a25f','#f8d9a4','#1d4a67','#173b52','#0f283a']),
'intro':('columns',8102,['#eef2f4','#f7f9fa','#d08b3c','#1f4f6e','#143449']),
'r1':('columns',8111,['#edf1f3','#f6f8f9','#cd8a3e','#1f4f6e','#143449']),
'r2':('hills',8112,['#e6eef0','#f2ecd6','#f2c988','#a9c2a4','#7fa28a','#567a68']),
'r3':('arches',8113,['#f2ebe1','#e6c493','#c07a3c','#1f4f6e','#143449']),
'g1':('skyline',8121,['#23557a','#e8a462','#f9dba8','#21516f','#1a4058','#112b3d']),
'g2':('columns',8122,['#ecf0f2','#f5f7f8','#ca883d','#1f4f6e','#143449']),
'g3':('hills',8123,['#e4edf0','#f1ebd4','#f0c784','#a6c0a1','#7c9f87','#537765']),
'g4':('arches',8124,['#f1e9de','#e4c08e','#bd773a','#1f4f6e','#143449']),
'g5':('skyline',8125,['#1d4c6b','#e59f5c','#f7d7a1','#1b4763','#15384e','#0e2636']),
'g6':('columns',8126,['#eaeff1','#f4f6f7','#c7853b','#1f4f6e','#143449'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Goartín · Hotel de 2 estrellas en Málaga, junto a la estación María Zambrano',see_rooms='Ver habitaciones',hero_k='Málaga · Cruz de Humilladero',hero_t='Tu punto de partida para descubrir Málaga',hero_s='Hotel de 2 estrellas en la calle Gerona, 32, a pocos minutos a pie de la estación María Zambrano.',
 intro_t='Málaga a tu alcance',intro_p1='Una ubicación práctica para ocio y trabajo: a unos 20 minutos a pie del centro histórico y a unos 15 de la playa de San Andrés.',
 intro_p2='Junto a la estación de tren María Zambrano, la principal estación de autobuses y la estación de metro La Unión, rodeado de bares y restaurantes de cocina mediterránea y malagueña.',
 stats=['2 estrellas','Junto a María Zambrano','Wifi gratuito','Metro La Unión'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Para viajar solo, en pareja o por trabajo.',
 svcs=['Wifi gratuito','Climatización frío y calor','Televisión','Teléfono directo','Escritorio','Baño privado con secador','Algunas habitaciones con terraza','Reserva directa en su web'],
 loc_p='C. Gerona, 32 · Cruz de Humilladero · 29006 Málaga. Licencia turística H/MA/02022.',
 chips=['¿Qué habitaciones tiene?','¿Dónde está el hotel?','¿Cómo llego al centro?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Goartín · Hotel de 2 estrelles a Màlaga, al costat de l\'estació María Zambrano',see_rooms='Veure habitacions',hero_k='Màlaga · Cruz de Humilladero',hero_t='El teu punt de partida per descobrir Màlaga',hero_s='Hotel de 2 estrelles al carrer Gerona, 32, a pocs minuts a peu de l\'estació María Zambrano.',
 intro_t='Màlaga al teu abast',intro_p1='Una ubicació pràctica per a oci i feina: a uns 20 minuts a peu del centre històric i a uns 15 de la platja de San Andrés.',
 intro_p2='Al costat de l\'estació de tren María Zambrano, la principal estació d\'autobusos i l\'estació de metro La Unión, envoltat de bars i restaurants de cuina mediterrània i malaguenya.',
 stats=['2 estrelles','Al costat de María Zambrano','Wifi gratuït','Metro La Unión'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Per viatjar sol, en parella o per feina.',
 svcs=['Wifi gratuït','Climatització fred i calor','Televisió','Telèfon directe','Escriptori','Bany privat amb assecador','Algunes habitacions amb terrassa','Reserva directa al seu web'],
 loc_p='C. Gerona, 32 · Cruz de Humilladero · 29006 Màlaga. Llicència turística H/MA/02022.',
 chips=['Quines habitacions té?','On és l\'hotel?','Com arribo al centre?','Com es reserva?']),
'en':dict(title='Hotel Goartín · 2-star hotel in Málaga, next to María Zambrano station',see_rooms='See the rooms',hero_k='Málaga · Cruz de Humilladero',hero_t='Your starting point to discover Málaga',hero_s='A 2-star hotel at Calle Gerona, 32, a few minutes\' walk from María Zambrano station.',
 intro_t='Málaga within your reach',intro_p1='A convenient location for leisure and work: about a 20-minute walk from the historic centre and about 15 minutes from San Andrés beach.',
 intro_p2='Next to María Zambrano train station, the main bus station and La Unión metro station, surrounded by bars and restaurants serving Mediterranean and Malagueño cooking.',
 stats=['2 stars','Next to María Zambrano','Free wifi','La Unión metro'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='For travelling alone, as a couple or for work.',
 svcs=['Free wifi','Heating and air conditioning','TV','Direct-dial phone','Desk','Private bathroom with hairdryer','Some rooms with terrace','Direct booking on its website'],
 loc_p='C. Gerona, 32 · Cruz de Humilladero · 29006 Málaga. Tourist licence H/MA/02022.',
 chips=['What rooms does it have?','Where is the hotel?','How do I get to the centre?','How do I book?']),
'fr':dict(title='Hotel Goartín · Hôtel 2 étoiles à Malaga, près de la gare María Zambrano',see_rooms='Voir les chambres',hero_k='Malaga · Cruz de Humilladero',hero_t='Votre point de départ pour découvrir Malaga',hero_s='Hôtel 2 étoiles calle Gerona, 32, à quelques minutes à pied de la gare María Zambrano.',
 intro_t='Malaga à votre portée',intro_p1='Un emplacement pratique pour les loisirs et le travail : à environ 20 minutes à pied du centre historique et à environ 15 minutes de la plage de San Andrés.',
 intro_p2='Près de la gare María Zambrano, de la principale gare routière et de la station de métro La Unión, entouré de bars et de restaurants de cuisine méditerranéenne et malaguène.',
 stats=['2 étoiles','Près de María Zambrano','Wifi gratuit','Métro La Unión'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Pour voyager seul, en couple ou pour le travail.',
 svcs=['Wifi gratuit','Climatisation chaud et froid','Télévision','Téléphone direct','Bureau','Salle de bain privée avec sèche-cheveux','Certaines chambres avec terrasse','Réservation directe sur son site'],
 loc_p='C. Gerona, 32 · Cruz de Humilladero · 29006 Malaga. Licence touristique H/MA/02022.',
 chips=['Quelles chambres a-t-il ?','Où est l\'hôtel ?','Comment aller au centre ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES_ES='https://www.hotelgoartin.com/es/booking/property?id=100079'; RES_EN='https://www.hotelgoartin.com/en/booking/property?id=100079'
BOOK=dict(mode='engine',url={'es':RES_ES,'ca':RES_ES,'en':RES_EN,'fr':RES_EN})
D=dict(name='Hotel Goartín',ac='#1f4f6e',ac2='#c07a3c',ac2_a11y='#8a4a1e',book=BOOK,around=[],foot=FOOT,
 address='C. Gerona, 32 · 29006 Málaga',phones=['+34 952 365 135'],emails=['administracion@hotelgoartin.com'],maps='Hotel Goartin, Calle Gerona 32, Málaga',t=T)
META=dict(repo='demo-hotel-goartin-malaga',name='Hotel Goartín',legal_name='R. Margo 2020, S.L.',registry_ids=['CIF B-01601079','Registro Mercantil de Málaga hoja MA-155890','Licencia turística H/MA/02022'],
 url='https://www.hotelgoartin.com/es',domain='hotelgoartin.com',municipality='Málaga',province='Málaga',sector='hotel de 2 estrellas junto a la estación María Zambrano de Málaga',
 read_at='2026-10-29T11:15:00+01:00',created_at='2026-10-29T11:16:00+01:00',built_at='2026-10-29T11:25:00+01:00',audit_date='2026-10-29T11:14:00+01:00',
 rating=dict(value=4.4,coincide=['telefono','web'],date='2026-10-29T10:24:53+01:00',url='https://www.google.com/maps/place/Hotel+Goartin/@36.7135232,-4.4392423,17z/data=!4m9!3m8!1s0xd72f7762f24230f:0xd86051409c9c123d!5m2!4m1!1i2!8m2!3d36.7135232!4d-4.4392423!16s%2Fg%2F1tdm9pgh'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas real del hotel (obehotel, /booking/property?id=100079, la pagina a la que lleva su buscador «Buscar disponibilidad»); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Hay habitaciones con terraza?','K02'),('¿Qué tienen las habitaciones?','K03'),('¿Dónde está el hotel?','K04'),('¿Está cerca de la estación de tren?','K05'),('¿Cómo llego al centro?','K06'),('¿Qué ver en Málaga?','K07'),('¿Se puede ir al Caminito del Rey?','K08'),('¿Cómo reservo?','K09'),('¿Quién es el titular?','K10'),('¿Hay ofertas?','K11'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K09'),('¿Tienen gimnasio?',None),('¿Hay piscina?',None),('¿Admiten mascotas?',None)],
'ca':[('Quines habitacions té?','K01'),('Hi ha habitacions amb terrassa?','K02'),('Què tenen les habitacions?','K03'),('On és l\'hotel?','K04'),('És a prop de l\'estació de tren?','K05'),('Com arribo al centre?','K06'),('Què es pot veure a Màlaga?','K07'),('Es pot anar al Caminito del Rey?','K08'),('Com reservo?','K09'),('Qui és el titular?','K10'),('Hi ha ofertes?','K11'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K09'),('Teniu gimnàs?',None),('Hi ha piscina?',None),('Admeteu mascotes?',None)],
'en':[('What rooms does it have?','K01'),('Are there rooms with a terrace?','K02'),('What do the rooms have?','K03'),('Where is the hotel?','K04'),('Is it near the train station?','K05'),('How do I get to the centre?','K06'),('What is there to see in Málaga?','K07'),('Can I visit the Caminito del Rey?','K08'),('How do I book?','K09'),('Who is the owner?','K10'),('Are there any special offers?','K11'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K09'),('Do you have a gym?',None),('Is there a swimming pool?',None),('Are pets allowed?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Y a-t-il des chambres avec terrasse ?','K02'),('Qu\'ont les chambres ?','K03'),('Où est l\'hôtel ?','K04'),('Est-il près de la gare ?','K05'),('Comment aller au centre ?','K06'),('Que voir à Malaga ?','K07'),('Peut-on aller au Caminito del Rey ?','K08'),('Comment réserver ?','K09'),('Qui est le titulaire ?','K10'),('Y a-t-il des offres ?','K11'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K09'),('Avez-vous une salle de sport ?',None),('Y a-t-il une piscine ?',None),('Les animaux sont-ils admis ?',None)]}
