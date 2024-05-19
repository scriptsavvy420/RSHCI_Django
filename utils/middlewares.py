
def admin_middleware(user):
    if user.is_superuser or user.is_staff:
        return True
    else:
        return False
        

def user_middleware(user):
    if not user.is_authenticated:
        return False
    
    if not user.is_active:
        return False
    
    return True


def employer_middleware(user):
    rslt = user_middleware(user)

    if rslt == False:
        return False
    else:
        if user.user_type == "employer":
            return True
        else:
            return False
        

def employee_middleware(user):
    rslt = user_middleware(user)

    if rslt == False:
        return False
    else:
        if user.user_type == "employee":
            return True
        else:
            return False
        

def proposal_middleware(user):
    rslt = employee_middleware(user)

    if rslt == False:
        return False
    else:
        if user.status == 3:
            return False
        else:
            return True