# 业务对象代理验权-perm_entitymap

## 业务对象代理验权-主表 t_perm_entitymap

- **表名称：** 业务对象代理验权-主表
- **表名：** t_perm_entitymap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | ftarentity | 目标对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | ftarapp | 目标应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 5 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 6 | fsrcentity | 源对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fsrcapp | 源应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_entitymap |  | fsrcentity,fsrcapp |
| 2 | pk_t_perm_entitymap |  | fid |
