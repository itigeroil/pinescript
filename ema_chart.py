import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 生成模拟价格数据（模拟一年的日线数据）
np.random.seed(42)
n_days = 250
base_price = 100

# 创建一个有趋势和波动的价格序列
trend = np.linspace(0, 30, n_days)  # 上升趋势
noise = np.random.randn(n_days) * 3  # 随机波动
prices = base_price + trend + noise

# 添加一些周期性波动
cycle = np.sin(np.linspace(0, 8*np.pi, n_days)) * 8
prices = prices + cycle

# 创建DataFrame
df = pd.DataFrame({'Close': prices})

# 计算EMA均线
def calculate_ema(data, period):
    return data.ewm(span=period, adjust=False).mean()

df['EMA20'] = calculate_ema(df['Close'], 20)
df['EMA50'] = calculate_ema(df['Close'], 50)
df['EMA100'] = calculate_ema(df['Close'], 100)
df['EMA200'] = calculate_ema(df['Close'], 200)

# 绘制图表
fig, ax = plt.subplots(figsize=(14, 8))

# 绘制价格线
ax.plot(df.index, df['Close'], label='Price', color='black', linewidth=1.5, alpha=0.7)

# 绘制EMA均线
ax.plot(df.index, df['EMA20'], label='EMA 20', color='blue', linewidth=2)
ax.plot(df.index, df['EMA50'], label='EMA 50', color='orange', linewidth=2)
ax.plot(df.index, df['EMA100'], label='EMA 100', color='purple', linewidth=2)
ax.plot(df.index, df['EMA200'], label='EMA 200', color='red', linewidth=2)

# 设置标题和标签
ax.set_title('EMA Moving Averages (20/50/100/200)', fontsize=16, fontweight='bold')
ax.set_xlabel('Days', fontsize=12)
ax.set_ylabel('Price', fontsize=12)

# 设置网格
ax.grid(True, alpha=0.3)

# 设置图例
ax.legend(loc='upper left', fontsize=11)

# 添加均线说明文本框
textstr = 'EMA Colors:\n• EMA20: Blue\n• EMA50: Orange\n• EMA100: Purple\n• EMA200: Red'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.savefig('/workspace/ema_chart.png', dpi=150, bbox_inches='tight')
plt.show()

print("图表已保存到: /workspace/ema_chart.png")