import pickle
import os.path

def input_scores():
    scores = []
    print('[점수 입력]')
    while True:
        n = int(input(f'#{len(scores) + 1}?'))
        if n < 0:
            break
        scores.append(n)
    return scores

def get_average(scores):
    return sum(scores) / len(scores)

def show_scores(scores):
    print("[파일 읽기]")
    print('\n[점수 출력]')
    print('입력 점수 :', ' '.join(str(score) for score in scores))

def save_scores(scores):
    with open('score.bin', 'wb') as file:
        pickle.dump(scores, file)

def load_scores():
    if os.path.exists('score.bin'):
        with open('score.bin', 'rb') as file:
            scores = pickle.load(file)
            return scores
    else:
        return []


scores = load_scores()
if scores:
    show_scores(scores)
else:
    scores = input_scores()
    save_scores(scores)

avg = get_average(scores)
print(f'평균 : {avg:.1f}')
