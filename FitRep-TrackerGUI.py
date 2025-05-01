import tkinter as tk
from tkinter import messagebox


def openWorkoutLog():
    """Opens the Workout log window and its content."""
    workoutLogWindow = tk.Toplevel(root)
    workoutLogWindow.title('Workout Log')
    workoutLogWindow.geometry('640x480+300+300')
    workoutLogWindow.resizable(True, True)
    workoutLogWindow.configure(bg = '#D3D3D3')
    #Prevents interaction with other windows while opened
    workoutLogWindow.grab_set()
    
    def backToMain():
        """Closes the Log subwindow"""
        workoutLogWindow.destroy()

    def openDayLog(day):
        """Opens window for specific day of week and its contents"""
        dayLogWindow = tk.Toplevel(workoutLogWindow)
        dayLogWindow.title(f'{day} Workout')
        dayLogWindow.geometry('640x480+300+300')
        dayLogWindow.configure(bg = '#D3D3D3')
        dayLogWindow.grab_set()

        def backToMain():
            '''Closes the Daylog subwindow'''
            dayLogWindow.destroy()


        #Buttons for dayLogWindow
        backDayButton = tk.Button(dayLogWindow, text = 'Back', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00',
                                  bd = 2, relief ='ridge', width =20, command = backToMain)
        saveDayButton = tk.Button(dayLogWindow, text = 'Save', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00',
                                  bd = 2, relief ='ridge', width =20)
        
        
        #grid Layout for DayLog Window
        backDayButton.grid(row = 99, column = 0, sticky = 'W', padx = 15, pady = 10)
        saveDayButton.grid(row = 99, column = 1, sticky = 'E', padx = 15, pady = 10)

    #Sunday-Saturday Workout Buttons using Index
    daysOfWeek = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for index, day in enumerate(daysOfWeek):
        dayButton = tk.Button(workoutLogWindow, text = day, font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00', 
                 bd = 2, relief = 'ridge', width = 20, command = lambda d = day: openDayLog(d))
        
    
    #Creates a grid based on the index
        dayButton.grid(row = index, column = 0, columnspan= 2, pady = 11, padx =10)
    backLogButton = tk.Button(workoutLogWindow, text = 'Back', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00', 
                 bd = 2, relief = 'ridge', width = 5, command = backToMain)
    backLogButton.grid(row = len(daysOfWeek), column = 0, sticky = 'W', padx = 15, pady = 10)

    #configures columns and rows making them expand and contract as window size changes
    for index in range(len(daysOfWeek)):
        workoutLogWindow.grid_rowconfigure(index, weight = 1)
    workoutLogWindow.grid_columnconfigure(0, weight = 1)
    workoutLogWindow.grid_rowconfigure(0,weight = 1)


def openWorkoutHistory():
    """Opens the Workout History Window and its content."""
    workoutHistoryWindow = tk.Toplevel(root)
    workoutHistoryWindow.title('Workout History')
    workoutHistoryWindow.geometry('640x480+300+300')
    workoutHistoryWindow.resizable(True, True)
    workoutHistoryWindow.configure(bg = '#D3D3D3')
    #Prevents interaction with other windows while opened
    workoutHistoryWindow.grab_set()

    def backToMain():
        """Closes the History subwindow"""
        workoutHistoryWindow.destroy()
        
    #Buttons for History Window
    backHistoryButton = tk.Button(workoutHistoryWindow, text = 'Back', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00', 
                 bd = 2, relief = 'ridge', width = 5, command = backToMain)
    searchButton = tk.Button(workoutHistoryWindow, text = 'Search', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00', 
                 bd = 2, relief = 'ridge', width = 5)
    deleteButton = tk.Button(workoutHistoryWindow, text = 'Delete', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00', 
                 bd = 2, relief = 'ridge', width = 5)
    
    #Grid for History Window
    backHistoryButton.grid(row = 0, column = 0, sticky = 'W', padx = 15, pady = 10)
    searchButton.grid(row = 0, column = 1, sticky = 'W', padx = 15, pady =10)
    deleteButton.grid(row = 0, column = 2, sticky = 'W', padx = 15, pady =10)    

def exitProgram():
    """Closes Program and Shows a confirmation dialog before quitting"""
    response = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if response:
        root.destroy()

root = tk.Tk()

#sets the GUI Title for the Main Window
root.title('FitRep Tracker')

#Sets the root window size and enables size change of window
root.geometry('640x480+300+300')
root.resizable(True, True)
root.configure(bg = '#D3D3D3')

#Widgets for the Main Window
title = tk.Label(root, text = ' Welcome to FitRep Tracker ', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00', 
                 bd = 2, relief = 'raised', width = 30)


#WorkoutLogButton
workoutLogButton = tk.Button(root, text = ' Workout Log ', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00', 
                 bd = 2, relief = 'ridge', width = 20, command = openWorkoutLog)


workoutHistoryButton = tk.Button(root, text = ' Workout History ', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00', 
                 bd = 2, relief = 'ridge', width = 20, command = openWorkoutHistory)

exitButton = tk.Button(root, text = 'Exit', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00', 
                 bd = 2, relief = 'ridge', width = 20, command = exitProgram)


#Widget Positions on Main Windows Grid
title.grid(row = 0, column = 0, columnspan = 2, pady = 40)
workoutLogButton.grid(row = 1, column = 0, padx = 20, pady = 20)
workoutHistoryButton.grid(row = 1, column = 1, padx = 20, pady = 20)
exitButton.grid(row = 2, column = 0, columnspan = 2, pady = 40)

#configures columns and rows making them expand and contract as window size changes
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 2)
root.grid_rowconfigure(2, weight = 1)

root.mainloop()
