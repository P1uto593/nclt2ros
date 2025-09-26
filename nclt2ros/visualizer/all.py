import matplotlib.pyplot as plt

# 假设这些模块已经存在
from nclt2ros.visualizer.plotter import Plotter
from nclt2ros.visualizer.gt import GroundTruth
from nclt2ros.visualizer.gps_rtk import GPS_RTK
from nclt2ros.visualizer.gps import GPS
from nclt2ros.visualizer.wheel_odom import WheelOdom

class AllSensors(object):
    """Class to visualize all sensor data in one plot using composition."""
    def __init__(self, date, plt_show=True):
        self.date = date
        self.plt_show = plt_show

        # 创建各个传感器类的实例，而不是继承它们
        self.plotter = Plotter(date=self.date)
        self.ground_truth = GroundTruth(date=self.date)
        self.gps_rtk = GPS_RTK(date=self.date)
        self.gps = GPS(date=self.date)
        self.wheel_odom = WheelOdom(date=self.date)

        # 从 Plotter 实例获取保存图片的路径
        self.visualization_png_all_dir = self.plotter.visualization_png_all_dir

    def plot(self):
        """visualize all data in one plot"""
        # 通过实例调用方法获取数据
        gt_x, gt_y = self.ground_truth.get_gt_data()
        gps_rtk_x, gps_rtk_y = self.gps_rtk.get_gps_rtk_data()
        gps_x, gps_y = self.gps.get_gps_data()
        wheel_odom_x, wheel_odom_y = self.wheel_odom.get_wheel_odom_data()

        # 绘制所有数据
        plt.plot(gt_y, gt_x, color="lime", label='ground truth')
        plt.plot(gps_rtk_y, gps_rtk_x, 'r-', label='gps rtk')
        plt.plot(gps_y, gps_x, 'y-', label='gps')
        plt.plot(wheel_odom_y, wheel_odom_x, 'm-', label='wheel odom')

        # 设置图表属性
        plt.title('All Sensors')
        plt.xlabel('x in meter')
        plt.ylabel('y in meter')
        plt.legend(loc='upper left')
        plt.grid(True)
        
        # 保存图片
        plt.savefig(self.visualization_png_all_dir + 'raw_data_all.png')
        
        # 显示图片
        if self.plt_show:
            plt.show()

    def get_png_all_dir(self):
        """get the png all sensors directory"""
        return self.visualization_png_all_dir

if __name__ == '__main__':
    # 代码的使用方式保持不变
    all_sensors_visualizer = AllSensors('2012-01-15', plt_show=False)
    all_sensors_visualizer.plot()