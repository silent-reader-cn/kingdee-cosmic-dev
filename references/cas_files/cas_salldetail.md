# 收款单核销订单中间表-cas_salldetail

## 收款单核销订单中间表-主表 t_cas_salldetail

- **表名称：** 收款单核销订单中间表-主表
- **表名：** t_cas_salldetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourcebillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 3 | fbillentryid | 收款单分录ID | int8 | 64 |  | √ | 0 | 收款单分录ID |
| 4 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 5 | fbillid | 收款单ID | int8 | 64 |  | √ | 0 | 收款单ID |
| 6 | fsalldetailid | 唯一标识ID | int8 | 64 |  | √ | 0 | 唯一标识ID |
| 7 | fmatchamt | 匹配金额 | numeric | 19 | 6 | √ | 0 | 匹配金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_salldetail |  | fsalldetailid |
| 2 | pk_t_cas_salldetail |  | fid |
