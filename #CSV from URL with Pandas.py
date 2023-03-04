#CSV from URL with Pandas

import pandas as pandas

print(df_NHL22 = pd.read_csv('https://moneypuck.com/moneypuck/playerData/seasonSummary/2021/regular/teams.csv'))

#rename columns
df_NHL22.rename(columns={'test':'homegoals', 'GTAG': 'test'}, inplace=True)

