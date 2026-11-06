# Lab 3: Fuse check

def fuse_status(current, rating):
    if current < (rating * .8):
        return("OK")
    elif (.8 * rating) <= current <= rating:
        return("WARNING")
    else:
        return("BLOWN")

print(fuse_status(1.5, 2))
