
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apis.models import SchoolStructure, Schools, Classes, Personnel, Subjects, StudentSubjectsScore


class StudentSubjectsScoreAPIView(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        """
        [Backend API and Data Validations Skill Test]

        description: create API Endpoint for insert score data of each student by following rules.

        rules:      - Score must be number, equal or greater than 0 and equal or less than 100.
                    - Credit must be integer, greater than 0 and equal or less than 3.
                    - Payload data must be contained `first_name`, `last_name`, `subject_title` and `score`.
                        - `first_name` in payload must be string (if not return bad request status).
                        - `last_name` in payload must be string (if not return bad request status).
                        - `subject_title` in payload must be string (if not return bad request status).
                        - `score` in payload must be number (if not return bad request status).

                    - Student's score of each subject must be unique (it's mean 1 student only have 1 row of score
                            of each subject).
                    - If student's score of each subject already existed, It will update new score
                            (Don't created it).
                    - If Update, Credit must not be changed.
                    - If Data Payload not complete return clearly message with bad request status.
                    - If Subject's Name or Student's Name not found in Database return clearly message with bad request status.
                    - If Success return student's details, subject's title, credit and score context with created status.

        remark:     - `score` is subject's score of each student.
                    - `credit` is subject's credit.
                    - student's first name, lastname and subject's title can find in DATABASE (you can create more
                            for test add new score).

        """

        subjects_context = [{"id": 1, "title": "Math"}, {"id": 2, "title": "Physics"}, {"id": 3, "title": "Chemistry"},
                            {"id": 4, "title": "Algorithm"}, {"id": 5, "title": "Coding"}]

        credits_context = [{"id": 6, "credit": 1, "subject_id_list_that_using_this_credit": [3]},
                           {"id": 7, "credit": 2, "subject_id_list_that_using_this_credit": [2, 4]},
                           {"id": 9, "credit": 3, "subject_id_list_that_using_this_credit": [1, 5]}]

        credits_mapping = [{"subject_id": 1, "credit_id": 9}, {"subject_id": 2, "credit_id": 7},
                           {"subject_id": 3, "credit_id": 6}, {"subject_id": 4, "credit_id": 7},
                           {"subject_id": 5, "credit_id": 9}]

        student_first_name = request.data.get("first_name", None)
        student_last_name = request.data.get("last_name", None)
        subjects_title = request.data.get("subject_title", None)
        score = request.data.get("score", None)

        # # Filter Objects Example
        # DataModel.objects.filter(filed_1=value_1, filed_2=value_2, filed_2=value_3)

        # # Create Objects Example
        # DataModel.objects.create(filed_1=value_1, filed_2=value_2, filed_2=value_3)

        return Response(status=status.HTTP_201_CREATED)


class StudentSubjectsScoreDetailsAPIView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        """
        [Backend API and Data Calculation Skill Test]

        description: get student details, subject's details, subject's credit, their score of each subject,
                    their grade of each subject and their grade point average by student's ID.

        pattern:     Data pattern in 'context_data' variable below.

        remark:     - `grade` will be A  if 80 <= score <= 100
                                      B+ if 75 <= score < 80
                                      B  if 70 <= score < 75
                                      C+ if 65 <= score < 70
                                      C  if 60 <= score < 65
                                      D+ if 55 <= score < 60
                                      D  if 50 <= score < 55
                                      F  if score < 50

        """

        student_id = kwargs.get("id", None)

        example_context_data = {
            "student":
                {
                    "id": "primary key of student in database",
                    "full_name": "student's full name",
                    "school": "student's school name"
                },

            "subject_detail": [
                {
                    "subject": "subject's title 1",
                    "credit": "subject's credit 1",
                    "score": "subject's score 1",
                    "grade": "subject's grade 1",
                },
                {
                    "subject": "subject's title 2",
                    "credit": "subject's credit 2",
                    "score": "subject's score 2",
                    "grade": "subject's grade 2",
                },
            ],

            "grade_point_average": "grade point average",
        }

        return Response(example_context_data, status=status.HTTP_200_OK)


class PersonnelDetailsAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """
        [Basic Skill and Observational Skill Test]

        description: get personnel details by school's name.

        data pattern:  {order}. school: {school's title}, role: {personnel type in string}, class: {class's order}, name: {first name} {last name}.

        result pattern : in `data_pattern` variable below.

        example:    1. school: Rose Garden School, role: Head of the room, class: 1, name: Reed Richards.
                    2. school: Rose Garden School, role: Student, class: 1, name: Blackagar Boltagon.

        rules:      - Personnel's name and School's title must be capitalize.
                    - Personnel's details order must be ordered by their role, their class order and their name.

        """

        data_pattern = [
            "1. school: Dorm Palace School, role: Teacher, class: 1,name: Mark Harmon",
            "2. school: Dorm Palace School, role: Teacher, class: 2,name: Jared Sanchez",
            "3. school: Dorm Palace School, role: Teacher, class: 3,name: Cheyenne Woodard",
            "4. school: Dorm Palace School, role: Teacher, class: 4,name: Roger Carter",
            "5. school: Dorm Palace School, role: Teacher, class: 5,name: Cynthia Mclaughlin",
            "6. school: Dorm Palace School, role: Head of the room, class: 1,name: Margaret Graves",
            "7. school: Dorm Palace School, role: Head of the room, class: 2,name: Darren Wyatt",
            "8. school: Dorm Palace School, role: Head of the room, class: 3,name: Carla Elliott",
            "9. school: Dorm Palace School, role: Head of the room, class: 4,name: Brittany Mullins",
            "10. school: Dorm Palace School, role: Head of the room, class: 5,name: Nathan Solis",
            "11. school: Dorm Palace School, role: Student, class: 1,name: Aaron Marquez",
            "12. school: Dorm Palace School, role: Student, class: 1,name: Benjamin Collins",
            "13. school: Dorm Palace School, role: Student, class: 1,name: Carolyn Reynolds",
            "14. school: Dorm Palace School, role: Student, class: 1,name: Christopher Austin",
            "15. school: Dorm Palace School, role: Student, class: 1,name: Deborah Mcdonald",
            "16. school: Dorm Palace School, role: Student, class: 1,name: Jessica Burgess",
            "17. school: Dorm Palace School, role: Student, class: 1,name: Jonathan Oneill",
            "18. school: Dorm Palace School, role: Student, class: 1,name: Katrina Davis",
            "19. school: Dorm Palace School, role: Student, class: 1,name: Kristen Robinson",
            "20. school: Dorm Palace School, role: Student, class: 1,name: Lindsay Haas",
            "21. school: Dorm Palace School, role: Student, class: 2,name: Abigail Beck",
            "22. school: Dorm Palace School, role: Student, class: 2,name: Andrew Williams",
            "23. school: Dorm Palace School, role: Student, class: 2,name: Ashley Berg",
            "24. school: Dorm Palace School, role: Student, class: 2,name: Elizabeth Anderson",
            "25. school: Dorm Palace School, role: Student, class: 2,name: Frank Mccormick",
            "26. school: Dorm Palace School, role: Student, class: 2,name: Jason Leon",
            "27. school: Dorm Palace School, role: Student, class: 2,name: Jessica Fowler",
            "28. school: Dorm Palace School, role: Student, class: 2,name: John Smith",
            "29. school: Dorm Palace School, role: Student, class: 2,name: Nicholas Smith",
            "30. school: Dorm Palace School, role: Student, class: 2,name: Scott Mckee",
            "31. school: Dorm Palace School, role: Student, class: 3,name: Abigail Smith",
            "32. school: Dorm Palace School, role: Student, class: 3,name: Cassandra Martinez",
            "33. school: Dorm Palace School, role: Student, class: 3,name: Elizabeth Anderson",
            "34. school: Dorm Palace School, role: Student, class: 3,name: John Scott",
            "35. school: Dorm Palace School, role: Student, class: 3,name: Kathryn Williams",
            "36. school: Dorm Palace School, role: Student, class: 3,name: Mary Miller",
            "37. school: Dorm Palace School, role: Student, class: 3,name: Ronald Mccullough",
            "38. school: Dorm Palace School, role: Student, class: 3,name: Sandra Davidson",
            "39. school: Dorm Palace School, role: Student, class: 3,name: Scott Martin",
            "40. school: Dorm Palace School, role: Student, class: 3,name: Victoria Jacobs",
            "41. school: Dorm Palace School, role: Student, class: 4,name: Carol Williams",
            "42. school: Dorm Palace School, role: Student, class: 4,name: Cassandra Huff",
            "43. school: Dorm Palace School, role: Student, class: 4,name: Deborah Harrison",
            "44. school: Dorm Palace School, role: Student, class: 4,name: Denise Young",
            "45. school: Dorm Palace School, role: Student, class: 4,name: Jennifer Pace",
            "46. school: Dorm Palace School, role: Student, class: 4,name: Joe Andrews",
            "47. school: Dorm Palace School, role: Student, class: 4,name: Michael Kelly",
            "48. school: Dorm Palace School, role: Student, class: 4,name: Monica Padilla",
            "49. school: Dorm Palace School, role: Student, class: 4,name: Tiffany Roman",
            "50. school: Dorm Palace School, role: Student, class: 4,name: Wendy Maxwell",
            "51. school: Dorm Palace School, role: Student, class: 5,name: Adam Smith",
            "52. school: Dorm Palace School, role: Student, class: 5,name: Angela Christian",
            "53. school: Dorm Palace School, role: Student, class: 5,name: Cody Edwards",
            "54. school: Dorm Palace School, role: Student, class: 5,name: Jacob Palmer",
            "55. school: Dorm Palace School, role: Student, class: 5,name: James Gonzalez",
            "56. school: Dorm Palace School, role: Student, class: 5,name: Justin Kaufman",
            "57. school: Dorm Palace School, role: Student, class: 5,name: Katrina Reid",
            "58. school: Dorm Palace School, role: Student, class: 5,name: Melissa Butler",
            "59. school: Dorm Palace School, role: Student, class: 5,name: Pamela Sutton",
            "60. school: Dorm Palace School, role: Student, class: 5,name: Sarah Murphy"
        ]

        school_title = kwargs.get("school_title", None)

        your_result = []

        return Response(your_result, status=status.HTTP_400_BAD_REQUEST)


class SchoolHierarchyAPIView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        """
        [Logical Test]

        description: get personnel list in hierarchy order by school's title, class and personnel's name.

        pattern: in `data_pattern` variable below.

        """

        data_pattern = [
            {
                "school": "Dorm Palace School",
                "class 1": {
                    "Teacher: Mark Harmon": [
                        {
                            "Head of the room": "Margaret Graves"
                        },
                        {
                            "Student": "Aaron Marquez"
                        },
                        {
                            "Student": "Benjamin Collins"
                        },
                        {
                            "Student": "Carolyn Reynolds"
                        },
                        {
                            "Student": "Christopher Austin"
                        },
                        {
                            "Student": "Deborah Mcdonald"
                        },
                        {
                            "Student": "Jessica Burgess"
                        },
                        {
                            "Student": "Jonathan Oneill"
                        },
                        {
                            "Student": "Katrina Davis"
                        },
                        {
                            "Student": "Kristen Robinson"
                        },
                        {
                            "Student": "Lindsay Haas"
                        }
                    ]
                },
                "class 2": {
                    "Teacher: Jared Sanchez": [
                        {
                            "Head of the room": "Darren Wyatt"
                        },
                        {
                            "Student": "Abigail Beck"
                        },
                        {
                            "Student": "Andrew Williams"
                        },
                        {
                            "Student": "Ashley Berg"
                        },
                        {
                            "Student": "Elizabeth Anderson"
                        },
                        {
                            "Student": "Frank Mccormick"
                        },
                        {
                            "Student": "Jason Leon"
                        },
                        {
                            "Student": "Jessica Fowler"
                        },
                        {
                            "Student": "John Smith"
                        },
                        {
                            "Student": "Nicholas Smith"
                        },
                        {
                            "Student": "Scott Mckee"
                        }
                    ]
                },
                "class 3": {
                    "Teacher: Cheyenne Woodard": [
                        {
                            "Head of the room": "Carla Elliott"
                        },
                        {
                            "Student": "Abigail Smith"
                        },
                        {
                            "Student": "Cassandra Martinez"
                        },
                        {
                            "Student": "Elizabeth Anderson"
                        },
                        {
                            "Student": "John Scott"
                        },
                        {
                            "Student": "Kathryn Williams"
                        },
                        {
                            "Student": "Mary Miller"
                        },
                        {
                            "Student": "Ronald Mccullough"
                        },
                        {
                            "Student": "Sandra Davidson"
                        },
                        {
                            "Student": "Scott Martin"
                        },
                        {
                            "Student": "Victoria Jacobs"
                        }
                    ]
                },
                "class 4": {
                    "Teacher: Roger Carter": [
                        {
                            "Head of the room": "Brittany Mullins"
                        },
                        {
                            "Student": "Carol Williams"
                        },
                        {
                            "Student": "Cassandra Huff"
                        },
                        {
                            "Student": "Deborah Harrison"
                        },
                        {
                            "Student": "Denise Young"
                        },
                        {
                            "Student": "Jennifer Pace"
                        },
                        {
                            "Student": "Joe Andrews"
                        },
                        {
                            "Student": "Michael Kelly"
                        },
                        {
                            "Student": "Monica Padilla"
                        },
                        {
                            "Student": "Tiffany Roman"
                        },
                        {
                            "Student": "Wendy Maxwell"
                        }
                    ]
                },
                "class 5": {
                    "Teacher: Cynthia Mclaughlin": [
                        {
                            "Head of the room": "Nathan Solis"
                        },
                        {
                            "Student": "Adam Smith"
                        },
                        {
                            "Student": "Angela Christian"
                        },
                        {
                            "Student": "Cody Edwards"
                        },
                        {
                            "Student": "Jacob Palmer"
                        },
                        {
                            "Student": "James Gonzalez"
                        },
                        {
                            "Student": "Justin Kaufman"
                        },
                        {
                            "Student": "Katrina Reid"
                        },
                        {
                            "Student": "Melissa Butler"
                        },
                        {
                            "Student": "Pamela Sutton"
                        },
                        {
                            "Student": "Sarah Murphy"
                        }
                    ]
                }
            },
            {
                "school": "Prepare Udom School",
                "class 1": {
                    "Teacher: Joshua Frazier": [
                        {
                            "Head of the room": "Tina Phillips"
                        },
                        {
                            "Student": "Amanda Howell"
                        },
                        {
                            "Student": "Colin George"
                        },
                        {
                            "Student": "Donald Stephens"
                        },
                        {
                            "Student": "Jennifer Lewis"
                        },
                        {
                            "Student": "Jorge Bowman"
                        },
                        {
                            "Student": "Kevin Hooper"
                        },
                        {
                            "Student": "Kimberly Lewis"
                        },
                        {
                            "Student": "Mary Sims"
                        },
                        {
                            "Student": "Ronald Tucker"
                        },
                        {
                            "Student": "Victoria Velez"
                        }
                    ]
                },
                "class 2": {
                    "Teacher: Zachary Anderson": [
                        {
                            "Head of the room": "Joseph Zimmerman"
                        },
                        {
                            "Student": "Alicia Serrano"
                        },
                        {
                            "Student": "Andrew West"
                        },
                        {
                            "Student": "Anthony Hartman"
                        },
                        {
                            "Student": "Dominic Frey"
                        },
                        {
                            "Student": "Gina Fernandez"
                        },
                        {
                            "Student": "Jennifer Riley"
                        },
                        {
                            "Student": "John Joseph"
                        },
                        {
                            "Student": "Katherine Cantu"
                        },
                        {
                            "Student": "Keith Watts"
                        },
                        {
                            "Student": "Phillip Skinner"
                        }
                    ]
                },
                "class 3": {
                    "Teacher: Steven Hunt": [
                        {
                            "Head of the room": "Antonio Hodges"
                        },
                        {
                            "Student": "Brian Lewis"
                        },
                        {
                            "Student": "Christina Wiggins"
                        },
                        {
                            "Student": "Christine Parker"
                        },
                        {
                            "Student": "Hannah Wilson"
                        },
                        {
                            "Student": "Jasmin Odom"
                        },
                        {
                            "Student": "Jeffery Graves"
                        },
                        {
                            "Student": "Mark Roberts"
                        },
                        {
                            "Student": "Paige Pearson"
                        },
                        {
                            "Student": "Philip Fowler"
                        },
                        {
                            "Student": "Steven Riggs"
                        }
                    ]
                },
                "class 4": {
                    "Teacher: Rachael Davenport": [
                        {
                            "Head of the room": "John Cunningham"
                        },
                        {
                            "Student": "Aaron Olson"
                        },
                        {
                            "Student": "Amanda Cuevas"
                        },
                        {
                            "Student": "Gary Smith"
                        },
                        {
                            "Student": "James Blair"
                        },
                        {
                            "Student": "Juan Boone"
                        },
                        {
                            "Student": "Julie Bowman"
                        },
                        {
                            "Student": "Melissa Williams"
                        },
                        {
                            "Student": "Phillip Bright"
                        },
                        {
                            "Student": "Sonia Gregory"
                        },
                        {
                            "Student": "William Martin"
                        }
                    ]
                },
                "class 5": {
                    "Teacher: Amber Clark": [
                        {
                            "Head of the room": "Mary Mason"
                        },
                        {
                            "Student": "Allen Norton"
                        },
                        {
                            "Student": "Eric English"
                        },
                        {
                            "Student": "Jesse Johnson"
                        },
                        {
                            "Student": "Kevin Martinez"
                        },
                        {
                            "Student": "Mark Hughes"
                        },
                        {
                            "Student": "Robert Sutton"
                        },
                        {
                            "Student": "Sherri Patrick"
                        },
                        {
                            "Student": "Steven Brown"
                        },
                        {
                            "Student": "Valerie Mcdaniel"
                        },
                        {
                            "Student": "William Roman"
                        }
                    ]
                }
            },
            {
                "school": "Rose Garden School",
                "class 1": {
                    "Teacher: Danny Clements": [
                        {
                            "Head of the room": "Troy Rodriguez"
                        },
                        {
                            "Student": "Annette Ware"
                        },
                        {
                            "Student": "Daniel Collins"
                        },
                        {
                            "Student": "Jacqueline Russell"
                        },
                        {
                            "Student": "Justin Kennedy"
                        },
                        {
                            "Student": "Lance Martinez"
                        },
                        {
                            "Student": "Maria Bennett"
                        },
                        {
                            "Student": "Mary Crawford"
                        },
                        {
                            "Student": "Rodney White"
                        },
                        {
                            "Student": "Timothy Kline"
                        },
                        {
                            "Student": "Tracey Nichols"
                        }
                    ]
                },
                "class 2": {
                    "Teacher: Ray Khan": [
                        {
                            "Head of the room": "Stephen Johnson"
                        },
                        {
                            "Student": "Ashley Jones"
                        },
                        {
                            "Student": "Breanna Baker"
                        },
                        {
                            "Student": "Brian Gardner"
                        },
                        {
                            "Student": "Elizabeth Shaw"
                        },
                        {
                            "Student": "Jason Walker"
                        },
                        {
                            "Student": "Katherine Campbell"
                        },
                        {
                            "Student": "Larry Tate"
                        },
                        {
                            "Student": "Lawrence Marshall"
                        },
                        {
                            "Student": "Malik Dean"
                        },
                        {
                            "Student": "Taylor Mckee"
                        }
                    ]
                },
                "class 3": {
                    "Teacher: Jennifer Diaz": [
                        {
                            "Head of the room": "Vicki Wallace"
                        },
                        {
                            "Student": "Brenda Montgomery"
                        },
                        {
                            "Student": "Daniel Wilson"
                        },
                        {
                            "Student": "David Dixon"
                        },
                        {
                            "Student": "John Robinson"
                        },
                        {
                            "Student": "Kimberly Smith"
                        },
                        {
                            "Student": "Michael Miller"
                        },
                        {
                            "Student": "Miranda Trujillo"
                        },
                        {
                            "Student": "Sara Bruce"
                        },
                        {
                            "Student": "Scott Williams"
                        },
                        {
                            "Student": "Taylor Levy"
                        }
                    ]
                },
                "class 4": {
                    "Teacher: Kendra Pierce": [
                        {
                            "Head of the room": "Christopher Stone"
                        },
                        {
                            "Student": "Brenda Tanner"
                        },
                        {
                            "Student": "Christopher Garcia"
                        },
                        {
                            "Student": "Curtis Flynn"
                        },
                        {
                            "Student": "Jason Horton"
                        },
                        {
                            "Student": "Julie Mullins"
                        },
                        {
                            "Student": "Kathleen Mckenzie"
                        },
                        {
                            "Student": "Larry Briggs"
                        },
                        {
                            "Student": "Michael Moyer"
                        },
                        {
                            "Student": "Tammy Smith"
                        },
                        {
                            "Student": "Thomas Martinez"
                        }
                    ]
                },
                "class 5": {
                    "Teacher: Elizabeth Hebert": [
                        {
                            "Head of the room": "Caitlin Lee"
                        },
                        {
                            "Student": "Alexander James"
                        },
                        {
                            "Student": "Amanda Weber"
                        },
                        {
                            "Student": "Christopher Clark"
                        },
                        {
                            "Student": "Devin Morgan"
                        },
                        {
                            "Student": "Gary Clark"
                        },
                        {
                            "Student": "Jenna Sanchez"
                        },
                        {
                            "Student": "Jeremy Meyers"
                        },
                        {
                            "Student": "John Dunn"
                        },
                        {
                            "Student": "Loretta Thomas"
                        },
                        {
                            "Student": "Matthew Vaughan"
                        }
                    ]
                }
            }
        ]

        your_result = []

        return Response(your_result, status=status.HTTP_200_OK)


class SchoolStructureAPIView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        """
        [Logical Test]

        description: get School's structure list in hierarchy.

        pattern: in `data_pattern` variable below.

        """

        data_pattern = [
            {
                "title": "มัธยมต้น",
                "sub": [
                    {
                        "title": "ม.1",
                        "sub": [
                            {
                                "title": "ห้อง 1/1"
                            },
                            {
                                "title": "ห้อง 1/2"
                            },
                            {
                                "title": "ห้อง 1/3"
                            },
                            {
                                "title": "ห้อง 1/4"
                            },
                            {
                                "title": "ห้อง 1/5"
                            },
                            {
                                "title": "ห้อง 1/6"
                            },
                            {
                                "title": "ห้อง 1/7"
                            }
                        ]
                    },
                    {
                        "title": "ม.2",
                        "sub": [
                            {
                                "title": "ห้อง 2/1"
                            },
                            {
                                "title": "ห้อง 2/2"
                            },
                            {
                                "title": "ห้อง 2/3"
                            },
                            {
                                "title": "ห้อง 2/4"
                            },
                            {
                                "title": "ห้อง 2/5"
                            },
                            {
                                "title": "ห้อง 2/6"
                            },
                            {
                                "title": "ห้อง 2/7"
                            }
                        ]
                    },
                    {
                        "title": "ม.3",
                        "sub": [
                            {
                                "title": "ห้อง 3/1"
                            },
                            {
                                "title": "ห้อง 3/2"
                            },
                            {
                                "title": "ห้อง 3/3"
                            },
                            {
                                "title": "ห้อง 3/4"
                            },
                            {
                                "title": "ห้อง 3/5"
                            },
                            {
                                "title": "ห้อง 3/6"
                            },
                            {
                                "title": "ห้อง 3/7"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "มัธยมปลาย",
                "sub": [
                    {
                        "title": "ม.4",
                        "sub": [
                            {
                                "title": "ห้อง 4/1"
                            },
                            {
                                "title": "ห้อง 4/2"
                            },
                            {
                                "title": "ห้อง 4/3"
                            },
                            {
                                "title": "ห้อง 4/4"
                            },
                            {
                                "title": "ห้อง 4/5"
                            },
                            {
                                "title": "ห้อง 4/6"
                            },
                            {
                                "title": "ห้อง 4/7"
                            }
                        ]
                    },
                    {
                        "title": "ม.5",
                        "sub": [
                            {
                                "title": "ห้อง 5/1"
                            },
                            {
                                "title": "ห้อง 5/2"
                            },
                            {
                                "title": "ห้อง 5/3"
                            },
                            {
                                "title": "ห้อง 5/4"
                            },
                            {
                                "title": "ห้อง 5/5"
                            },
                            {
                                "title": "ห้อง 5/6"
                            },
                            {
                                "title": "ห้อง 5/7"
                            }
                        ]
                    },
                    {
                        "title": "ม.6",
                        "sub": [
                            {
                                "title": "ห้อง 6/1"
                            },
                            {
                                "title": "ห้อง 6/2"
                            },
                            {
                                "title": "ห้อง 6/3"
                            },
                            {
                                "title": "ห้อง 6/4"
                            },
                            {
                                "title": "ห้อง 6/5"
                            },
                            {
                                "title": "ห้อง 6/6"
                            },
                            {
                                "title": "ห้อง 6/7"
                            }
                        ]
                    }
                ]
            }
        ]

        your_result = []

        return Response(your_result, status=status.HTTP_200_OK)
