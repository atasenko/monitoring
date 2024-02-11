### Задание повышенной сложности.  
В этот раз не осилил, сломался на запуске кластера elasticsearch.  

### Задание 1. Запуск контейнеров.  
Все шесть работают больше 5 минут.  
![Containers](img/monitoring03-01.png)  
Интерфейс Kibana:  
![Kibana](img/monitoring03-02.png)  

### Задание 2. Index-patterns, logs, dummy-app.  
Перешел в меню создания индекс-паттернов, создал паттерн Dummy по маске logstash-*  
![index-pattern](img/monitoring03-03.png)  

В меню просмотра логов уже накопилось более 900~~0~~ записей из докера:  
![docker logs](img/monitoring03-04.png)  

Если использовать полнотекстовый поиск можно найти рандомные записи сгенерированные приложением:  
![dummy logs](img/monitoring03-05.png)
