# in this excersice we will implemint the singleton design pattern as a decorator to restrict
# a more than one connection to database 

def singleton(instance):
    instances = {}
    def wrapper():
        if instance not in instances:
            instances[instance] = instance()
        return instances[instance]
    return wrapper

#Without the singletopn decorator
class MongoDb_Connection:
    def __init__(self):
        print("Connection is established")

@singleton
class MongoDb_Connection_Singleton:
    def __init__(self):
        print("Connection established one time")


if __name__ == '__main__':
    mongo_conn = MongoDb_Connection()
    mongo_conn2 = MongoDb_Connection()
    print(mongo_conn == mongo_conn2)#false cause we established it two times

    #With singleton
    mongo_conn_singleton = MongoDb_Connection_Singleton()
    mongo_conn_singleton2 = MongoDb_Connection_Singleton()
    print(mongo_conn_singleton == mongo_conn_singleton2) #True Cause we add a singletopn decorator
