def analisis_review(data_review):
    rating_terendah = min(data_review)
    rating_tertinggi = max(data_review)
    rata_rata_rating = sum(data_review) / len(data_review)

    return [int(rating_terendah), int(rating_tertinggi), round(rata_rata_rating, 1)]

review_1 = [4.5, 2.0, 1.5, 3.0, 2.5, 4.0, 5.0, 3.5, 2.0, 1.0]
hasil_1  = analisis_review(review_1)
print(hasil_1)

review_2 = [5,4,2.5,5,3.6,1.1,3.6,4,4.2,1.5]
hasil_2  = analisis_review(review_2)
print(hasil_2)