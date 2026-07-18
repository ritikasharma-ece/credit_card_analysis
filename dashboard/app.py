import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Credit Card Analytics Dashboard",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Card Analytics Dashboard")
st.markdown("Interactive dashboard for customer, spending and segmentation analysis.")

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "cleaned_data" / "customer_segments.csv"

df = pd.read_csv(DATA_PATH)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("Dashboard")

segment = st.sidebar.selectbox(
    "Customer Segment",
    ["All"] + sorted(df["customer_segment"].unique())
)

if segment != "All":
    df = df[df["customer_segment"] == segment]

# ---------------------------------------------------
# KPI Cards
# ---------------------------------------------------

st.subheader("Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Customers",
        f"{df['customer_id'].nunique():,}"
    )

with col2:
    st.metric(
        "Total Revenue",
        f"₹{df['total_spending'].sum():,.0f}"
    )

with col3:
    st.metric(
        "Average Transaction",
        f"₹{df['average_transaction'].mean():,.0f}"
    )

with col4:
    st.metric(
        "Cards Owned",
        f"{df['cards_owned'].sum():,}"
    )

st.divider()

# ---------------------------------------------------
# Charts Row 1
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("Customer Segments")

    fig, ax = plt.subplots(figsize=(6,4))

    df["customer_segment"].value_counts().plot(
        kind="bar",
        ax=ax
    )

    plt.xticks(rotation=30)

    st.pyplot(fig)

with col2:

    st.subheader("High Value Customers")

    fig, ax = plt.subplots(figsize=(6,4))

    df["high_value_customer"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )

    ax.set_ylabel("")

    st.pyplot(fig)

st.divider()

# ---------------------------------------------------
# Scatter Plot
# ---------------------------------------------------

st.subheader("Income vs Total Spending")

fig, ax = plt.subplots(figsize=(9,5))

scatter = ax.scatter(
    df["annual_income"],
    df["total_spending"],
    c=df["cluster"],
    cmap="viridis",
    alpha=0.7
)

plt.colorbar(scatter)

ax.set_xlabel("Annual Income")
ax.set_ylabel("Total Spending")

st.pyplot(fig)

st.divider()

# ---------------------------------------------------
# Cluster Distribution
# ---------------------------------------------------

st.subheader("Cluster Distribution")

fig, ax = plt.subplots(figsize=(7,4))

df["cluster"].value_counts().sort_index().plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Cluster")
ax.set_ylabel("Customers")

st.pyplot(fig)

st.divider()

# ---------------------------------------------------
# Cluster Summary
# ---------------------------------------------------

st.subheader("Cluster Summary")

cluster_summary = df.groupby("cluster")[
    [
        "annual_income",
        "total_spending",
        "average_transaction",
        "cards_owned",
        "spending_income_ratio"
    ]
].mean().round(2)

st.dataframe(cluster_summary, use_container_width=True)

st.divider()

# ---------------------------------------------------
# Top Customers
# ---------------------------------------------------

st.subheader("Top 10 Customers")

top_customers = (
    df.sort_values(
        "total_spending",
        ascending=False
    )
    .head(10)
)

st.dataframe(
    top_customers[
        [
            "customer_id",
            "annual_income",
            "total_spending",
            "average_transaction",
            "customer_segment",
            "cluster"
        ]
    ],
    use_container_width=True
)

st.divider()

# ---------------------------------------------------
# Complete Dataset
# ---------------------------------------------------

st.subheader("Customer Dataset")

st.dataframe(df, use_container_width=True)

st.divider()

# ---------------------------------------------------
# Business Insights
# ---------------------------------------------------

st.subheader("Key Business Insights")

st.success("""
• Standard customers represent the largest customer segment.

• High-value customers account for the highest overall spending.

• Customer clusters reveal distinct spending behaviors that can support personalized offers and marketing strategies.

• Spending-to-income ratio provides an additional indicator of customer spending patterns.
""")