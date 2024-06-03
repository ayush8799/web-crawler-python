

from fastapi import HTTPException, status

ACCESS_TOKEN = "eAs2u2b34v1256723bdfg" # Will be moved into an environment vairable file

async def check_token(request: object):
  try: 
    """Middleware to check for access token in headers.

    Args:
        request: The FastAPI request object.

    Raises:
        HTTPException: If the access token is missing or invalid.
    """
    print("DEBUG :: Middleware :: ", request)
    headers = request.headers
    authorizationToken = headers.get("access-token")
    print('Auithorization :: ', authorizationToken)
    if not authorizationToken or len(authorizationToken) == 0:
      raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid access token"
      )

    # Extract the token from the authorizationToken header
    # token = authorizationToken.split()[1]

    if authorizationToken != ACCESS_TOKEN:
      raise HTTPException(
          status_code=status.HTTP_403_FORBIDDEN, detail="Invalid access token"
      )
  except Exception as e:
    # print('middleware error : ', e)
    raise e

