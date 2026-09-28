# 明细和汇总模型数据映射-pa_detailsummarymapping

## 明细和汇总模型数据映射-主表 t_pa_detailsummarymapping

- **表名称：** 明细和汇总模型数据映射-主表
- **表名：** t_pa_detailsummarymapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsummaryid | 汇总数据id | int8 | 64 |  | √ | 0 | 汇总数据id |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fcreatetimestamp | 创建时间戳 | int8 | 64 |  | √ | 0 | 创建时间戳 |
| 5 | fdetailid | 明细数据id | int8 | 64 |  | √ | 0 | 明细数据id |
| 6 | fanalysismodel | 分析模型id | int8 | 64 |  | √ | 0 | 分析模型id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_summarydetail |  | fanalysismodel,fsummaryid,fdetailid |
| 2 | pk_t_pa_detailsummarymapping |  | fid |
