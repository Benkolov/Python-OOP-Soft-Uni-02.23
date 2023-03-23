from project.controller import Controller

controller = Controller()


print(controller.add_aquarium('FreshwaterAquarium', 'Aquarium'))

print(controller.add_decoration('Plant'))
print(controller.insert_decoration('Aquarium', 'Plant'))
print(controller.add_decoration('Ornament'))
print(controller.insert_decoration('Aquarium', 'Ornament'))
print(controller.add_fish('Aquarium', 'FreshwaterFish', 'Nemo', 'species', 2.60))
print(controller.add_fish('Aquarium', 'FreshwaterFish', 'Nemo2', 'species', 2.60))
print(controller.add_fish('Aquarium', 'FreshwaterFish', 'Nemo3', 'species', 2.60))
print(controller.feed_fish('Aquarium'))
print(controller.calculate_value('Aquarium'))
print(controller.add_aquarium('SaltwaterAquarium', 'Aquarium2'))
print(controller.report())
