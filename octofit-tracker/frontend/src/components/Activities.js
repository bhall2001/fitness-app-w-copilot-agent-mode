import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://fitness-app-w-copilot-agent-mode-8000.app.github.dev/api/activities/')
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div className="card shadow mb-4">
      <div className="card-body">
        <h2 className="card-title text-primary mb-4">Activities</h2>
        <div className="table-responsive">
          <table className="table table-striped table-hover align-middle">
            <thead className="table-primary">
              <tr>
                <th>User ID</th>
                <th>Type</th>
                <th>Duration</th>
                <th>Date</th>
              </tr>
            </thead>
            <tbody>
              {activities.map(activity => (
                <tr key={activity._id}>
                  <td>{activity.user_id || activity.user}</td>
                  <td>{activity.activity_type}</td>
                  <td>{activity.duration}</td>
                  <td>{activity.date}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <button className="btn btn-primary mt-3" type="button" data-bs-toggle="modal" data-bs-target="#addActivityModal">Add Activity</button>
        {/* Modal for adding activity */}
        <div className="modal fade" id="addActivityModal" tabIndex="-1" aria-labelledby="addActivityModalLabel" aria-hidden="true">
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title" id="addActivityModalLabel">Add Activity</h5>
                <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div className="modal-body">
                <form>
                  <div className="mb-3">
                    <label htmlFor="userId" className="form-label">User ID</label>
                    <input type="text" className="form-control" id="userId" placeholder="Enter user ID" />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="activityType" className="form-label">Type</label>
                    <input type="text" className="form-control" id="activityType" placeholder="Enter activity type" />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="duration" className="form-label">Duration</label>
                    <input type="number" className="form-control" id="duration" placeholder="Enter duration (minutes)" />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="date" className="form-label">Date</label>
                    <input type="date" className="form-control" id="date" />
                  </div>
                  <button type="submit" className="btn btn-success">Add</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Activities;
