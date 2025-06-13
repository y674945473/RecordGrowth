import requests
from bs4 import BeautifulSoup
import time
import csv

# 配置请求头模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

def get_product_info(url):
    """获取单个商品信息"""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查HTTP错误
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 示例解析逻辑（需根据实际网页结构调整）
        product_name = soup.find('h1', class_='product-title').text.strip()
        price = soup.find('span', class_='price').text.strip()
        rating = soup.find('div', class_='product-rating').get('data-score', 'N/A')
        
        return {
            'name': product_name,
            'price': price,
            'rating': rating,
            'url': url
        }
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")
        return None

def crawl_category(base_url, pages=3):
    """爬取分类页商品列表"""
    products = []
    for page in range(1, pages+1):
        url = f"{base_url}?page={page}"
        print(f"正在抓取第 {page} 页: {url}")
        
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 提取商品链接（示例选择器）
            product_links = soup.select('a.product-link')
            for link in product_links:
                product_url = link['href']
                if not product_url.startswith('http'):
                    product_url = base_url + product_url
                product_data = get_product_info(product_url)
                if product_data:
                    products.append(product_data)
                time.sleep(1)  # 请求间隔防止被封
                
        except Exception as e:
            print(f"页面抓取失败: {str(e)}")
        
        time.sleep(2)  # 页面间延迟
    
    return products


def save_to_csv(data, filename):
    """保存数据到CSV文件"""
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    # 示例使用（需替换实际URL）
    base_url = "https://example-store.com/category/electronics"
    products_data = crawl_category(base_url, pages=2)
    
    if products_data:
        save_to_csv(products_data, 'products.csv')
        print(f"成功抓取 {len(products_data)} 条数据")
    else:
        print("未抓取到有效数据")