# 印花税税金计提取数明细-tcret_yhs_sjjt_detail

## 印花税税金计提取数明细-主表 t_tcret_yhs_sjjt_detail

- **表名称：** 印花税税金计提取数明细-主表
- **表名：** t_tcret_yhs_sjjt_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 tctb_datasource_entry](../tctb_files/tctb_datasource_entry.md) |
| 4 | ftaxitem | 税目 | varchar | 50 |  | √ | ' ' | 税目 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 9 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 10 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 12 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 13 | fbizdimensiontype | 业务维度 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 15 | fsubtaxitem | 子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcsd_bizdef_entry |
| 16 | fruleid | 规则id | varchar | 50 |  | √ | ' ' | 规则id |
| 17 | fdeductiontype | 减免税类型 | varchar | 50 |  | √ | ' ' | 减免税类型,枚举: 1 :免税 2 :减征 3 :扣减 4 :抵减 5 :即征即退 6 :其他 |
| 18 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 19 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 20 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 23 | fadvancedconfjson | 高级配置JSON | text | 0 |  |  | null | 高级配置JSON |
| 24 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 25 | ftaxlimit | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: season :季度 year :年度 single :按次 |
| 26 | fbusdimensionmap | 业务维度映射（计税方案） | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 27 | fconditionjson | 过滤条件JSON | text | 0 |  |  | null | 过滤条件JSON |
| 28 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 29 | ftaxitemid | 税目 | int8 | 64 |  | √ | 0 | 印花税税率（树） tpo_tcsd_taxrateentrytree |
| 30 | ftype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: 1 :应税合同凭证 2 :产权转移书据 3 :资金账簿 |
| 31 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 32 | fbusdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 33 | fbusinessmap | 业务组织集合 | text | 0 |  |  | null | 业务组织集合 |
| 34 | fdatasource | 数据源 | varchar | 50 |  | √ | ' ' | 数据源 |
| 35 | fbizdimensionid | 业务维度值ID | varchar | 50 |  | √ | ' ' | 业务维度值ID |
| 36 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_yhs_sjjt_detail |  | fid |
| 2 | idx_tcret_yhs_sjjt_org |  | forgid,fskssqq,fskssqz |
