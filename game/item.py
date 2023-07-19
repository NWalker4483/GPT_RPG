import cv2
import numpy as np

from entity import Entity

class Item(Entity):
	def __init__(self, pos):
		# set item qualities
		self.name = "MISSING NAME";
		self.decription = "NO DESCRIPTION"
		self.stats = [0, 0, 0]; # HP, Attack, Agility

		# set visual qualities inside each item
		self.img = None;
		self.mask = None;
		self.layer = 3; # all items on 3rd layer

		super().__init__(pos, self.img, self.mask, self.layer);

	def getCopy(self, pos=None):
		if pos is None:
			pos = self.pos;
		copy_item = Item(pos);
		copy_item.name = self.name;
		copy_item.stats = self.stats[:];
		copy_item.img = np.copy(self.img);
		copy_item.mask = np.copy(self.mask);
		copy_item.layer = self.layer;
		return copy_item;

# credit: http://opengameart.org/content/dungeon-crawl-32x32-tiles
class Dagger(Item):
	def __init__(self, pos):
		super().__init__(pos);

		self.name = "Dagger";
		self.stats = [0, 1, 0];

		self.img = cv2.imread("Assets/Items/dagger.png");
		self.mask = cv2.inRange(self.img, (255,255,255), (255,255,255), cv2.THRESH_BINARY);
		self.mask = cv2.bitwise_not(self.mask);

		
class Sword(Item):
	def __init__(self, pos):
		super().__init__(pos);
		self.name = "Sword";
		self.stats = [0, 1, 0];

		self.img = cv2.imread("Assets/Items/sword.png");
		self.mask = cv2.inRange(self.img, (255,255,255), (255,255,255), cv2.THRESH_BINARY);
		self.mask = cv2.bitwise_not(self.mask);
  
class Shield(Item):
	def __init__(self, pos):
		super().__init__(pos)

		self.name = "Shield"
		self.stats = [0, 1, 0]

		self.img = cv2.imread("Assets/Items/shield.png");
		self.mask = cv2.inRange(self.img, (255,255,255), (255,255,255), cv2.THRESH_BINARY);
		self.mask = cv2.bitwise_not(self.mask);


class Potion(Item):
	def __init__(self, pos):
		super().__init__(pos);

		self.name = "Potion";
		self.stats = [0, 1, 0];

		self.img = cv2.imread("Assets/Items/potion.png");
		self.mask = cv2.inRange(self.img, (255,255,255), (255,255,255), cv2.THRESH_BINARY);
		self.mask = cv2.bitwise_not(self.mask);

if __name__ == "__main__":
	thing = Dagger((0,0));
	cv2.imshow("Thing", thing.mask);
	cv2.waitKey(0);