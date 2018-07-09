
df = pd.read_csv('erp.csv', header=None)
t = np.arange(-5, 5+0.05, 0.05)

fig, ax = plt.subplots()
ax.plot(t, df.iloc[0, :])
ax.set_xlabel('Time (s)')
ax.set_ylabel(r'Voltage ($\mu$V)')
ax.set_title("Trial 1")
plt.show()


