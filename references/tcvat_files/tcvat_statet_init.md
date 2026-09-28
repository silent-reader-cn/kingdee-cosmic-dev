# 留抵情况初始化-tcvat_statet_init

## 留抵情况初始化-主表 t_tcvat_statet_init

- **表名称：** 留抵情况初始化-主表
- **表名：** t_tcvat_statet_init

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fincrebackamount | 本期允许退还的增量留抵退税额 | numeric | 23 | 10 | √ | 0 | 本期允许退还的增量留抵退税额 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | famount | 本期期末留抵税额 | numeric | 23 | 10 | √ | 0 | 本期期末留抵税额 |
| 9 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fstockbackamount | 本期允许退还的存量留抵退税额 | numeric | 23 | 10 | √ | 0 | 本期允许退还的存量留抵退税额 |
| 13 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 14 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :系统生成 1 :数据引入 2 :手工新增 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_statet_init |  | fid |
| 2 | idx_tcvat_statet_init |  | fskssqq,fskssqz,forgid |
