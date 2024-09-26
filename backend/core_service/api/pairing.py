from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
from utils.general import get_redis
from services.external_services import initiate_audio_processing
import uuid

router = APIRouter()


@router.post("/pair", response_model=schemas.PairingResponse)
async def pair_mobile(
        pairing: schemas.PairingRequest,
        background_tasks: BackgroundTasks,
        redis=Depends(get_redis),
        db: Session = Depends(get_db)
):
    stored_token = await redis.get(f"token:{pairing.sessionId}")
    if not stored_token or stored_token != pairing.token:
        raise HTTPException(status_code=401, detail="Invalid pairing token")

    if await redis.exists(f"mobile_paired:{pairing.sessionId}"):
        raise HTTPException(status_code=400, detail="Session already paired")

    recording_id = str(uuid.uuid4())
    stream_url = f"http://localstack:4566/kinesis-streams/your-kinesis-stream-name"

    # Generate temporary credentials (simplified for this example)
    credentials = {
        "AccessKeyId": "temp_access_key",
        "SecretAccessKey": "temp_secret_key",
        "SessionToken": "temp_session_token",
        "Expiration": "2023-12-31T23:59:59Z"
    }

    await redis.set(f"mobile_paired:{pairing.sessionId}", recording_id)

    db_recording = models.Recording(id=recording_id, session_id=pairing.sessionId)
    db.add(db_recording)
    db.commit()

    # Initiate audio processing in the background
    background_tasks.add_task(initiate_audio_processing, pairing.sessionId, recording_id)

    return schemas.PairingResponse(
        recordingId=recording_id,
        streamUrl=stream_url,
        accessKeyId=credentials["AccessKeyId"],
        secretAccessKey=credentials["SecretAccessKey"],
        sessionToken=credentials["SessionToken"],
        expiration=credentials["Expiration"]
    )
