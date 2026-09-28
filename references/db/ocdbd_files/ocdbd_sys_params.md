# 企业全局参数-ocdbd_sys_params

## 企业全局参数-主表 t_ocdbd_sysparams

- **表名称：** 企业全局参数-主表
- **表名：** t_ocdbd_sysparams

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemstatuscontrol | 商品下架管控范围 | varchar | 20 |  | √ | ' ' | 商品下架管控范围,枚举: 0 :在渠道门户管控 1 :在渠道门户移动端管控 2 :在B2B订单中心管控 3 :在渠道管家管控 |
| 3 | fautomoneyincome | 财务收/付款单自动生成资金池收入单 | bpchar | 1 |  | √ | '0' | 财务收/付款单自动生成资金池收入单 |
| 4 | fispolicyrepetcheck | 价格政策唯一性强管控 | bpchar | 1 |  | √ | '0' | 价格政策唯一性强管控 |
| 5 | fisorderquantityforce | 订货批量是否强控制 | bpchar | 1 |  | √ | '0' | 订货批量是否强控制 |
| 6 | fissynccaddress | 客户/渠道收货地址同步(已废弃) | bpchar | 1 |  | √ | '1' | 客户/渠道收货地址同步(已废弃) |
| 7 | fismaterialsynitem | 物料同步更新商品 | bpchar | 1 |  | √ | '0' | 物料同步更新商品 |
| 8 | fsaleplaneditmonthqty | 销售计划滚动月份 | bpchar | 1 |  | √ | '2' | 销售计划滚动月份,枚举: 1 :滚动编辑下一个月 2 :滚动编辑下两个月 3 :滚动编辑下三个月 4 :滚动编辑下四个月 5 :滚动编辑下五个月 6 :滚动编辑下六个月 |
| 9 | forgpricesource | 组织供货价格来源 | bpchar | 1 |  | √ | 'A' | 组织供货价格来源,枚举: A :渠道价格政策 B :供应链销售价目表 C :二开扩展 |
| 10 | fisdisplayladdyprice | 订货显示数量阶梯价格 | bpchar | 1 |  | √ | '0' | 订货显示数量阶梯价格 |
| 11 | fismultiplepicking | 要货订单商品支持多次拣货 | bpchar | 1 |  | √ | '1' | 要货订单商品支持多次拣货 |
| 12 | factualqtycalmonthqty | 销售计划实际数统计(废弃) | bpchar | 1 |  | √ | '2' | 销售计划实际数统计(废弃),枚举: 1 :最近一个月 2 :最近两个月 3 :最近三个月 4 :最近四个月 5 :最近五个月 6 :最近六个月 7 :最近七个月 8 :最近八个月 9 :最近九个月 |
| 13 | fisenablemall | 启用门店门户（移动） | bpchar | 1 |  | √ | '0' | 启用门店门户（移动） |
| 14 | fmallloaditem | 商城图片展示 | bpchar | 1 |  | √ | 'A' | 商城图片展示,枚举: A :展示 B :不展示 |
| 15 | fbgshowregionprovince | 预算余额表显示省区大区 | bpchar | 1 |  | √ | 'A' | 预算余额表显示省区大区,枚举: A :按行政组织关联展示 B :按渠道组织信息展示 C :渠道优先组织 |
| 16 | fismergegetprice | 相同商品合计数量取价 | bpchar | 1 |  | √ | '0' | 相同商品合计数量取价 |
| 17 | fpushitemstatus | 物料同步创建商品的状态 | bpchar | 1 |  | √ | 'A' | 物料同步创建商品的状态,枚举: A :暂存 B :提交 C :审核 |
| 18 | fmallloadpromotion | 商城促销标签展示 | bpchar | 1 |  | √ | 'A' | 商城促销标签展示,枚举: A :即时匹配 B :不展示 |
| 19 | fcalactualqtymonthqty | 实际数统计月份 | int4 | 32 |  | √ | 0 | 实际数统计月份 |
| 20 | forderanalset | 订货分析金额展示 | varchar | 50 |  | √ | ' ' | 订货分析金额展示,枚举: sumactualtaxamount :实际价税合计 sumreceivableamount :应收金额 |
| 21 | fquickorderqty | 快速订货默认订货数量 | int4 | 32 |  | √ | 1 | 快速订货默认订货数量 |
| 22 | fpromotegroupexcute | fpromotegroupexcute | bpchar | 1 |  | √ | 'A' |  |
| 23 | fenableitemattr | 启用商品属性订货 | bpchar | 1 |  | √ | '0' | 启用商品属性订货 |
| 24 | fisitempricepermitzero | 商品价格为零不显示 | bpchar | 1 |  | √ | '1' | 商品价格为零不显示 |
| 25 | fpromotiondiscountype | fpromotiondiscountype | bpchar | 1 |  | √ | '1' |  |
| 26 | fhomepageallot | 首页开启分配模式 | bpchar | 1 |  | √ | '0' | 首页开启分配模式 |
| 27 | fisamountshowcurrent | 渠道门户移动端余额仅展示当前渠道 | bpchar | 1 |  | √ | '1' | 渠道门户移动端余额仅展示当前渠道 |
| 28 | fpushchannelstatus | 客户同步创建渠道的状态 | bpchar | 1 |  | √ | 'A' | 客户同步创建渠道的状态,枚举: A :暂存 B :提交 C :审核 |
| 29 | fischannelfilterbycuser | 渠道信息按渠道用户范围显示 | bpchar | 1 |  | √ | '0' | 渠道信息按渠道用户范围显示 |
| 30 | fpricingmethod | 产品取价方式 | bpchar | 1 |  | √ | 'A' | 产品取价方式,枚举: A :产品销售价格 B :产品成本单价 C :手工录入价格 |
| 31 | fchannelpricesource | 渠道供货价格来源 | bpchar | 1 |  | √ | 'A' | 渠道供货价格来源,枚举: A :渠道价格政策 C :二开扩展 |
| 32 | fmultiunitorder | 多单位订货设置 | bpchar | 1 |  | √ | 'A' | 多单位订货设置,枚举: A :按销售单位订货 B :按辅助单位订货 C :多销售单位订货 |
| 33 | fenableitemspu | 启用商品SPU | bpchar | 1 |  | √ | '0' | 启用商品SPU |
| 34 | fisenablepricedetail | 启用价格组成明细管理 | bpchar | 1 |  | √ | '0' | 启用价格组成明细管理 |
| 35 | fenablereplenishment | 启用货补池 | bpchar | 1 |  | √ | '0' | 启用货补池 |
| 36 | fenablemultiunit | 启用多单位订货 | bpchar | 1 |  | √ | '0' | 启用多单位订货 |
| 37 | fintegrationtype | 集成ERP | bpchar | 1 |  | √ | 'A' | 集成ERP,枚举: A :无 B :星空企业版 C :星瀚 D :其他ERP |
| 38 | fisbychanneluser | 业务单据按渠道用户隔离 | bpchar | 1 |  | √ | '0' | 业务单据按渠道用户隔离 |
| 39 | fcreditschema | 信用方案 | bpchar | 1 |  | √ | 'A' | 信用方案,枚举: A :旗舰版一体化 B :企业版集成 C :不启用 |
| 40 | fbudgetdimension | 营销费用预算维度 | bpchar | 1 |  | √ | 'A' | 营销费用预算维度,枚举: A :按年度 B :按月份 |
| 41 | fmallnavigationlevel | 移动商城分类导航显示级次 | int4 | 32 |  | √ | 1 | 移动商城分类导航显示级次 |
| 42 | forgpatternid | 所属大区（行政组织）的组织形态确定 | int8 | 64 |  | √ | 0 | [组织形态 bos_org_pattern](../base_files/bos_org_pattern.md) |
| 43 | fisallowordernegative | 控制要货订单更新后可用余额不允许为负 | bpchar | 1 |  | √ | '1' | 控制要货订单更新后可用余额不允许为负 |
| 44 | fiscustomersynchannel | 客户同步更新渠道 | bpchar | 1 |  | √ | '0' | 客户同步更新渠道 |
| 45 | fisaddrjoindistrict | 要货订单详细地址是否拼接省市区 | bpchar | 1 |  | √ | ' ' | 要货订单详细地址是否拼接省市区 |
| 46 | fenablepresubmit | 启用预提交（废弃） | bpchar | 1 |  | √ | '0' | 启用预提交（废弃） |
| 47 | fmultipromoteexecute | fmultipromoteexecute | bpchar | 1 |  | √ | 'A' |  |
| 48 | fisuserebateactidem | 启用资金池幂等性校验 | bpchar | 1 |  | √ | '0' | 启用资金池幂等性校验 |
| 49 | fenablesmartorder | 启用智能审单 | bpchar | 1 |  | √ | '0' | 启用智能审单 |
| 50 | fisuserebateamount | 启用资金池余额接口 | bpchar | 1 |  | √ | '0' | 启用资金池余额接口 |
| 51 | fcheckrepatecontroltype | 查重控制强度 | bpchar | 1 |  | √ | '2' | 查重控制强度,枚举: 0 :不控制 2 :预警提示 1 :不允许保存 |
| 52 | fisfilterbymatsale | 按物料销售信息管控策略隔离商品 | bpchar | 1 |  | √ | '0' | 按物料销售信息管控策略隔离商品 |
| 53 | fenbaleorderagent | 启用AI订货智能体 | bpchar | 1 |  | √ | '0' | 启用AI订货智能体 |
| 54 | fisdefaultsalecontrol | 供货关系默认可销控制 | bpchar | 1 |  | √ | '0' | 供货关系默认可销控制 |
| 55 | fismobcreditshow | 信用余额允许展示 | bpchar | 1 |  | √ | '1' | 信用余额允许展示 |
| 56 | fisbusinessorg | 是否启用经营组织 | bpchar | 1 |  | √ | '0' | 是否启用经营组织 |
| 57 | fchannelreqmobiletype | 移动端渠道申请流程 | bpchar | 1 |  | √ | 'B' | 移动端渠道申请流程,枚举: A :仅提交 B :一键认证成功 |
| 58 | fisorderqtyzero | 允许要货订单批准数量为0 | bpchar | 1 |  | √ | '0' | 允许要货订单批准数量为0 |
| 59 | fisenablebalmodel | 启用资金池余额服务 | bpchar | 1 |  | √ | '0' | 启用资金池余额服务 |
| 60 | fsalepricemodify | 销售开单价格允许修改 | bpchar | 1 |  | √ | '1' | 销售开单价格允许修改 |
| 61 | fpresubmitset | 启用预提交 | varchar | 255 |  | √ | ' ' | 启用预提交,枚举: ocbsoc_saleorder :支持要货订单 ocbsoc_returnorder :支持退货申请 ococic_transbill :支持渠道调拨 |
| 62 | fmobexpirymins | 移动端页面失效时间（分钟） | int4 | 32 |  | √ | 0 | 移动端页面失效时间（分钟） |
| 63 | fmallnavigationtype | 移动商城分类导航 | bpchar | 1 |  | √ | 'B' | 移动商城分类导航,枚举: A :上面图标导航模式 B :左边导航模式 |
| 64 | funitdiscountprecision | 单位总折扣精度 | int4 | 32 |  | √ | 6 | 单位总折扣精度 |
| 65 | frepeatbudgetcontrol | 重复预算控制 | bpchar | 1 |  | √ | 'A' | 重复预算控制,枚举: A :不允许重复预算 B :预警提示 C :不控制 |
| 66 | finvsourcefrom | 库存集成方式 | bpchar | 1 |  | √ | 'A' | 库存集成方式,枚举: A :与星空旗舰版一体化 B :与异构供应链集成 C :渠道云库存表 D :企业版API |
| 67 | fislowpricecheck | 最低限价控制 | bpchar | 1 |  | √ | '0' | 最低限价控制,枚举: 0 :不控制 1 :警告 2 :取消交易 |
| 68 | fsynccaddress | 客户/渠道收货地址同步 | bpchar | 1 |  | √ | ' ' | 客户/渠道收货地址同步,枚举: A :不同步 B :渠道地址更新客户地址 C :客户地址更新渠道地址 D :双向更新 |
| 69 | fsynchannelauthorizetype | 渠道同步供货关系控制 | bpchar | 1 |  | √ | '1' | 渠道同步供货关系控制,枚举: 0 :不同步 1 :同步新增 2 :同步新增删除 |
| 70 | fisuseonepromotion | fisuseonepromotion | bpchar | 1 |  | √ | '0' |  |
| 71 | fshowitemlabel | 展示标签 | bpchar | 1 |  | √ | '0' | 展示标签 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_sysparams |  | fid |
| 2 | idx_ocdbd_sysparams |  | fisorderquantityforce,fisuserebateamount,fisbusinessorg |
