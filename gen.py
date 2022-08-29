import json, random

triangle = {"name": "Triangle",
        "num_points": 3,
        "points": [
            0,
            1,
            0.5,
            0,
            1,
            1
        ],
        "powers": [
            0,
            0,
            0
        ],
        "smooth": False
        }
    
saw = {"name": "Saw Up",
        "num_points": 3,
        "points": [
            0,
            1,
            1,
            0,
            1,
            1
        ],
        "powers": [
            0,
            0,
            0
        ],
        "smooth": False
        }
        
sin = {"name": "Sin",
        "num_points": 3,
        "points": [
            0,
            1,
            0.5,
            0,
            1,
            1
        ],
        "powers": [
            0,
            0,
            0
        ],
        "smooth": True
        }
    
j = open('config.json', 'r')
config = json.load(j)
j.close()

name = input('Please enter name of preset:\n>>>')
while True:
    with open(f'{name}.vital', 'r+') as f:
        data = json.load(f)
        data['settings']["osc_3_wave_frame"] = float(random.randint(0, 256))
        data['settings']["osc_2_wave_frame"] = float(random.randint(0, 256))
        data['settings']["osc_1_wave_frame"] = float(random.randint(0, 256))

        if(config['Unison']):
            data['settings']['osc_1_unison_voices'] = random.choice([float(random.randint(1, 16)), 0.0])
            data['settings']['osc_2_unison_voices'] = random.choice([float(random.randint(1, 16)), 0.0])
            data['settings']['osc_3_unison_voices'] = random.choice([float(random.randint(1, 16)), 0.0])

            data['settings']['osc_1_unison_detune'] = float(random.randint(1, 5)) + 0.4721360206604
            data['settings']['osc_2_unison_detune'] = float(random.randint(1, 5)) + 0.4721360206604
            data['settings']['osc_3_unison_detune'] = float(random.randint(1, 5)) + 0.4721360206604

        if(config['Filter']):
            data['settings']['osc_1_destination'] = random.choice([0, 1, 3])
            data['settings']['osc_2_destination'] = random.choice([0, 1, 3])
            data['settings']['osc_3_destination'] = random.choice([0, 1, 3])

        data['settings']['osc_2_on'] = random.choice([1, 1, 0])
        data['settings']['osc_3_on'] = random.choice([1, 0])

        data['settings']['osc_1_level'] = random.choice([1.0, 0.7, random.random()])
        data['settings']['osc_2_level'] = random.choice([1.0, 0.7, random.random()])
        data['settings']['osc_3_level'] = random.choice([1.0, 0.7, random.random()])



        if(config['Filter']):
            data['settings']['filter_1_cutoff'] = random.randint(8, 136)
            data['settings']['filter_1_resonance'] = random.random()
            data['settings']['filter_1_blend'] = random.random()*2

            data['settings']['filter_2_cutoff'] = random.randint(8, 136)
            data['settings']['filter_2_resonance'] = random.random()
            data['settings']['filter_2_blend'] = random.random()*2


            if(config['Filter_LFO']):
                data['settings']['modulations'][0]['destination'] = random.choice(['filter_1_cutoff', 'filter_1_resonance', ''])
                data['settings']['modulation_1_amount'] = (random.random()*2)-1
                data['settings']['modulations'][0]['source'] = 'lfo_1'

                data['settings']['modulations'][1]['destination'] = random.choice(['filter_2_cutoff', 'filter_2_resonance', ''])
                data['settings']['modulation_2_amount'] = (random.random()*2)-1
                data['settings']['modulations'][1]['source'] = 'lfo_2'


                data['settings']['lfo_1_tempo'] = random.randint(6, 9)
                data['settings']['lfo_2_tempo'] = random.randint(6, 9)

                data['settings']['lfos'][0] = random.choice([saw, sin, triangle])
                data['settings']['lfos'][1] = random.choice([saw, sin, triangle])


        data['settings']['effect_chain_order'] = 45

        if(config['Distortion']):
            data['settings']['distortion_on'] = random.choice([0, 1])
            data['settings']['distortion_drive'] = random.randint(0, 20)

        if(config['Delay']):
            data['settings']['delay_on'] = random.choice([0, 1])
            data['settings']['delay_tempo'] = random.randint(8, 10)
        
        if(config['Reverb']):
            data['settings']['reverb_on'] = random.choice([0, 1])
            data['settings']['reverb_dry_wet'] = random.random()
            data['settings']['reverb_size'] = random.random()/2
            data['settings']['reverb_decay_time'] = random.randint(-8, 10)/10


        data['settings']['env_1_attack'] = random.randint(1, 50)/100
        data['settings']['env_1_release'] = random.randint(1, 150)/100


        if(config['FM']):
            data['settings']['osc_1_distortion_type'] = 0
            data['settings']['osc_1_distortion_amount'] = 0.5
            data['settings']['osc_1_transpose'] = 0

            data['settings']['osc_2_distortion_type'] = 0
            data['settings']['osc_2_distortion_amount'] = 0.5
            data['settings']['osc_2_transpose'] = 0

            data['settings']['osc_3_distortion_type'] = 0
            data['settings']['osc_3_distortion_amount'] = 0.5
            data['settings']['osc_3_transpose'] = 0
            
            if(random.randint(0, 2)==1):
                n = [1, 2, 3]
                o1 = random.randint(1, 3)
                n.pop(n.index(o1))
                o = random.randint(0, 1)
                data['settings'][f'osc_{o1}_distortion_type'] = o+7

                data['settings'][f'osc_{n[o]}_level'] = 0
                data['settings'][f'osc_{n[o]}_on'] = 1
                if(random.randint(0, 1)==0):
                    data['settings'][f'osc_{n[o]}_transpose'] = random.randint(-36, 36)

                data['settings'][f'osc_{o1}_on'] = 1
                data['settings'][f'osc_{o1}_distortion_amount'] = random.random()/2+0.5

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        f.close()
    input('Enter to generate again')