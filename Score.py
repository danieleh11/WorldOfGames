from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    with open(SCORES_FILE_NAME, "r") as readfile:
        score = int(readfile.read())
        POINTS_OF_WINNING = (difficulty * 3) + 5
        sum_points = score + POINTS_OF_WINNING
        total = str(sum_points)
        readfile.close()
    with open(SCORES_FILE_NAME, "w") as writefile:
        writefile.writelines(total)
        writefile.close()


def zero_on_score():
    score = open(SCORES_FILE_NAME, 'r')
    score_read = score.read()
    if score_read != '0':
        update_score = open(SCORES_FILE_NAME, 'w')
        update_score.writelines(str('0'))
        update_score.close()
