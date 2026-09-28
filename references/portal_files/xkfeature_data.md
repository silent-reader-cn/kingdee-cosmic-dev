# 特性数据-xkfeature_data

## 特性数据-主表 t_xk_fea_data

- **表名称：** 特性数据-主表
- **表名：** t_xk_fea_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fdata | 特性数据 | text | 0 |  |  | ' ' | 特性数据 |
| 4 | fversion | 版本号 | varchar | 32 |  | √ | ' ' | 版本号 |
| 5 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_fea_data |  | fid |
| 2 | idx_fea_data_fversion |  | fversion |
