from pydantic import BaseModel, Field
from typing import Optional, List


# Location model for technician coordinates
class Location(BaseModel):
    x: float = Field(description="X coordinate")
    y: float = Field(description="Y coordinate")
    z: float = Field(description="Z coordinate")


# Technician model
class Technician(BaseModel):
    id: str = Field(description="Unique technician identifier")
    location: Location = Field(
        description="Current location of the technician")


# Server model
class Server(BaseModel):
    id: str = Field(description="Unique server identifier")
    name: str = Field(description="Server name")
    location: Location = Field(description="Location of the server")


# Jira-related models
class JiraTicket(BaseModel):
    key: Optional[str] = None
    id: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    status_id: Optional[str] = None
    priority: Optional[str] = None
    assignee: Optional[str] = None
    reporter: Optional[str] = None
    created: Optional[str] = None
    updated: Optional[str] = None
    project: Optional[str] = None
    issue_type: Optional[str] = None
    labels: List[str] = []


class JiraTicketListResponse(BaseModel):
    tickets: List[JiraTicket]
    count: int
    message: str = "Successfully retrieved Jira tickets"


class JiraStatusUpdate(BaseModel):
    status: str = Field(
        description="The new status name (e.g., 'In Progress', 'Done')"
    )


class JiraComment(BaseModel):
    comment: str = Field(
        min_length=1,
        description="The comment text to add"
    )
