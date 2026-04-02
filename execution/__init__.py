# execution/__init__.py
# Package marker - Python-ს უთქვამს: "execution ფოლდერი = მოდული"

"""
Execution package - ბოტის გაშვება და ტრეიდინგი
"""

__version__ = "1.0.0"
__author__ = "GENIUS Trading Bot"

# დაიმპორტე მნიშვნელოვანი კლასი
try:
    from execution.regime_engine import MarketRegimeEngine
    from execution.order_executor import OrderExecutor
except ImportError as e:
    print(f"Warning: Could not import from execution: {e}")

__all__ = [
    'MarketRegimeEngine',
    'OrderExecutor',
]
