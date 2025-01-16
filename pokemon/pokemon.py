import csv
from collections import Counter
import re



#1-1
def fire_type_percentage(input_file, output_file):

    csv_reader = csv.DictReader(open(input_file))
    reader = list(csv_reader)
            
    with open(output_file, 'w', newline='') as write_file:
        fire_over40_counter = 0
        fire_counter = 0

        for num, row in enumerate(reader):
            if float(row['level']) >= 40 and row['type'] == 'fire':
                fire_over40_counter += 1
                fire_counter += 1
            elif(row['type'] == 'fire'):
                fire_counter += 1

        write_file.write(f'The percentage of fire type Pokemons at or above level 40 = {round((fire_over40_counter/fire_counter) * 100)}')

#1.2-1.3
def missing_NaN(input_file, output_file):
    csv_reader = csv.DictReader(open(input_file))
    reader = list(csv_reader)

    with open(output_file, 'w', newline='') as write_file:
        writer = csv.DictWriter(write_file, fieldnames=csv_reader.fieldnames)
        writer.writeheader()

        for num, row in enumerate(reader):
            #1.2
            if row['type'] == 'NaN':
                current_weakness = row['weakness']
                type_list = []
                for weakness_x in reader:
                    if weakness_x['weakness'] == current_weakness and weakness_x['type'] != 'NaN':
                        type_list.append(weakness_x['type'])
                        
                sorted_types = sorted(type_list)
                type_counter = Counter(sorted_types)
                most_common_type = type_counter.most_common(1)
                
                row['type'] = most_common_type[0][0]

            #1.3
            threshold = 40
            #atk
            if row['atk'] == 'NaN':
                current_level = row['level']
                if float(current_level) > threshold:
                    total_atk = 0
                    count_atk = 0
                    
                    for atk_x in reader:
                        if float(atk_x['level']) > threshold and atk_x['atk'] != 'NaN':
                            total_atk += float(atk_x['atk'])
                            count_atk += 1
                            
                    
                    atk_avg = total_atk/count_atk
                    
                    
                    row['atk'] = "{:.1f}".format(round(atk_avg, 1))

                if float(current_level) <= threshold:
                    total_atk2 = 0
                    count_atk2 = 0
                    
                    for atk_x in reader:
                        if float(atk_x['level']) <= threshold and atk_x['atk'] != 'NaN':
                            total_atk2 += float(atk_x['atk'])
                            count_atk2 += 1
                    
                    atk_avg2 = total_atk2/count_atk2
                    
                    
                    row['atk'] = "{:.1f}".format(round(atk_avg2, 1))

            #def
            if row['def'] == 'NaN':
                current_level = row['level']
                if float(current_level) > threshold:
                    total_def = 0
                    count_def = 0

                    for def_x in reader:
                        if float(def_x['level']) > threshold and def_x['def'] != 'NaN':
                            total_def += float(def_x['def'])
                            count_def += 1

                        
                    def_avg = total_def/count_def
                    
                    row['def'] = "{:.1f}".format(round(def_avg, 1))
                    
                if float(current_level) <= threshold:
                    total_def2 = 0
                    count_def2 = 0

                    for def_x in reader:
                        if float(def_x['level']) <= threshold and def_x['def'] != 'NaN':
                            total_def2 += float(def_x['def'])
                            count_def2 += 1

                    def_avg2 = total_def2/count_def2
                    
                    row['def'] = "{:.1f}".format(round(def_avg2, 1))
                    
                
            #hp
            if row['hp'] == 'NaN':
                current_level = row['level']
                if float(current_level) > threshold:
                    total_hp = 0
                    count_hp = 0

                    for hp_x in reader:
                        if float(hp_x['level']) > threshold and hp_x['hp'] != 'NaN':
                            total_hp += float(hp_x['hp'])
                            count_hp += 1

                    hp_avg = total_hp/count_hp
                    
                    row['hp'] = "{:.1f}".format(round(hp_avg, 1))
                    
                
                if float(current_level) <= threshold:
                    total_hp2 = 0
                    count_hp2 = 0

                    for hp_x in reader:
                        if float(hp_x['level']) <= threshold and hp_x['hp'] != 'NaN':
                            total_hp2 += float(hp_x['hp'])
                            count_hp2 += 1

                    hp_avg2 = total_hp2/count_hp2
                    
                    row['hp'] = "{:.1f}".format(round(hp_avg2, 1))
                    
                
            writer.writerow(row)

def personality_dict(input_file, output_file):
    csv_reader = csv.DictReader(open(input_file))
    reader = list(csv_reader)

    with open(output_file, 'w', newline='') as write_file:
        final_dict = {}
        for num, row in enumerate(reader):
            type = row['type']
            personality_list = []
            current_type = ''

            for count, type_x in enumerate(reader):
                if type_x['type'] == type:
                    current_type = type_x['type']
                    personality_list.append(type_x['personality'])
            
            sorted_list = sorted(personality_list)
            final_dict[current_type] = list(sorted_list) 
            
            final_dict_keys = list(final_dict.keys())
            final_dict_keys.sort()
            sorted_dict = {i:final_dict[i] for i in final_dict_keys}
            

        write_file.write('Pokemon type to personality mapping:\n\n\t')

        for key, value in sorted_dict.items():
            write_file.write(f'{key}: ')

            for number, line in enumerate(value):
                if number != len(value) - 1:
                    write_file.write(f'{line}, ')
                else:
                    write_file.write(f'{line}\n\t')

def stage3_avg_hp(input_file, output_file):
    csv_reader = csv.DictReader(open(input_file))
    reader = list(csv_reader)

    with open(output_file, 'w', newline='') as write_file:
        hp_total = 0
        count = 0
        for num, row in enumerate(reader):
            if row['stage'] == '3.0':
                hp_total += float(row['hp'])
                count += 1
            
        
        write_file.write(f'Average hit point for Pokemons of stage 3.0 = {round(hp_total/count)}')

fire_type_percentage('pokemonTrain.csv', 'pokemon1.txt')
missing_NaN('pokemonTrain.csv', 'pokemonResult.csv')
personality_dict('pokemonResult.csv', 'pokemon4.txt')
stage3_avg_hp('pokemonResult.csv', 'pokemon5.txt')
