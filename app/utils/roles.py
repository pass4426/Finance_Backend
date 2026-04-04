from fastapi import HTTPException, Depends


def require_role(allowed_roles: list):
    def role_checker(user_role: str):
        if user_role not in allowed_roles:
            raise HTTPException(status_code=403, detail="Access denied")
        return True
    return role_checker
