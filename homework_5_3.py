tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена',
    'Святослав', 'Антон', 'Марк', 'Матвей'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
if len(tutors) > len(klasses):
    [klasses.append(None) for i in range(len(tutors) - len(klasses))]

trpls = ((tutor, klasse) for tutor, klasse in zip(tutors, klasses))
# print(*trpls)
print(type(trpls))
print(next(trpls))
print(next(trpls))
print(next(trpls))
print(next(trpls))
print(*trpls)
