# 单据信用检查结果记录-ccm_billcheckrecord

## 单据信用检查结果记录-主表 t_ccm_billcheckrecord

- **表名称：** 单据信用检查结果记录-主表
- **表名：** t_ccm_billcheckrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsingleamtquota | 单笔额度 | numeric | 23 | 10 | √ | 0 | 单笔额度 |
| 4 | farchivename | 档案名称 | varchar | 255 |  | √ | ' ' | 档案名称 |
| 5 | forgid | 授信组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdimensionid | 信控维度 | int8 | 64 |  | √ | 0 | [信控维度 ccm_dimension](../ccm_files/ccm_dimension.md) |
| 7 | fbillids | 单据 | varchar | 1000 |  | √ | ' ' | 单据 |
| 8 | fnote | 说明 | varchar | 2000 |  | √ | ' ' | 说明 |
| 9 | frecordtype | 记录类型 | varchar | 30 |  | √ | ' ' | 记录类型,枚举: 1 :正式记录（供客户查询） 0 :非正式记录 |
| 10 | fscheme | 信控方案 | int8 | 64 |  | √ | 0 | [信用控制方案 ccm_schemes](../ccm_files/ccm_schemes.md) |
| 11 | fbillcurrencyid | 单据币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 12 | fdayquota | 信用天数额度 | int4 | 32 |  | √ | 0 | 信用天数额度 |
| 13 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 14 | foccupyamount | 占用金额(档案币种) | numeric | 23 | 10 | √ | 0 | 占用金额(档案币种) |
| 15 | funitid | 单位 | int8 | 64 |  | √ | 0 | 单位 |
| 16 | fexcessbillamount | 超标单笔限额 | numeric | 23 | 10 | √ | 0 | 超标单笔限额 |
| 17 | froletype2 | 维度成员类型2 | varchar | 36 |  | √ | ' ' | 维度成员类型2,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 18 | froletype3 | 维度成员类型3 | varchar | 36 |  | √ | ' ' | 维度成员类型3,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 19 | foverduebillno | 逾期单据编号 | varchar | 100 |  | √ | ' ' | 逾期单据编号 |
| 20 | fbillamount | 单据金额 | numeric | 23 | 10 | √ | 0 | 单据金额 |
| 21 | froletype0 | 维度成员类型0 | varchar | 36 |  | √ | ' ' | 维度成员类型0,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 22 | froletype1 | 维度成员类型1 | varchar | 36 |  | √ | ' ' | 维度成员类型1,枚举: bd_customer :客户 ccm_cusunicode :客户统一码 bd_material :物料 bos_org :业务单元 bd_operatorgroup :业务组 bd_supplier :供应商 bos_adminorg :行政组织 bd_materialgroup :物料分类 bos_user :人员 |
| 23 | fsuccess | 检查通过 | bpchar | 1 |  | √ | ' ' | 检查通过 |
| 24 | fbalance | 余额 | numeric | 23 | 10 | √ | 0 | 余额 |
| 25 | fquotatype | 额度类型 | varchar | 30 |  | √ | ' ' | 额度类型,枚举: amount :信用额度 qty :信用数量 days :信用天数 overdueamt :逾期额度 |
| 26 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 27 | foveramtquota | 逾期额度 | numeric | 23 | 10 | √ | 0 | 逾期额度 |
| 28 | fdirection | 更新方向 | varchar | 30 |  | √ | ' ' | 更新方向,枚举: reduce :减少 increase :增加 |
| 29 | fexcessamount | 超标金额(档案币种) | numeric | 23 | 10 | √ | 0 | 超标金额(档案币种) |
| 30 | farchiveid | 信用档案ID | int8 | 64 |  | √ | 0 | 信用档案ID |
| 31 | fop | 业务操作 | varchar | 30 |  | √ | ' ' | 业务操作,枚举: save :保存 submit :提交 audit :审核 unaudit :反审核 unsubmit :撤销提交 bizclose :业务关闭 bizunclose :业务反关闭 rowunclose :行反关闭 rowclose :行关闭 rowunterminate :行反终止 rowterminate :行终止 receivingrec :确认收款 cancelrec :取消收款 pay :确认付款 cancelpay :取消付款 bizfreeze :冻结 bizunfreeze :反冻结 bizcancel :作废 bizuncancel :反作废 bizvalid :生效 bizinvalid :反生效 bizterminate :单据终止 billchange :单据变更 |
| 32 | fexcessoveramount | 超标逾期额度 | numeric | 23 | 10 | √ | 0 | 超标逾期额度 |
| 33 | fbilldate | 业务单据日期 | timestamp | 0 |  |  | null | 业务单据日期 |
| 34 | famount | 本单增加额度 | numeric | 23 | 10 | √ | 0 | 本单增加额度 |
| 35 | fcontrolmode | 信用控制强度 | varchar | 30 |  | √ | ' ' | 信用控制强度,枚举: cancel :取消交易 warning :预警提示 billspec :单笔特批 |
| 36 | fpressquota | 压批额度 | int4 | 32 |  | √ | 0 | 压批额度 |
| 37 | farchivecurrencyid | 档案币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 38 | frole0 | 维度成员值0 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 39 | frole1 | 维度成员值1 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 40 | frole2 | 维度成员值2 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 41 | frole3 | 维度成员值3 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 42 | fdealresult | 处理结果 | varchar | 30 |  | √ | ' ' | 处理结果,枚举: cancel :取消交易 warning_1 :预警提示：继续操作 warning_0 :预警提示：未继续操作 billspec_1 :单笔特批：特批通过 billspec_0 :单笔特批：特批不通过 totalspec_1 :总额特批：特批通过 totalspec_0 :总额特批：特批不通过 billspec_noperm :单笔特批：无特批权限 billspec_noquota :单笔特批：特批额度不足 |
| 43 | ftraceid | TRACEID | varchar | 50 |  | √ | ' ' | TRACEID |
| 44 | famountquota | 信用额度 | numeric | 23 | 10 | √ | 0 | 信用额度 |
| 45 | fcreatetime | 处理日期 | timestamp | 0 |  |  | null | 处理日期 |
| 46 | fexcessdays | 超标天数 | int4 | 32 |  | √ | 0 | 超标天数 |
| 47 | fentitykey | 业务单据 | varchar | 36 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 48 | funsettlebillcount | 未结压批批数 | int4 | 32 |  | √ | 0 | 未结压批批数 |
| 49 | flogtype | 日志类型 | varchar | 30 |  | √ | ' ' | 日志类型,枚举: check :正常检查日志 other :其他日志 |
| 50 | fbilltype | 业务单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_billcheckrecord |  | fid |
| 2 | idx_ccm_billchkrec_time |  | fcreatetime |
| 3 | idx_ccm_billchkrec_date |  | fbilldate |
