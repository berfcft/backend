from fastapi import WebSocket, WebSocketDisconnect, Depends, HTTPException
from app.core.security import decode_access_token

async def websocket_endpoint(websocket: WebSocket, token: str):
    # Decode and verify the JWT token
    payload = decode_access_token(token)
    if payload is None:
        await websocket.close(code=1008)
        raise HTTPException(status_code=403, detail="Invalid token")

    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # Here you can process the incoming data and send responses
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        print("Client disconnected") 