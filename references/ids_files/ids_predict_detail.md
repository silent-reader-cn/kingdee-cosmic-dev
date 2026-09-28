# 预测明细（废弃）-ids_predict_detail

## 预测明细（废弃）-主表 t_ids_predict_detail

- **表名称：** 预测明细（废弃）-主表
- **表名：** t_ids_predict_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 日期 | varchar | 50 |  | √ | ' ' | 日期 |
| 3 | fprevalue | 预测值 | varchar | 50 |  | √ | ' ' | 预测值 |
| 4 | fsaledeptidfname | 销售部门 | varchar | 100 |  | √ | ' ' | 销售部门 |
| 5 | foffsetvalue | 绝对偏差 | varchar | 50 |  | √ | ' ' | 绝对偏差 |
| 6 | fcustidfname | 客户 | varchar | 100 |  | √ | ' ' | 客户 |
| 7 | foffsetpercent | 绝对百分比偏差(%) | varchar | 50 |  | √ | ' ' | 绝对百分比偏差(%) |
| 8 | fsaleorgidfname | 销售组织 | varchar | 100 |  | √ | ' ' | 销售组织 |
| 9 | factvalue | 实际值 | varchar | 50 |  | √ | ' ' | 实际值 |
| 10 | fmaterialidfname | 物料 | varchar | 100 |  | √ | ' ' | 物料 |
| 11 | fcustgroupfname | 客户分组 | varchar | 100 |  | √ | ' ' | 客户分组 |
| 12 | fmaterialgroupfname | 物料分组 | varchar | 100 |  | √ | ' ' | 物料分组 |
| 13 | fsalgroupfname | 销售分组 | varchar | 100 |  | √ | ' ' | 销售分组 |
| 14 | fmaterialnumber | 物料编码 | varchar | 100 |  | √ | ' ' | 物料编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_predict_detail |  | fid |
| 2 | idx_ftime |  | ftime |
