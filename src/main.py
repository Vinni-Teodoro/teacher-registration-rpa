import pandas as pd

from automation import TeacherRegistrationBot
from models import Teacher
from report import export_report


def main():

    print("\nTeacher Registration RPA\n")

    teachers_df = pd.read_excel("../examples/teachers.xlsx")

    teachers = []

    for _, row in teachers_df.iterrows():

        teachers.append(

            Teacher(

                name=row["Name"],
                email=row["Email"],
                document=row["Document"]

            )

        )

    bot = TeacherRegistrationBot()

    bot.login()

    results = []

    for teacher in teachers:

        result = bot.process_teacher(teacher)

        results.append(result)

    export_report(results)

    bot.close()


if __name__ == "__main__":
    main()