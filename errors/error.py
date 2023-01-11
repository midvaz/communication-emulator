import datetime

path = "../logs"

def create_log_file():
    log_name = str(datetime.datetime.now())
    try:
        with open(file=f"{path}/{log_name}.txt", mode="w", encoding="UTF-8") as f:
            return f
    except:
        print("Error at write error")



def write_errors_in_file (message_error: str):
    file = create_log_file()
    file.writelines([
            message_error,
            str(datetime.datetime.now())
    ])