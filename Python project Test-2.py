print("ALEXIS DINNER")
menu_item = "pizza"
guests = 11
print("Menu item:" ,menu_item)
print("number of persons:" ,guests)
menu_item = "biryani"
print("Updated menu item is: "+ menu_item)
guests_alergic_Menu1= 0
print("guests alergic biryan:", guests_alergic_Menu1)
biryani_per_person= 1
biryani_needed= biryani_per_person*guests
print("biryan needed:",biryani_needed)
biryani_prepared= 11
enough_biryani= biryani_prepared == biryani_needed
biryani_per_guests= biryani_prepared/guests
print("biryan per person:" ,biryani_per_guests )
menu_item2="South Salad"
print("Menu item 2:", menu_item2)
guests_alergic_Menu2= 6
print("guests alergic South Salad:", guests_alergic_Menu2)
guests_Not_alergic= 5
print("guestes not alergic:", guests_Not_alergic)
South_Salad_per_person= 1
South_Salad_prepared=5
South_Salad_needed= South_Salad_per_person*South_Salad_prepared
print("South Salad needed:",South_Salad_needed)
enough_South_Salad= South_Salad_prepared == South_Salad_needed
South_Salad_per_guests= South_Salad_prepared/guests_Not_alergic
print("South Salad per person:" ,South_Salad_per_guests )
print("____________________________")
