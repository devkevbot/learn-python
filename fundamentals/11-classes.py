class Vehicle:
    electric: bool
    num_steats: int
    max_speed: float
    requires_licence: bool
    purchase_price: float
    colour: str

    acceptable_paint_colours: "list[str]" = [
        "red", "black", "silver", "blue", "green"
    ]

    def __init__(self,
                 electric: bool = False,
                 num_seats: int = 1,
                 max_speed: float = 100.00,
                 requires_license: bool = True,
                 purchase_price: float = 10_000.00,
                 colour: str = "silver"
                 ) -> None:
        self.electric = electric
        self.num_steats = num_seats
        self.max_speed = max_speed
        self.requires_licence = requires_license
        self.purchase_price = purchase_price
        self.colour = colour

    def convert_to_electric(self) -> None:
        self.electric = True

    def paint_new_color(self, new_color: str) -> None:
        if new_color not in self.acceptable_paint_colours:
            raise ValueError(
                f"Expected argument 'new_color' to be one of: {self.acceptable_paint_colours}, got: '{new_color}'"
            )


my_car = Vehicle()
my_car.paint_new_color("red")
my_car.convert_to_electric()
