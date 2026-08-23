import pandas as pd
import matplotlib.pyplot as plt

#Marketing Campaign data
data = {
    "Campaign" : ["Facebook", "Instagram", "Google", "Twitter"],
    "Spend" : [500, 400, 700, 800],
    "Clicks" : [1200, 1000, 1500, 2000,],
    "Conversions" : [60, 45, 90,150],
    "Impressions" : [50000 , 45000 , 40000 , 10000] ,
    "Revenue" : [1000 , 800 , 1200 , 1000]
}

df = pd.DataFrame(data)

print (df)

# Overall Campaign Results
total_spend = df["Spend"].sum()
total_conversions = df["Conversions"].sum()
total_clicks = df["Clicks"].sum()

print (total_spend)
print (total_conversions)
print (total_clicks)

# Cost per conversion for each campaign
df["Cost_per_Conversion"] = df["Spend"] / df["Conversions"]

# Conversion rate for each campaign
df["Conversion_Rate"] = df["Conversions"] / df["Clicks"]

print(df)

#The best performing campaign portrayed through cost per conversion
lowest_cost= df["Cost_per_Conversion"].min()

best_campaign_index = df["Cost_per_Conversion"].idxmin()

best_campaign = df.loc[best_campaign_index, "Campaign"]

print ("Lowest cost per conversion:", lowest_cost)
print ("Best campaign", best_campaign)

#CTR (Click-Through Rate)
df["CTR"] = df["Clicks"] / df["Impressions"]

#ROAS (Return on Ad Spending)
df["ROAS"] = df["Revenue"] / df["Spend"]



# Summary of Campaign analytics

campaign_summary = df.groupby("Campaign").agg({
    "Spend": "sum",
    "Clicks": "sum",
    "Conversions": "sum",
    "Revenue": "sum"
})

campaign_summary["ROAS"] = (
    campaign_summary["Revenue"] / campaign_summary["Spend"]
)

campaign_summary = campaign_summary.sort_values(
    "ROAS",
    ascending=False
)


#Chart Administration

# ROAS chart

plt.bar(campaign_summary.index, campaign_summary["ROAS"])

plt.title("ROAS by Campaign")
plt.xlabel("Campaign")
plt.ylabel("ROAS")

plt.savefig("charts/roas_by_campaign.png")

plt.show()

plt.figure()

# Revenue Chart

plt.bar(campaign_summary.index, campaign_summary["Revenue"])

plt.title("Revenue by Campaign")
plt.xlabel("Campaign")
plt.ylabel("Revenue (£)")

print ("Now creating revenue chart")
plt.savefig("charts/revenue_by_campaign.png")
import os
print(os.path.abspath("charts/revenue_by_campaign.png"))

plt.show()





