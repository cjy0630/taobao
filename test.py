from requests_html import HTMLSession

if __name__ == '__main__':
    DEFAULT_REQUEST_HEADERS = {
        'cookie': 'cna=eRpfFSQ/oFgCAXL1PV77YkyL; t=36778dd604d00ba8001dc47d6bd9e818; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; miid=232293011727815606; uc3=vt3=F8dBy3jc5SHqWSQOuw8%3D&id2=UUkGUYyXZqM%3D&nk2=AHDYax8iWw%3D%3D&lg2=UtASsssmOIJ0bQ%3D%3D; tracknick=cjy0630; lgc=cjy0630; _cc_=UtASsssmfA%3D%3D; tg=0; enc=EfNORQXAfCl2iPKt2ZTQMxqEIERzhz1%2BWrD39ZSYuQ%2FhIEs0l%2BSYiZWsTe8QtNwRHPmZjBa7lKw8zk1ZruGXpA%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; mt=ci=-1_0; cookie2=1af4f1f6d46f0437e1ba4320b2c63fcc; _tb_token_=ee383b785e71; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; swfstore=292025; JSESSIONID=6C307E79FD7803439D7E5A5C7CA88885; uc1=cookie14=UoTaGqymsIcsiA%3D%3D; isg=BFhY9M-6sSemBJxb3i7K7eMpKYYq6dnJyFFr0pJLrBJ4LfsXOlUfWyrPZSW4PXSj; l=bBNxpH8ev5OF57KQBOfwquI8S87toQAbzsPzw4GXGIB1tQ13QdQHmHwQG3Z9I3Q_E_fQ9etPjJDd8REpyizKg',
        'referer': 'https://detail.tmall.com/item.htm?spm=a230r.1.14.1.5219103aCuWjV1&id=595949445810&cm_id=140105335569ed55e27b&abbucket=17'
    }

    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=595949445810&sellerId=726984974&currentPage=2'
    session = HTMLSession()
    html = session.get(url, headers=DEFAULT_REQUEST_HEADERS, verify=False)

    print(type(html.text))

    print(html.text)
