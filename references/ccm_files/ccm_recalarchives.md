# 信用重算的档案-ccm_recalarchives

## 信用重算的档案-主表 t_ccm_recalarchive

- **表名称：** 信用重算的档案-主表
- **表名：** t_ccm_recalarchive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farchiveid | 信用档案 | int8 | 64 |  | √ | 0 | 信用档案 |
| 3 | fcreatetime | 长日期 | timestamp | 0 |  |  | null | 长日期 |
| 4 | fsessionid | 线程ID | varchar | 100 |  | √ | ' ' | 线程ID |
| 5 | fscheme | 信控方案 | int8 | 64 |  | √ | 0 | 信控方案 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_recalarchiveid |  | farchiveid |
| 2 | pk_ccm_recalarchive |  | fid |
