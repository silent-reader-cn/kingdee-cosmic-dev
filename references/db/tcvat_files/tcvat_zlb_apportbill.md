# 税款分摊表单据-tcvat_zlb_apportbill

## 税款分摊表单据-主表 t_tcvat_zlb_apportbill

- **表名称：** 税款分摊表单据-主表
- **表名：** t_tcvat_zlb_apportbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 3 | fdqxse | 当期销售额 | numeric | 23 | 10 | √ | 0 | 当期销售额 |
| 4 | fljxse | 累计销售额 | numeric | 23 | 10 | √ | 0 | 累计销售额 |
| 5 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fjsbl | 计算比例 | numeric | 23 | 10 | √ | 0 | 计算比例 |
| 8 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: |
| 9 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 10 | fsuborg | 汇总方案组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_zlb_apportbill_s |  | fsuborg,fstartdate,fenddate |
| 2 | pk_tcvat_zlb_apportbill |  | fid |
| 3 | idx_t_tcvat_zlb_apportbill |  | forgid,fstartdate,fenddate |
