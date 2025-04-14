
# 🛍️ Progressive Personalized Recommendation System

This project demonstrates a lightweight **personalized recommendation engine** using Python. It evolves recommendations for a shopping app based on **user interactions** (clicks/likes).

---

## 🚀 Features

1. **Cold Start Recommendations**  
   Suggests popular products when there's no user history.

2. **User Click Simulation**  
   Simulates a user clicking on 2–3 products, which updates their preferences.

3. **Lightweight User Profile**  
   Builds a profile from clicked product tags and categories.

4. **Personalized Recommendations**  
   Suggests products similar to what the user interacted with — still mixes in some popular ones.

5. **Visualization**  
   Displays a bar chart of the user's preferred tags.

---

## 🧠 Recommendation Logic

### 📌 Content Filtering
- Checks for **overlap between product tags** and user's preferred tags.
- Also checks **category match**.

### 📊 Hybrid Scoring Formula
```
final_score = tag_match_count + category_match (1 or 0) + (popularity_score * 0.01)
```

### 🤝 Collaborative Filtering (Simulated)
- Products with higher popularity_score are considered **trendy**.

---

## 📂 File Structure

| File         | Description |
|--------------|-------------|
| `products.csv` | Sample catalog of 20 products |
| `users.csv`    | Simulated user interactions |
| `recommend.py` | Python script implementing the full logic |
| `user_profile_tags.png` | (optional) bar chart of tag frequency |

---

## ✅ How to Run

1. Install dependencies:
```bash
pip install pandas matplotlib tabulate
```

2. Run the script:
```bash
python recommend.py
```

---

## 🔍 Sample Output

```txt
=== ROUND 1: Cold Start Recommendations ===
(product table with popularity)

=== Simulated User Clicked on Products ===
(clicked product titles/tags)

=== UPDATED USER PROFILE ===
Preferred Tags: ['boho', 'pastel', 'summer']
Liked Categories: ['tops']

=== ROUND 2: Personalized Recommendations ===
(products matched based on user profile)
```

---

## 🏅 Extras

- Uses `tabulate` for clean terminal display.
- Modularized code into functions.
- Visual profile generation using `matplotlib`.

---
