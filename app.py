from flask import redirect, url_for, render_template, request, session, flash
from _database_model import *
from exercises import *

valid_workout = False # a valid workout should have no repeats
while not valid_workout:
    workout = Workout([])
    for muscle_group in gym_schedule[today]:
        if  gym_schedule[today] == 'rest':
            workout.exercises = 'rest'
        else:
            n = random.randint(0,len(muscle_group) - 1)
            workout.exercises.append(muscle_group[n])
    valid_workout = workout.check_if_workout_valid()
    
file = open('exercise_index.txt', 'w')
file.write('0')
file.close()

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'GET':
        print(workout)
        for exercise in workout.exercises:
            flash(exercise)
        flash(f'today you have to do {len(workout.exercises)} exercises')
        df = pd.read_csv('exercises.csv')
        df.drop(['Unnamed: 0'],axis=1, inplace=True)

        exercise_index = open('exercise_index.txt', 'r')
        _id = int(exercise_index.read())
        exercise_index.close()

        name = workout.exercises[_id].name
        print(name)
        weight = df[name][0]
        sets = df[name][1]
        reps = df[name][2]

        return render_template(
            'index.html',
            weight=weight,
            sets=sets,
            reps=reps,
            name=name
        )

    else:
        for exercise in workout.exercises:
            flash(exercise)
        print(workout)
        flash(f'today you have to do {len(workout.exercises)} exercises')
        weight = request.form['weight']
        sets = request.form['sets']
        reps = request.form['reps']
        df = pd.read_csv('exercises.csv')
        df.drop(['Unnamed: 0'],axis=1, inplace=True)

        exercise_index = open('exercise_index.txt', 'r')
        _id = int(exercise_index.read())
        exercise_index.close()

        name = workout.exercises[_id].name
        print(name)

        df[name] = pd.DataFrame([weight,sets,reps])
        print(df)
        df.to_csv('exercises.csv')

        exercise_index = open('exercise_index.txt', 'w+')
        _id = _id + 1
        exercise_index.write(str(_id))
        exercise_index.close()

        return render_template(
            'index.html',
            weight=weight,
            sets=sets,
            reps=reps,
            name=name
        )

@app.route('/<page>/', methods=['POST','GET'])
def show(page):
    if page == 'index':
        return redirect(url_for('home'))
    else:
        pass
    return render_template(f'{page}.html')
 
if __name__ == '__main__':
    app.run(debug=True, port=5500) 