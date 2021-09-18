from Vector3 import Vector3, UnitVectorRequiredError
import math
import matplotlib.pyplot as plt

# ALL ANGLES ARE ASSUMED TO BE IN RADIANS

SOLAR_FLUX = 1361 # In W / m^2
CELL_EFFICIENCY = 0.29
THERMAL_EFFICIENCY = 0.001 # / degrees Celsius
BATTERY_EFFICIENCY = 0.85
MAX_OPERATING_TEMPERATURE = 40 # In degrees Celsius
AREA_EFFICIENCY = 0.8


ECLIPSE_TIME = 0
ANNUAL_DEGRADATION = 0.03 # Per year
ELAPSED_MISSION_YEARS = 0 # In years

# Area should be in m^2
def get_generated_power_for_face(normal_face_vector, sun_incidence_vec, area):
  if abs(normal_face_vector.norm2() - 1) > 0.0001:
    raise UnitVectorRequiredError("Normal face vector must be a unit vector!")
  if abs(sun_incidence_vec.norm2() -1) > 0.0001:
    raise UnitVectorRequiredError("Sun incidence vector must be a unit vector!")
  vector_angle = math.acos(Vector3.dot_product(normal_face_vector, sun_incidence_vec))
  
  if vector_angle < math.pi/2: # The sun isn't hitting this face of the satellite
    return 0
  
  else:
    incidence_angle = math.pi - vector_angle
    power_generated = SOLAR_FLUX * (1-ECLIPSE_TIME)*1000 * area * BATTERY_EFFICIENCY * (CELL_EFFICIENCY-THERMAL_EFFICIENCY*MAX_OPERATING_TEMPERATURE) * math.cos(incidence_angle) * AREA_EFFICIENCY / (1+ANNUAL_DEGRADATION*ELAPSED_MISSION_YEARS)
    # print("Captured energy: " + str(power_generated))
    return power_generated

def main():
  # Using readline()
  file1 = open('BodyData.txt', 'r')
  count = 0
  line = file1.readline() # Ignore file headers

  captured_energies = []
  elapsed_days = []

  print('Calculating captured energy...')
  while True:
      count += 1
  
      # Get next line from file
      line = file1.readline().split(' ')
      if not line or len(line) < 12:
          break

      line_vals = [float(word) for word in line if len(word) > 0 and word != '\n']

      sat_position = Vector3(line_vals[3], line_vals[4], line_vals[5])
      sun_position = Vector3(line_vals[6], line_vals[7], line_vals[8])
      moon_position = Vector3(line_vals[9], line_vals[10], line_vals[11])

      sun_sat_vec = Vector3.normalize(sat_position - sun_position)

      sat_moon_vec = Vector3.normalize(moon_position - sat_position)

      total_captured_energy = 0

      face1 = sat_moon_vec
      face2 = -sat_moon_vec
      face3 = Vector3.normalize(Vector3(sat_moon_vec.y - sat_moon_vec.z, -sat_moon_vec.x + sat_moon_vec.z, sat_moon_vec.x - sat_moon_vec.y)) # 𝑏−𝑐,−𝑎+𝑐,𝑎−𝑏)
      face4 = -face3
      face5 = Vector3.normalize(Vector3.cross_product(face1, face3))
      face6 = -face5

      # total_captured_energy += get_generated_power_for_face(face1, sun_sat_vec, 0.01)
      total_captured_energy += get_generated_power_for_face(face2, sun_sat_vec, 0.01)
      total_captured_energy += get_generated_power_for_face(face3, sun_sat_vec, 0.03)
      total_captured_energy += get_generated_power_for_face(face3, sun_sat_vec, 0.03)
      total_captured_energy += get_generated_power_for_face(face3, sun_sat_vec, 0.03)
      total_captured_energy += get_generated_power_for_face(face4, sun_sat_vec, 0.03)
      total_captured_energy += get_generated_power_for_face(face5, sun_sat_vec, 0.03)
      total_captured_energy += get_generated_power_for_face(face6, sun_sat_vec, 0.03)

      captured_energies.append(total_captured_energy)
      elapsed_days.append(count * 0.004942076)

  average_energy = sum(captured_energies) / len(captured_energies)
  print('Calculation complete! Average energy was ' + str(average_energy) + 'mW. generating plot...')

  plt.plot(elapsed_days, captured_energies)
  plt.ylabel('Potencia capturada [mW]')
  plt.xlabel('Día de la misión')
  plt.title('Energia promedio:' + str(average_energy) + 'mW')
  plt.show()
  file1.close()




if __name__ == "__main__":
    main()
