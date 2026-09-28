# 分配比例计算单据-tcvat_ybhz_assign_bill

## 分配比例计算单据-主表 t_tcvat_ybhz_assign_bill

- **表名称：** 分配比例计算单据-主表
- **表名：** t_tcvat_ybhz_assign_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftaxassign | 应税服务分配比例 | numeric | 23 | 10 | √ | 0.0000000000 | 应税服务分配比例 |
| 4 | ftaxjzjtassign | 应税服务即征即退分配比例 | numeric | 23 | 10 | √ | 0.0000000000 | 应税服务即征即退分配比例 |
| 5 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :被汇总 2 :汇总 |
| 6 | fnormaljzjtassign | 一般货物及劳务即征即退分配额 | numeric | 23 | 10 | √ | 0.0000000000 | 一般货物及劳务即征即退分配额 |
| 7 | fmainorgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 9 | fnormalassign | 一般货物及劳务分配比例 | numeric | 23 | 10 | √ | 0.0000000000 | 一般货物及劳务分配比例 |
| 10 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 11 | fnormalsales | 一般货物及劳务销售收入 | numeric | 23 | 10 | √ | 0.0000000000 | 一般货物及劳务销售收入 |
| 12 | ftaxsales | 应税服务销售收入 | numeric | 23 | 10 | √ | 0.0000000000 | 应税服务销售收入 |
| 13 | fnormaljzjtsales | 一般货物及劳务即征即退销售收入 | numeric | 23 | 10 | √ | 0.0000000000 | 一般货物及劳务即征即退销售收入 |
| 14 | ftaxjzjtsales | 应税服务即征即退销售收入 | numeric | 23 | 10 | √ | 0.0000000000 | 应税服务即征即退销售收入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ybhz_assign_bill |  | fid |
| 2 | idx_tcvat_ybhz_assign_bill |  | forgid,fstartdate,fenddate |
