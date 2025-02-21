import yaml
import xml.etree.ElementTree as xml_tree

# Opening the YAML file
with open('test.yaml', 'r') as file:
    # Properly load the YAML file using safe_load
    yaml_data = yaml.safe_load(file)

    rss_element = xml_tree.Element('rss', {
        'version':'2.0'})
    channel_element = xml_tree.SubElement(rss_element, 'channel')
    xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
    xml_tree.SubElement(channel_element, 'url').text = yaml_data['url']
    xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']

    cta_element = xml_tree.SubElement(channel_element, 'cta')
    hash_element = xml_tree.SubElement(channel_element, 'cta')

    xml_tree.SubElement(cta_element, 'text').text = yaml_data['cta']
    xml_tree.SubElement(cta_element, 'url').text = yaml_data['cta_url']

    for tag in yaml_data['hashtags']:
        xml_tree.SubElement(hash_element, 'tag').text = tag
    
    xml_tree.SubElement(channel_element, 'link').text = yaml_data['link']

    latest = xml_tree.SubElement(channel_element, 'latest_video')
    xml_tree.SubElement(latest, 'title').text = yaml_data['latest_video']['title']
    xml_tree.SubElement(latest, 'url').text = yaml_data['latest_video']['url']

    output_tree = xml_tree.ElementTree(rss_element)
    output_tree.write('youtube.xml', encoding='UTF-8', xml_declaration=True)
