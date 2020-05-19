# LifeExpectancy

## Interactive visualization demonstrating life expectancy probability curves at any age

While we often hear life expectancy described as a specific age to which one would expect to live; in fact, life expectancy is more usefully described as a probability distribution.  You can think of the age through which you have a 50% probability of surviving as your median life expectancy.  Furthermore, using the probability distribution you can also estimate your probability of living to 70, 80, 90, or other ages.  An example of the utility of the entire curve is retirement scenario planning, in which you don’t want to run out of money at your median life expectancy, since there is a 50% probability of living beyond this age.

This interactive graphic shows the life expectancy probability (blue) curve for males or females at any given current age (as controlled by the “Current Age” slider).  The underlying life table data are from the <a href="https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_07-508.pdf" target="_blank">2017 CDC Life Tables</a>.  

The graphic also allows you to enter an estimated mortality rate from a new event risk not accounted for in the life tables, to show the effect of this risk on the overall life expectancy chart (updated survival probabilities represented by the pink shaded area), and on the 1-year survival rate.  For simplicity, the application applies the entire mortality risk to the first year, and assumes no residual impact on life expectancy following survival of the one-time new event.

More about Life Tables follows.  Life tables report the probability of surviving one year for a wide range of ages (typically 0-100 years old, and typically separately for males and females).   These can be used to project a probability distribution for life expectancy for males or females at any given current age.  For example, let’s define P<sub>22</sub> to be the probability of a male who has already survived to their 21st birthday surviving to their 22nd birthday  (this probability is 99.87%, according to the 2017 CDC Life tables, which we will use for this application). Likewise, we will call the probability of surviving from the 22nd birthday to the 23rd birthday P<sub>23</sub>.  Hence, the probability of someone at their 21st birthday surviving to their 23rd birthday = P<sub>22</sub> x P<sub>23</sub>.  And to survive to their 50th birthday, the probability is the product of surviving through each year from 21 to 50 = P<sub>22</sub> x P<sub>23</sub> x … x P<sub>49</sub> x P<sub>50</sub>.  The above interactive graphic is built using this concept.

The older a person is, the higher likelihood they have of living to a specific future age (say, 70); consequently, the median life expectancy age increases as one’s current age advances.  While these changes may be imperceptible when comparing the curves for a 10-year-old and 20-year-old; the changes become more obvious as a person approaches their 60s.  For example, for someone at their 69th birthday, their probability of surviving to their 70th birthday is merely P<sub>70</sub>.  Hence, the probability of a 69-year-old surviving to 70 is higher than the probability of a 21-year-old surviving to 70, since the 69-year-old has already survived to 69, whereas the 21 year old has less than 100% probability of surviving to 69 (P<sub>22</sub> x P<sub>23</sub> x … x P<sub>69</sub>).

A perhaps unexpected observation is that everyone dies before their current life expectancy.  For example, 97.76% of all 70-year-old males would be expected to survive to 71, with the median life expectancy to 84.7 years old.  The unfortunate 70-year-old that dies is part of the 2.24% of 70-year-old males that is expected to die before reaching age 71, about 14 years younger than the median life expectancy.

**Assumptions**

While we using are separate tables for males and females, in this application we do not further break down by race, by current health, or by other factors.  For example, it has been estimated (<a href="https://www.ncbi.nlm.nih.gov/books/NBK179276/pdf/Bookshelf_NBK179276.pdf" target="_blank">US Surgeon General Report, 2014</a>) that *smoking reduces the median life expectancy by 11-12 years for a 25-year-old, and by 7.5 years for a 35 years old*.  Similarly, it has been estimated (<a href="https://www.webmd.com/diabetes/news/20101201/diabetes-cuts-years-off-life-span-of-americans#1" target="_blank">National Academy on an Aging Society, 2010 </a>) that *Type II Diabetes reduces median life expectancy by 8.5 years for a 50-year-old, and by 5.4 years for a 60-year-old*.

In this graphic, the new-event mortality rate is applied completely to the first year survival probability.  For example, if there is a 99% probability of surviving year 1 without the new risk and 98% probability of surviving year 2, and 5% probability of dying from the new risk, the application applies the entire 5% risk to year 1 (so that the probability of surviving year 1 is now 99% x 95%, surviving year 2 remains at 98%, so that the probability of surviving year 1 and year 2 is (99% x 95%) x 98%.   The methodology does not incorporate any residual impact on life expectancy for survivors of year one.
