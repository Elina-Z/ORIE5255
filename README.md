# ORIE 5255 Project: Using Large Language Models (LLMs) for Investment

**Authors**:  
- Elina (Fuwei) Zhuang: fz266  
- Hudson Chen: hc884  
- Shun Wang: sw2337  

---

## Overview

Investment strategies often vary significantly depending on market conditions. This project explores the potential of regime-switching strategies, which aim to offer more adaptive and consistent returns by leveraging both **market performance** and **investor sentiment**.

We used a combination of the **Gaussian Mixture Model (GMM)** and **Large Language Models (LLMs)** to identify distinct market regimes. By calculating the probability of the next day's regime, we derived the expected return and covariance matrix, which were used to allocate investments via **Modern Portfolio Theory (MPT)**. The results demonstrated that our approach outperformed the S&P 500.

---

## Key Innovations

Our **2D-Bayesian Regime Switch Strategy** introduced three major advancements compared to traditional regime-switching strategies:

### 1. Two-Dimensional Regimes
- **Traditional Approach**: Tracks recent market trends using GMM.  
- **Our Approach**: Combines GMM-based market performance with LLM-based market sentiment.  
  - Leveraged **GPT-4o** to interpret market news, incorporating sentiment as a critical driver of market movements.  
  - Used the product of vector spaces to model the interaction between market trends and sentiments effectively.

### 2. Rational and Adaptive Decisions
- Instead of reacting solely to the **most likely regime**, decisions are tailored based on regime probability distributions.  
- For example, strategies adjust dynamically whether a "neutral" condition has a 51% or 100% likelihood.  
- Bayesian updates enable continuous learning from market data, improving long-term performance.

### 3. Enhanced Fit with Modern Portfolio Theory (MPT)
- Traditional MPT assumes normally distributed returns with constant correlations, which is often unrealistic.  
- By implementing GMM, each regime's returns were fitted into normal distributions, and correlation coefficients within each regime were relatively stable.  
- This resulted in improved MPT performance compared to approaches using raw returns.

---

## Project Goals
1. **Identify Market Regimes**: Classify regimes using market performance and investor sentiment.  
2. **Predict Future Regimes**: Compute probability distributions of the next day's regime using Bayesian methods.  
3. **Optimize Portfolio Allocations**: Apply MPT to the calculated probabilities for robust and adaptive investment decisions.  
4. **Outperform the S&P 500**: Demonstrate the effectiveness of our strategy in a backtesting period.  

---

## Results
- **Backtesting Period**: 2016-01-05 to 2019-12-31.  
- **Performance**: Outperformed the S&P 500 by 17.38% in cumulative returns.  
- **Risk-Adjusted Returns**: Increased the Sharpe ratio by 0.09, showing improved risk efficiency.  
- **Dynamic Adaptation**: Demonstrated consistent returns across various market conditions, including volatile periods like the 2008 financial crisis and the 2020 pandemic.

---

## Conclusion

Our 2D-Bayesian Regime Switch Strategy successfully combined the predictive power of GMM and LLMs to adapt to market conditions dynamically. By leveraging sentiment analysis and probabilistic decision-making, the strategy achieved superior performance over traditional approaches. The incorporation of Bayesian updates and proper alignment with MPT ensured robust and adaptive investment outcomes.

---
