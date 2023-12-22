from gradio_client import Client

client = Client("https://phoughton-london-architecture.hf.space/--replicas/8r8d7/")
result = client.predict(
		"https://raw.githubusercontent.com/phoughton/london_architype/a646ed8efe35b2a5f1617e7531558ad3d797de9a/images/tudor_1.jpg",	# filepath  in 'the_image' Image component
							api_name="/predict"
)
print(result)