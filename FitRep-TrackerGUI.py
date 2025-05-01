import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
exerciseLog = []

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
        dayLogWindow.geometry('800x720+300+300')
        dayLogWindow.configure(bg = '#D3D3D3')
        dayLogWindow.grab_set()

        def addWorkoutToLog():
            """adds exercise to the log after inputs are selected"""
            name = exerciseNameEntry.get().strip()
            excerciseType = exerciseTypeDropdown.get().strip()
            weight = weightEntry.get().strip()
            sets = setsEntry.get().strip()
            reps = repsEntry.get().strip()
            intensity = intensityDropdown.get().strip()
            day = dayLogWindow.title().split(' ')[0]

            # Check if any field is empty or invalid
            if not name or excerciseType == 'Select Type' or not weight or not sets or not reps or intensity == '1–10':
                messagebox.showwarning("Missing Info", "Please fill out all fields correctly.")
                return

            # Validate that weight, sets, reps, and intensity are numbers
            try:
                weightNum = float(weight)
                setsNum = int(sets)
                repsNum = int(reps)
                intensityNum = int(intensity)
            except ValueError:
                messagebox.showerror("Invalid Input", "Weight must be a number, and Sets, Reps, Intensity must be integers.")
                return

            # Format the entry
            entryText = f"{name} | {excerciseType} | {weightNum} lbs | {setsNum} sets | {repsNum} reps | Intensity {intensityNum}"

            #Adds exercises to shared list of daylog and history log
            exerciseLog.append((day, entryText)) 

            # Add to log display
            entryLabel = tk.Label(logDisplayFrame, text=entryText, font=('Georgia', 12),
                           anchor='n', bg='white', relief='groove')
            entryLabel.pack(fill='x', padx=5, pady=2)

            # Clear fields
            exerciseNameEntry.delete(0, tk.END)
            exerciseTypeDropdown.set('Select Type')
            weightEntry.delete(0, tk.END)
            setsEntry.delete(0, tk.END)
            repsEntry.delete(0, tk.END)
            intensityDropdown.set('1–10')


        def backToMain():
            '''Closes the Daylog subwindow'''
            dayLogWindow.destroy()

        def saveWorkoutLog():
            """Confirms that workout data was saved (already added to exerciseLog)"""
            for widget in logDisplayFrame.winfo_children():
                widget.destroy()
                #resets entry windows
                exerciseNameEntry.delete(0, tk.END)
                exerciseTypeDropdown.set('Select Type')
                weightEntry.delete(0, tk.END)
                setsEntry.delete(0, tk.END)
                repsEntry.delete(0, tk.END)
                intensityDropdown.set('1–10')
            messagebox.showinfo('Saved', 'Added to History')

        #Top Frame and Headers for Daylog spreadsheet layout
        #Top Frame
        contentFrame = tk.Frame(dayLogWindow, bg = '#D3D3D3')
        contentFrame.grid(row = 0, column = 0, sticky = 'NSEW', padx = 10, pady = 10)

        #Headers for Frame
        headers = ['Add (+)', 'Exercise Name', 'Exercise Type/Weight Type', 'Weight (lbs)', 'Sets', 'Reps', 'Intensity (1–10)']
        headerLabels = []
        
        #Grid for headers
        for columnIndex, header in enumerate(headers):
            headerLabel = tk.Label(contentFrame, text=header, font=('Georgia', 12, 'bold'), bg='#D3D3D3')
            headerLabels.append(headerLabel)

        for columnIndex, headerLabel in enumerate(headerLabels):
            headerLabel.grid(row=0, column = columnIndex, padx = 5, pady = 5)
        for columns in range(7):  # One for each header column
            contentFrame.grid_columnconfigure(columns, weight=1)

        #Add Button for adding exercise to etc.
        addButton = tk.Button(contentFrame, text = '+', font = ('Georgia', 9, 'bold'), fg = 'blue', bg = '#FFDF00',
                                  bd = 2, relief ='ridge', width =5, command = addWorkoutToLog)
        #List Index for Row 1's exercise types and intensity scales
        exerciseTypes = ['Dumbbells', 'Barbell and Plates', 'Machine', 'Body Weight']
        intensityScale = [str(i) for i in range(1, 11)]

        #Comboboxs for Entry selection 
        exerciseTypes = ['Dumbbells', 'Barbell and Plates', 'Machine', 'Body Weight']
        exerciseTypeDropdown = ttk.Combobox(contentFrame, values=exerciseTypes, state='readonly')
        exerciseTypeDropdown.set('Select Type')

        intensityScale = [str(i) for i in range(1, 11)]
        intensityDropdown = ttk.Combobox(contentFrame, values=intensityScale, state='readonly')
        intensityDropdown.set('1–10')

        #Input Entry sections for Exercises
        exerciseNameEntry = tk.Entry(contentFrame, width = 20)
        weightEntry = tk.Entry(contentFrame, width = 10)
        setsEntry = tk.Entry(contentFrame, width = 5)
        repsEntry = tk.Entry(contentFrame, width = 5)

        #Grid layout for entrys
        addButton.grid(row = 1, column = 0, padx = 5, pady = (0,2), sticky = 'N')
        exerciseNameEntry.grid(row = 1, column = 1, padx = 5, pady = (0,2), sticky = 'N')
        exerciseTypeDropdown.grid(row = 1, column = 2, padx = 5, pady = (0,2), sticky = 'N')
        weightEntry.grid(row = 1, column = 3, padx = 5, pady = (0,2), sticky = 'N')
        setsEntry.grid(row = 1, column = 4, padx= 5, pady = (0,2), sticky = 'N')
        repsEntry.grid(row = 1, column = 5, padx = 5, pady = (0,2), sticky = 'N')
        intensityDropdown.grid(row = 1, column = 6, padx = 5 ,pady = (0,2), sticky = 'N')
        contentFrame.grid_rowconfigure(2, weight=1)
        
        #log display
        logDisplayFrame = tk.Frame(contentFrame, bg='#EDEDED', bd=1, relief='sunken')
        logDisplayFrame.grid(row = 2, column = 0, columnspan = 7, pady = (5 , 0), sticky = 'NEW')
        logDisplayFrame.grid_columnconfigure(0, weight=1)
        

        #Bottom Frame for buttons
        bottomFrame = tk.Frame(dayLogWindow, bg='#D3D3D3')
        bottomFrame.grid(row=1, column=0, sticky='ew', pady=20)
        
        #Buttons for dayLogWindow bottom frame
        backDayButton = tk.Button(bottomFrame, text = 'Back', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00',
                                  bd = 2, relief ='ridge', width = 5, command = backToMain)
        saveButton = tk.Button(bottomFrame, text = 'Save', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00',
                                  bd = 2, relief ='ridge', width = 5, command = saveWorkoutLog)
        
        backDayButton.grid(row = 0, column = 0, padx= 10)
        saveButton.grid(row = 0, column = 1, padx= 10)
        
        #grid Layout for DayLog Window
        dayLogWindow.grid_rowconfigure(0, weight=1)
        dayLogWindow.grid_rowconfigure(1, weight=0)
        dayLogWindow.grid_columnconfigure(0, weight=1)

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
    workoutLogWindow.grid_rowconfigure(0, weight = 1)


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

    def deleteWorkoutHistoryEntry():
        """Deletes the selected workout entry from the history"""
        selectedIndex = historyDisplay.curselection()
        if selectedIndex:
            index = selectedIndex[0]
            del exerciseLog[index]
            historyDisplay.delete(index)
            messagebox.showinfo('Deleted Entry', 'The selected workout has been deleted.')

    # Create a frame to display history
    historyFrame = tk.Frame(workoutHistoryWindow, bg='#D3D3D3')
    historyFrame.grid(row=0, column=0, sticky='NSEW', padx=10, pady=10)

    # Create a scrollbar for the history window
    historyScroll = tk.Scrollbar(historyFrame)
    historyScroll.grid(row=0, column=1, sticky='NS')

    # Display the workout history logs
    historyDisplay = tk.Listbox(historyFrame, yscrollcommand=historyScroll.set, width=80, height=20)
    for entry in exerciseLog:  # Populate the listbox with the log entries
        historyDisplay.insert(tk.END, entry)

    historyDisplay.grid(row=0, column=0, padx=10, pady=10)
    historyScroll.config(command=historyDisplay.yview)
        
    #Frame for Bottom
    bottomFrame = tk.Frame(workoutHistoryWindow, bg = '#D3D3D3')
    bottomFrame.grid(row = 1, column = 0, sticky = 'EW', pady = 20)

    #History widget buttons
    backHistoryButton = tk.Button(bottomFrame, text = 'Back', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00', 
                 bd = 2, relief = 'ridge', width = 5, command = backToMain)
    deleteButton = tk.Button(bottomFrame, text = 'Delete', font = ('Georgia', 16, 'bold'), fg = 'blue', bg = '#FFDF00', 
                 bd = 2, relief = 'ridge', width = 5, command = deleteWorkoutHistoryEntry)
    
    #Grid for History Window
    backHistoryButton.grid(row = 0, column = 0, sticky = 'W', padx = 15, pady = 10)
    deleteButton.grid(row = 0, column = 2, sticky = 'W', padx = 15, pady =10)

    #Grid Layout for History Window
    workoutHistoryWindow.grid_rowconfigure(0, weight = 1)
    workoutHistoryWindow.grid_rowconfigure(1, weight=0)
    workoutHistoryWindow.grid_columnconfigure(0, weight=1)

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
