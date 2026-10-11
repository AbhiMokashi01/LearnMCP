from mcp.server import MCPServer

mcp=MCPServer()

@mcp.tool()
def calculate_average(a:int,b:int,c:int)->float:
    """Accepts three numbers as argument to calculate and return average of three numbers"""
    total=a+b+c
    return total/3


@mcp.resource("studybuddy://subject/{subject}")
def studybuddy(subject:str)->str:
    """act as resource and returns some information of subject"""
    return f"\nA short"+{subject}+" guide\n\n\n"


@mcp.prompt()
def prompt(topic:str,difficulty:str)->str:
    """requests model to explain on a topic with certain difficulty"""
    return f"explain about the "+ {topic} +" for a "+{difficulty}


if __name__=="__main__":
    mcp.run(transport="streamable-http")