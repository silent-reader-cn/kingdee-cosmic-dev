# 印花税税源采集取数明细-tcret_ysh_tax_source_de

## 印花税税源采集取数明细-主表 t_tcret_sycj_yhsqsmx

- **表名称：** 印花税税源采集取数明细-主表
- **表名：** t_tcret_sycj_yhsqsmx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 7 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0.0000000000 | 取数金额 |
| 11 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 12 | fbizdimensiontype | 业务维度 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 13 | fabsolute | 绝对值 | bpchar | 1 |  | √ | ' ' | 绝对值 |
| 14 | fruleid | 规则id | varchar | 50 |  | √ | ' ' | 规则id |
| 15 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 16 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |
| 17 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 20 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 21 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 22 | ftype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: 1 :应税合同凭证 2 :产权转移书据 3 :资金账簿 |
| 23 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 24 | fbizdimensionid | 业务维度值ID | varchar | 50 |  | √ | ' ' | 业务维度值ID |
| 25 | fdatatype | 取数方式 | varchar | 50 |  | √ | ' ' | 取数方式,枚举: zjqs :直接取数 jsflqs :价税分离取数 cysldsqs :除以税率倒算取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_sycj_yhsqsmx |  | forgid,ftaxperiod,fskssqq,fskssqz |
| 2 | pk_tcret_sycj_yhsqsmx |  | fid |
