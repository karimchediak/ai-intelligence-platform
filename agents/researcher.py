def research(query,index):
 hits=index.search(query); return {'query':query,'evidence':hits,'count':len(hits)}
