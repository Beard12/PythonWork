class Underscore(object):
    def map(self,arr,callback):
        for x in xrange(len(arr)):
            arr[x] = callback(arr[x])
        return arr

    def reduce(self,arr,memo, callback):
        new = memo
        for x in xrange(len(arr)):
            new = callback(new,arr[x])
        return new
    def find(self,arr,callback):
        for x in xrange(len(arr)):
            if callback(arr[x]):
                return arr[x]
        return None
         
    def filter(self,arr, callback):
        newarr = []
        for x in xrange(0, len(arr)):
            if callback(arr[x]):
                newarr.append(arr[x])
        return newarr
        
    def reject(self,arr,callback):
        newarr = []
        for x in xrange(0, len(arr)):
            if not callback(arr[x]):
                newarr.append(arr[x])
        return newarr
    
_ = Underscore() 
# yes we are setting our instance to a variable that is an underscore
evens = _.reject([1, 0, 3, 4, 5, 6],lambda x: x > 2)
print evens
# should return [2, 4, 6] after you finish implementing the code above
