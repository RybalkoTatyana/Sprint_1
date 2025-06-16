timing = '1h 45m,360s,25m,30m 120s,2h 60s'
timing = timing.replace(',', ' ')
timing = timing.split()
timong_sum = 0
for i in timing:
    if 'm' in i:
        timong_sum += int(i[:-1])
    elif 'h' in i:
        timong_sum +=( int(i[:-1]) * 60)
    elif 's' in i:
        timong_sum +=( int(i[:-1]) // 60)
print(timong_sum)