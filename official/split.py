import os
import hashlib


def split_file_to_chunk(file_path, split_size, chunk_dir):
	# calculate origin file md5
	with open(file_path, 'rb') as f:
		data = f.read()
		m = hashlib.md5()
		m.update(data)
		h = m.hexdigest()
		print(file_path, 'md5:', h)
		with open(os.path.join(chunk_dir, 'md5.txt'), 'w') as f2:
			f2.write(h)

	with open(file_path, 'rb') as f:
		chunk_id = 1
		chunk = f.read(split_size)
		while chunk:
			with open(os.path.join(chunk_dir, 'chunk', 'chunk_%d' %(chunk_id)), 'wb') as chunk_file:
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
	file_path = 'atlassian-jira-core-8.20.12.zip'
	chunk_dir = 'split'

	output_file_path = 'jira-core-9.0.0-merge.tar'

	split_file_to_chunk(file_path, split_size, chunk_dir)

	# merge_file_from_chunk(chunk_dir, output_file_path)