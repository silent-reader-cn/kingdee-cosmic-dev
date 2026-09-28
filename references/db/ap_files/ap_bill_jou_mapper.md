# 单据流水字段映射配置-ap_bill_jou_mapper

## 单据流水字段映射配置-主表 t_ap_billjoumapper

- **表名称：** 单据流水字段映射配置-主表
- **表名：** t_ap_billjoumapper

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapp | 应用 | varchar | 50 |  | √ | ' ' | 应用,枚举: ap :应付 ar :应收 |
| 3 | fbillentity | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 4 | fjournalentity | 流水标识 | varchar | 50 |  | √ | ' ' | 流水标识 |
| 5 | fjournalkey | 流水字段标识 | varchar | 50 |  | √ | ' ' | 流水字段标识 |
| 6 | fbillkey | 单据字段标识 | varchar | 50 |  | √ | ' ' | 单据字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_billjoumapper |  | fid |
| 2 | idx_ap_joumapper_fbillentity |  | fbillentity |
