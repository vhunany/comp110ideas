class Plants:
    def __init__(self):
        # Initialize seeds_available with an empty dictionary
        self.seeds_available = {}
        # Initialize seed_info with an empty dictionary
        self.seed_info = {}

    def add_seed(self, plant_name, number_of_seeds, harvest_per_plant):
        # Update seeds_available with the new seeds
        if plant_name in self.seeds_available:
            self.seeds_available[plant_name] += number_of_seeds
        else:
            self.seeds_available[plant_name] = number_of_seeds

        # Update seed_info with the harvest information
        self.seed_info[plant_name] = harvest_per_plant

    def use_seeds(self, plant_name, number_of_seeds):
        # Check if enough seeds are available
        if plant_name in self.seeds_available and self.seeds_available[plant_name] >= number_of_seeds:
            self.seeds_available[plant_name] -= number_of_seeds
            return True
        return False

class Garden:
    def __init__(self):
        # Initialize garden_plots with an empty dictionary
        self.garden_plots = {}

    def add_plot(self, plot_name):
        # Add a new plot to the garden if it doesn't exist
        if plot_name not in self.garden_plots:
            self.garden_plots[plot_name] = {}

    def add_plant_to_plot(self, plot_name, plant_name, number_of_plants):
        # Add plants to a specific plot
        if plot_name in self.garden_plots:
            if plant_name in self.garden_plots[plot_name]:
                self.garden_plots[plot_name][plant_name] += number_of_plants
            else:
                self.garden_plots[plot_name][plant_name] = number_of_plants
        else:
            print(f"Plot {plot_name} does not exist.")

    def get_plot(self, plot_name):
        # Return information about a specific plot
        if plot_name in self.garden_plots:
            return self.garden_plots[plot_name]
        else:
            return "Plot does not exist."

    def __str__(self):
        # Create a string representation of the Garden object
        garden_str = "Garden Overview:\n"
        if not self.garden_plots:
            return garden_str + "No plots available."

        # Manually build the plot_names list
        plot_names = []
        for plot in self.garden_plots:
            plot_names.append(plot)

        for i in range(len(plot_names)):
            plot = plot_names[i]
            garden_str += f"\n{plot}:\n"

            # Check if there are plants in this plot
            if not self.garden_plots[plot]:
                garden_str += "  No plants in this plot.\n"
            else:
                # Manually build the plant_names list
                plant_names = []
                for plant in self.garden_plots[plot]:
                    plant_names.append(plant)

                for j in range(len(plant_names)):
                    plant = plant_names[j]
                    count = self.garden_plots[plot][plant]
                    garden_str += f"  {plant}: {count} plant(s)\n"

        return garden_str
