# 报账数据初始化-dhc_billdatainit

## 报账数据初始化-主表 t_dhc_billdatainit

- **表名称：** 报账数据初始化-主表
- **表名：** t_dhc_billdatainit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | finitbegintime | 初始化开始时间 | timestamp | 0 |  |  | null | 初始化开始时间 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | finitstatus | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: A :未执行 B :执行中 C :部分执行完成 D :执行完成 E :执行失败 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fisinit | 是否初始化 | bpchar | 1 |  | √ | ' ' | 是否初始化 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | finitfinishtime | 初始化完成时间 | timestamp | 0 |  |  | null | 初始化完成时间 |
| 12 | fbillid | 单据 | varchar | 36 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 13 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dhc_datainit_blid |  | fbillid |
| 2 | t_dhc_billdatainit_pkey |  | fid |
