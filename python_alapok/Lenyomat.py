import hashlib


def lenyomat(str_):
	h=hashlib.sha256(str_.encode())
	return h.hexdigest()


if __name__ == "__main__":
	print("This is a haslib test.")

	s="alma"
	print(s," = ",lenyomat(s))
	s="korte"
	print(s," = ",lenyomat(s))


