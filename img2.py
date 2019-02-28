import fresh_tomatoes
import media
Bhadra=media.MovieTrailer("Bhadra","Telugu action film ",
                         "http://www.andhrawatch.com/wp-content/uploads/2016/02/bhadra-telugu-movie-online.jpg",
                         "https://youtu.be/Nsx7EOHx8Hg")

#print(hyper.moviestory)
Nenunnanu=media.MovieTrailer("Nenunnanu","family enterainment drama",
                            "https://upload.wikimedia.org/wikipedia/en/9/91/Nenunnanudvd.jpg",
                             "https://youtu.be/yDAUYRw4sww")
#print(Nenunnanu.moviestory)
#Bichagadu.show_trailer()
Suswagatham=media.MovieTrailer("Suswagatham","Telugu romantic film ",
                              "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1IDE08gajts15P0UDob3rI_moKB78_LzNMZnGwPl0nx_3Onl3aA",
                              "https://youtu.be/NUdGYKQMwqk")
Trinethram=media.MovieTrailer("Trinethram","devotional film",
                                "https://i.ytimg.com/vi/HDE7DSqoeZE/maxresdefault.jpg",
                                "https://youtu.be/VGQSvgYLJYc")

SwethaNagu=media.MovieTrailer("Swetha nagu","devitional film",
                            "https://naasongs.com/wp-content/uploads/2016/04/Swetha-Naagu-2003-250x250.jpg",
                            "https://youtu.be/nhNTJtxbXRI")
Mayabazar=media.MovieTrailer("mayabazar"," Indian epic fantasy film ",
                          "https://i.ytimg.com/vi/tas_30CdOss/maxresdefault.jpg",
                          "https://youtu.be/GuXx69GS9Eo")
Narthanasala=media.MovieTrailer("Narthanasal","Indian Telugu-language historical period drama film",
                                    "https://i.pinimg.com/originals/f1/80/68/f18068762f8d5a4abd95479716fc40ce.jpg",
                                    "https://youtu.be/yyBUQalTQCA")
Bhookailasa=media.MovieTrailer("Bhookailasa","Devotional film",
                              "https://sensongsmp3.org/wp-content/uploads/2017/11/Bhookailas-1958jpeg.jpg",
                             "https://youtu.be/BhDjLx0K7_0" )
Balanagamma=media.MovieTrailer("Bala Nagamma","Telugu swashbuckling adventure fantasy film",
                             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNhYuffZAcyi47CkIdmbNS2Be04BqQcal41JVQTYOF0pArAPMQ",
                               "https://youtu.be/4KjETdQwzGA")

movies=[Bhadra,Nenunnanu,Suswagatham,Trinethram,SwethaNagu,Mayabazar,Narthanasala,Bhookailasa,Balanagamma]
fresh_tomatoes.open_movies_page(movies)
                                    
