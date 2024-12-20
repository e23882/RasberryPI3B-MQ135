import spidev
import time

# 初始化 SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

# ADC 讀取函數
def read_adc(channel):
    assert 0 <= channel <= 7, "通道範圍必須在 0-7 之間"
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data


# 設定參數
RL = 10.0  # 負載電阻 (kΩ)
R0 = 10.0  # 基準電阻 (校正後獲得)
A = 2.3    # 氣體的基準濃度係數
B = -0.45  # 曲線斜率
# 無瓦斯情況下的基準濃度
no_gas_ppm = 0.71



while True:
    # 取得 ADC 數值
    adcValue = read_adc(0)  # 假設通道 0
    # print(f"ADC 數值: {adcValue}")

    # 計算 Rs 值
    if adcValue > 0:
        Rs = RL * ((1023.0 / adcValue) - 1.0)
        # print(f"Rs 值: {Rs:.2f} kΩ")

        # 計算 PPM 值
        PPM = A * (Rs / R0) ** B 
        print(f"硫化氫濃度: {PPM:.2f} PPM  (Leo舊家參考值0.71-0.84)")
    else:
        print("ADC 數值無效，請檢查感測器或電路連接")
    
    time.sleep(1)