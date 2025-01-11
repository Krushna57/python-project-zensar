from utils.DBConnection import Connection

class ComplaintsOperable:
    def most_common_complaints(limit=5):
        try:
            conn = Connection.get_db_connection()
            cursor = conn.cursor(dictionary=True)
            query = """
            SELECT comments, COUNT(*) AS frequency 
            FROM feedback
            GROUP BY comments
            ORDER BY frequency DESC
            LIMIT %s
            """
            cursor.execute(query, (limit,))
            result = cursor.fetchall()
            print(f"Most common complaints (Top {limit}):")
            for row in result:
                print(f"Complaint: {row['comments']}, Frequency: {row['frequency']}")

        except Exception as e:
            print(f"Error finding most common complaints: {e}")
            return []

        finally:
            if conn.is_connected():
                conn.close()

        
    def complaint_summary_by_product():
        try:
            conn = Connection.get_db_connection()
            cursor = conn.cursor(dictionary=True)
            query = """
            SELECT Product.name, COUNT(Feedback.feedback_id) AS complaint_count
            FROM Feedback
            JOIN Product ON Feedback.product_id = Product.product_id
            WHERE Feedback.comments IS NOT NULL
            GROUP BY Product.name
            ORDER BY complaint_count DESC
            """
            cursor.execute(query)
            result = cursor.fetchall()
            print("Complaint Summary by Product:")
            for row in result:
                print(f"Product: {row['name']}, Complaint Count: {row['complaint_count']}")

        except Exception as e:
            print(f"Error generating complaint summary by product: {e}")
        finally:
            if conn.is_connected():
                conn.close()


    def complaint_summary_by_region():
        try:
            conn = Connection.get_db_connection()
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT Region.region_name, COUNT(Feedback.feedback_id) AS complaint_count
                FROM Feedback
                JOIN Customer ON Feedback.customer_id = Customer.customer_id
                JOIN Region ON Customer.region_id = Region.region_id
                WHERE Feedback.comments IS NOT NULL
                GROUP BY Region.region_name
                ORDER BY complaint_count DESC
                """
            cursor.execute(query)
            result = cursor.fetchall()
            print("Complaint Summary by Region:")
            for row in result:
                print(f"Region: {row['region_name']}, Complaint Count: {row['complaint_count']}")
        except Exception as e:
            print(f"Error generating complaint summary by region: {e}")
            return []

        finally:
            if conn.is_connected():
                conn.close()

