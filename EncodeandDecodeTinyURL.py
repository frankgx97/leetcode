class Codec:
    '''
    dictionary and increasing integer - ac
    use a dictionary to store the mapping of shortUrl and longUrl
    '''
    last = 0
    dic = {}
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.last += 1
        self.dic['http://tinyurl.com/'+str(self.last)] = longUrl
        return 'http://tinyurl.com/'+str(self.last)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dic[shortUrl]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
