"""
問題：仕訳の向きチェッカー

勘定科目が「増えた／減った」ときに、借方・貸方の
どちらに記入するかを判定するプログラムを作成してください。

① Account クラスを作成してください。
次の2つの属性を持たせます。
・name：科目名
・element：要素（資産・負債・純資産・収益・費用）

② Account クラスに get_side メソッドを作成してください。
引数 change に「増えた」または「減った」を受け取り、
次のルールに従って「借方」か「貸方」を返してください。

            増えたとき   減ったとき
資産・費用       借方         貸方
負債・純資産・収益 貸方         借方

判定には if 文を使ってください。

③ 次の5つのインスタンスを作成し、リストに入れてください。
・現金：資産
・借入金：負債
・資本金：純資産
・売上：収益
・給料：費用

④ for 文でリストから勘定科目を順に取り出し、
get_side メソッドを使って、増えた場合・減った場合の
判定結果をそれぞれ表示してください。

⑤ ターミナルで実行すると、次のように表示されるようにしてください。

現金（資産）が増えたら → 借方
現金（資産）が減ったら → 貸方
借入金（負債）が増えたら → 貸方
借入金（負債）が減ったら → 借方
資本金（純資産）が増えたら → 貸方
資本金（純資産）が減ったら → 借方
売上（収益）が増えたら → 貸方
売上（収益）が減ったら → 借方
給料（費用）が増えたら → 借方
給料（費用）が減ったら → 貸方

※ 入力は指定された要素と「増えた」「減った」だけを扱います。
ターミナル入力や、不正な値への対応は不要です。
"""

# ここに解答コードを書いてください
class Account:
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def get_side(self, change):    
        if self.element == "資産" or self.element == "費用":
            if change == "増えた":
                return "借方"
            else:
                return "貸方"
        else:
            if change == "増えた":
                return "貸方"
            else:
                return "借方"
accounts = [
    Account("現金", "資産"),
    Account("借入金", "負債"),
    Account("資本金", "純資産"),
    Account("売上", "収益"),
    Account("給料", "費用"),
]
for account in accounts:
    print(f"{account.name}（{account.element}）が増えたら → {account.get_side('増えた')}")
    print(f"{account.name}（{account.element}）が減ったら → {account.get_side('減った')}")
