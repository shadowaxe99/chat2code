# API Reference

The Amorphic project provides the following APIs:

- `/tags`
  - `POST /tags`: Create a new tag
  - `GET /tags`: List all tags
  - `GET /tags/{tagId}`: Get a specific tag
  - `DELETE /tags/{tagId}`: Delete a specific tag
  - `PATCH /tags/{tagId}`: Patch a specific tag

- `/auth`
  - `POST /auth/sign-in`: Sign in
  - `POST /auth/sign-up`: Sign up
  - `POST /auth/oauth/callback`: OAuth callback

- `/users`
  - `GET /users/me`: Get current user
  - `GET /users/{userId}`: Get a specific user

- `/documents`
  - `POST /documents`: Create a new document
  - `GET /documents`: List all documents
  - `GET /documents/{documentId}`: Get a specific document
  - `DELETE /documents/{documentId}`: Delete a specific document
  - `PATCH /documents/{documentId}`: Patch a specific document

- `/tools`
  - `POST /tools`: Create a new tool
  - `GET /tools`: List all tools
  - `GET /tools/{toolId}`: Get a specific tool
  - `DELETE /tools/{toolId}`: Delete a specific tool
  - `PATCH /tools/{toolId}`: Patch a specific tool

Refer to the individual API endpoints for more details on their usage and parameters.
