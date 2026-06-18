class TreeNode:
    """
    Representasi node pada Binary Search Tree.
    Setiap node menyimpan objek Product dan referensi ke anak kiri/kanan.
    """
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None

class PriceBST:
    """
    Struktur data Binary Search Tree khusus untuk mengindeks harga produk.
    Kiri: Harga lebih murah. Kanan: Harga lebih mahal atau sama.
    """
    def __init__(self):
        self.root = None

    def insert(self, product):
        """Memasukkan produk ke dalam BST berdasarkan harga."""
        if not self.root:
            self.root = TreeNode(product)
        else:
            self._insert_recursive(self.root, product)

    def _insert_recursive(self, node, product):
        # Jika harga lebih murah, masukkan ke sub-tree kiri
        if product.harga < node.product.harga:
            if node.left is None:
                node.left = TreeNode(product)
            else:
                self._insert_recursive(node.left, product)
        # Jika harga lebih mahal atau SAMA, masukkan ke sub-tree kanan
        else:
            if node.right is None:
                node.right = TreeNode(product)
            else:
                self._insert_recursive(node.right, product)

    def search_by_price_range(self, min_price, max_price):
        """
        Mencari produk dalam rentang harga menggunakan In-Order Traversal.
        Mengembalikan list berisi produk yang terurut dari harga termurah.
        """
        result = []
        self._range_search_recursive(self.root, min_price, max_price, result)
        return result

    def _range_search_recursive(self, node, min_price, max_price, result):
        if node is None:
            return

        # OPTIMASI: Hanya telusuri cabang kiri jika harga minimal masih lebih kecil 
        # dari harga node saat ini (memotong cabang yang tidak relevan)
        if min_price < node.product.harga:
            self._range_search_recursive(node.left, min_price, max_price, result)

        # IN-ORDER TRAVERSAL: Proses node saat ini jika masuk dalam rentang harga
        if min_price <= node.product.harga <= max_price:
            result.append(node.product)

        # OPTIMASI: Hanya telusuri cabang kanan jika harga maksimal masih lebih besar 
        # dari harga node saat ini
        if max_price >= node.product.harga:
            self._range_search_recursive(node.right, min_price, max_price, result)