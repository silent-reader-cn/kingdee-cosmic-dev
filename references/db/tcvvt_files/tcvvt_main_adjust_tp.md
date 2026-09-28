# 财务报表取数调整临时表-tcvvt_main_adjust_tp

## 财务报表取数调整临时表-主表 t_tcvvt_main_adjust_tp

- **表名称：** 财务报表取数调整临时表-主表
- **表名：** t_tcvvt_main_adjust_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fadjustamount | 调整额 | numeric | 23 | 10 | √ | 0 | 调整额 |
| 3 | fskssqz | 税款所属期.结束 | timestamp | 0 |  |  | null | 税款所属期.结束 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fskssqq | 税款所属期.开始 | timestamp | 0 |  |  | null | 税款所属期.开始 |
| 6 | ftitlename | 调整项目 | varchar | 50 |  | √ | ' ' | 调整项目 |
| 7 | fcellid | 单元格行列维 | varchar | 50 |  | √ | ' ' | 单元格行列维 |
| 8 | foldamount | 原始总额 | numeric | 23 | 10 | √ | 0 | 原始总额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvvt_main_adjust_tp |  | fid |
| 2 | idx_tcvvt_main_adjust_tp |  | forgid,fskssqq,fskssqz,fcellid |
