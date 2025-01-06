import unittest
from VendingMachine import VendingMachine



#стартовые параметры
adminCode = 117345294655382
max1 = 30
max2 = 40
maxc1 = 50
maxc2 = 50
num1 = 0
num2 = 0
price1 = 8
price2 = 5
coins1 = 0
coins2 = 0
balance = 0
coinval1 = 1
coinval2 = 2


class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.VM = VendingMachine()

    def testGetNumberOfProduct1(self):
        print ("getNumberOfProduct1", num1)
        self.assertEqual(num1, self.VM.getNumberOfProduct1())

    def testGetNumberOfProduct2(self):
        print ("getNumberOfProduct2", num2)
        self.assertEqual(num2, self.VM.getNumberOfProduct2())

    def testGetCurrentBalance(self):
        print ("getCurrentBalance", balance)
        self.assertEqual(balance, self.VM.getCurrentBalance())

    def testGetCurrentMode(self):
        print ("getCurrentMode", self.VM.Mode.OPERATION)
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())

    def testGetCurrentSumOperationMode(self):
        print ("getCurrentSumOperationMode", 0)
        self.assertEqual(0, self.VM.getCurrentSum())

    def testGetCoins1OperationMode(self):
        print ("getCoins1OperationMode", coins1)
        self.assertEqual(coins1, self.VM.getCoins1())

    def testGetCoins2OperationMode(self):
        print ("getCoins2OperationMode", coins2)
        self.assertEqual(coins2, self.VM.getCoins2())

    def testGetPrice1(self):
        print ("getPrice1", price1)
        self.assertEqual(price1, self.VM.getPrice1())

    def testGetPrice2(self):
        print ("getPrice2", price2)
        self.assertEqual(price2, self.VM.getPrice2())

    def testFillProductsOperationMode(self):
        print ("fillProductsOperationMode")
        self.assertEqual(self.VM.Response.ILLEGAL_OPERATION, self.VM.fillProducts())

    def testFillCoinsOperationMode(self):
        print ("fillCoinsOperationMode")
        self.assertEqual(self.VM.Response.ILLEGAL_OPERATION, self.VM.fillCoins(0, 0))

    def testEnterAdminModeWrongMode(self):
        print ("enterAdminModeWrongMode")
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.enterAdminMode(0))
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())

    def testEnterAdminModeCorrect(self):
        print ("enterAdminModeCorrect")
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())

    def testFillProductsAdministeringMode(self):
        print ("fillProductsAdministeringMode")
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.OK, self.VM.fillProducts())
        self.assertEqual(max1, self.VM.getNumberOfProduct1())
        self.assertEqual(max2, self.VM.getNumberOfProduct2())
    
    def testFillCoinsAdministeringMode(self):
        print ("fillCoinsAdministeringMode")
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        print ("fillCoinsAdministeringMode", -1, -1)
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.fillCoins(-1, -1))
        self.assertEqual(coins1, self.VM.getCoins1())
        self.assertEqual(coins2, self.VM.getCoins2())
        print ("fillCoinsAdministeringMode", 0, 0)
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.fillCoins(0, 0))
        self.assertEqual(coins1, self.VM.getCoins1())
        self.assertEqual(coins2, self.VM.getCoins2())
        print ("fillCoinsAdministeringMode", 1, -1)
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.fillCoins(1, -1))
        self.assertEqual(coins1, self.VM.getCoins1())
        self.assertEqual(coins2, self.VM.getCoins2())
        print ("fillCoinsAdministeringMode", -1, 1)
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.fillCoins(-1, 1))
        self.assertEqual(coins1, self.VM.getCoins1())
        self.assertEqual(coins2, self.VM.getCoins2())
        print ("fillCoinsAdministeringMode", maxc1 + 1, maxc2 + 1)
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.fillCoins(maxc1 + 1, maxc2 + 1))
        self.assertEqual(coins1, self.VM.getCoins1())
        self.assertEqual(coins2, self.VM.getCoins2())
        print ("fillCoinsAdministeringMode", 1, maxc2 + 1)
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.fillCoins(1, maxc2 + 1))
        self.assertEqual(coins1, self.VM.getCoins1())
        self.assertEqual(coins2, self.VM.getCoins2())
        print ("fillCoinsAdministeringMode", maxc1 + 1, 1)
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.fillCoins(maxc1 + 1, 1))
        self.assertEqual(coins1, self.VM.getCoins1())
        self.assertEqual(coins2, self.VM.getCoins2())
        for i in range(1, 51):
            for j in range(1, 51):
                print ("fillCoinsAdministeringMode", i, j, self.VM.Response.OK)
                self.assertEqual(self.VM.Response.OK, self.VM.fillCoins(i, j))
                self.assertEqual(i, self.VM.getCoins1())
                self.assertEqual(j, self.VM.getCoins2())
                self.assertEqual(i * coinval1 + j * coinval2, self.VM.getCurrentSum())
    
    def testExitAdminMode(self):
        print ("exitAdminMode")
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
    
    def testSetPrices(self):
        print ("setPricesOperationMode")
        self.assertEqual(self.VM.Response.ILLEGAL_OPERATION, self.VM.setPrices(1, 1))
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        print ("setPricesAdministeringMode", 0, 0)
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.setPrices(0, 0))
        print ("setPricesAdministeringMode", 1, 0)
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.setPrices(1, 0))
        print ("setPricesAdministeringMode", 0, 1)
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.setPrices(0, 1))
        print ("setPricesAdministeringMode", -1, -1)
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.setPrices(-1, -1))
        for i in range (1, 100, 10):
            for j in range (1, 100, 10):
                print ("setPricesAdministeringMode", i, j, self.VM.Response.OK)
                self.assertEqual(self.VM.Response.OK, self.VM.setPrices(i, j))
                self.assertEqual(i, self.VM.getPrice1())
                self.assertEqual(j, self.VM.getPrice2())
    
    def testPutCoin1(self):
        print ("putCoin1AdministeringMode")
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.ILLEGAL_OPERATION, self.VM.putCoin1())
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        for i in range (1, maxc1 + 1):
            print ("putCoin1OperrationMode", i)
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
            self.assertEqual(i * coinval1, self.VM.getCurrentBalance())
        self.assertEqual(self.VM.Response.CANNOT_PERFORM, self.VM.putCoin1())
        print ("enterAdminModeBalance")
        self.assertEqual(self.VM.Response.CANNOT_PERFORM, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
    
    def testPutCoin2(self):
        print ("putCoin2AdministeringMode")
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.ILLEGAL_OPERATION, self.VM.putCoin2())
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        for i in range (1, maxc2 + 1):
            print ("putCoin2OperrationMode", i)
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin2())
            self.assertEqual(i * coinval2, self.VM.getCurrentBalance())
        self.assertEqual(self.VM.Response.CANNOT_PERFORM, self.VM.putCoin2())
        print ("enterAdminModeBalance")
        self.assertEqual(self.VM.Response.CANNOT_PERFORM, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
    
    def testPutCoin1and2(self):
        for i in range (1, min(maxc1 + 1, maxc2 + 1)):
            print ("putCoin1and2OperrationMode", i)
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin2())
            self.assertEqual(i * coinval1 + i * coinval2, self.VM.getCurrentBalance())
        self.assertEqual(self.VM.Response.CANNOT_PERFORM, self.VM.putCoin2())
        self.assertEqual(self.VM.Response.CANNOT_PERFORM, self.VM.putCoin1())
        print ("enterAdminModeBalance")
        self.assertEqual(self.VM.Response.CANNOT_PERFORM, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
    
    def testReturnMoney(self):
        print ("returnMoneyAdministeringMode")
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.ILLEGAL_OPERATION, self.VM.returnMoney())
        self.VM.exitAdminMode()
        print ("returnMoneyOperrationMode", 0)
        self.assertEqual(self.VM.Response.OK, self.VM.returnMoney())
        print ("returnMoneyOperrationMode", 5, 1)
        c1 = 5
        c2 = 1
        for i in range(0, c1):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        for i in range(0, c2):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin2())
        self.assertEqual(self.VM.Response.OK, self.VM.returnMoney())
        self.assertEqual(0, self.VM.getCurrentBalance())
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(0, self.VM.getCoins1())
        self.assertEqual(0, self.VM.getCoins2())
    
    def testReturnMoneySpec1(self):
        # В автомат водились монетки номиналом 1, но в автомате для выдачи был номинал 2 достаточного для выдачи только им
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.OK, self.VM.fillCoins(1, 10))
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        for i in range(0, 10):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        # Монет 11 и 10 соответсвенно, должны потратиться 5 монет номинала 2
        self.assertEqual(self.VM.Response.OK, self.VM.returnMoney())
        self.assertEqual(0, self.VM.getCurrentBalance())
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(11, self.VM.getCoins1())
        self.assertEqual(5, self.VM.getCoins2())
    
    def testReturnMoneySpec2(self):
        # В автомат водились монетки номиналом 1, но в автомате для выдачи был номинал 2 для выдачи части им
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.OK, self.VM.fillCoins(1, 1))
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        for i in range(0, 10):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        # Монет 11 и 1 соответсвенно, должны потратиться 1 монет номинала 2 и 8 номинала 1
        self.assertEqual(self.VM.Response.OK, self.VM.returnMoney())
        self.assertEqual(0, self.VM.getCurrentBalance())
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(3, self.VM.getCoins1())
        self.assertEqual(0, self.VM.getCoins2())
    
    def testReturnMoneySpec3(self):
        # В автомат водились монетки номиналом 1, но в автомате для выдачи был номинал 2 достаточного для выдачи только им, исключая разницу в нечётности
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.OK, self.VM.fillCoins(1, 10))
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        for i in range(0, 9):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        # Монет 10 и 10 соответсвенно, должны потратиться 4 монет номинала 2 и 1 номинала 1
        self.assertEqual(self.VM.Response.OK, self.VM.returnMoney())
        self.assertEqual(0, self.VM.getCurrentBalance())
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(9, self.VM.getCoins1())
        self.assertEqual(6, self.VM.getCoins2())

    def testGiveProduct1(self):
        print ("giveProduct1AdministeringMode")
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.ILLEGAL_OPERATION, self.VM.giveProduct1(1))
        self.assertEqual(self.VM.Response.OK, self.VM.fillProducts())
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        print ("giveProduct1OperrationModeError", self.VM.Response.INVALID_PARAM)
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.giveProduct1(0))
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.giveProduct1(-1))
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.giveProduct1(max1 + 1))
        print ("giveProduct1OperrationModeNormal")
        for i in range(0, price1):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        self.assertEqual(self.VM.Response.OK, self.VM.giveProduct1(1))
        self.assertEqual(0, self.VM.getCurrentBalance())
        self.assertEqual(max1 - 1, self.VM.getNumberOfProduct1())
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(price1, self.VM.getCoins1())
        self.assertEqual(0, self.VM.getCoins2())
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        print ("giveProduct1OperrationModeError", self.VM.Response.INSUFFICIENT_PRODUCT)
        self.assertEqual(self.VM.Response.INSUFFICIENT_PRODUCT, self.VM.giveProduct1(max1))
        print ("giveProduct1OperrationModeError", self.VM.Response.INSUFFICIENT_MONEY)
        self.assertEqual(self.VM.Response.INSUFFICIENT_MONEY, self.VM.giveProduct1(max1 - 1))
        for i in range(0, price1):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        self.assertEqual(self.VM.Response.INSUFFICIENT_MONEY, self.VM.giveProduct1(2))
        self.assertEqual(price1, self.VM.getCurrentBalance())
    
    def testGiveProduct1Spec1(self):
        # В автомат водились монетки номиналом 1, но в автомате для выдачи был номинал 2 достаточного для выдачи только им
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.OK, self.VM.fillProducts())
        # Устанавливаем цену на продукт 1 в виде 2
        self.assertEqual(self.VM.Response.OK, self.VM.setPrices(2, 1))
        self.assertEqual(2, self.VM.getPrice1())
        self.assertEqual(1, self.VM.getPrice2())
        self.assertEqual(self.VM.Response.OK, self.VM.fillCoins(1, 10))
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        for i in range(0, 10):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        # Монет 11 и 10 соответсвенно, после покупки одного продукта 1 должно потратиться 2 из баланса и возвращено быть 4 монеты номинала 2
        self.assertEqual(self.VM.Response.OK, self.VM.giveProduct1(1))
        self.assertEqual(max1 - 1, self.VM.getNumberOfProduct1())
        self.assertEqual(0, self.VM.getCurrentBalance())
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(11, self.VM.getCoins1())
        self.assertEqual(6, self.VM.getCoins2())

    def testGiveProduct1Spec2(self):
        # В автомат водились монетки номиналом 1, но в автомате для выдачи был номинал 2 достаточного для выдачи части ими
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.OK, self.VM.fillProducts())
        # Устанавливаем цену на продукт 1 в виде 2
        self.assertEqual(self.VM.Response.OK, self.VM.setPrices(2, 1))
        self.assertEqual(2, self.VM.getPrice1())
        self.assertEqual(1, self.VM.getPrice2())
        self.assertEqual(self.VM.Response.OK, self.VM.fillCoins(1, 1))
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        for i in range(0, 10):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        # Монет 11 и 1 соответсвенно, после покупки одного продукта 1 должно потратиться 2 из баланса и возвращено быть 1 монеты номинала 2 и 6 монет номинала 1
        self.assertEqual(self.VM.Response.OK, self.VM.giveProduct1(1))
        self.assertEqual(max1 - 1, self.VM.getNumberOfProduct1())
        self.assertEqual(0, self.VM.getCurrentBalance())
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(5, self.VM.getCoins1())
        self.assertEqual(0, self.VM.getCoins2())
    
    def testGiveProduct1Spec3(self):
        # В автомат водились монетки номиналом 1, но в автомате для выдачи был номинал 2 достаточного для выдачи только им, исключая разницу в нечётности
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.OK, self.VM.fillProducts())
        # Устанавливаем цену на продукт 1 в виде 2
        self.assertEqual(self.VM.Response.OK, self.VM.setPrices(2, 1))
        self.assertEqual(2, self.VM.getPrice1())
        self.assertEqual(1, self.VM.getPrice2())
        self.assertEqual(self.VM.Response.OK, self.VM.fillCoins(1, 4))
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        for i in range(0, 9):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        # Монет 10 и 4 соответсвенно, после покупки одного продукта 1 должно потратиться 2 из баланса и возвращено быть 3 монеты номинала 2 и 1 монет номинала 1
        self.assertEqual(self.VM.Response.OK, self.VM.giveProduct1(1))
        self.assertEqual(max1 - 1, self.VM.getNumberOfProduct1())
        self.assertEqual(0, self.VM.getCurrentBalance())
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(9, self.VM.getCoins1())
        self.assertEqual(1, self.VM.getCoins2())
    
    def testGiveProduct1Spec4(self):
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.OK, self.VM.fillProducts())
        # Устанавливаем цену на продукт 1 в виде 3
        self.assertEqual(self.VM.Response.OK, self.VM.setPrices(3, 1))
        self.assertEqual(3, self.VM.getPrice1())
        self.assertEqual(1, self.VM.getPrice2())
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        # Вводятся две монетки номинала 2, монеток номинала 1 нет
        for i in range(0, 2):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin2())
        # Монет 0 и 2 соответсвенно, после покупки одного продукта 1 должно потратиться 3 из баланса и возвращено 1 монет номинала 1, которых нет, что выдаст ошибку
        self.assertEqual(self.VM.Response.UNSUITABLE_CHANGE, self.VM.giveProduct1(1))
        self.assertEqual(4, self.VM.getCurrentBalance())
    
    def testGiveProduct2(self):
        print ("giveProduct2AdministeringMode")
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.ILLEGAL_OPERATION, self.VM.giveProduct2(1))
        self.assertEqual(self.VM.Response.OK, self.VM.fillProducts())
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        print ("giveProduct2OperrationModeError", self.VM.Response.INVALID_PARAM)
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.giveProduct2(0))
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.giveProduct2(-1))
        self.assertEqual(self.VM.Response.INVALID_PARAM, self.VM.giveProduct2(max2 + 1))
        print ("giveProduct2OperrationModeNormal")
        for i in range(0, price2):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        self.assertEqual(self.VM.Response.OK, self.VM.giveProduct2(1))
        self.assertEqual(0, self.VM.getCurrentBalance())
        self.assertEqual(max2 - 1, self.VM.getNumberOfProduct2())
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(price2, self.VM.getCoins1())
        self.assertEqual(0, self.VM.getCoins2())
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        print ("giveProduct2OperrationModeError", self.VM.Response.INSUFFICIENT_PRODUCT)
        self.assertEqual(self.VM.Response.INSUFFICIENT_PRODUCT, self.VM.giveProduct2(max2))
        print ("giveProduct2OperrationModeError", self.VM.Response.INSUFFICIENT_MONEY)
        self.assertEqual(self.VM.Response.INSUFFICIENT_MONEY, self.VM.giveProduct2(max2 - 1))
        for i in range(0, price2):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        self.assertEqual(self.VM.Response.INSUFFICIENT_MONEY, self.VM.giveProduct2(2))
        self.assertEqual(price2, self.VM.getCurrentBalance())
    
    def testGiveProduct2Spec1(self):
        # В автомат водились монетки номиналом 1, но в автомате для выдачи был номинал 2 достаточного для выдачи только им
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.OK, self.VM.fillProducts())
        # Устанавливаем цену на продукт 2 в виде 2
        self.assertEqual(self.VM.Response.OK, self.VM.setPrices(1, 2))
        self.assertEqual(1, self.VM.getPrice1())
        self.assertEqual(2, self.VM.getPrice2())
        self.assertEqual(self.VM.Response.OK, self.VM.fillCoins(1, 10))
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        for i in range(0, 10):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        # Монет 11 и 10 соответсвенно, после покупки одного продукта 2 должно потратиться 2 из баланса и возвращено быть 4 монеты номинала 2
        self.assertEqual(self.VM.Response.OK, self.VM.giveProduct2(1))
        self.assertEqual(max2 - 1, self.VM.getNumberOfProduct2())
        self.assertEqual(0, self.VM.getCurrentBalance())
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(11, self.VM.getCoins1())
        self.assertEqual(6, self.VM.getCoins2())

    def testGiveProduct2Spec2(self):
        # В автомат водились монетки номиналом 1, но в автомате для выдачи был номинал 2 достаточного для выдачи части ими
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.OK, self.VM.fillProducts())
        # Устанавливаем цену на продукт 2 в виде 2
        self.assertEqual(self.VM.Response.OK, self.VM.setPrices(1, 2))
        self.assertEqual(1, self.VM.getPrice1())
        self.assertEqual(2, self.VM.getPrice2())
        self.assertEqual(self.VM.Response.OK, self.VM.fillCoins(1, 1))
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        for i in range(0, 10):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        # Монет 11 и 1 соответсвенно, после покупки одного продукта 2 должно потратиться 2 из баланса и возвращено быть 1 монеты номинала 2 и 6 монет номинала 1
        self.assertEqual(self.VM.Response.OK, self.VM.giveProduct2(1))
        self.assertEqual(max2 - 1, self.VM.getNumberOfProduct2())
        self.assertEqual(0, self.VM.getCurrentBalance())
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(5, self.VM.getCoins1())
        self.assertEqual(0, self.VM.getCoins2())
    
    def testGiveProduct2Spec3(self):
        # В автомат водились монетки номиналом 1, но в автомате для выдачи был номинал 2 достаточного для выдачи только им, исключая разницу в нечётности
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.OK, self.VM.fillProducts())
        # Устанавливаем цену на продукт 2 в виде 2
        self.assertEqual(self.VM.Response.OK, self.VM.setPrices(1, 2))
        self.assertEqual(1, self.VM.getPrice1())
        self.assertEqual(2, self.VM.getPrice2())
        self.assertEqual(self.VM.Response.OK, self.VM.fillCoins(1, 4))
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        for i in range(0, 9):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin1())
        # Монет 10 и 4 соответсвенно, после покупки одного продукта 2 должно потратиться 2 из баланса и возвращено быть 3 монеты номинала 2 и 1 монет номинала 1
        self.assertEqual(self.VM.Response.OK, self.VM.giveProduct2(1))
        self.assertEqual(max2 - 1, self.VM.getNumberOfProduct2())
        self.assertEqual(0, self.VM.getCurrentBalance())
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(9, self.VM.getCoins1())
        self.assertEqual(1, self.VM.getCoins2())
    
    def testGiveProduct2Spec4(self):
        self.assertEqual(self.VM.Response.OK, self.VM.enterAdminMode(adminCode))
        self.assertEqual(self.VM.Mode.ADMINISTERING, self.VM.getCurrentMode())
        self.assertEqual(self.VM.Response.OK, self.VM.fillProducts())
        # Устанавливаем цену на продукт 2 в виде 3
        self.assertEqual(self.VM.Response.OK, self.VM.setPrices(1, 3))
        self.assertEqual(1, self.VM.getPrice1())
        self.assertEqual(3, self.VM.getPrice2())
        self.VM.exitAdminMode()
        self.assertEqual(self.VM.Mode.OPERATION, self.VM.getCurrentMode())
        # Вводятся две монетки номинала 2, монеток номинала 1 нет
        for i in range(0, 2):
            self.assertEqual(self.VM.Response.OK, self.VM.putCoin2())
        # Монет 0 и 2 соответсвенно, после покупки одного продукта 1 должно потратиться 3 из баланса и возвращено 1 монет номинала 1, которых нет, что выдаст ошибку
        self.assertEqual(self.VM.Response.UNSUITABLE_CHANGE, self.VM.giveProduct2(1))
        self.assertEqual(4, self.VM.getCurrentBalance())
    






    


    

    



    



    


if __name__ == "__main__":
  unittest.main()

