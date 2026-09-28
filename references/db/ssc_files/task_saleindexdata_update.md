# 业务员首页数据持续更新-task_saleindexdata_update

## 业务员首页数据持续更新-主表 t_tk_saleindexdata

- **表名称：** 业务员首页数据持续更新-主表
- **表名：** t_tk_saleindexdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpropvalue | 属性值 | int8 | 64 |  | √ | 0 | 属性值 |
| 3 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fpropname | 属性名 | varchar | 32 |  | √ | ' ' | 属性名 |
| 5 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_saleindexdata_pkey |  | fid |
| 2 | index_ssc_saleindexdata |  | fuser |
