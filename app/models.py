from pydantic import BaseModel, Field


class TaskRequest(BaseModel):
    description: str = Field(..., min_length=5, description="The task to analyze")


class TaskResponse(BaseModel):
    priority: str = Field(description="low, medium, or high")
    category: str = Field(description="bug, feature, or support")
    estimated_effort: str = Field(description="e.g. '2 hours'")
    suggested_team: str = Field(description="e.g. 'backend'")
    reasoning: str = Field(description="One sentence explanation")