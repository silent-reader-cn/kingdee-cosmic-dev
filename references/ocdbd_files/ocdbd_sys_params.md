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
| 4 | fisbychanneluser | 业务单据按渠道用户隔离 | bpchar | 1 |  | √ | '0' | 业务单据按渠道用户隔离 |
| 5 | fbudgetdimension | 营销费用预算维度 | bpchar | 1 |  | √ | 'A' | 营销费用预算维度,枚举: A :按年度 B :按月份 |
| 6 | forgpatternid | 所属大区（行政组织）的组织形态确定 | int8 | 64 |  | √ | 0 | 组织形态 bos_org_pattern |
| 7 | fispolicyrepetcheck | 价格政策唯一性强管控 | bpchar | 1 |  | √ | '0' | 价格政策唯一性强管控 |
| 8 | fisallowordernegative | 控制要货订单更新后可用余额不允许为负 | bpchar | 1 |  | √ | '1' | 控制要货订单更新后可用余额不允许为负 |
| 9 | fiscustomersynchannel | 客户同步更新渠道 | bpchar | 1 |  | √ | '0' | 客户同步更新渠道 |
| 10 | fisorderquantityforce | 订货批量是否强控制 | bpchar | 1 |  | √ | '0' | 订货批量是否强控制 |
| 11 | fissynccaddress | 客户/渠道收货地址同步 | bpchar | 1 |  | √ | '1' | 客户/渠道收货地址同步 |
| 12 | fismaterialsynitem | 物料同步更新商品 | bpchar | 1 |  | √ | '0' | 物料同步更新商品 |
| 13 | fenablepresubmit | 启用预提交（废弃） | bpchar | 1 |  | √ | '0' | 启用预提交（废弃） |
| 14 | fmultipromoteexecute | fmultipromoteexecute | bpchar | 1 |  | √ | 'A' |  |
| 15 | fisuserebateactidem | 启用资金池幂等性校验 | bpchar | 1 |  | √ | '0' | 启用资金池幂等性校验 |
| 16 | forgpricesource | 组织供货价格来源 | bpchar | 1 |  | √ | 'A' | 组织供货价格来源,枚举: A :渠道价格政策 B :供应链销售价目表 C :二开扩展 |
| 17 | fisdisplayladdyprice | 订货显示数量阶梯价格 | bpchar | 1 |  | √ | '0' | 订货显示数量阶梯价格 |
| 18 | fismultiplepicking | 要货订单商品支持多次拣货 | bpchar | 1 |  | √ | '1' | 要货订单商品支持多次拣货 |
| 19 | fisuserebateamount | 启用资金池余额接口 | bpchar | 1 |  | √ | '0' | 启用资金池余额接口 |
| 20 | fcheckrepatecontroltype | 查重控制强度 | bpchar | 1 |  | √ | '2' | 查重控制强度,枚举: 0 :不控制 2 :预警提示 1 :不允许保存 |
| 21 | fisenablemall | 启用门店门户（移动） | bpchar | 1 |  | √ | '0' | 启用门店门户（移动） |
| 22 | fismergegetprice | 相同商品合计数量取价 | bpchar | 1 |  | √ | '0' | 相同商品合计数量取价 |
| 23 | fisdefaultsalecontrol | 供货关系默认可销控制 | bpchar | 1 |  | √ | '0' | 供货关系默认可销控制 |
| 24 | fpushitemstatus | 物料同步创建商品的状态 | bpchar | 1 |  | √ | 'A' | 物料同步创建商品的状态,枚举: A :暂存 B :提交 C :审核 |
| 25 | fisbusinessorg | 是否启用经营组织 | bpchar | 1 |  | √ | '0' | 是否启用经营组织 |
| 26 | fchannelreqmobiletype | 移动端渠道申请流程 | bpchar | 1 |  | √ | 'B' | 移动端渠道申请流程,枚举: A :仅提交 B :一键认证成功 |
| 27 | fisorderqtyzero | 允许要货订单批准数量为0 | bpchar | 1 |  | √ | '0' | 允许要货订单批准数量为0 |
| 28 | fisenablebalmodel | 启用资金池余额服务 | bpchar | 1 |  | √ | '0' | 启用资金池余额服务 |
| 29 | fquickorderqty | 快速订货默认订货数量 | int4 | 32 |  | √ | 1 | 快速订货默认订货数量 |
| 30 | fpromotegroupexcute | fpromotegroupexcute | bpchar | 1 |  | √ | 'A' |  |
| 31 | fpresubmitset | 启用预提交 | varchar | 255 |  | √ | ' ' | 启用预提交,枚举: ocbsoc_saleorder :支持要货订单 ocbsoc_returnorder :支持退货申请 ococic_transbill :支持渠道调拨 |
| 32 | fenableitemattr | 启用商品属性订货 | bpchar | 1 |  | √ | '0' | 启用商品属性订货 |
| 33 | fisitempricepermitzero | 商品价格为零不显示 | bpchar | 1 |  | √ | '1' | 商品价格为零不显示 |
| 34 | fmobexpirymins | 移动端页面失效时间（分钟） | int4 | 32 |  | √ | 0 | 移动端页面失效时间（分钟） |
| 35 | fpromotiondiscountype | fpromotiondiscountype | bpchar | 1 |  | √ | '1' |  |
| 36 | funitdiscountprecision | 单位总折扣精度 | int4 | 32 |  | √ | 6 | 单位总折扣精度 |
| 37 | frepeatbudgetcontrol | 重复预算控制 | bpchar | 1 |  | √ | 'A' | 重复预算控制,枚举: A :不允许重复预算 B :预警提示 C :不控制 |
| 38 | finvsourcefrom | 库存集成方式 | bpchar | 1 |  | √ | 'A' | 库存集成方式,枚举: A :与星空旗舰版一体化 B :与异构供应链集成 |
| 39 | fislowpricecheck | 最低限价控制 | bpchar | 1 |  | √ | '0' | 最低限价控制,枚举: 0 :不控制 1 :警告 2 :取消交易 |
| 40 | fpushchannelstatus | 客户同步创建渠道的状态 | bpchar | 1 |  | √ | 'A' | 客户同步创建渠道的状态,枚举: A :暂存 B :提交 C :审核 |
| 41 | fischannelfilterbycuser | 渠道信息按渠道用户范围显示 | bpchar | 1 |  | √ | '0' | 渠道信息按渠道用户范围显示 |
| 42 | fsynchannelauthorizetype | 渠道同步供货关系控制 | bpchar | 1 |  | √ | '1' | 渠道同步供货关系控制,枚举: 0 :不同步 1 :同步新增 2 :同步新增删除 |
| 43 | fisuseonepromotion | fisuseonepromotion | bpchar | 1 |  | √ | '0' |  |
| 44 | fchannelpricesource | 渠道供货价格来源 | bpchar | 1 |  | √ | 'A' | 渠道供货价格来源,枚举: A :渠道价格政策 C :二开扩展 |
| 45 | fmultiunitorder | 多单位订货设置 | bpchar | 1 |  | √ | 'A' | 多单位订货设置,枚举: A :按销售单位订货 B :按辅助单位订货 C :多销售单位订货 |
| 46 | fenableitemspu | 启用商品SPU | bpchar | 1 |  | √ | '0' | 启用商品SPU |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_sysparams |  | fid |
| 2 | idx_ocdbd_sysparams |  | fisorderquantityforce,fisuserebateamount,fisbusinessorg |
