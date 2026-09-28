# 检查记录表-bd_datacheckrecord

## 检查记录表-主表 t_bd_datacheckrecord

- **表名称：** 检查记录表-主表
- **表名：** t_bd_datacheckrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fispass | 是否通过 | bpchar | 1 |  | √ | '1' | 是否通过,枚举: 1 :是 0 :否 |
| 3 | fcheckresult | 检查结果 | varchar | 500 |  | √ | ' ' | 检查结果 |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fcheckresult_tag | 检查结果_详情 | text | 0 |  |  | null | 检查结果_详情 |
| 6 | fdatachecktaskno | 关联的检查任务编码 | varchar | 50 |  | √ | ' ' | 关联的检查任务编码 |
| 7 | fappid | 应用id | varchar | 50 |  | √ | ' ' | 应用id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_datacheckrecord |  | fid |
| 2 | idx_bd_record_no |  | fdatachecktaskno |
