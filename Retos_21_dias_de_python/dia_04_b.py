""" DIA #4-B Obtén el promedio de los estudiantes

En este desafío, deberás calcular el promedio general de una clase, así como el promedio individual de cada estudiante.
Para ello, se te proporcionará una lista de diccionarios, cada uno de los cuales representará a un estudiante y tendrá las siguientes propiedades:
"name": El nombre del estudiante
"grades": Las notas de cada materia del estudiante
A partir de esta información, debes retornar un nuevo diccionario que tenga la propiedad "class_average" con el promedio de la clase y
 una lista de "students" con los estudiantes y sus promedios individuales.

Es importante mencionar que los promedios deben ser calculados con precisión y
se deben redondear a dos decimales para que los test pasen sin problema alguno.
Puedes usar el método round() el cual se usa de la siguiente manera

number = 100.32433
number = round(number, 2)
# 100.32

Ejemplo:
Input: get_student_average([{ "name": "Pedro",
                                "grades": [90, 87, 88, 90],
                            },
                          {
                            "name": "Jose",
                            "grades": [99, 71, 88, 96],
                          },
                          {
                            "name": "Maria",
                            "grades": [92, 81, 80, 96],
                          },
                        ])

Output: {
          "class_average": 88.17,
          "students": [
            {
              "name": "Pedro",
              "average": 88.75
            },
            {
              "name": "Jose",
              "average": 88.5
            },
            {
              "name": "Maria",
              "average": 87.25
            }
  ]
}
"""
import copy
import numbers

def get_student_average(students) -> dict:
    """Analiza las notas de un grupo de estudiantes a partir de sus notas individuales
    Args:
        students:
            lista de diccionarios

    Returns:
        {
          "class_average": float,
          "students": list[dict]  # sin grades, con average
        }

    """

    if not isinstance(students, list) or len(students) == 0:
        raise ValueError("debes ingresar una lista no vacía")
    for student in students:
        if not isinstance(student, dict):
            raise  ValueError("La lista debe contener diccionarios con el nombre del estudiante y una lista de sus notas")
        if "grades" not in student:
            raise ValueError("Cada estudiante debe tener la clave 'grades'")
        if not isinstance(student["grades"], list):
            raise ValueError("debe ser una lista")
        elif len(student["grades"]) == 0:
            raise ValueError("La lista de notas de cada estudiante debe ser no vacía")
        for n in student["grades"]:
            if not isinstance(n, numbers.Real):
                raise ValueError("Las notas deben ser números reales")


    students_average = [round(sum(student["grades"])/len(student["grades"]),2) for student in  students]
    class_average = round(sum(students_average) /len(students_average),2)

    data_students =  copy.deepcopy(students)
    for student, n  in zip(data_students, students_average):
        student["average"] = n
        del student['grades']

    class_info = {
            "class_average" : class_average,
            "students" : data_students
                 }

    return class_info


students = [{ "name": "Pedro",
                                "grades": [90, 87, 88, 90],
                            },
                          {
                            "name": "Jose",
                            "grades": [99, 71, 88, 96],
                          },
                          {
                            "name": "Maria",
                            "grades": [92, 81, 80, 96],
                          },
                        ]

print(get_student_average(students))


