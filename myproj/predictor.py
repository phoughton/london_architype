from gradio_client import Client

client = Client("https://phoughton-london-architecture.hf.space/--replicas/8r8d7/")
result = client.predict(
		https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png,	# filepath  in 'the_image' Image component
							api_name="/predict"
)
print(result)