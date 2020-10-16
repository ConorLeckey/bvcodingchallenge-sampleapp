from helpers.database_helper import Database


class StatsHelper():

    def __init__(self):
        self.database = Database()
        print("Stats Helping initialising!")

    def caculate_ave_overall_rating(self):
        result = self.database.fetch_one("SELECT AVG(review_overall) FROM reviews")
        return result[0]

    def caculate_ave_aroma_rating(self):
        result = self.database.fetch_one("SELECT AVG(review_aroma) FROM reviews")
        return result[0]

    def get_ordered_by_ave_overall_rating(self):
        result = self.database.fetch_all("SELECT beer_name, review_overall FROM reviews GROUP BY beer_name, review_overall")
        return result





    # HINT: You can define more queries here, along with some python logic to calculate!
    def calculate_another_stat(self):
      # all_rows = self.database.fetch_all("")
      return None
