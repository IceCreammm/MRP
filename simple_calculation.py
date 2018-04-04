import pandas as pd
import matplotlib.pyplot as plt

sector_dir = {'sector':['Consumer Discretionary', 'Consumer Staples', 'Utilities', 
                        'Technology', 'Health Care', 'Financial', 'Energy' , 'Telecom', 
                        'Industrials', 'Material', 'Real Estate'],'Market_Cap':[5.59, 3.58, 1.24, 9.04, 4.96, 7.67, 
                                                                3.69, 1.69,4.21, 2.14, 1.13]}
sector_importance = pd.DataFrame(data=sector_dir)


print(sector_importance)

sector_importance['weight'] = sector_importance['Market_Cap']/sector_importance['Market_Cap'].sum()

sector_importance = sector_importance.sort_values(by='weight', ascending=False)
sector_importance.plot(x= 'sector' , y= 'weight' , kind='bar')

plt.show()






