# 业务追踪单据许可参数-pbd_trackerlicens

## 业务追踪单据许可参数-主表 t_pbd_trackerlicens

- **表名称：** 业务追踪单据许可参数-主表
- **表名：** t_pbd_trackerlicens

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftargetbill | 目标单据 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 3 | fbizappid | 应用 | varchar | 80 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_trackerlicens |  | fid |
| 2 | t_pbd_trackerlicens_ftarget |  | ftargetbill |
