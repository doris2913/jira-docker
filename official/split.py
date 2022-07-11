import os



def split_file_to_chunk(file_path, split_size, chunk_dir):
	with open(file_path, 'rb') as f:
		chunk_id = 1
		chunk = f.read(split_size)
		while chunk:
			with open(os.path.join(chunk_dir, 'chunk_%d' %(chunk_id)), 'wb') as chunk_file:
				chunk_file.write(chunk)
			chunk_id += 1
			chunk = f.read(split_size)


def merge_file_from_chunk(chunk_dir, output_file_path):
	chunks = []
	for chunk_id in range(1, 21):
		print(chunk_id)
		with open(os.path.join(chunk_dir, 'chunk_%d'%(chunk_id)), 'rb') as f:
			chunk = f.read()
			chunks.append(chunk)

	file_content = b''.join(chunks)
	with open(output_file_path, 'wb') as f:
		f.write(file_content)


if __name__ == '__main__':
	split_size = 50 * 1024 * 1024
	file_path = 'jira-core-9.0.0.tar'
	chunk_dir = 'split'

	output_file_path = 'jira-core-9.0.0-merge.tar'

	# split_file_to_chunk(file_path, split_size, chunk_dir)

	merge_file_from_chunk(chunk_dir, output_file_path)