import pandas as pd 
import random 
import datetime

def construct_exercise(name):
    df = pd.read_csv('exercises.csv')
    df.drop(['Unnamed: 0'],axis=1, inplace=True)
    df[name] = pd.DataFrame([0,0,0])
    print(df)
    df.to_csv('exercises.csv')

class Exercise(object):

    def __init__(self, name):
        self.name = name
        df = pd.read_csv('exercises.csv')
        try:
            self.weight = df[self.name][0]
            self.sets = df[self.name][1]
            self.reps = df[self.name][2]
        except KeyError:
            construct_exercise(name)
    
    def __repr__(self):
        return f'''
        name : {self.name},
        weight: {self.weight} Kg,
        sets: {self.sets},
        reps: {self.reps}       
        '''
    
    def record_weight(self):
        pass
        
class Workout(list):

    def __init__(self, exercises):
        self.exercises: list = exercises
    
    def __repr__(self):
        return f'''
            {self.exercises}
        '''
    
    def check_if_workout_valid(self):
        unique_exercise_workout = []
        for exercise in self.exercises:
            if exercise in unique_exercise_workout:
                pass
            else:
                unique_exercise_workout.append(exercise)
        if len(unique_exercise_workout) != len(self.exercises):
            return False
        else:
            return True
    
    def record_workout(self):
        pass

# Textual month, day and year
today = datetime.date.today().weekday()

biceps_heavy: list = [Exercise('barbel curl'),Exercise('preacher curl')] # turn the contents of this list as exercises
biceps_light: list = [Exercise('superman curl'), Exercise('inclined bench curl superset'),Exercise('hammer curl superset'),Exercise('cable')]
triceps_heavy: list = [Exercise('deep'),Exercise('overhead tricpes'),Exercise('easy bar'),Exercise('heavy cable')]
triceps_light: list = [Exercise('cable triplesuperset close weights'),Exercise('straight bar'),Exercise('superset'),Exercise('inclined bench')]
shoulders_heavy: list = [Exercise('military press'),Exercise('heavy shoulder press')]
shoulders_light: list = [Exercise('cable extensions'),Exercise('lateral raises'),Exercise('shoulder machine superset'),Exercise('arnold press')]
back_heavy: list = [Exercise('muscle ups'),Exercise('barbell rows'),Exercise('heavy lat pull downs')]
back_light: list = [Exercise('lat pull downs controlled'),Exercise('changed grip lat pull down'),Exercise('pull ups'),Exercise('chin ups')]
abs: list = [Exercise('leg raises'),Exercise('L seats'),Exercise('clock raises'),Exercise('lateral leg rasies')]
chest: list = [Exercise('bench')]

# the form will tell you the exercises and inser as a placeholder the previous weight sets and reps that you have done 
# then you will only have to fill in the form and huit record 

gym_schedule:list = [
    [chest, biceps_heavy,triceps_heavy,abs,biceps_light,triceps_light,abs,biceps_light,triceps_light],
    'rest',
    [back_heavy,shoulders_heavy,abs,back_light,shoulders_light,abs,back_light,shoulders_light],
    'rest',
    [chest, biceps_heavy,triceps_heavy,abs,biceps_light,triceps_light,abs,biceps_light,triceps_light],
    [back_heavy,shoulders_heavy,abs,back_light,shoulders_light,abs,back_light,shoulders_light],
    'rest'
]




