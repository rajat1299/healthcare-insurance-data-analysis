import scrapy

class InsuranceSpider(scrapy.Spider):
    name = "insurance"

    # List of URLs to scrape
    start_urls = [
        "https://example-insurance.com/plans"
    ]

    def parse(self, response):
        for plan in response.css("div.plan-card"):
            yield {
                "plan_name": plan.css("h2.plan-title::text").get(),
                "monthly_premium": plan.css("span.premium::text").get(),
                "deductible": plan.css("span.deductible::text").get(),
                "coverage_details": plan.css("p.coverage-details::text").get(),
            }

        # Follow pagination links
        next_page = response.css("a.next-page::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
