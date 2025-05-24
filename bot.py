from datetime import datetime, timedelta
import pytz

TIMEZONE = pytz.timezone("America/Sao_Paulo")
ANTICIPATION = timedelta(minutes=2)
SIGNAL_DURATION = 5

pending_signals = []
ATIVOS = ["BTCUSDT", "ETHUSDT", "EURUSD", "GBPUSD"]

def get_price_data(symbol):
    # Simulação de dados reais
    return [1] * 50

def calculate_indicators(data):
    return {"rsi": 50, "macd": 0, "ema": 1, "bollinger": 1}

def detect_trend(data):
    return "up"

def generate_signal(indicators, trend):
    if trend == "up":
        return "buy"
    elif trend == "down":
        return "sell"
    return None

def check_and_generate():
    now = datetime.now(TIMEZONE)
    mod = now.minute % 5
    target_mod = (5 - ANTICIPATION.seconds // 60) % 5

    if mod == target_mod and now.second < 15:
        for symbol in ATIVOS:
            df = get_price_data(symbol)
            if df is None or len(df) < 30:
                continue

            indicators = calculate_indicators(df)
            trend = detect_trend(df)

            signal_type = generate_signal(indicators, trend)
            if signal_type:
                entry_time = now + ANTICIPATION
                exit_time = entry_time + timedelta(minutes=SIGNAL_DURATION)

                signal = {
                    "symbol": symbol,
                    "signal": signal_type,
                    "entry_time": entry_time.strftime("%H:%M"),
                    "exit_time": exit_time.strftime("%H:%M"),
                    "timestamp": now.strftime("%Y-%m-%d %H:%M:%S")
                }
                pending_signals.append(signal)
                print(f"[SINAL] {signal}")