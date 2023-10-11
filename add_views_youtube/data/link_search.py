CANAL_URLS = (
    'https://www.youtube.com/channel/UCSOXYurvA9cUM3wf1LkAJag',
    'https://www.youtube.com/channel/UCSOXYurvA9cUM3wf1LkAJag/videos',
)

SEARCH_URLS_BASE = (
    # CANAL_URLS[0],
    # CANAL_URLS[1],
    # 'https://www.youtube.com/results?search_query=zmusical',
    'https://www.youtube.com/results?search_query=musica+country+para+trabajar',
    'https://www.youtube.com/results?search_query=sonidos+de+las+olas+del+mar+zmusical',
    'https://www.youtube.com/results?search_query=sonido+de+gaviotas+en+el+mar',
    'https://www.youtube.com/results?search_query=gaviotas+en+la+playa',
    'https://www.youtube.com/results?search_query=sonido+de+gaviotas+en+la+playa',
    'https://www.youtube.com/results?search_query=musica+para+restaurantes+2021',
    'https://www.youtube.com/results?search_query=Musica+para+bar+2021',
    'https://www.youtube.com/results?search_query=Musica+Relajante+Para+Calmar+Perros+Intranquilos+o+Nerviosos',
    'https://www.youtube.com/results?search_query=sonido+de+fuego+ardiendo',
    'https://www.youtube.com/results?search_query=pantalla+negra+sonido+de+lluvia+zmusical',
    'https://www.youtube.com/results?search_query=m%C3%BAsica+para+viajar+en+coche',
    'https://www.youtube.com/results?search_query=musica+para+conducir+en+carretera',
    'https://www.youtube.com/results?search_query=m%C3%BAsica+de+piano+para+dormir+zmusical',
)

SEARCH_URLS_PRIORITY = (
    'https://www.youtube.com/results?search_query=sonido+de+fuego+ardiendo',
    'https://www.youtube.com/results?search_query=sonido+de+fuego+ardiendo',
    'https://www.youtube.com/results?search_query=m%C3%BAsica+para+viajar+en+coche',
    'https://www.youtube.com/results?search_query=m%C3%BAsica+para+viajar+en+coche',
    'https://www.youtube.com/results?search_query=musica+para+conducir+en+carretera',
    'https://www.youtube.com/results?search_query=musica+para+conducir+en+carretera',
)

SEARCH_URLS = tuple(SEARCH_URLS_BASE + SEARCH_URLS_PRIORITY)