import heapq

# =====================================================
# GRAPH + ALGORITMA DIJKSTRA
# =====================================================

class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_rute(self, kota_asal: str, kota_tujuan: str, jarak: int):
        if kota_asal not in self.graph:
            self.graph[kota_asal] = []
        if kota_tujuan not in self.graph:
            self.graph[kota_tujuan] = []
        
        self.graph[kota_asal].append((kota_tujuan, jarak))
        self.graph[kota_tujuan].append((kota_asal, jarak))

    def dijkstra(self, start: str, end: str):
        if start not in self.graph or end not in self.graph:
            return float('inf'), []
        
        pq = [(0, start, [start])]
        jarak_terpendek = {kota: float('inf') for kota in self.graph}
        jarak_terpendek[start] = 0
        
        while pq:
            jarak_sekarang, kota_sekarang, jalur = heapq.heappop(pq)
            
            if kota_sekarang == end:
                return jarak_sekarang, jalur
            
            if jarak_sekarang > jarak_terpendek[kota_sekarang]:
                continue
                
            for tetangga, bobot in self.graph[kota_sekarang]:
                jarak_baru = jarak_sekarang + bobot
                if jarak_baru < jarak_terpendek[tetangga]:
                    jarak_terpendek[tetangga] = jarak_baru
                    heapq.heappush(pq, (jarak_baru, tetangga, jalur + [tetangga]))
        
        return float('inf'), []