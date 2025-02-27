from fastapi import APIRouter, HTTPException, UploadFile, File
from utils import process_csv_for_bulk_check_in

router = APIRouter()

@router.post("/attendees/bulk-check-in")
def bulk_check_in_attendees(
    file: UploadFile = File(...),  
):
    
    csv_data = file.file.read().decode("utf-8")
    
   
    process_csv_for_bulk_check_in(csv_data)
    
    return {"message": "Bulk check-in completed successfully"}