import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('telco_cleaned.csv')

# Create tenure groups
df['tenure_group'] = pd.cut(df['tenure'], 
                              bins=[0, 12, 24, 48, 72, 100],
                              labels=['0-12', '13-24', '25-48', '49-72', '73+'])

# Create dashboard
fig = plt.figure(figsize=(16, 10))
fig.suptitle('Telco Customer Churn Dashboard', fontsize=20, fontweight='bold')

# 1. Overall churn
ax1 = plt.subplot(2, 3, 1)
churn_counts = df['Churn'].value_counts()
colors = ['green', 'red']
bars = ax1.bar(['Stayed', 'Churned'], churn_counts, color=colors)
ax1.set_title('Customer Churn Distribution', fontsize=12)
ax1.set_ylabel('Number of Customers')
for bar, count in zip(bars, churn_counts):
    ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 50, 
             f'{count}', ha='center', fontsize=10)
churn_rate = df['Churn'].mean() * 100
ax1.text(0.5, -0.15, f'Overall Churn Rate: {churn_rate:.1f}%', 
         transform=ax1.transAxes, ha='center', fontsize=12, fontweight='bold')

# 2. Churn by Contract
ax2 = plt.subplot(2, 3, 2)
contract_churn = df.groupby('Contract')['Churn'].mean() * 100
colors = ['red', 'orange', 'green']
ax2.bar(contract_churn.index, contract_churn.values, color=colors)
ax2.set_title('Churn Rate by Contract Type', fontsize=12)
ax2.set_ylabel('Churn Rate (%)')
ax2.set_ylim(0, 60)
for i, (contract, rate) in enumerate(contract_churn.items()):
    ax2.text(i, rate + 2, f'{rate:.1f}%', ha='center', fontsize=10)

# 3. Churn by Payment Method
ax3 = plt.subplot(2, 3, 3)
payment_churn = df.groupby('PaymentMethod')['Churn'].mean() * 100
payment_churn = payment_churn.sort_values(ascending=False)
colors = ['red', 'orange', 'orange', 'green']
ax3.bar(payment_churn.index, payment_churn.values, color=colors)
ax3.set_title('Churn Rate by Payment Method', fontsize=12)
ax3.set_ylabel('Churn Rate (%)')
ax3.tick_params(axis='x', rotation=45)
for i, (method, rate) in enumerate(payment_churn.items()):
    ax3.text(i, rate + 1, f'{rate:.1f}%', ha='center', fontsize=9)

# 4. Churn by Tenure
ax4 = plt.subplot(2, 3, 4)
tenure_churn = df.groupby('tenure_group', observed=True)['Churn'].mean() * 100
colors = ['red', 'orange', 'orange', 'green', 'green']
ax4.bar(tenure_churn.index, tenure_churn.values, color=colors)
ax4.set_title('Churn Rate by Tenure', fontsize=12)
ax4.set_ylabel('Churn Rate (%)')
for i, (group, rate) in enumerate(tenure_churn.items()):
    ax4.text(i, rate + 1, f'{rate:.1f}%', ha='center', fontsize=9)

# 5. Churn by Internet Service
ax5 = plt.subplot(2, 3, 5)
internet_churn = df.groupby('InternetService')['Churn'].mean() * 100
colors = ['red', 'orange', 'green']
ax5.bar(internet_churn.index, internet_churn.values, color=colors)
ax5.set_title('Churn Rate by Internet Service', fontsize=12)
ax5.set_ylabel('Churn Rate (%)')
for i, (service, rate) in enumerate(internet_churn.items()):
    ax5.text(i, rate + 1, f'{rate:.1f}%', ha='center', fontsize=10)

# 6. Key Insights
ax6 = plt.subplot(2, 3, 6)
ax6.axis('off')
insights = [
    "🔑 KEY FINDINGS:",
    "",
    f"• Overall churn: {churn_rate:.1f}%",
    f"• Month-to-month churn: {contract_churn['Month-to-month']:.1f}%",
    f"• Two-year churn: {contract_churn['Two year']:.1f}%",
    f"• Electronic check: {payment_churn['Electronic check']:.1f}%",
    "",
    "💡 RECOMMENDATIONS:",
    "• Convert to annual contracts",
    "• Promote auto-pay discounts",
    "• Improve new customer onboarding"
]
text = '\n'.join(insights)
ax6.text(0.1, 0.9, text, transform=ax6.transAxes, fontsize=11, verticalalignment='top')

plt.tight_layout()
plt.savefig('churn_dashboard.png', dpi=150, bbox_inches='tight')
plt.show()

print("\n" + "="*50)
print("✅ Dashboard saved as 'churn_dashboard.png'")
print("📁 This image is ready for your GitHub portfolio!")
print("="*50)