# 寻源项目(后台元数据)-src_decisionsumpro

## 寻源项目(后台元数据)-主表 t_src_decisionsum_pro

- **表名称：** 寻源项目(后台元数据)-主表
- **表名：** t_src_decisionsum_pro

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [定标F7 src_decisionf7](../src_files/src_decisionf7.md) |
| 3 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_sum_pro_fprojectid |  | fprojectid |
| 2 | pk_src_decisionsum_pro |  | fentryid |
