# 最近使用-plm_plmsm_recently

## 最近使用-主表 t_plmsm_recentlyused

- **表名称：** 最近使用-主表
- **表名：** t_plmsm_recentlyused

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frecentlyusedclasssify | 最近使用分类 | varchar | 200 |  | √ | ' ' | 最近使用分类 |
| 3 | fmodelid | 分类视图 | varchar | 200 |  | √ | ' ' | 分类视图 |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | frecentlyused | 新建模型最近使用（废弃字段） | varchar | 200 |  | √ | ' ' | 新建模型最近使用（废弃字段） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmsm_recently_fuserid |  | fuserid |
| 2 | pk_t_plmsm_recentlyused |  | fid |
