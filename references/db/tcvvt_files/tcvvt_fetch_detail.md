# 规则取数取数明细表-tcvvt_fetch_detail

## 规则取数取数明细表-主表 t_tcvvt_fetch_detail

- **表名称：** 规则取数取数明细表-主表
- **表名：** t_tcvvt_fetch_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | famountfield | 金额字段 | int8 | 64 |  | √ | 0 | 数据源字段配置 tctb_datasource_entry |
| 4 | fserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | ftemplatetype | 模板类型 | varchar | 100 |  | √ | ' ' | 模板类型 |
| 10 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 13 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 14 | ftable | 数据源 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 15 | fabsolute | 绝对值 | bpchar | 1 |  | √ | '0' | 绝对值 |
| 16 | fruleid | 规则id | varchar | 50 |  | √ | ' ' | 规则id |
| 17 | freportingamount | 填报金额 | numeric | 23 | 10 | √ | 0 | 填报金额 |
| 18 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 19 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 20 | fdatadirection | 取数方向 | varchar | 50 |  | √ | ' ' | 取数方向,枚举: positive :正向 reverse :反向 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_fetchdetail_no |  | fserialno |
| 2 | pk_tcvvt_fetch_detail |  | fid |
| 3 | idx_tcvvt_fetchdetail_org |  | forgid,fskssqq,fskssqz |
