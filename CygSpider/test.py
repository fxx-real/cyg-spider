from scrapy.selector import Selector

content = '''
<html lang="en"><head>
	<meta charset="utf-8">
	<meta name="keywords" content="畅易阁，changyige， 线下交易， 畅游官方，天龙八部畅易阁，天龙畅易阁，畅易阁官网， daoju，daojufang，道具，道具坊，道具购买，道具商城，搜狐畅游，游戏商城，天龙八部，斗破苍穹，鹿鼎记，刀剑英雄，新水浒Q传，暗影之剑、新天龙、竞拍，特惠，打折，促销，免费，优惠，特价，官方，活动，抽奖，积分，畅游币，元宝，畅游点，充值，扣点、C2C、B2C、WEB商城、web商城">
	<meta name="description" content="畅易阁道具坊：搜狐畅游官方道具销售及官方线下交易平台，每一笔交易都与游戏数据对应,支持多种支付方式，该平台提供旗下全部游戏的道具销售。在这个平台上，玩家可以享受到各式各样的价格优惠，并参加丰富多彩的游戏促销活动，全部交易由官方提供安全保证。畅易阁道具坊的目标是成为玩家国内最安全、最权威、服务最完善的网络游戏交易平台。">
	<meta name="viewport" content="width=device-width">
    <meta name="renderer" content="webkit">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <link href="http://public.npt.changyou.com/assets/img/common/bitbug_favicon.ico" type="image/x-icon" rel="icon">
    <link rel="stylesheet" type="text/css" href="http://public.npt.changyou.com/assets/css/site.css">
    <script>
        window.gameListfromServer= [{"id":1,"platformId":1,"platform":"畅游天下","gameId":16,"gameName":"新水浒Q传","gameAbbrName":"xsh","logo":"","vendor":"畅游","gameType":1,"createTime":"2014-08-22 11:57:52","authKey":"","status":1,"crossServer":0,"gameInfor":"新水浒Q传","weight":0,"statusText":"已激活","gameTypeText":"端游","crossServerText":"不支持"},{"id":2,"platformId":1,"platform":"畅游天下","gameId":3,"gameName":"天龙八部","gameAbbrName":"tl","logo":"","vendor":"畅游","gameType":1,"createTime":"2014-08-22 11:59:20","authKey":"","status":1,"crossServer":0,"gameInfor":"新天龙八部","weight":0,"statusText":"已激活","gameTypeText":"端游","crossServerText":"不支持"},{"id":13,"platformId":1,"platform":"畅游天下","gameId":2,"gameName":"刀剑英雄","gameAbbrName":"dj","logo":"无","vendor":"畅游","gameType":1,"createTime":"1970-01-01 00:00:00","authKey":" 无","status":1,"crossServer":0,"gameInfor":"刀剑英雄","weight":0,"statusText":"已激活","gameTypeText":"端游","crossServerText":"不支持"}];
        window.formToken = "";
        window.publicPath = "http://public.npt.changyou.com/";
        window.imagePath = "http://public.npt.changyou.com";
        window.assetsPath = "http://public.npt.changyou.com/assets/";
        window.production = true;
        window.curVersion = "1.1.14";

        function AddFavorite(sURL, sTitle){
            try{
                window.external.addFavorite(sURL, sTitle);
            }
            catch(e){
                try{
                    window.sidebar.addPanel(sTitle, sURL, "");
                }
                catch(e){
                    alert("收藏网站失败，请使用Ctrl+D进行添加");
                };
            };
        };
        window.imgError = function(obj,width){
            if(width){
                obj.src = publicPath + "assets/img/common/none"+width+".jpg";
            }else{
                obj.src = publicPath + "assets/img/common/none160.jpg";
            }
        }

        //声明_czc对象，CNZZ自定义事件预配置。
        var _czc = _czc || [];
        //绑定siteid，请用您的siteid替换下方"XXXXXXXX"部分
        _czc.push(["_setAccount", "5373220"]);
    </script>

    <!--[if lt IE 9]>
        <script src="http://public.npt.changyou.com/assets/js/vendor/html5.js" type="text/javascript"></script>
    <![endif]-->
    <!--[if IE 6]>
        <script src="http://public.npt.changyou.com/assets/js/vendor/DD_belatedPNG.js" type="text/javascript"></script>
    <![endif]-->
	
		<link type="text/css" rel="stylesheet" href="http://public.npt.changyou.com/assets/css/modules/list.css?v=1.1.14">
	
		<title>畅易阁网游交易平台|角色交易|装备交易|游戏币交易|畅游官方合作交易平台</title>
<style>.arale-dialog-1_3_0 .ui-dialog{background-color:rgba(0,0,0,.5);border:0;FILTER:progid:DXImageTransform.Microsoft.Gradient(startColorstr=#88000000, endColorstr=#88000000);padding:6px;outline:0}.arale-dialog-1_3_0 .ui-dialog-content{background:#fff}:root .arale-dialog-1_3_0 .ui-dialog{FILTER:none\9}.arale-dialog-1_3_0 .ui-dialog-close{color:#999;cursor:pointer;display:block;font-family:tahoma;font-size:24px;font-weight:700;height:18px;line-height:14px;position:absolute;right:16px;text-decoration:none;top:16px;z-index:10}.arale-dialog-1_3_0 .ui-dialog-close:hover{color:#666;text-shadow:0 0 2px #aaa}.arale-dialog-1_3_0 .ui-dialog-title{height:45px;font-size:16px;font-family:'微软雅黑','黑体',Arial;line-height:46px;border-bottom:1px solid #E1E1E1;color:#4d4d4d;text-indent:20px;background-color:#f9f9f9;background:-webkit-gradient(linear,left top,left bottom,from(#fcfcfc),to(#f9f9f9));background:-moz-linear-gradient(top,#fcfcfc,#f9f9f9);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fcfcfc', endColorstr='#f9f9f9');background:-o-linear-gradient(top,#fcfcfc,#f9f9f9);background:-ms-linear-gradient(top,#fcfcfc,#f9f9f9);background:linear-gradient(top,#fcfcfc,#f9f9f9)}.arale-dialog-1_3_0 .ui-dialog-container{padding:15px 20px 20px;font-size:12px}.arale-dialog-1_3_0 .ui-dialog-message{margin-bottom:15px}.arale-dialog-1_3_0 .ui-dialog-operation{zoom:1}.arale-dialog-1_3_0 .ui-dialog-confirm,.arale-dialog-1_3_0 .ui-dialog-cancel{display:inline}.arale-dialog-1_3_0 .ui-dialog-operation .ui-dialog-confirm{margin-right:4px}.arale-dialog-1_3_0 .ui-dialog-button-orange,.arale-dialog-1_3_0 .ui-dialog-button-white{display:inline-block;*display:inline;*zoom:1;text-align:center;text-decoration:none;vertical-align:middle;cursor:pointer;font-size:12px;font-weight:700;border-radius:2px;padding:0 12px;line-height:23px;height:23px;*overflow:visible;background-image:none}.arale-dialog-1_3_0 a.ui-dialog-button-orange:hover,.arale-dialog-1_3_0 a.ui-dialog-button-white:hover{text-decoration:none}.arale-dialog-1_3_0 .ui-dialog-button-orange{color:#fff;border:1px solid #d66500;background-color:#f57403}.arale-dialog-1_3_0 .ui-dialog-button-orange:hover{background-color:#fb8318}.arale-dialog-1_3_0 .ui-dialog-button-white{border:1px solid #afafaf;background-color:#f3f3f3;color:#777}.arale-dialog-1_3_0 .ui-dialog-button-white:hover{border:1px solid #8e8e8e;background-color:#fcfbfb;color:#676d70}</style></head>
<body>


<!-- 顶部导航条 -->
<div class="g-body  m-top">
	<div class="g-center">
		<div class="m-top-left">
			<span class="m-top-welcome">您好！欢迎访问畅易阁</span>
                            <span class="m-top-userHandle">
                    <a href="###" class="toLogin">[登录]</a>
                </span>
                <span class="m-top-userHandle">
                    <a href="http://zhuce.changyou.com/regInit.act?gameType=PE-ZHPT">[免费注册]</a>
                </span>


		</div>
		<div class="m-top-buttons">

		 
			<div class="m-top-userbar m-top-slidebar">
				<a href="http://cyg.changyou.com/user/myCenter/">我的畅易阁</a>
				<i class="f-iconfont"></i>
				<ul class="f-dn">
					<li><a href="http://cyg.changyou.com/userTrade/myBuyed">我购买的商品</a></li>
					<li><a href="http://cyg.changyou.com/userTrade/mySelling">我出售的商品</a></li>
					<li><a href="http://cyg.changyou.com/focus/focusGoodsList">我关注的商品</a></li>
					<li><a href="http://cyg.changyou.com/mycenter/message/messageList/">站內信</a></li>
				</ul>
			</div>

			<div class="m-top-cyt m-top-link">
				<a href="http://pay.cyg.changyou.com/">畅易通</a>
			</div>
			<div class="m-top-advice m-top-link">
				<a href="http://cyg.changyou.com/feedback/index">意见反馈</a>
			</div>
			<div class="m-top-help m-top-link">
				<a href="http://cyg.changyou.com/help/index">帮助中心</a>
			</div>
			<div class="m-top-stolenback m-top-link">
				<a href="http://gm.changyou.com/html/forms/form-1001.jsp" target="_blank">被盗找回</a>
			</div>
		</div>
		
	</div>
</div>
<!-- / 顶部导航条 -->

<!-- 头部 -->
<header class="g-body m-header">
	<div class="g-center">
		<div class="m-header-top">
			
			<div class="m-header-logo"><a href="http://cyg.changyou.com/" class="m-logo-link"></a></div>

			<!-- 搜索框 -->
			<div class="m-header-tools">
				<div class="m-header-search f-fr">
					<div class="m-header-gameSelect u-gameselect-trigger" id="gameSelect" style="width: 127px;"><span data-role="trigger-content">新水浒Q传</span> <i class="f-iconfont"></i>
					</div>
					<div class="m-header-serverSelect" data-widget-cid="widget-2"><span class="alreadySelect">%E7%94%B5%E4%BF%A1%E4%B8%80%E5%8C%BA-%E4%BE%A0%E5%AE%A2%E5%B2%9B</span> <i class="f-iconfont"></i></div>
					<input class="m-header-goodsInput" maxlength="40" type="text">
					<button class="m-header-searchBtn">搜&nbsp;索</button>
				</div>
			</div>
			<!-- /搜索框 -->
		</div>
		
		<!-- 菜单 -->
		<nav class="m-menu">
                <a href="/" class="m-menu-active">首页</a>
                <a href="/activity">活动专区</a>

			<a href="http://pay.cyg.changyou.com/charge/init">充值</a>
			<a href="http://pay.cyg.changyou.com/withd/init">提现</a>
		</nav>
		<!-- /菜单 -->

	
	</div>	
</header>
<!-- / 头部 -->
		<div id="server-box" class="m-server-wrap server-list" data-widget-cid="widget-1">  <a class="f-iconfont server-list-close" href="javascript:void(0);" title="关闭"></a> <div class="hd"> <div class="fn-left select-text">  <span id="select-guide" class="select-search-area">请选择游戏区：</span> <a href="javascript:void (0);" class="all-below">全部区服</a>  </div> <div class="fn-right search-info" id="select-step"> <span class="active">1.选择大区</span> <i class="f-iconfont"></i> <span>2.选择服务器</span> <i class="f-iconfont"></i> <span>3.筛选完成</span> </div> <div class="fn-right select-search" data-widget-cid="widget-16"> <a class="ui-btn-search fn-right">搜索</a> <input class="select-search-input fn-right" placeholder="全区快搜" type="text"> <ul class="select-search-tip"></ul> </div> </div> <div id="server-area-list" class="bd f-clearfix">  <div class="area-list">    <span class="server-item"> <a data-key="world_id" data-value="冬日恋歌" data-area="" data-other="冬日恋歌" data-serverid="" data-groupid="" href="javascript:void (0);">冬日恋歌</a> </span>  <span class="server-item"> <a data-key="world_id" data-value="天降雄狮" data-area="" data-other="天降雄狮" data-serverid="" data-groupid="" href="javascript:void (0);">天降雄狮</a> </span>  <span class="server-item"> <a data-key="world_id" data-value="王者归来" data-area="" data-other="王者归来" data-serverid="" data-groupid="" href="javascript:void (0);">王者归来</a> </span>  <span class="server-item"> <a data-key="world_id" data-value="电信一区" data-area="" data-other="电信一区" data-serverid="" data-groupid="" href="javascript:void (0);">电信一区</a> </span>  <span class="server-item"> <a data-key="world_id" data-value="电信四区" data-area="" data-other="电信四区" data-serverid="" data-groupid="" href="javascript:void (0);">电信四区</a> </span>  <span class="server-item"> <a data-key="world_id" data-value="网通一区" data-area="" data-other="网通一区" data-serverid="" data-groupid="" href="javascript:void (0);">网通一区</a> </span>  </div> </div> </div>

	<div class="g-body m-main">
		<div class="g-center g-inner-wrap">
			<div class="g-main" id="goodsList">
                <div class="m-choice" data-widget-cid="widget-4">
				    <input value="16" id="currentGame" type="hidden">
                    <div class="nav" data-widget-cid="widget-6">
                        <label class="select-wrap">已选条件  <i class="u-arrow-left"></i></label>
                        <div class="nav-content">
                            <div class="js-games-btn ui-select-box ui-bold-select ui-select-trigger" style="width: 127px;">
                                <span id="choiceGames" class="property-content" data-role="trigger-content">新水浒Q传</span>
                                <i class="u-arrow-down"></i>
                            </div>
                            <i class="u-arrow-left"></i>
                            <div class="js-server-btn ui-select-box ui-bold-select" data-widget-cid="widget-8">
                                <span id="choiceServer" class="alreadySelect property-content">%E7%94%B5%E4%BF%A1%E4%B8%80%E5%8C%BA-%E4%BE%A0%E5%AE%A2%E5%B2%9B</span>
                                <i class="u-arrow-down"></i>
                            </div>
                            <div id="server-filter" class="m-server-wrap" data-widget-cid="widget-7">  <a class="f-iconfont server-list-close" href="javascript:void(0);" title="关闭"></a> <div class="hd"> <div class="fn-left select-text">  <span id="select-guide" class="select-search-area">请选择游戏区：</span> <a href="javascript:void (0);" class="all-below">全部区服</a>  </div> <div class="fn-right search-info" id="select-step"> <span class="active">1.选择大区</span> <i class="f-iconfont"></i> <span>2.选择服务器</span> <i class="f-iconfont"></i> <span>3.筛选完成</span> </div> <div class="fn-right select-search" data-widget-cid="widget-12"> <a class="ui-btn-search fn-right">搜索</a> <input class="select-search-input fn-right" placeholder="全区快搜" type="text"> <ul class="select-search-tip"></ul> </div> </div> <div id="server-area-list" class="bd f-clearfix">  <div class="area-list">    <span class="server-item"> <a data-key="world_id" data-value="冬日恋歌" data-area="" data-other="冬日恋歌" data-serverid="" data-groupid="" href="javascript:void (0);">冬日恋歌</a> </span>  <span class="server-item"> <a data-key="world_id" data-value="天降雄狮" data-area="" data-other="天降雄狮" data-serverid="" data-groupid="" href="javascript:void (0);">天降雄狮</a> </span>  <span class="server-item"> <a data-key="world_id" data-value="王者归来" data-area="" data-other="王者归来" data-serverid="" data-groupid="" href="javascript:void (0);">王者归来</a> </span>  <span class="server-item"> <a data-key="world_id" data-value="电信一区" data-area="" data-other="电信一区" data-serverid="" data-groupid="" href="javascript:void (0);">电信一区</a> </span>  <span class="server-item"> <a data-key="world_id" data-value="电信四区" data-area="" data-other="电信四区" data-serverid="" data-groupid="" href="javascript:void (0);">电信四区</a> </span>  <span class="server-item"> <a data-key="world_id" data-value="网通一区" data-area="" data-other="网通一区" data-serverid="" data-groupid="" href="javascript:void (0);">网通一区</a> </span>  </div> </div> </div>
                        <span class="custom-filter"><i class="u-arrow-left"></i>
                            <span class="custom-select"><div class="f-db nav-item">  <div class="ui-select-box select ui-select-trigger" data-field="goodsType" style="width: 76px;"> <span class="property-content" data-role="trigger-content">召唤兽</span> <i class="u-arrow-down"></i> </div> <i class="u-arrow-left"></i>  </div> </span><span class="custom-property"></span>
                        </span>
                        </div>

					</div>
                    <!-- 筛选项，异步加载 in page/list/list.js -->
                    <div class="filter" style="height: auto;">  <p class="select-wrap" data-field="status" data-fieldname="商品状态"> <label class="title">商品状态：</label> <span class="content">  <a href="javascript:void(0)" class="filterItem" data-item-field="1" data-parent-field="status" data-fieldname="公示商品" data-type="1">公示商品</a>  <a href="javascript:void(0)" class="filterItem" data-item-field="2" data-parent-field="status" data-fieldname="待售商品" data-type="1">待售商品</a>  </span> </p>   <p class="select-wrap" data-field="rebornCount" data-fieldname="转生次数"> <label class="title">转生次数：</label> <span class="content">  <a href="javascript:void(0)" class="filterItem" data-item-field="0" data-parent-field="rebornCount" data-fieldname="0次以上" data-type="4">0次以上</a>  <a href="javascript:void(0)" class="filterItem" data-item-field="1" data-parent-field="rebornCount" data-fieldname="1次以上" data-type="4">1次以上</a>  <a href="javascript:void(0)" class="filterItem" data-item-field="2" data-parent-field="rebornCount" data-fieldname="2次以上" data-type="4">2次以上</a>  <a href="javascript:void(0)" class="filterItem" data-item-field="3" data-parent-field="rebornCount" data-fieldname="3次以上" data-type="4">3次以上</a>  <a href="javascript:void(0)" class="filterItem" data-item-field="4" data-parent-field="rebornCount" data-fieldname="4次以上" data-type="4">4次以上</a>  <a href="javascript:void(0)" class="filterItem" data-item-field="5" data-parent-field="rebornCount" data-fieldname="5次以上" data-type="4">5次以上</a>  </span> </p>   <p class="select-wrap" data-field="useLevel" data-fieldname="使用等级"> <label class="title">使用等级：</label> <span class="content">  <a href="javascript:void(0)" class="filterItem" data-item-field="0-79" data-parent-field="useLevel" data-fieldname="0-79级" data-type="6">0-79级</a>  <a href="javascript:void(0)" class="filterItem" data-item-field="80-99" data-parent-field="useLevel" data-fieldname="80-99级" data-type="6">80-99级</a>  <a href="javascript:void(0)" class="filterItem" data-item-field="100-199" data-parent-field="useLevel" data-fieldname="100-119级" data-type="6">100-119级</a>  <a href="javascript:void(0)" class="filterItem" data-item-field="120-139" data-parent-field="useLevel" data-fieldname="120-139级" data-type="6">120-139级</a>  <a href="javascript:void(0)" class="filterItem" data-item-field="140-149" data-parent-field="useLevel" data-fieldname="140-149级" data-type="6">140-149级</a>  </span> </p>   <p class="select-wrap" data-field="shMonsterLevel" data-fieldname="召唤兽等级"> <label class="title">召唤兽等级：</label> <span class="content">  <a href="javascript:void(0)" class="filterItem" data-item-field="0-80" data-parent-field="shMonsterLevel" data-fieldname="0-80级" data-type="6">0-80级</a>  <a href="javascript:void(0)" class="filterItem" data-item-field="81-125" data-parent-field="shMonsterLevel" data-fieldname="81-125级" data-type="6">81-125级</a>  <a href="javascript:void(0)" class="filterItem" data-item-field="126-149" data-parent-field="shMonsterLevel" data-fieldname="126-149级" data-type="6">126-149级</a>  </span> </p>      </div>
				</div>
				<div class="u-btn-more js-btn-more f-dn" style="display: none;">更多选项<i class="moreitem">（召唤兽等级，...）</i><span><i class="f-iconfont"></i></span></div>

                <div class="m-list-wrap" style="position: relative;">
                    <div class="m-sort" data-widget-cid="widget-10">
                        <span class="text">共<span class="js-num">91</span>件商品</span>
                         <a href="javascript:void(0)" class="" data-key="offlineTime"> 剩余时间   <i class="u-sort-up"></i>   </a>  <a href="javascript:void(0)" class="active last" data-key="price"> 价格   <i class="u-sort-up"></i>   </a> </div>
                    <div class="m-list" id="goodsListWrap">  <ul>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802160055330010"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26208.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802160055330010" target="_blank">[0转 1级] 足球少女</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.35</span><span>心力资质：2.43</span><span>敏捷资质：1.70</span><span>力量资质：1.83</span><span>耐力资质：2.73</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>公示剩余时间：<span class="time timeClose" data-remain="118072325">1天8小时47分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>190 </span>  <a class="u-btn-gray" href="/details?goodsCode=1621802160055330010" target="_blank">公示中</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802041609550115"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/20051.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802041609550115" target="_blank">[0转 34级] 深山狐妖B</a></h2> <p class="info"><span class="propitem"> <span>体力资质：1.70</span><span>心力资质：1.99</span><span>敏捷资质：1.33</span><span>力量资质：1.02</span><span>耐力资质：1.72</span><span>贵重：否</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="345734259">4天0小时1分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>216 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802041609550115" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802101504100141"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26073.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802101504100141" target="_blank">[0转 1级] 米米</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.11</span><span>心力资质：1.91</span><span>敏捷资质：1.92</span><span>力量资质：2.49</span><span>耐力资质：2.13</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="860188259">9天22小时56分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>238 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802101504100141" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802132108480243"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/27018.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802132108480243" target="_blank">[0转 157级] 文文</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.58</span><span>心力资质：2.70</span><span>敏捷资质：1.94</span><span>力量资质：1.96</span><span>耐力资质：3.08</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="1141268259">13天5小时0分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>244 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802132108480243" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802022351040286"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26082.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802022351040286" target="_blank">[0转 1级] 虫虫</a></h2> <p class="info"><span class="propitem"> <span>体力资质：1.97</span><span>心力资质：1.98</span><span>敏捷资质：1.62</span><span>力量资质：2.50</span><span>耐力资质：2.72</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time timeClose" data-remain="200603258">2天7小时43分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>245 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802022351040286" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802152148590244"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26007.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802152148590244" target="_blank">[0转 51级] 铁铜人</a></h2> <p class="info"><span class="propitem"> <span>体力资质：1.61</span><span>心力资质：1.33</span><span>敏捷资质：1.55</span><span>力量资质：1.57</span><span>耐力资质：1.91</span><span>贵重：否</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>公示剩余时间：<span class="time timeClose" data-remain="106878201">1天5小时40分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>255 </span>  <a class="u-btn-gray" href="/details?goodsCode=1621802152148590244" target="_blank">公示中</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802071851390138"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26128.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802071851390138" target="_blank">[0转 158级] 卡卡</a></h2> <p class="info"><span class="propitem"> <span>体力资质：1.79</span><span>心力资质：1.95</span><span>敏捷资质：1.62</span><span>力量资质：2.43</span><span>耐力资质：1.82</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="614638258">7天2小时43分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>255 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802071851390138" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802081810120146"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26082.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802081810120146" target="_blank">[0转 108级] 虫虫</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.12</span><span>心力资质：2.02</span><span>敏捷资质：1.76</span><span>力量资质：2.76</span><span>耐力资质：2.97</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="698551258">8天2小时2分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>260 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802081810120146" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802072248460228"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/27012.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802072248460228" target="_blank">[0转 156级] 玲玲</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.57</span><span>心力资质：2.62</span><span>敏捷资质：1.83</span><span>力量资质：1.91</span><span>耐力资质：2.92</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="628864258">7天6小时40分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>260 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802072248460228" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802092210210236"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26073.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802092210210236" target="_blank">[0转 49级] 米米</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.23</span><span>心力资质：2.01</span><span>敏捷资质：1.97</span><span>力量资质：2.55</span><span>耐力资质：2.22</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="799359258">9天6小时2分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>260 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802092210210236" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802151407480111"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26232.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802151407480111" target="_blank">[0转 159级] 锐锐</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.24</span><span>心力资质：2.24</span><span>敏捷资质：1.76</span><span>力量资质：2.69</span><span>耐力资质：2.96</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>公示剩余时间：<span class="time timeClose" data-remain="79207257">21小时59分48秒</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>276 </span>  <a class="u-btn-gray" href="/details?goodsCode=1621802151407480111" target="_blank">公示中</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802061140060042"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/27021.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802061140060042" target="_blank">[1转 104级] 乔不思</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.37</span><span>心力资质：2.13</span><span>敏捷资质：2.15</span><span>力量资质：2.65</span><span>耐力资质：2.30</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="502346257">5天19小时32分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>288 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802061140060042" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802102238360266"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26097.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802102238360266" target="_blank">[0转 159级] 神火狂魔</a></h2> <p class="info"><span class="propitem"> <span>体力资质：1.74</span><span>心力资质：1.44</span><span>敏捷资质：2.25</span><span>力量资质：2.12</span><span>耐力资质：1.89</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="887455257">10天6小时30分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>299 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802102238360266" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802150919040050"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26131.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802150919040050" target="_blank">[1转 1级] 妮妮</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.43</span><span>心力资质：2.62</span><span>敏捷资质：1.86</span><span>力量资质：2.03</span><span>耐力资质：2.97</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>公示剩余时间：<span class="time timeClose" data-remain="61883041">17小时11分4秒</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>300 </span>  <a class="u-btn-gray" href="/details?goodsCode=1621802150919040050" target="_blank">公示中</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802120058330017"> <img src="http://public.npt.changyou.com/assets/img/common/none70.jpg" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802120058330017" target="_blank">[0转 1级] 鸡妈妈</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.32</span><span>心力资质：2.40</span><span>敏捷资质：1.67</span><span>力量资质：1.81</span><span>耐力资质：2.70</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="982251257">11天8小时50分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>300 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802120058330017" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802100016190001"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26009.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802100016190001" target="_blank">[4转 158级] 破军铁兽</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.83</span><span>心力资质：2.56</span><span>敏捷资质：2.83</span><span>力量资质：2.14</span><span>耐力资质：2.37</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="806917257">9天8小时8分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>300 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802100016190001" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802101459280138"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26082.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802101459280138" target="_blank">[0转 149级] 虫虫</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.03</span><span>心力资质：2.22</span><span>敏捷资质：2.04</span><span>力量资质：2.92</span><span>耐力资质：2.92</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="859907256">9天22小时51分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>310 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802101459280138" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802081814070149"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26072.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802081814070149" target="_blank">[0转 112级] 奇奇</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.97</span><span>心力资质：2.20</span><span>敏捷资质：1.94</span><span>力量资质：1.93</span><span>耐力资质：3.68</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="698785256">8天2小时6分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>310 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802081814070149" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802141519390139"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26232.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802141519390139" target="_blank">[0转 158级] 锐锐</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.05</span><span>心力资质：2.10</span><span>敏捷资质：1.85</span><span>力量资质：2.97</span><span>耐力资质：2.82</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>出售剩余时间：<span class="time" data-remain="1206719256">13天23小时11分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>320 </span>  <a class="u-btn-buy" href="/details?goodsCode=1621802141519390139" target="_blank">购 买</a>  </div> </div> </li>  <li class="item"> <div class="sperate-line"> <a class="item-img" target="_blank" href="/details?goodsCode=1621802171224180050"> <img src="http://public.npt.changyou.com/images/16/2/1/monster/head/70/26078.png" onerror="imgError(this,70)">  </a> <div class="item-info"> <h2><a href="/details/?goodsCode=1621802171224180050" target="_blank">[0转 156级] 牛牛</a></h2> <p class="info"><span class="propitem"> <span>体力资质：2.15</span><span>心力资质：2.18</span><span>敏捷资质：2.15</span><span>力量资质：2.72</span><span>耐力资质：3.02</span><span>贵重：是</span> </span></p> <p class="info attr">  <span class="server-info" data-server="104">游戏区服：<span class="server-holder" title="电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 ">电信一区—侠客岛/七星台/云梦泽/芳草地/临安初雨/缘定三生/创世英雄/纯白之恋/替天行乐 </span></span>   <span>公示剩余时间：<span class="time timeClose" data-remain="245797084">2天20小时16分</span></span>  </p> </div> <div class="item-opr"> <span class="price"><i class="f-iconfont"></i>325 </span>  <a class="u-btn-gray" href="/details?goodsCode=1621802171224180050" target="_blank">公示中</a>  </div> </div> </li>  </ul>   <div class="u-pagination" data-widget-cid="widget-18">  <a title="上一页" href="javascript:void(0)" class="pre"><span data-curr-num="1" class="span">上一页</span></a>    <a href="javascript:void(0)" class="num"><span data-curr-num="1" class="span">1</span></a>    <a href="javascript:void(0)" class="num active"><span data-curr-num="2" class="span curr">2</span></a>    <a href="javascript:void(0)" class="num"><span data-curr-num="3" class="span">3</span></a>    <a href="javascript:void(0)" class="num"><span data-curr-num="4" class="span">4</span></a>    <a href="javascript:void(0)" class="num"><span data-curr-num="5" class="span">5</span></a>    <a title="下一页" href="javascript:void(0)" class="after"><span data-curr-num="3" class="span">下一页</span></a>  </div> </div>
                </div>

			</div>

			<!-- 侧边栏 -->
<div class="g-sidebar m-sidebar">

    <div class="u-rank-col3 m-neworder ui-switchable" data-widget-cid="widget-17">
        <div class="u-widget-title">
            <h2>最新成交<i class="icon icon-new"></i></h2>
        </div>
        <div class="m-rank-title">
            <span class="u-rank-span m-rank-username m-rank-span-title">商品</span>
            <span class="u-rank-span m-rank-money m-rank-span-title">标价</span>
            <span class="u-rank-span m-rank-fans m-rank-span-title">交易时间</span>
        </div>
        <div class="m-neworder-wrap" style="position: relative;">
            <ul data-switchable-role="content" class="ui-switchable-content" style="position: relative; top: -554.75px;"> <li class="ui-switchable-panel" style="position: relative; top: 700px;"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802131928120212">不知道起啥名4</a></div> <div class="u-rank-span m-rank-money f-red-bold">180元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel" style="position: relative; top: 700px;"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802131126430069">神工精炼石</a></div> <div class="u-rank-span m-rank-money f-red-bold">120元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel" style="position: relative; top: 700px;"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802110220070028">神工精炼石</a></div> <div class="u-rank-span m-rank-money f-red-bold">115元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel" style="position: relative; top: 700px;"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802032154170211">带套加攻击°</a></div> <div class="u-rank-span m-rank-money f-red-bold">500元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel" style="position: relative; top: 700px;"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802031636000122">狐仙</a></div> <div class="u-rank-span m-rank-money f-red-bold">72元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802092357310268">乔不尚</a></div> <div class="u-rank-span m-rank-money f-red-bold">50元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802131508290121">羽仙</a></div> <div class="u-rank-span m-rank-money f-red-bold">60元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141110240103">左端</a></div> <div class="u-rank-span m-rank-money f-red-bold">4400元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802100904430048">银两 x1.5亿</a></div> <div class="u-rank-span m-rank-money f-red-bold">55元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141138000112">小生！宁采臣</a></div> <div class="u-rank-span m-rank-money f-red-bold">550元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802140137120044">轩辕丶小雨a</a></div> <div class="u-rank-span m-rank-money f-red-bold">431元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141113510105">╰一纸夙愿づ</a></div> <div class="u-rank-span m-rank-money f-red-bold">1500元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141043420088">SK丶旧梦</a></div> <div class="u-rank-span m-rank-money f-red-bold">1200元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141045390094">SK丶忘情</a></div> <div class="u-rank-span m-rank-money f-red-bold">1200元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802112020210200">乔不思</a></div> <div class="u-rank-span m-rank-money f-red-bold">277元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802122025500227">因为有你′</a></div> <div class="u-rank-span m-rank-money f-red-bold">1600元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141053490098">请叫我咪咪女王</a></div> <div class="u-rank-span m-rank-money f-red-bold">499元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141042470087">SK丶空城</a></div> <div class="u-rank-span m-rank-money f-red-bold">1200元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802131733150158">帝耀</a></div> <div class="u-rank-span m-rank-money f-red-bold">550元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li class="ui-switchable-panel"> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141008590083">银两 x2.5亿</a></div> <div class="u-rank-span m-rank-money f-red-bold">100元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li> </ul>
        </div>
    <ul class="ui-switchable-nav"> <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802131928120212">不知道起啥名4</a></div> <div class="u-rank-span m-rank-money f-red-bold">180元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802131126430069">神工精炼石</a></div> <div class="u-rank-span m-rank-money f-red-bold">120元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802110220070028">神工精炼石</a></div> <div class="u-rank-span m-rank-money f-red-bold">115元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802032154170211">带套加攻击°</a></div> <div class="u-rank-span m-rank-money f-red-bold">500元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802031636000122">狐仙</a></div> <div class="u-rank-span m-rank-money f-red-bold">72元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802092357310268">乔不尚</a></div> <div class="u-rank-span m-rank-money f-red-bold">50元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802131508290121">羽仙</a></div> <div class="u-rank-span m-rank-money f-red-bold">60元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141110240103">左端</a></div> <div class="u-rank-span m-rank-money f-red-bold">4400元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802100904430048">银两 x1.5亿</a></div> <div class="u-rank-span m-rank-money f-red-bold">55元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141138000112">小生！宁采臣</a></div> <div class="u-rank-span m-rank-money f-red-bold">550元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802140137120044">轩辕丶小雨a</a></div> <div class="u-rank-span m-rank-money f-red-bold">431元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141113510105">╰一纸夙愿づ</a></div> <div class="u-rank-span m-rank-money f-red-bold">1500元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141043420088">SK丶旧梦</a></div> <div class="u-rank-span m-rank-money f-red-bold">1200元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141045390094">SK丶忘情</a></div> <div class="u-rank-span m-rank-money f-red-bold">1200元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802112020210200">乔不思</a></div> <div class="u-rank-span m-rank-money f-red-bold">277元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802122025500227">因为有你′</a></div> <div class="u-rank-span m-rank-money f-red-bold">1600元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141053490098">请叫我咪咪女王</a></div> <div class="u-rank-span m-rank-money f-red-bold">499元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141042470087">SK丶空城</a></div> <div class="u-rank-span m-rank-money f-red-bold">1200元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802131733150158">帝耀</a></div> <div class="u-rank-span m-rank-money f-red-bold">550元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141008590083">银两 x2.5亿</a></div> <div class="u-rank-span m-rank-money f-red-bold">100元</div> <div class="u-rank-span m-rank-fans"> NaN-aN-aN </div> </li> </ul><ul class="ui-switchable-nav"><li class="ui-switchable-trigger ui-switchable-active">1</li><li class="ui-switchable-trigger">2</li><li class="ui-switchable-trigger">3</li><li class="ui-switchable-trigger">4</li></ul></div>


    <div class="u-rank-col3 m-hotsale">
        <div class="u-widget-title">
            <h2>商品热卖<i class="icon icon-hot"></i></h2>
        </div>
        <div class="m-rank-title">
            <span class="u-rank-span m-rank-username m-rank-span-title">商品</span>
            <span class="u-rank-span m-rank-money m-rank-span-title">标价</span>
            <span class="u-rank-span m-rank-fans m-rank-span-title">浏览次数</span>
        </div>
        <ul data-switchable-role="content"> <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621705051349080102">思敏</a></div> <div class="u-rank-span m-rank-money f-red-bold">400元</div> <div class="u-rank-span m-rank-fans"> 4414 </div> </li> </ul>
    </div>

    <div class="u-rank-col3 m-freshGoods">
        <div class="u-widget-title">
            <h2>新鲜出炉<i class="icon icon-new"></i></h2>
        </div>
        <div class="m-rank-title">
            <span class="u-rank-span m-rank-username m-rank-span-title">商品</span>
            <span class="u-rank-span m-rank-sects m-rank-span-title">门派</span>
            <span class="u-rank-span m-rank-fans m-rank-span-title">上架时间</span>
        </div>
        <ul data-switchable-role="content"> <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141605090150">Wedding丶Dream</a></div> <div class="u-rank-span m-rank-money f-red-bold">剑客</div> <div class="u-rank-span m-rank-fans"> 3天前 </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141603360149">人间至味是梅香</a></div> <div class="u-rank-span m-rank-money f-red-bold">浪子</div> <div class="u-rank-span m-rank-fans"> 3天前 </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141558000147">℡丨罗刹街°ゞ</a></div> <div class="u-rank-span m-rank-money f-red-bold">剑客</div> <div class="u-rank-span m-rank-fans"> 3天前 </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141545350146">银两 x2.6亿</a></div> <div class="u-rank-span m-rank-money f-red-bold">--</div> <div class="u-rank-span m-rank-fans"> 3天前 </div> </li>  <li> <div class="u-rank-span m-rank-username left-username"><a href="/details?goodsCode=1621802141544170145">女仆控．み</a></div> <div class="u-rank-span m-rank-money f-red-bold">剑客</div> <div class="u-rank-span m-rank-fans"> 3天前 </div> </li> </ul>

    </div>
    <div class="m-ad-wrap"><div class="m-ad">  </div></div>
</div>
		</div>
	</div>



<div class="m-footer-wrapper">
    <div class="m-footer">
        <div class="m-footer-main">
            <div class="m-logo-wrap">
                <a class="m-logo" target="_blank" title="畅游" href="http://www.changyou.com"></a>
                <a class="m-beian" target="_blank" title="经营性网站备案信息" href="http://www.hd315.gov.cn/beian/view.asp?bianhao=010202008090900025"></a>
                <a class="m-stamp" target="_blank" title="电子图章" href="http://182.131.21.137/ccnt-apply/admin/business/preview/business-preview!lookUrlRFID.action?main_id=6D050B0F3296450A9690D264233719BD"></a>
            </div>

            <div class="m-cont">
                <p><a href="http://www.changyou.com/declaration.shtml" target="_blank">法律声明</a> | <a href="http://www.changyou.com/cu.shtml" target="_blank">联系我们</a></p>
                <p>北京畅游时代数码技术有限公司 版权所有 Copyright ©2012 ChangYou.com Limited. All rights reserved. </p>
                <p><a href="http://i1.itc.cn/20120308/2b88_54fc22d2_d391_bb9a_99d7_672a89a5b7f0_1.jpg">京网文[2011]0260-093号</a> &nbsp;|&nbsp;京ICP证：070525号&nbsp;| <a href="http://cyg.changyou.com/declare" target="_blank">畅易阁用户服务协议</a></p>
            </div>
        </div>
    </div>
</div>
    <script>
        window.gameList = (function (selectIndex) {
            var currentEle = document.getElementById("currentGame");
            var currentGame = currentEle? currentEle.value : 0;
            var ret = [];
            if (typeof window.gameListfromServer == "string") {
                try {
                    window.gameListfromServer = JSON.parse(window.gameListfromServer);
                } catch (e) {

                }
            }
            for (var i in window.gameListfromServer) {
                if (window.gameListfromServer[i].gameId == currentGame || i == selectIndex) {
                    ret.push({
                        value: window.gameListfromServer[i].gameId,
                        text: window.gameListfromServer[i].gameName,
                        selected: true
                    });
                } else {
                    ret.push({
                        value: window.gameListfromServer[i].gameId,
                        text: window.gameListfromServer[i].gameName
                    });
                }

            }
            return ret;
        })(0);
    </script>
    
		<script src="http://public.npt.changyou.com/assets/js/vendor/seajs/seajs/2.2.1/sea.js?v=1.1.14"></script>
		<script src="http://public.npt.changyou.com/assets/js/config.js?v=1.1.14"></script>
    		<script>seajs.use("http://public.npt.changyou.com/assets/js/site");</script>


		<script>		var XSH_CONFIG = 123
</script>
			<script>seajs.use("http://public.npt.changyou.com/assets/js/page/list/list.js");</script>


	
    <script>
        window.onload = function(){
            var cnzz = document.createElement('script');
            cnzz.src="http://s11.cnzz.com/stat.php?id=5373220&web_id=5373220";
            document.body.appendChild(cnzz);
        }
    </script>

<div class="u-gameselect" data-widget-cid="widget-3" id="gameListWrap" style="z-index: 99; display: none; position: absolute; left: -9999px; top: -9999px;">
    <ul class="u-gameselect-content" data-role="content">
        
        <li data-role="item" class="u-gameselect-item  u-gameselect-selected" data-value="16" data-defaultselected="true" data-selected="true" data-disabled="false">新水浒Q传</li>
        
        <li data-role="item" class="u-gameselect-item " data-value="3" data-defaultselected="false" data-selected="false" data-disabled="false">天龙八部</li>
        
        <li data-role="item" class="u-gameselect-item " data-value="2" data-defaultselected="false" data-selected="false" data-disabled="false">刀剑英雄</li>
        
    </ul>
</div><script src="http://s11.cnzz.com/stat.php?id=5373220&amp;web_id=5373220"></script><div class="ui-select" data-widget-cid="widget-9" id="m-gameselect-list" style="width: 133px; z-index: 99; display: none; position: absolute; left: -9999px; top: -9999px;">
    <ul class="ui-select-content" data-role="content">
        
        <li data-role="item" class="ui-select-item  ui-select-selected" data-value="16" data-defaultselected="true" data-selected="true" data-disabled="false">新水浒Q传</li>
        
        <li data-role="item" class="ui-select-item " data-value="3" data-defaultselected="false" data-selected="false" data-disabled="false">天龙八部</li>
        
        <li data-role="item" class="ui-select-item " data-value="2" data-defaultselected="false" data-selected="false" data-disabled="false">刀剑英雄</li>
        
    </ul>
</div><div class="ui-select" data-widget-cid="widget-11" style="width: 76px; z-index: 99; display: none; position: absolute; left: -9999px; top: -9999px;">
    <ul class="ui-select-content" data-role="content">
        
        <li data-role="item" class="ui-select-item" data-value="all" data-defaultselected="false" data-selected="false" data-disabled="false">全部</li>
        
        <li data-role="item" class="ui-select-item " data-value="1" data-defaultselected="false" data-selected="false" data-disabled="false">角色</li>
        
        <li data-role="item" class="ui-select-item " data-value="2" data-defaultselected="false" data-selected="false" data-disabled="false">游戏币</li>
        
        <li data-role="item" class="ui-select-item " data-value="3" data-defaultselected="false" data-selected="false" data-disabled="false">装备</li>
        
        <li data-role="item" class="ui-select-item " data-value="11" data-defaultselected="false" data-selected="false" data-disabled="false">道具</li>
        
        <li data-role="item" class="ui-select-item  ui-select-selected" data-value="4" data-defaultselected="false" data-selected="true" data-disabled="false">召唤兽</li>
        
    </ul>
</div></body></html>'''

selector = Selector(text = content)
re1 = "li.item > div > div > h2 > a::attr(href)"
re2 = "a[href*='details?goodsCode']::attr(href)"
print(selector.css(re1).extract())