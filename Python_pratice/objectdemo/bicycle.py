"""
写一个 Bicycle (自行车)类，有run （骑行）方法，调用时显示骑行里程km(骑行里程为传入的数字)
再写一个电动自行车类EBicycle继承Bicycle，添加电池电量 battery_level 属性通过参数传入，
同时有两个方法：
1、fill_charge(vol)  用来充电， vol为电量
2、run(km) 方法用于骑行，每骑行10km消耗电量1度，当电量耗尽时调用Bicycle的run方法骑行，
通过传入的骑行里程数，显示骑行结果（就是当电量耗尽，需要你真正骑的里程数）。
"""
import yaml


class Bicycle:
    def run(self, km):
        print(f'骑行里程数：{km} km')


class EBicycle(Bicycle):
    def __init__(self, battery_level):
        # 初始化电量
        self.battery_lever = battery_level

    def fill_charge(self, vol):
        # 充电
        self.battery_lever = self.battery_lever + vol

    def run(self, km):
        # 用电骑，用脚蹬
        miles = km - self.battery_lever * 10  # 用脚蹬的里程数
        if miles > 0:
            print(f'已经使用电骑行：{self.battery_lever * 10} km')
            # bicycle = Bicycle()  # 和下面的 super()一样
            # bicycle.run(miles)
            super().run(miles)  # 用脚蹬的里程数，调用了父类的run方法
        else:
            print(f'已经使用电骑行：{km} km')


if __name__ == '__main__':
    with open('bicycle_config.yml', encoding='utf8') as f:
        datas = yaml.safe_load(f)

    # print(datas['default'])
    battery_lever = datas['default']['battery_level']
    run_km = datas['default']['run_km']
    eb = EBicycle(battery_lever)
    # eb.fill_charge(5)
    eb.run(run_km)

    # eb = EBicycle(10)  # 10为初始电量battery_level
    # eb.fill_charge(5)  # 充5度电
    # print(eb.battery_lever)
    # eb.run(199)
