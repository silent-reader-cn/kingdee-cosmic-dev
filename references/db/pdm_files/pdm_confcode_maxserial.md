# 配置号规则最大流水号（废弃）-pdm_confcode_maxserial

## 配置号规则最大流水号（废弃）-主表 t_pdm_rulemaxserial

- **表名称：** 配置号规则最大流水号（废弃）-主表
- **表名：** t_pdm_rulemaxserial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconfcoderuleid | 配置号规则ID | int8 | 64 |  | √ | 0 | 配置号规则ID |
| 3 | faccordpropid | 依据属性ID | int8 | 64 |  | √ | 0 | 依据属性ID |
| 4 | fmaxserial | 最大流水号 | int8 | 64 |  | √ | 0 | 最大流水号 |
| 5 | fmaterialid | 物料ID（预留） | int8 | 64 |  | √ | 0 | 物料ID（预留） |
| 6 | fconfcoderulenumber | 配置号规则编码 | varchar | 100 |  | √ | ' ' | 配置号规则编码 |
| 7 | faccordpropnumber | 依据属性编码 | varchar | 100 |  | √ | ' ' | 依据属性编码 |
| 8 | finitserial | 初始流水号 | int8 | 64 |  | √ | 0 | 初始流水号 |
| 9 | fmaterialnumber | 物料编码（预留） | varchar | 100 |  | √ | ' ' | 物料编码（预留） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_maxserial |  | fconfcoderuleid,faccordpropnumber |
| 2 | pk_t_pdm_rulemaxserial |  | fid |
