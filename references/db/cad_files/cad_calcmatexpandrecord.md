# 标准成本卷算物料展开记录-cad_calcmatexpandrecord

## 标准成本卷算物料展开记录-主表 t_cad_calcsuccessrecord

- **表名称：** 标准成本卷算物料展开记录-主表
- **表名：** t_cad_calcsuccessrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcalctaskid | 卷算任务id | int8 | 64 |  | √ | 0 | 卷算任务id |
| 3 | fsuccessmatcount | 物料成功展开的数量 | int8 | 64 |  | √ | 0 | 物料成功展开的数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_calcsuccessrecord |  | fid |
| 2 | idx_cad_calcsuccessrecord |  | fcalctaskid |
