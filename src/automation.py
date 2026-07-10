import random
import time


class TeacherRegistrationBot:

    def __init__(self):
        self.logged = False

    def login(self):
        print("=" * 50)
        print("Conectando ao ERP...")
        time.sleep(1)

        self.logged = True

        print("Login realizado com sucesso.")
        print("=" * 50)

    def teacher_exists(self, teacher):
        print(f"[CHECK] Verificando docente: {teacher.name}")
        time.sleep(1)

        exists = random.choice([False, False, False, True])

        if exists:
            print("Docente já cadastrado.")
        else:
            print("Docente não encontrado.")

        return exists

    def register_teacher(self, teacher):
        print(f"[REGISTER] Cadastrando {teacher.name}")
        time.sleep(1)

        print("Cadastro realizado com sucesso.")

    def link_teacher(self, teacher):
        print(f"[LINK] Vinculando {teacher.name}")
        time.sleep(1)

        print("Vínculo realizado.")

    def process_teacher(self, teacher):

        print("-" * 50)

        if self.teacher_exists(teacher):
            return {
                "Teacher": teacher.name,
                "Status": "Already Registered"
            }

        self.register_teacher(teacher)
        self.link_teacher(teacher)

        return {
            "Teacher": teacher.name,
            "Status": "Registered"
        }

    def close(self):
        print("=" * 50)
        print("Encerrando automação...")
        print("=" * 50)