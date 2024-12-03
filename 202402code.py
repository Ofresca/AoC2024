import copy

D = open("202402in.txt").read().split('\n')

# Rules:
#    The levels are either all increasing or all decreasing.
#    Any two adjacent levels differ by at least one and at most three.

p1 = p2 = 0

def is_safe(report):
    report_dif = [y-x for x,y in zip(report, report[1:])]
    return set(report_dif) <= {1, 2, 3} or set(report_dif) <= {-1, -2, -3}

for report in D:
    report = list(map(int, report.split()))
    p1 += is_safe(report)
    p2 += any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))
    
print(p1)
print(p2) 


""" p2 += is_safe(report, 1)

    report_dif = [y-x for x,y in zip(report, report[1:])]
    if (not (min(report_dif) < 0 < max(report_dif))) and 4>abs(min(report_dif))>0 and 0<abs(max(report_dif))<4:
        p1 += 1
        p2 += 1
    else:
        c_report = copy.deepcopy(report)
        for i in range(len(c_report)):
            report = copy.deepcopy(c_report)
            report.pop(i)
            report_dif = [y-x for x,y in zip(report, report[1:])]
            if (not (min(report_dif) < 0 < max(report_dif))) and 4>abs(min(report_dif))>0 and 0<abs(max(report_dif))<4:
                p2 += 1
                break
 """