# 源数据与模型表数据映射-pa_sourcemodelmapping

## 源数据与模型表数据映射-主表 t_pa_sourcemodelmapping

- **表名称：** 源数据与模型表数据映射-主表
- **表名：** t_pa_sourcemodelmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourcenumber | 数据源实体标识 | varchar | 30 |  | √ | ' ' | 数据源实体标识 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fmodeltableid | 模型表id | int8 | 64 |  | √ | 0 | 模型表id |
| 5 | fanalysismodel | 分析模型id | int8 | 64 |  | √ | 0 | 分析模型id |
| 6 | fsourceentityid | 数据实体id | int8 | 64 |  | √ | 0 | 数据实体id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_sourcemodel |  | fanalysismodel,fmodeltableid |
| 2 | pk_t_pa_sourcemodelmapping |  | fid |
