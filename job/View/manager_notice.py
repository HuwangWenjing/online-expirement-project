from job.models import notice
from job.serializers import NoticeSer
from rest_framework.views import APIView, Response
from job.views import m_chk_token


class get_notice_list(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN')

        ma_id = m_chk_token(token)
        if isinstance(ma_id, Response):
            return ma_id

        notice_list = notice.objects.all()

        return Response({
            'info': 'success',
            'code': 200,
            'data': NoticeSer(notice_list, many=True).data
        }, status=200)


class add_notice(APIView):
    def post(self, request):
        token = request.META.get('HTTP_TOKEN')
        title = request.POST.get('title')
        content = request.POST.get('content')
        pubtime = request.POST.get('pubtime')

        ma_id = m_chk_token(token)
        if isinstance(ma_id, Response):
            return ma_id

        create_notice = notice.objects.create(
            Title=title,
            Content=content,
            PubTime=pubtime
        )

        all_notice = notice.objects.all()

        return Response({
            'info': 'success',
            'code': 200,
            'data': NoticeSer(all_notice).data
        }, status=200)


class modify_notice(APIView):
    def post(self, request):
        token = request.META.get('HTTP_TOKEN')
        notice_id = request.GET.get('notice_id')
        new_title = request.POST.get('new_title')
        new_content = request.POST.get('new_content')

        ma_id = m_chk_token(token)
        if isinstance(ma_id, Response):
            return ma_id

        update_notice = notice.objects.get(pk=notice_id)
        update_notice.Title = new_title
        update_notice.Content = new_content
        update_notice.save()

        all_notice = notice.objects.all()

        return Response({
            'info': 'success',
            'code': 200,
            'data': NoticeSer(all_notice).data
        }, status=200)


class delete_notice(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN')
        notice_id = request.GET.get('notice_id')

        ma_id = m_chk_token(token)
        if isinstance(ma_id, Response):
            return ma_id

        n = notice.objects.get(pk=notice_id)
        n.delete()

        return Response({
            'info': 'success',
            'code': 200,
            'data': NoticeSer(n).data
        }, status=200)