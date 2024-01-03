from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, Literal
from datetime import datetime

RequestingEntity = Literal["Tenant", "Owner", "Staff", "Vendor"]

TaskType = Literal[
    "To Do", "Resident Request", "Rental Owner Request", "Contact Request"
]

TaskStatus = Literal["New", "In Progress", "Completed", "Deferred", "Closed"]

TaskPriority = Literal["Low", "Normal", "High"]

TaskCategory = Literal[
    "Contribution Request",
    "General Inquiry",
    "Maintenance Request",
    "Uncategorized",
    "Complaint",
    "Doors Locks & Windows",
    "Electrical",
    "Elevator",
    "Emergency",
    "Exterior Lighting",
    "Feedback Suggestion",
    "Gate System",
    "Grounds Landscape",
    "HVAC",
    "Laundry",
    "Other",
    "Plumbing",
    "Pool & Gym",
]


class TaskRequest(BaseModel):
    # task_type: TaskType = Field(
    #     ..., description="The type of the task", alias="TaskType"
    # )
    subject: str = Field(..., description="The subject of the task (in English)", alias="Subject")
    description: str = Field(
        ..., description="The description of the task (in English)", alias="Description"
    )
    category_id: TaskCategory = Field(
        ..., description="The task category ID of the task", alias="CategoryId"
    )
    # subcategory_id: Optional[int] = Field(
    #     None, description="The subcategory ID of the task", alias="SubcategoryId"
    # )
    # assigned_to_user_id: int = Field(
    #     ...,
    #     description="The user ID to whom the task is assigned",
    #     alias="AssignedToUserId",
    # )
    # task_status: TaskStatus = Field(
    #     ..., description="The status of the task", alias="TaskStatus"
    # )
    # due_date: Optional[datetime] = Field(
    #     None, description="The due date of the task", alias="DueDate"
    # )
    task_priority: TaskPriority = Field(
        ..., description="The priority of the task", alias="TaskPriority"
    )
    # property_id: int = Field(
    #     ..., description="The property ID related to the task", alias="PropertyId"
    # )
    # unit_id: int = Field(
    #     ..., description="The unit ID related to the task", alias="UnitId"
    # )
    # appliance_id: Optional[int] = Field(
    #     None, description="The appliance ID related to the task", alias="ApplianceId"
    # )
    # requesting_entity_id: RequestingEntity = Field(
    #     ..., description="The entity ID requesting the task", alias="RequestingEntityId"
    # )
