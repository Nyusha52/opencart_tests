from pages.catalog_page import CatalogPage


class TestCatalogPage:

    def test_count_goods(self, browser):
        catalog = CatalogPage(browser)
        catalog.get_url("/desktops/")
        count_goods = catalog.count_goods
        assert len(count_goods) <= 20

    def test_sort_goods_z_a(self, browser):
        lst = []
        sorted_lst = []
        catalog = CatalogPage(browser)
        catalog.get_url("/desktops/")
        goods = catalog.count_goods
        for i in range(len(goods)):
            lst.append(goods[i].text.lower())
        lst.sort(reverse=True)
        catalog.sort_goods_by_name()
        sorted_goods = catalog.sorted_goods
        for i in range(len(sorted_goods)):
            sorted_lst.append(sorted_goods[i].text.lower())
        assert lst == sorted_lst
