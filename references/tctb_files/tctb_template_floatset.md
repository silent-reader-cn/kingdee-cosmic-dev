# 模板浮动设置-tctb_template_floatset

## 模板浮动设置-主表 t_tctb_template_floatset

- **表名称：** 模板浮动设置-主表
- **表名：** t_tctb_template_floatset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstartrowindex | 起点横坐标 | int8 | 64 |  | √ | 0 | 起点横坐标 |
| 3 | ftableentity | 浮动表标识 | varchar | 50 |  | √ | ' ' | 浮动表标识,枚举: |
| 4 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fdirect | 罗列方向 | varchar | 30 |  | √ | ' ' | 罗列方向,枚举: 1 :列浮动（横向罗列） 2 :行浮动（纵向罗列） |
| 9 | ftype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tctb_template_type |
| 10 | fbasetemplateid | 基础模板主键id | int8 | 64 |  | √ | 0 | 基础模板主键id |
| 11 | fmaxrow | 浮动最大行数 | int8 | 64 |  | √ | 0 | 浮动最大行数 |
| 12 | fenable | 启用状态 | varchar | 30 |  | √ | ' ' | 启用状态,枚举: 0 :禁用 1 :启用 |
| 13 | fendrowindex | 终点横坐标 | int8 | 64 |  | √ | 0 | 终点横坐标 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_template_floatset |  | fid |
| 2 | idx_tctb_template_floatset |  | fbasetemplateid |
