import faker

INSTANCE=None

def getFakerInstance():
    global INSTANCE
    
    if not INSTANCE:
        return faker.Faker()
    
    return INSTANCE 