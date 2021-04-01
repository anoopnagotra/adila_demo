from django.core.paginator import Paginator
from .filters import serialize_valued_numbers, serialize_valued_admin_numbers


class VIPNumberPaginator(Paginator):

    def __init__(self, object_list, per_page, my_wishlist_number, shuffle=False, orphans=0, allow_empty_first_page=True):
        super().__init__(object_list, per_page, orphans, allow_empty_first_page)
        self.my_wishlist_number = my_wishlist_number
        self.serializer = self.get_serializer()
        self.prefix = self.get_prefix()
        self.shuffle = shuffle

    def page(self, number):
        """Return a Page object for the given 1-based page number."""
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        if top + self.orphans >= self.count:
            top = self.count
        if self.shuffle:
            self.object_list = self.object_list.order_by('?')
        self.object_list = self.get_object_values_list()[bottom:top]
        self.object_list = self.serializer(self.object_list, self.my_wishlist_number, prefix=self.prefix)
        return self._get_page(self.object_list, number, self)

    def get_object_values_list(self):
        return self.object_list.values(
            self.prefix + 'id', self.prefix + 'display_number', self.prefix + 'selling_price', self.prefix + 'selling_price',
            self.prefix + 'total_views', self.prefix + 'total_likes', self.prefix + 'number_total', self.prefix + 'number_sum',
            self.prefix + 'rtp', self.prefix + 'user__premium_seller_tag',
            self.prefix + 'user__seller_rating', self.prefix + 'user__is_premium', self.prefix + 'cod')

    def get_serializer(self):
        return serialize_valued_numbers

    def get_prefix(self):
        return ''


class VIPCategoryNumberPaginator(VIPNumberPaginator):

    def get_prefix(self):
        return 'number__'



class VIPNumberAdminPaginator(Paginator):

    def __init__(self, object_list, per_page, my_wishlist_number, shuffle=False, category_tags=False, orphans=0, allow_empty_first_page=True):
        super().__init__(object_list, per_page, orphans, allow_empty_first_page)
        self.my_wishlist_number = my_wishlist_number
        self.serializer = self.get_serializer()
        self.prefix = self.get_prefix()
        self.shuffle = shuffle
        self.category_tags = category_tags

    def page(self, number):
        """Return a Page object for the given 1-based page number."""
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        if top + self.orphans >= self.count:
            top = self.count
        
        self.object_list = self.get_object_values_list()[bottom:top]
        self.object_list = self.serializer(self.object_list, self.my_wishlist_number, prefix=self.prefix, category_tags=self.category_tags)
        return self._get_page(self.object_list, number, self)

    def get_object_values_list(self):
        return self.object_list.values(
            self.prefix + 'id', self.prefix + 'display_number', self.prefix + 'selling_price', self.prefix + 'selling_price',
            self.prefix + 'total_views', self.prefix + 'total_likes', self.prefix + 'number_total', self.prefix + 'number_sum',
            self.prefix + 'rtp', self.prefix + 'user__premium_seller_tag',
            self.prefix + 'user__seller_rating', self.prefix + 'user__is_premium', self.prefix + 'cod', self.prefix + 'user__name', self.prefix + 'group_number',self.prefix + 'created_at')

    def get_serializer(self):
        return serialize_valued_admin_numbers

    def get_prefix(self):
        return ''

