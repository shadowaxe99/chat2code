# API Documentation

The Amorphic project provides a set of APIs that allow you to interact with the AI agent system. These APIs enable you to send requests to the system and receive responses.

## Endpoints

The following endpoints are available:

- `/api/agents`: This endpoint allows you to retrieve information about the agents in the system.
- `/api/agents/{id}`: This endpoint allows you to retrieve information about a specific agent.
- `/api/agents/{id}/tasks`: This endpoint allows you to retrieve the tasks assigned to a specific agent.
- `/api/tasks`: This endpoint allows you to retrieve information about all tasks in the system.
- `/api/tasks/{id}`: This endpoint allows you to retrieve information about a specific task.

## Request and Response Format

The APIs accept and return data in JSON format. Here is an example of a request and response:

**Request**:

```json
{
  "id": "123",
  "task": "Analyze data"
}
```

**Response**:

```json
{
  "status": "success",
  "data": {
    "id": "123",
    "task": "Analyze data",
    "status": "completed"
  }
}
```

Please refer to the individual API documentation for more detailed information on the request and response format.