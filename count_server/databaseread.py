import redis
import os
class databaseread():
    def __init__(self):
        self.count = 0      
        self.postgrehost = 'localhost'
        print(os.environ.get('REDISGRESHOST'))
       

    def read_current_value(self, key):
        if(os.environ.get('REDISGRESHOST') != None):
            self.postgrehost = os.environ.get('REDISGRESHOST')
        self.con = redis.StrictRedis(host=self.postgrehost, port=6379, db=0)   
        cur_value = self.con.get(key)
        
        return int(cur_value)