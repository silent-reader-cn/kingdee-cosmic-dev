# 库存预警参数数据-im_warnparamdata

## 库存预警参数数据-主表 t_im_warnparamdata

- **表名称：** 库存预警参数数据-主表
- **表名：** t_im_warnparamdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparam | 参数 | text | 0 |  |  | null | 参数 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fformid | 表单标识 | varchar | 50 |  | √ | ' ' | 表单标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_warnparamdata |  | fid |
