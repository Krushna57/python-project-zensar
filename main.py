from service.feedback_analysis import FeedbackOperable
from service.complaints import ComplaintsOperable

def main():
    print("Welcome to the Feedback and Complaints Analysis System")
    ob1 = ComplaintsOperable
    ob2 = FeedbackOperable
    
    while True:
        print("\nPlease choose an option:")
        print("1. Most Common Complaints")
        print("2. Complaint Summary by Product")
        print("3. Complaint Summary by Region")
        print("4. Aggregate Feedback by Product")
        print("5. Aggregate Feedback by Rating")
        print("6. Aggregate Feedback by Region")
        print("7. Feedback Trends by Date")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            ob1.most_common_complaints()

        elif choice == "2":
            ob1.complaint_summary_by_product()

        elif choice == "3":
            ob1.complaint_summary_by_region()

        elif choice == "4":
            ob2.aggregate_by_product()

        elif choice == "5":
            ob2.aggregate_by_rating()

        elif choice == "6":
            ob2.aggregate_by_region()

        elif choice == "7":
            ob2.feedback_trends()

        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")
            

if __name__ == "__main__":
    main()
