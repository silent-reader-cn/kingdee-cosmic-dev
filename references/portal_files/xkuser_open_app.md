# 用户默认打开的应用工作台-xkuser_open_app

## 用户默认打开的应用工作台-主表 t_xkportal_open_app

- **表名称：** 用户默认打开的应用工作台-主表
- **表名：** t_xkportal_open_app

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fissetting | 是否设置 | bpchar | 1 |  | √ | '0' | 是否设置,枚举: 0 :未设置 1 :已设置 |
| 4 | fbizappid | 选择默认打开的应用 | varchar | 50 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_app_fuserid |  | fuserid |
| 2 | pk_t_xkportal_open_app |  | fid |
