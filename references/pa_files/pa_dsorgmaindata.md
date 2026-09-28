# 组织接口表-pa_dsorgmaindata

## 组织接口表-主表 t_pa_dsorgmaindata

- **表名称：** 组织接口表-主表
- **表名：** t_pa_dsorgmaindata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fparent | 上级 | varchar | 50 |  | √ | ' ' | 上级 |
| 4 | flongnumber | 长编码 | varchar | 100 |  | √ | ' ' | 长编码 |
| 5 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_dsorgmaindata |  | fid |
| 2 | idx_pa_dsorgmaindata |  | fnumber |
