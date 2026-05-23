from fastapi import FastAPI, HTTPException

app_1 = FastAPI()

# Sample student data
students = {
    1: {
        "name": "Mahesh",
        "course": "Computer Engineering"
    },
    2: {
        "name": "Rahul",
        "course": "Information Technology"
    },
    3: {
        "name": "Aman",
        "course": "AI & Data Science"
    }
}


@app_1.get("/")
def welcome():
    return {
        "message": "Welcome to the FastAPI app!"
    }


@app_1.get("/about")
def about():
    return {
        "name": "Durga Mahesh Uppu",
        "internship_title": "Software Development Intern"
    }


# Endpoint to get student by ID
@app_1.get("/students/{student_id}")
def get_student(student_id: int):

    # Error handling
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student ID not found"
        )

    return students[student_id]