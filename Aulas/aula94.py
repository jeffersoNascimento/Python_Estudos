# try except, else e finally
try:
    print(123)
    # 8/0
except ZeroDivisionError:
    print('Dividiu por zero')
else:
    print('não deu erro')
finally: # sempre será executado mesmo que ocorra um erro
    print(456)