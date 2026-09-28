# 财务报表项目取数调整明细-tcvvt_main_adjust

## 财务报表项目取数调整明细-主表 t_tcvvt_main_adjust

- **表名称：** 财务报表项目取数调整明细-主表
- **表名：** t_tcvvt_main_adjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fadjustamount | 调整额 | numeric | 23 | 10 | √ | 0 | 调整额 |
| 3 | fskssqz | 税款所属期.结束 | timestamp | 0 |  |  | null | 税款所属期.结束 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 6 | fskssqq | 税款所属期.开始 | timestamp | 0 |  |  | null | 税款所属期.开始 |
| 7 | ftitlename | 调整项目 | varchar | 50 |  | √ | ' ' | 调整项目 |
| 8 | fcellid | 单元格行列维 | varchar | 80 |  | √ | ' ' | 单元格行列维 |
| 9 | foldamount | 原始总额 | numeric | 23 | 10 | √ | 0 | 原始总额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvvt_main_adjust |  | fid |
| 2 | idx_tcvvt_main_adjust |  | forgid,fskssqq,fskssqz,fcellid |
