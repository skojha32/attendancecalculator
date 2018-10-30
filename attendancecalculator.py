#Added new features hence declared as global variables
atd_req = None
ur_att = None
def accept():
    """ This function accepts all the information required for the program to run
    accepts:
        total no. of classes, No. of classes attended and the attendance % required
    args:
        None
    returns:
        It returns a tuple of the total no. of classes and no. of classes attended"""
    global atd_req
    tot_cls = int(input('Enter total no. of classes: '))
    cls_atd = int(input('Enter no. of classes attended: '))
    atd_req = int(input('Enter the attendance required: '))
    tup = tot_cls, cls_atd
    return tup

def compute(tup):
    """This function calculates the no. of classes needed for maintaining 75% attendance
    and also calculates the no. of extra classes required to make the attendance 75% and
    it calculates the current attendance %
    args:
        It accepts a tuple of the total no. of classes and the number of classes attended
    returns:
        It returns the no.of extra classes required to make the attendance 75% if the present
        attendance % is below 75% else tells u that u already have 75% of attendance."""
    global ur_att
    tot_cls, cls_atd = tup
    ur_att = int(cls_atd/tot_cls * 100)
    min_att = (atd_req*tot_cls)/100
    if cls_atd >= min_att:
        return 0
    else:
        m = cls_atd
        flag=0
        while flag<atd_req:
            tot_cls+=1
            cls_atd+=1
            flag = (cls_atd/tot_cls)*100
    return cls_atd-m

def print_result(flag):
    """It prints the output of the program.
    args:
        It accepts no. of classes required for the student to get above 75% if the student has
        below 75% attendance or else it says the student has more than 75% attendance.
    return:
         It prints out the output"""
    print("Your attendance percentage is: {}".format(ur_att))
    if flag == 0:
        print("You have more than {}% attendance.".format(atd_req))
    else:
        print("You have less than {}% attendance and you need more {} classes to make it up.".format(atd_req, flag))


tup = accept()
flag = compute(tup)
print_result(flag)
