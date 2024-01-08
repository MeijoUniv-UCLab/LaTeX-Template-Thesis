# 素数か否かを判定するプログラム

num = 29

# ユーザが入力する場合
#num = int(input("Enter a number: "))

# フラグ変数の定義
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # 約数のチェック
    for i in range(2, num):
        if (num % i) == 0:
            # 約数が見つかったらflagをTrueにする
            flag = True
            # ループを脱ける
            break

    # flagがTrueかチェック
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")