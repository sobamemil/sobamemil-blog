import os

POST_KO = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts/195-ha-diy-애터미-공기청정기-home-assistant-로컬-연동-방법-tuya-esp8.md"
POST_EN = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts/195-ha-diy-애터미-공기청정기-home-assistant-로컬-연동-방법-tuya-esp8.en.md"

YAML_SNIPPET = """    - name: "Atomy PM1.0"
      unique_id: atomy_pm1_0
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      unit_of_measurement: "µg/m³"
      device_class: pm1
      value_template: "{{ value_json.get('8') if value_json.get('8') is not none else value_json.get('20', {}).get('8') }}"

    - name: "Atomy PM2.5"
      unique_id: atomy_pm25
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      unit_of_measurement: "µg/m³"
      device_class: pm25
      value_template: "{{ value_json.get('10') if value_json.get('10') is not none else value_json.get('20', {}).get('10') }}"

    - name: "Atomy PM10"
      unique_id: atomy_pm10
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      unit_of_measurement: "µg/m³"
      device_class: pm10
      value_template: "{{ value_json.get('9') if value_json.get('9') is not none else value_json.get('20', {}).get('9') }}" """

for path in [POST_KO, POST_EN]:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update sensor definition block
        if 'name: "Atomy PM2.5"' in content:
            old_block = """    - name: "Atomy PM2.5"
      unique_id: atomy_pm25
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      unit_of_measurement: "µg/m³"
      device_class: pm25
      value_template: "{{ value_json.get('10') if value_json.get('10') is not none else value_json.get('20', {}).get('10') }}" """
            content = content.replace(old_block, YAML_SNIPPET)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated HA configuration YAML in blog posts with PM1.0, PM2.5, and PM10 entities!")
