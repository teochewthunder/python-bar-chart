# Python Bar Chart

## Data
- This is a dictionary that has seasonal data. Each season has a sub-dictionary of players.
- Each player has a sub-dictionary of goals and appearances.

## Script
- Display a numbered list of available seasons in the data, with a 0 for exiting.
- Request for input.
- Utilize a `Try-catch` to ensure only numerical data is entered.
- If value is numerical but out of bounds, do-over.
- If value is 0, end program.
- If value is valid, display a menu of options for goals and appearances, with a 0 for exiting.
- Use the selected season and the stat type to generate the bar chart.

## Chart
We use the `matplotlib` library to plot the bar chart, and the `numpy` library to access aggregation functions.
- An average line can be drawn using the `axhline()` method from `matplotlib`, using as an an argument a value derived from using the `nanmean()` method of `numpy`.
- Labels can be rotated by using the `rotation` property in the `xticks()` method of `matplotlib`.
- Labels to display the numerical values:
  - Requires a `For` loop on the enumerated values.
  - Use the index for horizontal positioning, and the value for vertical positioning.
  - Use `ylim()` method from `matplotlib` to give more head room to display these values.
