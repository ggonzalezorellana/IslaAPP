import random

def divide_teams(people):
    # Separate men and women
    men = [person for person in people if person['gender'] == 'male']
    women = [person for person in people if person['gender'] == 'female']
    
    # Shuffle the men and women separately
    random.shuffle(men)
    random.shuffle(women)
    
    # Divide each group into three teams
    teams = []
    for i in range(3):
        team = {'men': [], 'women': []}
        
        # Add two good and two bad men and women to the team
        good_men = [man for man in men[i*4:i*4+4] if man['quality'] == 'good']
        bad_men = [man for man in men[i*4:i*4+4] if man['quality'] == 'bad']
        good_women = [woman for woman in women[i*4:i*4+4] if woman['quality'] == 'good']
        bad_women = [woman for woman in women[i*4:i*4+4] if woman['quality'] == 'bad']
        team['men'].extend(good_men[:2])
        team['men'].extend(bad_men[:2])
        team['women'].extend(good_women[:2])
        team['women'].extend(bad_women[:2])
        
        # Add three more people (either good or bad) to the team
        if len(team['men']) == 4:
            good_extra = [man for man in men[12+i*2:12+i*2+2] if man['quality'] == 'good']
            bad_extra = [man for man in men[12+i*2:12+i*2+2] if man['quality'] == 'bad']
            if len(good_extra) == 2:
                team['men'].extend(good_extra)
                team['women'].extend(women[12+i])
            else:
                team['men'].extend(bad_extra[:2])
                team['women'].extend(bad_extra[2:])
        else:
            good_extra = [woman for woman in women[12+i*2:12+i*2+2] if woman['quality'] == 'good']
            bad_extra = [woman for woman in women[12+i*2:12+i*2+2] if woman['quality'] == 'bad']
            if len(good_extra) == 2:
                team['women'].extend(good_extra)
                team['men'].extend(men[12+i])
            else:
                team['women'].extend(bad_extra[:2])
                team['men'].extend(bad_extra[2:])
        
        # Add the team to the list of teams
        teams.append(team)
    
    return teams