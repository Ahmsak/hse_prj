from bitshares import BitShares
from bitshares.account import Account
from bitshares.asset import Asset
from bitshares.market import Market
from bitshares.amount import Amount
from bitshares.dex import Dex

# коннектимся к рудексу
bitshares = BitShares("wss://node.market.rudex.org")
dex = Dex(bitshares)

# открываем свой локальный кошелек
dex.bitshares.wallet.unlock("secret_wallet_password")
# открываем свой локальный кошелек
#bitshares.wallet.unlock("secret_wallet_password")

# наш коэф. перекрытия
init_ratio = 2.00
max_ratio = 2.10
margin_ratio = 1.75

# наш аккаунт
our_account = "id-b0t"
our_symbol = "CNY"
current_ratio = 0

# наша пара
base = Asset(our_symbol)
quote = Asset("BTS")

# выбираем рынок
market = Market(base, quote)

# открываем свой локальный кошелек
market.bitshares.wallet.unlock("secret_wallet_password")

# получаем аккаунт для работы бота
account = Account(our_account)
print(account)

# проверяем есть ли займы по нашему битассету
cp = account.callpositions
# если есть любые займы
if len(cp) > 0:
    print(cp)
    # проверяем есть ли по юаню
    cp2 = cp.get(our_symbol)
    if cp2 is not None:
        print(cp2)
        # получаем коэффициент перекрытия
        current_ratio = cp2.get('ratio')
        print(current_ratio)

    # проверяем не повысился ли коэффициент перекрытия выше нормы
    if current_ratio > max_ratio:
        # если увеличился, то  
        open_orders = market.accountopenorders(account)
        print(len(open_orders))
        # удаляем ордер на откуп шар по МК
        dex.close_debt_position(our_symbol, our_account)

        #if len(open_orders) == 1:
        #    for h in account.history(1,1,10):
        #        print(h)
        #        o_num = h.get('result')
        #        first = o_num[0]
        #        print(first)
        #        order_num = o_num[1]
        #        print(order_num)
        #        if first == 1:
        #            #market.cancel(order_num, account)
        #            break  
        # удаляем старый займ
    elif current_ratio <= margin_ratio: 
        # если поймали моржа
        bbitasset = account.balance(base)
        print(bitasset)

        # подготавливаем переменную вида "1 CNY"
        amount = Amount(bitasset, base)
        print(amount)

        # ставим ордер на откуп нашего МК
        market.sell(0.00001, amount, 8640000, False, our_account) 

else:
    # займов нет, надо брать :)
    # расчитываем сколько юаней можем напечатать

    # получаем цену погашения
    ticker = market.ticker()
    data = ticker.get('quoteSettlement_price')
    feed_price = data.get('price')
    print(feed_price)

    # получаем баланс в шарах на аккаунте
    balance = account.balance(quote)
    # всегда берем целую часть шар для займа. остаток оставляем на комиссии
    collateral = int(balance.get('amount'))
    print(collateral)

    if collateral > 0:
        # находим сколько можно напечатать юаней с нашим перекрытием
        debt = (1/feed_price)/init_ratio*collateral
        print(debt)

        # подготавливаем переменную вида "1 CNY"
        amount = Amount(debt, base)
        print(amount)

        # печатаем битассет
        dex.borrow(amount, collateral, our_account)

        # расчитываем call price
        #call_price = 1/((debt/collateral)*margin_ratio)
        #print(call_price)


print('done!')


