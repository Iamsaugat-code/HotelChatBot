
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("about_hotel")

@mcp.tool()
async def abouthotel(city:str)->str:
    """about hotel list in city """
    return f"list of hotel in {city} are : "

@mcp.tool()
async def internalHotelInfo(query: str) -> str:
    """Handle requests for restricted or internal hotel information.
    This tool returns the application's standard response for information
    that is not available to users.
    """
    return "This type of information is not provided by our application."

@mcp.tool()
async def higher_class(query: str) -> str:
    """Get the price of a HIGHER-CLASS hotel room.
    Use this tool when the user asks for higher class room price.
    """
    return "Higher class room price: $180/day"

@mcp.tool()
async def middle_class(query: str) -> str:
    """Get the price of a MIDDLE-CLASS hotel room.
    Use this tool when the user asks for middle class,
    mid class, medium class, or middle-class room price.
    """
    return "Middle class room price: $120/day"
    
@mcp.tool()
async def lower_class(query: str) -> str:
    """Get the price of a LOWER-CLASS hotel room.
    Use this tool when the user asks for lower class room price.
    """
    return "Lower class room price: $80/day"


@mcp.tool()
async def hotelbooking(query:str)->str:
    """about hotel booking time (open and closed time)"""
    return """
    Booking Open At : 6:00 am
    Booking Close At : 9:00 pm
    """

@mcp.tool()
async def hotelServiceContent(query:str)->str:
    """about hotel service content or helpline contant of hotel"""
    return """
    Contact list:
    1. Account : 0900
    2. Room Service : 10101
    3. Booking Contant : 0977
    """

if __name__ == '__main__':
    mcp.run(transport='streamable-http')