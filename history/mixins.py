from .signals import object_viewed_signal

class ObjectViewMixin:
    def dispatch(self, request, *args, **kwargs):
        # try:
        
        
        # except self.model.DoesNotExist:
        #     instance = None
        
        if request.user.is_authenticated :
            object_viewed_signal.send(sender = self.__class__, request=request)

        return super(ObjectViewMixin, self).dispatch(request, *args, **kwargs)