from pages.catalog_page import CatalogPage


class TestCatalogPage:
    def test_count_goods(self, browser):
        browser.get(browser.base_url + "/desktops/")
        count_goods = browser.find_elements(*CatalogPage.COUNT)
        assert len(count_goods) <= 20

    def test_sort_goods_z_a(self, browser):
        lst = []
        sorted_lst = []
        browser.get(browser.base_url + "/desktops/")
        goods = browser.find_elements(*CatalogPage.COUNT)
        for i in range(len(goods)):
            lst.append(goods[i].text.lower())
        lst.sort(reverse=True)
        browser.find_element(*CatalogPage.SORT).click()
        browser.find_element(*CatalogPage.SORT_NAME_DESC).click()
        sorted_goods = browser.find_elements(*CatalogPage.COUNT)
        for i in range(len(sorted_goods)):
            sorted_lst.append(sorted_goods[i].text.lower())
        assert lst == sorted_lst
