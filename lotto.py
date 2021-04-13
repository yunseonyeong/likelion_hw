import random

INPUT_BUY_LOTTO_MESSAGE = "> 구입금액을 입력해 주세요:"
PRINTER_HOWMANY_LOTTO = "장의 로또를 구입하셨습니다."
INPUT_LAST_WINNING_MESSAGE = "> 지난 주 당첨 번호를 입력해 주세요:"
LOTTO_RANDOM_START_INDEX = 1
LOTTO_RANDOM_FINISH_INDEX = 45
LOTTO_AMOUNT_IN_ONE = 6
LOTTO_WINNING_RESULT_MESSAGE = "> 로또 당첨 결과"
LOTTO_PROFIT_MESSAGE = "> 수익률"

def main():
    lotto()

# lotto 금액을 입력받고 리턴하는 함수
def input_buy_lotto():
    input_buy = int(input(INPUT_BUY_LOTTO_MESSAGE))
    return input_buy

# ~원 >> ~장 으로 계산해주는 함수
def cal_howmany_lotto(input_buy):
    how_many = input_buy//1000
    printer_howmany_lotto(how_many)
    return how_many

# lotto 를 몇 장 구매했는지 프린트 해주는 함수
def printer_howmany_lotto(how_many):
    print('> ' + str(how_many) + PRINTER_HOWMANY_LOTTO)

# 랜덤으로 로또 숫자를 생성하는 함수
def random_create_lotto(how_many, lotto_nums):
    for i in range(how_many):
        for j in range(LOTTO_AMOUNT_IN_ONE):
            while True:
                num = random.randint(LOTTO_RANDOM_START_INDEX,LOTTO_RANDOM_FINISH_INDEX)
                if num not in lotto_nums[i]:
                    lotto_nums[i][j] = num
                    break
    
        lotto_nums[i].sort()    # 자동 정렬

# 생성된 로또 번호를 예쁘게 출력해준다.
def printer_lotto_nums(how_many, lotto_nums):
    for i in range(how_many) :
        print(lotto_nums[i])
    print("")

# 지난주 로또 당첨 번호를 한번에 받아온다.
def input_last_winning_num():
    last_winning = list(map(int, input(INPUT_LAST_WINNING_MESSAGE).split(",")))
    return last_winning

# 구입한 로또의 1등 ~ 4등 수 카운트 함수
def cal_matched_count(total_matched_count, matched_count):
    if matched_count == 3:
        total_matched_count[0] += 1
    elif matched_count == 4:
        total_matched_count[1] += 1
    elif matched_count == 5:
        total_matched_count[2] += 1
    elif matched_count == 6 : 
        total_matched_count[3] += 1

    return total_matched_count
    
# 로또 당첨 유무 확인하는 함수. 
def winning_lotto(how_many, last_winning, lotto_nums):
    
    total_matched_count = [0]*4     # 1등 ~ 4등 당첨 수 0으로 초기화

    for i in range(how_many):
        matched_count = 0       # 로또 1장 당 맞는 번호 수를 체크해주기 위해 초기화
        for j in range(LOTTO_AMOUNT_IN_ONE):
            if lotto_nums[i][j] in last_winning :       # 지난주 당첨번호에 내가 구입한 로또 번호가 존재한다면
                matched_count += 1                      # 카운트 + 1
        total_matched_count = cal_matched_count(total_matched_count,matched_count)  # 1등 ~ 4등 당첨 수 카운트 해주는 함수 불러옴

    print(LOTTO_WINNING_RESULT_MESSAGE)
    print("4등(3개가 맞을 때) - 5000원 -" + str(total_matched_count[0]) + "개")
    print("3등(4개가 맞을 때) - 20000원 -" + str(total_matched_count[1]) + "개")
    print("2등(5개가 맞을 때) - 100000원 -" + str(total_matched_count[2]) + "개")
    print("1등(6개가 맞을 때) - 5000000원 -" + str(total_matched_count[3]) + "개")

    return total_matched_count

# 수익률 계산 후 소수 둘째자리 까지 출력
def cal_profit(total_matched_count, input_buy):
    winning_money = (5000*total_matched_count[0] + 20000*total_matched_count[1] + 100000*total_matched_count[2] + 5000000*total_matched_count[3])
    profit = winning_money / input_buy
    print(LOTTO_PROFIT_MESSAGE)
    print("%0.2f"%profit + " 배")

# 로또 main 함수
def lotto():
    
    input_buy = input_buy_lotto()   # 구입 금액을 입력 받음
    how_many = cal_howmany_lotto(input_buy)     # 몇 장의 로또를 구입했는지 계산
    lotto_nums = [[-1]*LOTTO_AMOUNT_IN_ONE for i in range(how_many)]    # 로또 번호 리스트 초기화
    random_create_lotto(how_many,lotto_nums)            # 랜덤 로또 번호 생성
    printer_lotto_nums(how_many,lotto_nums)             # 생성된 로또 번호 자동 정렬 후 열 맞춰 출력 
    last_winning = input_last_winning_num()             # 지난 주 로또 당첨 번호 입력 받음
    total_matched_count = winning_lotto(how_many, last_winning, lotto_nums)     # 로또 1등 ~ 4등 당첨 수 계산 후 결과 반환
    cal_profit(total_matched_count, input_buy)                                  # 수익률 계산

if __name__ == "__main__":
    main()