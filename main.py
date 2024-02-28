import json


#watch_list = []
# example
watch_list = [["gang", 6],["god", 10,"watched"],["fff", 9], ["how", 2]]

while True:
    print("1.to add a film")
    print("2.to delete a film")
    print("3.to mark a film as watched")
    print("4.to split(filter) watched and non watched films")
    print("5.to get top 10 films by marks ")
    print("6.to empty a watchlist")
    print("7.to search a film by part of name")
    print("8.to exit")
    command = int(input())

    if command < 9 and command > 0:

        if command == 1:
            # 1. to add a film
            film = input()
            movie = film.split(" ")
            # !!! checking if everything is ok with count of chars
            if len(movie[0]) < 121 and len(movie[0]) > 1 and int(movie[1]) < 11 and int(movie[1]) > 0 :
            # !!! checking if every value is in right type
                try:
                    watch_list.append([str(movie[0]),int(movie[1])])
                except:
                    print("smth got wrong")
                print(watch_list)
            else:
               print("smth got wrong")

        if command == 2:
            # 2. to delete a film
            film_to_delete = input()
            x = 0
            # !!! searching film to delete in watch_list
            for i in watch_list:
            # !!! if there is that film so we delete it
                if film_to_delete == i[0]:
                    del watch_list[x]
                else:
                    print("")
                x +=1
            print(watch_list)

        if command == 3:
            # 3. to mark a film as watched
            film_is_watched = input()
            # !!! scrolling whole watch_list to find a film we watched
            for i in watch_list:
            # !!! if there is we mark it as watched
                if film_is_watched in i:
                    i.append("watched")
            print(watch_list)

        if command == 4:
            # 4. to split(filter) watched and non watched films
            watched_films = []
            non_watched_films = []
            # !!! scrolling the whole watch_list
            for i in watch_list:
            # !!! if there is some extra value(watched) we add this film in watched list
                if len(i) == 3:
                    watched_films.append(i)
                else:
                    non_watched_films.append(i)
            print(watched_films)
            print(non_watched_films)
            
        if command == 5:
            # 5. to get top 10 films by marks
            # returning only marks
            def myFunc(e):
                return e[1]
            watch_list.sort(key=myFunc,reverse=True)
            # !!! printing only first 10 films from sorted list
            for i in range(10):
                print(watch_list[i])

        if command == 6:
            # 6. to empty a watch_list
            del watch_list[:]
            print(watch_list)

        if command == 7:
            # 7. to search a film by part of name
            # !!! checking that our string is string
            try:
                part = str(input())
            except:
                print("smth got wrong")
            # !!! scrolling list
            for i in watch_list:
            # !!! it will print these films if there would be just a part of whole name
                if part in i[0]:
                    print(i)
        if command == 8:
            break