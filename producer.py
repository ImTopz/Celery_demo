from tasks import send_msg, send_email,toUpdate



if __name__ == '__main__':
    for i in range(10):
        result = toUpdate()
        print(result.id)
