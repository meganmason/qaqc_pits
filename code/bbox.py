# reference: https://techoverflow.net/2017/02/23/computing-bounding-box-for-a-list-of-coordinates-in-python/
import pandas as pd


class BoundingBox(object):
    """
    A 2D bounding box
    """
    def __init__(self, points):
        if len(points) == 0:
            raise ValueError("Can't compute bounding box of empty list")
        self.minx, self.miny = float("inf"), float("inf")
        self.maxx, self.maxy = float("-inf"), float("-inf")
        for x, y in points:
            # Set min coords
            if x < self.minx:
                self.minx = x
            if y < self.miny:
                self.miny = y
            # Set max coords
            if x > self.maxx:
                self.maxx = x
            if y > self.maxy: #had to modify (link has elif, but you want if)
                self.maxy = y
    @property
    def width(self):
        return self.maxx - self.minx
    @property
    def height(self):
        return self.maxy - self.miny
    def __repr__(self):
        return "BoundingBox({}, {}, {}, {})".format(
            self.minx, self.maxx, self.miny, self.maxy)

#initialize ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
c_list = []
df = pd.DataFrame(columns = ['Site', 'UL-lat', 'UL-lon', 'LR-lat', 'LR-lon'])

#sites ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

site = 'American River' #repeat coords and it works...
coords = [(38.71029, -120.04186),
          (38.71029, -120.04186)]

bbox = BoundingBox(coords)
c_list.append("{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))
df = df.append({
'Site':site, 'UL-lat':bbox.minx,
'UL-lon':bbox.miny,
'LR-lat':bbox.maxx,
'LR-lon':bbox.maxy},
ignore_index=True)
print("\n{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))

site = 'Mammoth Lakes'
coords = [(37.64324, -119.02906),
          (37.61963, -119.00030)]

bbox = BoundingBox(coords)
c_list.append("{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))
df = df.append({
'Site':site, 'UL-lat':bbox.minx,
'UL-lon':bbox.miny,
'LR-lat':bbox.maxx,
'LR-lon':bbox.maxy},
ignore_index=True)
print("\n{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))

site = 'Sagehen'
coords = [(39.42955, -120.24210),
          (39.43037, -120.23982),
          (39.42216, -120.29898)]

bbox = BoundingBox(coords)
c_list.append("{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))
df = df.append({
'Site':site, 'UL-lat':bbox.minx,
'UL-lon':bbox.miny,
'LR-lat':bbox.maxx,
'LR-lon':bbox.maxy},
ignore_index=True)
print("\n{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))

site = 'Cameron Pass'
coords = [(40.52406, -105.89345),
          (40.51865, -105.89197)]

bbox = BoundingBox(coords)
c_list.append("{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))
df = df.append({
'Site':site, 'UL-lat':bbox.minx,
'UL-lon':bbox.miny,
'LR-lat':bbox.maxx,
'LR-lon':bbox.maxy},
ignore_index=True)
print("\n{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))

site = 'Fraser'
coords = [(39.90556, -105.88281),
          (39.90612, -105.88255),
          (39.90697, -105.87783),
          (39.90703, -105.87904)]

bbox = BoundingBox(coords)
c_list.append("{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))
df = df.append({
'Site':site, 'UL-lat':bbox.minx,
'UL-lon':bbox.miny,
'LR-lat':bbox.maxx,
'LR-lon':bbox.maxy},
ignore_index=True)
print("\n{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))

site = 'Grand Mesa'
coords = [(39.03053, -108.03217),
          (39.03223, -108.03431),
          (39.04415, -108.06202),
          (39.04494, -108.06313)]

bbox = BoundingBox(coords)
c_list.append("{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))
df = df.append({
'Site':site, 'UL-lat':bbox.minx,
'UL-lon':bbox.miny,
'LR-lat':bbox.maxx,
'LR-lon':bbox.maxy},
ignore_index=True)
print("\n{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))

site = 'Niwot Ridge'
coords = [(40.03317, -105.54616),
          (40.05497, -105.59065)]

bbox = BoundingBox(coords)
c_list.append("{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))
df = df.append({
'Site':site, 'UL-lat':bbox.minx,
'UL-lon':bbox.miny,
'LR-lat':bbox.maxx,
'LR-lon':bbox.maxy},
ignore_index=True)
print("\n{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))

site = 'Senator Beck'
coords = [(37.90714, -107.71121),
          (37.90705, -107.72626)]

bbox = BoundingBox(coords)
c_list.append("{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))
df = df.append({
'Site':site, 'UL-lat':bbox.minx,
'UL-lon':bbox.miny,
'LR-lat':bbox.maxx,
'LR-lon':bbox.maxy},
ignore_index=True)
print("\n{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))

site = 'Upper Gunnison'
coords = [(38.95925, -106.99053),
          (38.88812, -107.10796)]

bbox = BoundingBox(coords)
c_list.append("{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))
df = df.append({
'Site':site, 'UL-lat':bbox.minx,
'UL-lon':bbox.miny,
'LR-lat':bbox.maxx,
'LR-lon':bbox.maxy},
ignore_index=True)
print("\n{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))

site = 'Boise River'
coords = [(44.30455, -115.23605),
          (44.30362, -115.23456),
          (43.75884, -116.09017),
          (43.73703, -116.12185),
          (43.73634, -116.12053),
          (43.94735, -115.67666)]

bbox = BoundingBox(coords)
c_list.append("{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))
df = df.append({
'Site':site, 'UL-lat':bbox.minx,
'UL-lon':bbox.miny,
'LR-lat':bbox.maxx,
'LR-lon':bbox.maxy},
ignore_index=True)
print("\n{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))

site = 'Jemez River'
coords = [(35.88859, -106.53184),
          (35.85794, -106.52137)]

bbox = BoundingBox(coords)
c_list.append("{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))
df = df.append({
'Site':site, 'UL-lat':bbox.minx,
'UL-lon':bbox.miny,
'LR-lat':bbox.maxx,
'LR-lon':bbox.maxy},
ignore_index=True)
print("\n{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))


site = 'Little Cottonwood'
coords = [(40.57210, -111.62997),
          (40.59125, -111.63759)]

bbox = BoundingBox(coords)
c_list.append("{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))
df = df.append({
'Site':site, 'UL-lat':bbox.minx,
'UL-lon':bbox.miny,
'LR-lat':bbox.maxx,
'LR-lon':bbox.maxy},
ignore_index=True)
print("\n{}: (UL) {}, {}, (LR) {}, {};".
format(site, bbox.minx, bbox.miny, bbox.maxx, bbox.maxy))

# finsih ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for line in c_list:
    print(line)

df.to_csv('../bbox.csv', sep=',', header=True)

print('done!')
