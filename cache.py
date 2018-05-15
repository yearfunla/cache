class cache:
    '''
    The class is creating the cache obj with max 3 spaces to store the cache
    '''
    def __init__(self):
        '''
        :param: creating a dict for the cache, where each key will contain a tuple (value, counter)
                the range of the counter is between 1 and 3
                When counter of the key is 1, it will be the next pop candidate
                When write a new key or read from the existing key, the counter will reset to 3.
                All the other keys will have to decrease the counter by 1
        '''
        self.cache = dict()
    def update(self,new_key):
        '''
        Creating an update method to handle the counter update for the existing key in the cache
        :param new_key: is the key that we newly access which conter is already been handled,
               will focus on updating counters for keys other than new_key
        '''
        # loop in the cache for finding and updating the other key
        for key in self.cache.keys():
            # store the value and the count for the updating in the future
            value, count = self.cache[key]

            if not new_key is key:
                # if the current key is not the new_key, decrease the counter by 1
                # the counter cannot be lower than 1
                self.cache[key] = (value,max(count-1,1))
    def get_cache(self):
        '''
        :return: the cache prevent people from access the cache variable
        '''
        return self.cache
    def read(self,key):
        '''
        Read the value of the key if cache has the key or return error msg
        :param key: the key we are looking for to get the value out
        :return: value of key is found or None as not found
        '''
        print "Trying to read key: " + key
        print 'Current cache: '
        print self.cache
        if key in self.cache.keys():
            # store the value and count from the tuple
            value, count = self.cache[key]
            # update the counter of the key to the current leng of cache or 3 if cache is fully stacked
            # however, we already handle the leng of the cache, in the write method, we can read how long is the cache directly
            # instead of comparing the len of the cache and 3 and taking the min value.
            self.cache[key] = (value,len(self.cache))
            if count < len(self.cache):
                self.update(key)
            print 'Found key ' + key + " is " + value
            print 'Updated cache is '
            print self.cache
            print '---------------------'
            return value
        else:
            print "We dont have key(" + key + ") in the cache"
            return None


    def write(self,key,value):
        # count of leng of cache
        print '---------------------'
        print "Adding " + key + ":" + value
        counts = len(self.cache.keys())
        cache_dict = self.cache

        # if key already in the list, overwrite the value
        if key in cache_dict.keys():
            cache_dict[key] = (value, min(3, counts + 1))
            # update other keys' counter
            self.update(key)
        elif counts < 3:
            # if cache still have space, add the key and value pair
            cache_dict.setdefault(key,(value,counts+1))
            # keys less than cache, no need to update counter
        elif counts == 3:
            # pop the key value pair out from the cache
            for it in cache_dict:
                if cache_dict[it][1] == 1 :
                    del cache_dict[it]
                    break
            cache_dict.setdefault(key, (value,3))
            self.update(key)
        #print cache_dict
        self.cache = cache_dict
        print "Updated cache: "
        print self.cache
        print '---------------------'
        return self.cache

print "Creating cache obj with default leng of 3"
c1 = cache()
c1.write('a','1')
c1.write('b','2')
c1.read('a')
c1.write('c','3')
c1.write('d','4')
c1.write('c','5')
c1.read('d')
print "Trying to revisit d and see if the cache stayed the same ot not"
c1.read('d')
c1.read('c')
print "Trying to access a invalid key"
c1.read('e')
c1.write('e','6')
