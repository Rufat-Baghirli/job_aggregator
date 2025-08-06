from abc import ABC, abstractmethod
from core.types import Job

class JobScraper(ABC):
    @abstractmethod
    def scrape(self) -> list[Job]:
        pass
