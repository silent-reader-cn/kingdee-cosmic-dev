# 产品特征选配计数器-pdm_prodfeaturecounter

## 产品特征选配计数器-主表 t_pdm_prodfeatcounter

- **表名称：** 产品特征选配计数器-主表
- **表名：** t_pdm_prodfeatcounter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 3 | fcount | 计数 | int8 | 64 |  | √ | 0 | 计数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_prodfeatcounter |  | fid |
| 2 | idx_prodfeatcounter_fyear |  | fyear |
