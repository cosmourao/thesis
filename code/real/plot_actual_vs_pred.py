# Plotting
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms
import matplotlib.ticker as ticker
import matplotlib.pylab as pl

def plot_actual_vs_pred(actual, pred, title, info):
    
    # Gasses
    gasses = ['NO', 'NO_2', 'NH_3']
    
    # Getting axis limits to have uniform plots for all gasses
    axis_min = pred.min()
    axis_max = pred.max()
    
    # print(axis_min)
    # print(axis_max)
    
    # Dividing into 3 subplots
    fig, axs = plt.subplots(1,3, figsize=(30,10), dpi = 300)
    
    # Main title
    fig.suptitle(title, fontsize=35)
    
     # Axis params
    plt.xticks(rotation=45)
    
    
    for i, ax in enumerate(axs.flat):
        
        # Data
        ax.scatter(actual[:,i], pred[:,i], c='black', alpha = 0.4)
        
        # Identity line y=x
        line = mlines.Line2D([0, 1], [0, 1], color='red')
        transform = ax.transAxes
        line.set_transform(transform)
        ax.add_line(line)
        
        # Text box with information of the fit
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.6)
        textstr = info
        ax.text(0.05, 0.95,
                textstr,
                transform = ax.transAxes,
                fontsize = 20,
                verticalalignment = 'top',
                bbox = props,
                fontname = 'Helvetica'
               )
        
        # Plot title and axis names
        ax.set_title(f'${gasses[i]}$', fontname = 'Helvetica', fontsize = 30)
        ax.set_ylabel('Predicted (ppm)', fontname = 'Helvetica', fontsize = 25)
        ax.set_xlabel('Actual (ppm)', fontname = 'Helvetica', fontsize = 25)
        
        # Setting axis limits (defined above)
        if axis_min >0 or axis_max < 80:
            ax.set_xlim(-5, 85)
            ax.set_ylim(-5, 85)
        else:
            ax.set_xlim(axis_min + 5, axis_max + 5)
            ax.set_ylim(axis_min + 5, axis_max + 5)
        
        # Setting minor ticks in fixed levels (5, 10, 20, 40, 80)
        ax.xaxis.set_minor_locator(ticker.FixedLocator([5,10,20,40,80]))
        ax.yaxis.set_minor_locator(ticker.FixedLocator([5,10,20,40,80]))
        
        # Major tick style
        ax.grid(linestyle='-', linewidth=0.5)
        ax.tick_params(axis='x', which='major', labelsize=20, rotation = 45)
        # Font size of tick labels (numbers)
        ax.tick_params(axis='both', which='major', labelsize=20)
        
        # Minor tick style
        ax.grid(axis = 'x', which = 'minor',linestyle=':', linewidth=0.5,color = "fuchsia")
        ax.tick_params(which = 'minor', axis="x", direction="in",
                       length=10, width=3, color="fuchsia", rotation = 45, labelsize = 12)
        ax.xaxis.set_minor_formatter('{x:.0f}')
        
        
    
    plt.show()