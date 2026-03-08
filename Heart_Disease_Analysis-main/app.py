from flask import Flask, render_template
import pandas as pd
import seaborn as sns
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

df = pd.read_csv("Heart_new2.csv")

df.columns = ['HeartDisease','BMI','Smoking','AlcoholDrinking','Stroke',
              'PhysicalHealth','MentalHealth','DiffWalking','Sex',
              'AgeCategory','Race','Diabetic','PhysicalActivity',
              'GenHealth','SleepTime','Asthma','KidneyDisease','SkinCancer']

if not os.path.exists("static"):
    os.makedirs("static")

# Heart Disease Distribution
plt.figure(figsize=(6,4))
df['HeartDisease'].value_counts().plot(kind='bar',color=["salmon","lightblue"])
plt.title("Heart Disease Distribution")
plt.savefig("static/heart.png")
plt.close()

# Sex vs Heart Disease
plt.figure(figsize=(6,4))
sns.countplot(x='Sex', hue='HeartDisease', data=df)
plt.title("Sex vs Heart Disease")
plt.savefig("static/sex.png")
plt.close()

# Age Category
plt.figure(figsize=(8,4))
sns.countplot(x='AgeCategory', hue='HeartDisease', data=df)
plt.xticks(rotation=45)
plt.title("Heart Disease by Age Category")
plt.savefig("static/age.png")
plt.close()

# Smoking
plt.figure(figsize=(6,4))
sns.countplot(x='Smoking', hue='HeartDisease', data=df)
plt.title("Smoking vs Heart Disease")
plt.savefig("static/smoking.png")
plt.close()

# BMI vs Sleep
plt.figure(figsize=(6,4))
sns.scatterplot(x='BMI',y='SleepTime',hue='HeartDisease',data=df)
plt.title("BMI vs Sleep Time")
plt.savefig("static/bmi.png")
plt.close()

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)