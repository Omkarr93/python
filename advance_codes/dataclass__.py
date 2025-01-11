from dataclasses import dataclass, field
from typing import List

@dataclass
class Input:
    unit: str
    is_patient_specific: int
    measure_id: List[str]
    entity_id: int
    parent_entity_id: List[int]
    measure_details: list = field(default_factory=list)  # Default value
    entity_name: str = "practice"  # Default value
    duration_from: str = "2024-01-01 00:00:00"  # Default value
    duration_to: str = "2024-12-31 23:59:59"  # Default value

# Create an instance of the Input dataclass
input_instance = Input(
    unit="hours",
    is_patient_specific=1,
    measure_id=["M123", "M456"],
    entity_id=101,
    parent_entity_id=[202, 303]
)

# The instance has all attributes automatically initialized
print(input_instance)
