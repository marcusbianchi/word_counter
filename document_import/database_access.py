#!/usr/bin/env python3
import redis
import os


class database_access:
    def __init__(self):
        self.count = 0      
        self.postgrehost = 'localhost'

        if(os.environ.get('REDISGRESHOST') != None):
            self.postgrehost = os.environ.get('REDISGRESHOST')
        self.con = redis.StrictRedis(host=self.postgrehost, port=6379, db=0)


    

    
    def add_value_to_word_count(self, key,value):
        cur_value = self.con.get(key)
        if(cur_value==None):
            self.con.set(key, value)            
        else:
            cur = int(cur_value)
            self.con.set(key, cur+value)
