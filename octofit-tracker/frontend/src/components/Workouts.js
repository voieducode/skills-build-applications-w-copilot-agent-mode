import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://laughing-space-spoon-69vjg64949fw5v-8000.app.github.dev/api/workouts/')
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div className="card shadow-sm">
      <div className="card-body">
        <h1 className="card-title">Workouts</h1>
        <ul className="list-group">
          {workouts.map(workout => (
            <li key={workout._id} className="list-group-item">
              <strong>{workout.name}</strong>: {workout.description}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Workouts;
