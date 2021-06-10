#https://classroom.udacity.com/courses/ud036
import media
import fresh_tomatoes

your_name = media.Movie("Kimi no Na wa",
                        "หลับตาฝันถึงชื่อเธอ",
                        "Two teenagers share a profound, magical connection upon discovering they are swapping bodies.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/0/0b/Your_Name_poster.png/220px-Your_Name_poster.png",
                        "https://www.youtube.com/watch?v=3KR8_igDs1Y"
                        )

# print(your_name.storyline)

the_garden_of_words = media.Movie("The Garden of Words",
                    "ยามเมื่อสายฝนโปร่ยปราย",
                    "When a lonely teenager skips his morning lessons to sit in a lovely garden, he meets a mysterious older woman who shares his feelings of alienation.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Garden_of_Words_poster.png/220px-Garden_of_Words_poster.png",
                    "https://www.youtube.com/watch?v=udDIkl6z8X0"
                    )

# print(the_garden_of_words.storyline)
# the_garden_of_words.show_trailer()

five_cent_per_sec = media.Movie("5 Centimeters per Second",
                            "ยามซากุระร่วงโรย",
                             "Two kids are walking together as the cherry blossom petals fall. After the girl reveals that the falling speed of a cherry blossom petal is 5 centimeters per second",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/7/79/5_Centimeters_Per_Second_poster.jpg/220px-5_Centimeters_Per_Second_poster.jpg",
                             "https://www.youtube.com/watch?v=wdM7athAem0"
                             )

kaze_tachinu = media.Movie("Kaze Tachinu",
                            "ปีกแห่งฝัน วันแห่งรัก",
                            "A lifelong love of flight inspires Japanese aviation engineer Jiro Horikoshi (Hideaki Anno), whose storied career includes the creation of the A6M World War II fighter plane.",
                            "https://upload.wikimedia.org/wikipedia/en/a/a3/Kaze_Tachinu_poster.jpg",
                            "https://www.youtube.com/watch?v=Myo3DOPU8jo"
                            )

inception = media.Movie("Inception",
                                "อินเซ็ปชั่น จิตพิฆาตโลก",
                                "Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter people's dreams and steal their secrets from their subconscious.",
                                "https://flxt.tmsimg.com/assets/p7825626_p_v10_af.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY"
                                )

about_time = media.Movie("About Time",
                            "ย้อนเวลา ให้เธอปิ๊งรัก",
                            "The men in their family can travel through time. Although he can't change history, Tim resolves to improve his life by getting a girlfriend.",
                            "https://upload.wikimedia.org/wikipedia/en/7/7c/About_Time_%282013_film%29_Poster.jpg",
                            "https://www.youtube.com/watch?v=7OIFdWk83no"
                           )   

movies = [your_name, the_garden_of_words, five_cent_per_sec, kaze_tachinu, inception, about_time]
fresh_tomatoes.open_movies_page(movies)
