#Напишите программу, удаляющую из текста все слова, содержащие "абв". 
 
s='Привет!Чудеса под подабв Новый год габвод случаются тогда тогабвда, когда их ихабв не ждёшь ждешабвь.' 
 
s=' '.join(filter(lambda x: not'абв' in x, s.lower().split())) 
print(s)