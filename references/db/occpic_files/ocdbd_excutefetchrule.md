# 取数规则执行情况表-ocdbd_excutefetchrule

## 取数规则执行情况表-主表 t_ocdbd_excutefetchrule

- **表名称：** 取数规则执行情况表-主表
- **表名：** t_ocdbd_excutefetchrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffetchruleid | 取数规则Id | int8 | 64 |  | √ | 0 | 取数规则Id |
| 3 | flastmodifydate | 单据最后修改时间 | timestamp | 0 |  |  | null | 单据最后修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_excutefetchrule |  | fid |
| 2 | idx_ocdbd_excutefetchrule_rid |  | ffetchruleid |
