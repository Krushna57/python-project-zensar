from utils.DBConnection import Connection
class FeedbackOperable:
    def aggregate_by_rating():
        try:
            conn = Connection.get_db_connection()
            cursor = conn.cursor(dictionary=True)
            query = """
            SELECT rating, COUNT(*) AS count 
            FROM Feedback 
            GROUP BY rating 
            ORDER BY rating
            """

            cursor.execute(query)
            result = cursor.fetchall()

            print("Feedback Aggregated by Rating:")
            for row in result:
                print(f"Rating: {row['rating']}, Count: {row['count']}")

        except Exception as e:
            print(f"Error aggregating feedback by rating: {e}")
            return []

        finally:
            if conn.is_connected():
                conn.close()

    def aggregate_by_product():
        try:
            conn = Connection.get_db_connection()
            cursor = conn.cursor(dictionary=True)

            query = """
            SELECT Product.name, COUNT(Feedback.feedback_id) AS count 
            FROM Feedback
            JOIN Product ON Feedback.product_id = Product.product_id
            GROUP BY Product.name
            ORDER BY count DESC
            """

            cursor.execute(query)
            result = cursor.fetchall()

            print("Feedback Aggregated by Product:")
            for row in result:
                print(f"Product: {row['name']}, Count: {row['count']}")

        except Exception as e:
            print(f"Error aggregating feedback by product: {e}")
            return []

        finally:
            if conn.is_connected():
                conn.close()
    

    def aggregate_by_region():
        try:
            conn = Connection.get_db_connection()
            cursor = conn.cursor(dictionary=True)

            query = """
            SELECT Region.region_name, COUNT(Feedback.feedback_id) AS count 
            FROM Feedback
            JOIN Customer ON Feedback.customer_id = Customer.customer_id
            JOIN Region ON Customer.region_id = Region.region_id
            GROUP BY Region.region_name
            ORDER BY count DESC
            """
            cursor.execute(query)
            result = cursor.fetchall()

            print("Feedback Aggregated by Region:")
            for row in result:
                print(f"Region: {row['region_name']}, Count: {row['count']}")

            return result

        except Exception as e:
            print(f"Error aggregating feedback by region: {e}")
            return []

        finally:
            if conn.is_connected():
                conn.close()


    def feedback_trends():
        try:
            conn = Connection.get_db_connection()
            cursor = conn.cursor(dictionary=True)

            query = """
            SELECT DATE(feedback_date) AS feedback_date, COUNT(*) AS count
            FROM Feedback
            GROUP BY DATE(feedback_date)
            ORDER BY feedback_date
            """

            cursor.execute(query)
            result = cursor.fetchall()

            print("Feedback Trends by Date:")
            for row in result:
                print(f"Date: {row['feedback_date']}, Count: {row['count']}")

            return result

        except Exception as e:
            print(f"Error analyzing feedback trends: {e}")
            return []

        finally:
            if conn.is_connected():
                conn.close()
