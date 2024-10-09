i have this:
access_token
: 
"eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly92YW1vczE3LnVzLmF1dGgwLmNvbS8ifQ..y1sb3mm2Srp7dha3.9rHK0lBVJ2lfpF0qIPMbX6q1as_LhYU5y_QBr0RkKPEQyjdEZVgNCuKRZ8hCNlTTVBy6X41Ow2QrPlIR9Ey_n5q4Ih9UzME4RgSSb7qM8ouQGatLyhwBjnrmTAJT6cy2Kgk7l_3zq41m6aaGqIYZw4SaD_obUbW4kxA2IN_7LHayeAMOsjBPzo7RDZu3pkSahkDxeDDMRH4xMcGuKxjqSJ0kbku8Jsr8P_zjwSQRdBIwQSgsEaXpbrLb_y1ITxT8Y82euHfAyZXyZKXLPg0rPSVMRLy5rqVgzLjeSEGviMSUPQkvlT7ZfsXqdQp9.SBqYcMOu0W1szKogqod2cw"
expires_at
: 
1728404750
expires_in
: 
86400
id_token
: 
"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlktRV8yOVcyRU9jSF9wM05OanJxMCJ9.eyJnaXZlbl9uYW1lIjoiam9obiIsImZhbWlseV9uYW1lIjoic21pdGgiLCJuaWNrbmFtZSI6ImpvaG5zbWl0aDk2NDQxIiwibmFtZSI6ImpvaG4gc21pdGgiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jS3dxc0YtRURjRWk5NjU2dDJjM0p6bFpwWk1QMmFoVDBwYXNVOWlLYUxtdnZvX2p3PXM5Ni1jIiwidXBkYXRlZF9hdCI6IjIwMjQtMTAtMDdUMTY6MjU6NDguNzkzWiIsImVtYWlsIjoiam9obnNtaXRoOTY0NDFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vdmFtb3MxNy51cy5hdXRoMC5jb20vIiwiYXVkIjoiQmVrWUx4R3dQQk1FVDBKbVUyTExnMXViakNrY3pKM1kiLCJpYXQiOjE3MjgzMTgzNDksImV4cCI6MTcyODM1NDM0OSwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDUyODY4NzU0OTM3MzEyMjY1NjgiLCJzaWQiOiI4N3B0Umdld0piYW1ySnR0Rk1vZFFFYm50SmFEbkM5WSIsIm5vbmNlIjoiaGE0cXJaZ2Z5emdRZmFtRlpQbkYifQ.iWmyk6Sh8UxS2gZDQNtPhV-ojDx_ApBEJVGdcPCWj0KRBt7wrOfAn-Zy86KFTZpr7z2UoQeLk1LeXPOlJIGXLjVCSipmXGQ7FFfdNO62DJzU5wZ1i4cnujyD4nOburxReB1KPZkCHiLPyrxlu2XzR_RvsM38qpo7sFdPHRZlyquYUBHD3NAXxAY5L41LOcW_6xgWpbLFxUtx7SJyroPwdL92OdllIT5SoJY_6PAjzGMu82LJ1SfXQeKw_BQRzkDM9xSa1buZFj2MEoOYJ9BvUt__ylfJrJGF_6Cr8hwmQepZGfYSwalZuWuZ81vaXdqgnRXgBPi6NEbdW9m12qZ-8A"
scope
: 
"openid profile email"
token_type
: 
"Bearer"

this is from the Oauth2 using open id connect...

currently this is how i am checking for authentication..:
step 1: the frontend runs this logic:
useEffect(()=>{
    console.log("checkLoginStatus");
    
    checkLoginStatus()
  }, [])

  const checkLoginStatus = async () =>{
    try {
      // const response = await fetch(`${backend_url}/api/is_logged_in`, {
      //   method: "GET",
      //   credentials: "include",
      // })
      const response = await axios.get(`${backend_url}/api/is_logged_in`,{
        withCredentials: true,
      })
      // const data = await response.json()
      console.log("response.data", response.data)      

      if(response.data.logged_in){
        setIsAuthenticated(true)
      }else{
        setIsAuthenticated(false)
      }
    } catch (error) {
      console.error("Error checking login status:", error);      
    }finally{
      setLoading(false)
    }
  }

the backend api is:
# check login status
@api_view(['GET'])
def is_logged_in(request):
    user = request.session.get("user", None)
    if user:
        return Response({"logged_in": True, "user": user}, status=status.HTTP_200_OK)
    else:
        return Response({"logged_in": False}, status=status.HTTP_401_UNAUTHORIZED)

instead of checking if the user session exists, i want the following to happen:

1. when the logic to check for authentication is run, the frontend should store the token and expiration time in localstorage.
2. when the logic runs again, the code 